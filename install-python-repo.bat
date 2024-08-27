@echo off

:: Set Python version and installer URL
set PYTHON_VERSION=3.11.9
set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%

:: Set Python installation path
set PYTHON_DIR=C:\Python%PYTHON_VERSION%

:: Check if Python is installed
echo Checking for Python installation...
%PYTHON_DIR%\python.exe --version >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo Python %PYTHON_VERSION% is already installed.
) else (
    echo Python %PYTHON_VERSION% is not installed, proceeding with installation...
    
    :: Download Python installer if it does not exist
    if not exist %PYTHON_INSTALLER% (
        echo Downloading Python %PYTHON_VERSION% installer...
        curl -O %PYTHON_URL%
    ) else (
        echo Python installer already downloaded.
    )

    :: Install Python silently with default options and add to PATH
    echo Installing Python %PYTHON_VERSION%...
    %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 TargetDir=%PYTHON_DIR%

    :: Verify Python installation
    echo Verifying Python installation...
    %PYTHON_DIR%\python.exe --version
    if %ERRORLEVEL% neq 0 (
        echo Python installation failed.
        pause
        exit /b 1
    )
)

:: Check if speedtest-cli exists
if not exist speedtest.exe (
    echo Downloading speedtest-cli...
    curl -Lo speedtest.zip https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-win64.zip

    echo Unzipping speedtest-cli...
    tar -xf speedtest.zip
) else (
    echo speedtest-cli already exists.
)

:: Create results directory if it does not exist
if not exist results (
    echo Creating results directory...
    mkdir results
) else (
    echo Results directory already exists.
)

echo Python %PYTHON_VERSION% and speedtest-cli have been installed successfully.
pause
