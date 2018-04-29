@echo off

echo This will use powershell to convert HTML to DOCX (opens WINWORD.exe process)
echo.
PAUSE
cls

cd resultUTFSig

mkdir word

for /R %%a in (*.html) do (
	echo %%a
	powershell.exe -noprofile -executionpolicy bypass -file ..\html2docx.ps1 -html "%%a" -docx "word\%%~na".docx
)