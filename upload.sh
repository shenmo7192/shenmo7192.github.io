#!/bin/sh
git config  core.quotepath false
git add .
git commit -m make-timestamps
hugo -d docs
git add .
git commit -m update-blogs
git push

