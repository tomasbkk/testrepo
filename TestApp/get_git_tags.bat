@echo off
setlocal enabledelayedexpansion

set "TAG_COUNT=0"

for /f "delims=" %%i in ('git for-each-ref --count=2 --sort=-creatordate --format "%%(refname:short)" refs/tags') do (
  set /a TAG_COUNT+=1
  if !TAG_COUNT! equ 1 (
    set "TAG1=%%i"
    echo "REPO_TAG1=!TAG1!" >> $env:GITHUB_ENV
  ) else if !TAG_COUNT! equ 2 (
    set "TAG2=%%i"
    echo "REPO_TAG2=!TAG2!" >> $env:GITHUB_ENV
  )
)

endlocal
