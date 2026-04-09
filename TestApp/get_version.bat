@echo off
setlocal enabledelayedexpansion

REM Change to the directory where this script resides
cd /d "%~dp0"

REM Initialize variables
set "VERSION_MAJOR="
set "VERSION_MINOR="
set "VERSION_PATCH="
set "VERSION_REV="

REM Read version.txt and set variables
for /f "tokens=1,2" %%A in (version.txt) do (
    if "%%A"=="VERSION_MAJOR" set "VERSION_MAJOR=%%B"
    if "%%A"=="VERSION_MINOR" set "VERSION_MINOR=%%B"
    if "%%A"=="VERSION_PATCH" set "VERSION_PATCH=%%B"
    if "%%A"=="VERSION_REV" set "VERSION_REV=%%B"
)

REM Check if all variables are set
if not defined VERSION_MAJOR (
    echo Error: VERSION_MAJOR not found in version.txt
    exit /b 1
)
if not defined VERSION_MINOR (
    echo Error: VERSION_MINOR not found in version.txt
    exit /b 1
)
if not defined VERSION_PATCH (
    echo Error: VERSION_PATCH not found in version.txt
    exit /b 1
)
if not defined VERSION_REV (
    echo Error: VERSION_REV not found in version.txt
    exit /b 1
)

REM Set the environment variable with the version number
set "VERSION=!VERSION_MAJOR!.!VERSION_MINOR!.!VERSION_PATCH!.!VERSION_REV!"

REM Output the version number
echo Version: !VERSION!

REM Set the BUILD_VERSION environment variable as per GitHub Actions format
echo BUILD_VERSION=!VERSION! >> %GITHUB_ENV%


endlocal
