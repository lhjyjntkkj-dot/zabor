@echo off
title CH PROJECT
cd /d "%~dp0"

where node >nul 2>nul
if errorlevel 1 goto nonode

echo.
echo   Starting CH PROJECT site...
echo.
echo   Open in browser:  http://localhost:8080
echo.
echo   To stop: press Ctrl+C or close this window
echo.

start "" http://localhost:8080
node start-site.js

echo.
echo   Site stopped. Press any key.
pause >nul
exit

:nonode
echo.
echo   ERROR: Node.js not installed.
echo.
echo   1. Open nodejs.org
echo   2. Download and install (green LTS button)
echo   3. Restart computer
echo   4. Run this file again
echo.
pause
