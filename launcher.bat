@echo off
echo Navigating to the target directory
cd /d C:\Users\lesek\OneDrive\Bureau\py_crea\password\generator

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
