@echo off
title AvtoGaz Telegram Boti - @stag_tashkent_unitbot

set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not exist "%PYTHON_EXE%" (
    set "PYTHON_EXE=python"
)

echo ========================================================
echo        AvtoGaz Telegram Boti Ishga Tushmoqda...
echo ========================================================
echo.

"%PYTHON_EXE%" bot.py

if errorlevel 1 (
    echo.
    echo ========================================================
    echo  Xatolik yuz berdi yoki bot to'xtadi.
    echo ========================================================
    pause
)
