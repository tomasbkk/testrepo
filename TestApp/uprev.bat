@echo off
setlocal enabledelayedexpansion

set "filename=version.txt"
set "tempfile=temp.txt"
set "param=%~1"

if "%param%"=="major" (
    set "pattern=VERSION_MAJOR"
    set "reset_minor=true"
    set "reset_patch=true"
    set "reset_rev=true"
) else if "%param%"=="minor" (
    set "pattern=VERSION_MINOR"
    set "reset_patch=true"
    set "reset_rev=true"
) else if "%param%"=="patch" (
    set "pattern=VERSION_PATCH"
    set "reset_rev=true"
) else if "%param%"=="rev" (
    set "pattern=VERSION_REV"
) else (
    echo Invalid parameter. Usage: uprev.bat [major | minor | patch | rev]
    exit /b
)

if not exist "%filename%" (
    echo %filename% does not exist.
    exit /b
)

set "resetting=false"
> "%tempfile%" (
    for /f "usebackq tokens=1,* delims= " %%a in ("%filename%") do (
        if "%%a"=="%pattern%" (
            set "value=%%b"
            set /a "value+=1"
            echo %pattern% !value!
            set "resetting=true"
        ) else if "%%a"=="VERSION_MINOR" (
            if defined reset_minor (
                echo VERSION_MINOR 0
            ) else (
                echo %%a %%b
            )
        ) else if "%%a"=="VERSION_PATCH" (
            if defined reset_patch (
                echo VERSION_PATCH 0
            ) else (
                echo %%a %%b
            )
        ) else if "%%a"=="VERSION_REV" (
            if defined reset_rev (
                echo VERSION_REV 0
            ) else (
                echo %%a %%b
            )
        ) else (
            echo %%a %%b
        )
    )
)

move /y "%tempfile%" "%filename%" > nul
echo %filename% updated successfully.

endlocal
