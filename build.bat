@echo off

cd /d %~dp0
uv run --locked pyinstaller --clean --noconfirm --onefile --name RotatePDF src\rotatepdf\main.py

if errorLevel 1 (
    echo ビルドに失敗しました。
    pause
    exit /b 1
)

if not exist dist\PDFRotater mkdir dist\PDFRotater
move /Y dist\RotatePDF.exe dist\PDFRotater\RotatePDF.exe

if not exist dist\PDFRotater\input mkdir dist\PDFRotater\input
if not exist dist\PDFRotater\output mkdir dist\PDFRotater\output

echo ビルドが完了しました。
pause