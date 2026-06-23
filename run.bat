@echo off
REM Smart Task Manager - Setup and Run Script for Windows

echo.
echo 🚀 Smart Task Manager - Setup Script
echo =====================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+
    pause
    exit /b 1
)

REM Create virtual environment if not exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo ✅ Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create .env if not exists
if not exist ".env" (
    echo 🔧 Creating .env file from template...
    copy .env.example .env
    echo ⚠️  Please edit .env and configure your database settings
)

REM Run app
echo.
echo 🌟 Starting Smart Task Manager...
python app.py

pause
