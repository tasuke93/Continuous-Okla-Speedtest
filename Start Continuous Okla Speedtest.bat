@echo off
:: Create results directory if it does not exist
if not exist results (
    echo Creating results directory...
    mkdir results
) else (
    echo Results directory already exists.
)

set SCRIPT_NAME=Continuous-okla-Speedtest.py

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel%==0 (
    echo Python found. Running script with 'python'.
    python %SCRIPT_NAME%
    goto :EOF
)

:: Check if Python3 is installed
where python3 >nul 2>nul
if %errorlevel%==0 (
    echo Python3 found. Running script with 'python3'.
    python3 %SCRIPT_NAME%
    goto :EOF
)

:: If neither is found, display a message
echo Neither Python nor Python3 is installed. Please install Python to continue.

pause