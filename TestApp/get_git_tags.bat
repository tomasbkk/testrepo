@echo on
for /f "tokens=*" %%i in ('git for-each-ref --count=2 --sort=-creatordate --format "%%(refname:short)" refs/tags') do (
  if not defined TAG1 (
    echo %%i
    echo "REPO_TAG1=%%i" >> $env:GITHUB_ENV
  ) else (
    echo %%i
    echo "REPO_TAG2=%%i" >> $env:GITHUB_ENV
  )
)

echo First tag: %REPO_TAG1%
echo Second tag: %REPO_TAG2%
