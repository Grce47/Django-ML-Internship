#!/bin/bash
echo `git status`
echo `git add .`
echo `git commit -m $1`
echo `git push origin main`