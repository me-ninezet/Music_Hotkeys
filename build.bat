@echo off
chcp 65001 > nul
echo Сборка Music Hotkeys в EXE...

:: Очистка предыдущих сборок
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

:: Сборка с spec файлом
pyinstaller build.spec --noconfirm

echo.
echo Сборка завершена!
echo Исполняемый файл: dist\MusicHotkeys\MusicHotkeys.exe
echo.
pause