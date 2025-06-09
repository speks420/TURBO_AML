@echo off
title TURBO_AML IP Update Script
echo ========================================
echo TURBO_AML IP Update Script
echo ========================================
echo.

if "%1"=="" (
    echo Usage: update-ip.bat NEW_IP_ADDRESS
    echo Example: update-ip.bat 95.68.116.88
    echo.
    echo Current external IP from .env file:
    if exist .env (
        findstr "EXTERNAL_IP=" .env
    ) else (
        echo .env file not found
    )
    pause
    exit /b 1
)

set NEW_IP=%1
echo Updating external IP to: %NEW_IP%
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
)

REM Update IP in .env file
echo Updating .env file...
powershell -Command "(gc .env) -replace 'EXTERNAL_IP=.*', 'EXTERNAL_IP=%NEW_IP%' | Out-File -encoding ascii .env"

REM Update backend .env if it exists
if exist backend\.env (
    echo Updating backend/.env file...
    powershell -Command "(gc backend\.env) -replace 'EXTERNAL_IP=.*', 'EXTERNAL_IP=%NEW_IP%' | Out-File -encoding ascii backend\.env"
)

REM Update frontend .env if it exists
if exist frontend\.env (
    echo Updating frontend/.env file...
    powershell -Command "(gc frontend\.env) -replace 'VITE_API_URL=.*', 'VITE_API_URL=http://%NEW_IP%:8000' | Out-File -encoding ascii frontend\.env"
)

echo.
echo IP updated successfully!
echo.
echo Choose deployment option:
echo 1. Development (localhost:5173 + localhost:8000)
echo 2. Production (nginx on port 80)
echo 3. Just update IP (no restart)
echo.
set /p choice="Enter choice (1-3): "

if "%choice%"=="1" (
    echo Stopping current containers...
    docker-compose -f docker-compose.dev.yml down
    echo Starting development environment...
    docker-compose -f docker-compose.dev.yml up --build -d
    echo.
    echo Development environment started!
    echo - Frontend: http://%NEW_IP%:5173
    echo - Backend: http://%NEW_IP%:8000/docs
)

if "%choice%"=="2" (
    echo Stopping current containers...
    docker-compose -f docker-compose.dev.yml down
    docker-compose -f docker-compose.prod.yml down
    echo Starting production environment...
    docker-compose -f docker-compose.prod.yml up --build -d
    echo.
    echo Production environment started!
    echo - Application: http://%NEW_IP%
    echo - API: http://%NEW_IP%/api/docs
)

if "%choice%"=="3" (
    echo IP updated. Services not restarted.
)

echo.
echo Firewall reminder:
echo - Make sure Windows Firewall allows ports 80, 8000, and 5173
echo - Router port forwarding may be needed for internet access
echo.
pause 