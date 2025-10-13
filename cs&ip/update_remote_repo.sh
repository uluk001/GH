#!/usr/bin/env bash

if git status | grep -q "Untracked files" || git status | grep -q "Changes not staged for commit"; then
    git add .
    echo "Все новые изменения внесены на стадию stage"
fi

