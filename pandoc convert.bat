@echo off

echo This will use pandoc.exe to convert HTML to DOCX (faster than powershell)
echo.
PAUSE
cls

cd resultUTFSig

mkdir pandoc

for /R %%a in (*.html) do (
	echo %%a
	..\pandoc.exe -s -f html -t docx -o "pandoc\%%~na".docx "%%a"
)