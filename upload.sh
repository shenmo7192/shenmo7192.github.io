#!/bin/sh
git config  core.quotepath false
git add .
git commit -m æmake-timestamps
hugo -D
git add .
git commit -m update-blogs
git push

