#!/usr/bin/env python3
"""
Deepin 论坛帖子导入工具
========================
自动从 bbs.deepin.org.cn 抓取指定用户的论坛帖子，
并将比博客当前最新文章更新的帖子导入到 Hugo 博客中。

使用方法:
    python3 import-forum-posts.py

环境要求:
    Python 3.6+

配置说明:
    修改脚本中的 USER_ID 变量为目标用户 ID（默认 223313）。
    脚本会自动识别 content/post/ 目录下的现有文章，并跳过已存在的标题。
"""

import json
import os
import re
import urllib.request
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser

# ==================== 配置 ====================
USER_ID = 223313
POST_DIR = "content/post"
BLOG_URL = "https://bbs.deepin.org.cn"
# =============================================

class HTMLToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.in_code = False
        self.in_pre = False
        self.in_a = False
        self.a_href = ""
        self.list_stack = []
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.current_tag = tag

        if tag == 'br':
            self.result.append('\n')
        elif tag == 'p':
            if self.result and not self.result[-1].endswith('\n'):
                self.result.append('\n\n')
        elif tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', '')
            self.result.append(f"\n![{alt}]({src})\n")
        elif tag == 'a':
            self.in_a = True
            self.a_href = attrs_dict.get('href', '')
        elif tag in ('strong', 'b'):
            self.result.append('**')
        elif tag in ('em', 'i'):
            self.result.append('*')
        elif tag == 'code':
            self.in_code = True
            self.result.append('`')
        elif tag == 'pre':
            self.in_pre = True
            self.result.append('\n```\n')
        elif tag == 'ul':
            self.list_stack.append('ul')
        elif tag == 'ol':
            self.list_stack.append('ol')
        elif tag == 'li':
            indent = '  ' * (len(self.list_stack) - 1)
            marker = '- ' if self.list_stack[-1] == 'ul' else '1. '
            self.result.append(f"\n{indent}{marker}")
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            level = int(tag[1])
            self.result.append(f"\n{'#' * level} ")
        elif tag == 'blockquote':
            self.result.append('\n> ')
        elif tag == 'div':
            if self.result and not self.result[-1].endswith('\n'):
                self.result.append('\n')

    def handle_endtag(self, tag):
        if tag == 'a':
            self.in_a = False
            self.a_href = ""
        elif tag in ('strong', 'b'):
            self.result.append('**')
        elif tag in ('em', 'i'):
            self.result.append('*')
        elif tag == 'code':
            self.in_code = False
            self.result.append('`')
        elif tag == 'pre':
            self.in_pre = False
            self.result.append('\n```\n')
        elif tag == 'ul':
            if self.list_stack:
                self.list_stack.pop()
        elif tag == 'ol':
            if self.list_stack:
                self.list_stack.pop()
        elif tag == 'li':
            pass
        elif tag in ('p', 'div'):
            if self.result and not self.result[-1].endswith('\n'):
                self.result.append('\n')

    def handle_data(self, data):
        self.result.append(data)

    def get_markdown(self):
        text = ''.join(self.result)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()


def html_to_md(html):
    if not html:
        return ""
    parser = HTMLToMarkdown()
    try:
        parser.feed(html)
        return parser.get_markdown()
    except Exception:
        return re.sub(r'<[^>]+>', '', html)


def fetch_url(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8')


def extract_post_detail(html):
    start = html.find('<script id="ng-state" type="application/json">')
    if start == -1:
        return None
    start += len('<script id="ng-state" type="application/json">')
    end = html.find('</script>', start)
    if end == -1:
        return None
    data = json.loads(html[start:end])
    return data.get('post-detail')


def get_existing_posts():
    posts = {}
    if not os.path.isdir(POST_DIR):
        return posts
    for fname in os.listdir(POST_DIR):
        if fname.endswith('.md'):
            path = os.path.join(POST_DIR, fname)
            with open(path, encoding='utf-8') as f:
                content = f.read()
            title_match = re.search(r'^title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
            date_match = re.search(r'^date:\s*(.*)$', content, re.MULTILINE)
            if title_match and date_match:
                title = title_match.group(1).strip().strip('"').strip("'")
                date_str = date_match.group(1).strip()
                posts[title] = {'file': fname, 'date': date_str}
    return posts


def main():
    print("Fetching user threads...")
    threads_url = f"{BLOG_URL}/api/v1/user/thread?id={USER_ID}&limit=100&offset=0"
    html = fetch_url(threads_url)
    data = json.loads(html)
    threads = data.get('data', [])
    print(f"Found {len(threads)} threads")

    existing = get_existing_posts()

    latest_blog_date = None
    for p in existing.values():
        try:
            d = datetime.fromisoformat(p['date'].replace('Z', '+00:00'))
            if latest_blog_date is None or d > latest_blog_date:
                latest_blog_date = d
        except Exception:
            pass
    print(f"Latest blog date: {latest_blog_date}")

    new_threads = []
    for t in threads:
        try:
            thread_date = datetime.fromisoformat(t['created_at'].replace('Z', '+00:00'))
            if latest_blog_date is None or thread_date > latest_blog_date:
                if t['subject'] not in existing:
                    new_threads.append(t)
        except Exception:
            pass

    print(f"New threads to add: {len(new_threads)}")

    tz_8 = timezone(timedelta(hours=8))

    for t in new_threads:
        thread_id = t['id']
        subject = t['subject']
        created_at = t['created_at']

        print(f"Processing: {subject} ({thread_id})")

        try:
            post_html = fetch_url(f"{BLOG_URL}/post/{thread_id}")
            detail = extract_post_detail(post_html)
            if not detail:
                print(f"  Warning: no post-detail found for {thread_id}")
                continue

            info = detail.get('info', {})
            if info.get('code') != 0:
                print(f"  Warning: error code {info.get('code')} for {thread_id}")
                continue

            thread_data = info.get('data', {})
            post_data = thread_data.get('post', {})
            message_html = post_data.get('message', '')
            md_content = html_to_md(message_html)

            dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            dt_8 = dt.astimezone(tz_8)
            date_str = dt_8.strftime('%Y-%m-%dT%H:%M:%S+08:00')

            safe_title = re.sub(r'[^\w\u4e00-\u9fff\-]+', '-', subject).strip('-')
            if not safe_title:
                safe_title = str(thread_id)
            fname = os.path.join(POST_DIR, f"{safe_title}.md")

            counter = 1
            base_fname = fname
            while os.path.exists(fname):
                fname = base_fname.replace('.md', f'-{counter}.md')
                counter += 1

            # Escape quotes in title for YAML
            safe_subject = subject.replace('"', '\\"')
            # Build summary: first meaningful line, or title if none found
            summary = subject
            for line in md_content.strip().split('\n'):
                line = line.strip()
                if not line:
                    continue
                if line.startswith('![') or line.startswith('```') or line.startswith('---'):
                    continue
                if line.startswith('<') and line.endswith('>'):
                    continue
                if line.startswith('http'):
                    continue
                summary = line[:120] + ('...' if len(line) > 120 else '')
                break
            frontmatter = f"""---
title: "{safe_subject}"
date: {date_str}
avatar: /img/avatar.jpeg
categories:
  - Linux
tags:
  - Linux
draft: false
---

{summary}

<!--more-->

{md_content}
"""

            with open(fname, 'w', encoding='utf-8') as f:
                f.write(frontmatter)
            print(f"  Written: {fname}")

        except Exception as e:
            print(f"  Error processing {thread_id}: {e}")
            import traceback
            traceback.print_exc()

    print("Done!")


if __name__ == '__main__':
    main()
