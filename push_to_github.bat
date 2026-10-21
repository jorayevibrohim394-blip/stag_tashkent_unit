@echo off
title GitHub ga yuklash (Push) - stag_tashkent_unit
chcp 65001 >nul
cls

echo ========================================================
echo        GitHub ga loyihani yuklash (Push)
echo ========================================================
echo.

git status
echo.
echo GitHub hisobingizga yuklash uchun Personal Access Token kerak.
echo (Agar tokeningiz bo'lmasa: https://github.com/settings/tokens dan oling)
echo.

set /p TOKEN="GitHub Tokeningizni kiriting: "

if "%TOKEN%"=="" (
    echo Token kiritilmadi!
    pause
    exit /b 1
)

echo.
echo Yuklanmoqda...
git push -u https://%TOKEN%@github.com/jorayevibrohim394-blip/stag_tashkent_unit.git main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo  Muvaffaqiyatli yuklandi!
    echo  https://github.com/jorayevibrohim394-blip/stag_tashkent_unit
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo  Xatolik yuz berdi. Token to'g'riligini tekshiring.
    echo ========================================================
)
pause
