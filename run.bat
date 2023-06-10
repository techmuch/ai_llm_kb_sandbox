@echo off

REM Get Jira login info
set /p user_name=Enter your JIRA username: 
set /p password=Enter your JIRA password: 

REM Set the environmental variables
set "JIRA_USERNAME=%user_name%"
set "JIRA_PASSWORD=%password%"

set /p display_var=Do you want to display the username and password? (yes/no): 

if /i "%display_var%"=="yes" (
    REM Display the set values
    echo Username: %JIRA_USERNAME%
    echo Password: %JIRA_PASSWORD%
)

rem Get the path to the Python executable
set python_exe=%PATH%\python.exe

rem Check if the Python executable exists
if not exist "%python_exe%" (
  echo Python executable not found.
  goto :eof
)

rem Run the Python program
"%python_exe%" scripts/check_requirements.py requirements.txt

rem Display the message "Press any key to continue"
echo Press any key to continue...

rem Wait for the user to press a key
pause >nul