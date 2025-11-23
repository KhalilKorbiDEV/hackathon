@echo off
REM Fake News Detection - Quick Start Script for Windows

echo.
echo ============================================================
echo  Fake News Detection System - Quick Start
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/4] Training model...
python train.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Model training failed
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  Setup Complete!
echo ============================================================
echo.
echo Starting Flask web server...
echo.
echo The application will be available at:
echo   http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
