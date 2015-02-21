REM This is a batch file in order to determine how long it takes to execute each 'Hello World' program in C and Python

REM Note: C program must already be compiled & linked

echo %time%
HelloWorld
echo %time%

pause

echo %time%
python Hello_World.py
echo %time%

pause