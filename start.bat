@echo off
call dependencies.bat > nul
echo Started client. To exit, Ctrl^+C -^> Y -^> Enter
python main.py
pause
exit