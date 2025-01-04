@echo off
echo Navigating to the directory of the batch script

set SCRIPT_DIR=%~dp0
cd /d %SCRIPT_DIR%

:: DEV KAGAMI 1321633141705936898
:: DEV KAGAMI 1321633141705936898


if %errorlevel% neq 0 (
    echo Failed to navigate to the target directory. Exiting script.
    exit /b %errorlevel%
)

echo Installing required Python package: win10toast
pip install win10toast
pip install pynput

if %errorlevel% neq 0 (
    echo Failed to install win10toast. Exiting script.
    exit /b %errorlevel%
)

echo Running Genrator.py
python Genrator.py

if %errorlevel% neq 0 (
    echo Failed to run Generator.py. Exiting script.
    exit /b %errorlevel%
)

echo Script executed successfully.
pause
