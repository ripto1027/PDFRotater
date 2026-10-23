@echo off

cd /d %~dp0
uv run --locked pyinstaller --clean --noconfirm --onefile --name PdfEditor src\pdfeditor\main.py

if errorLevel 1 (
    echo ビルドに失敗しました。
    pause
    exit /b 1
)

echo ビルドに成功しました。
pause