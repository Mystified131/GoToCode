@ECHO OFF
CLS

TITLE Shortcut Creator (%date% %time:~-11,5%)
ECHO.

ECHO =============================
ECHO Running Admin Shell
ECHO =============================

:init
setlocal DisableDelayedExpansion
set cmdInvoke=1
set winSysFolder=System32
set "batchPath=%~0"
for %%k in (%0) do set batchName=%%~nk
set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
setlocal EnableDelayedExpansion

:checkPrivileges
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
ECHO.
ECHO **************************************
ECHO Invoking UAC for Privilege Escalation
ECHO **************************************

ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
ECHO args = "ELEV " >> "%vbsGetPrivileges%"
ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
ECHO Next >> "%vbsGetPrivileges%"

if '%cmdInvoke%'=='1' goto InvokeCmd 

ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
goto ExecElevation

:InvokeCmd
ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

:ExecElevation
"%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
exit /B

:gotPrivileges
setlocal & pushd %~dp0
if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)

::::::::::::::::::::::::::::
::START
::::::::::::::::::::::::::::

MKDIR "C:\ProgramData\RuleStream\8.16.4\Batch Scripts\"
MKDIR "C:\ProgramData\RuleStream\8.16.4\Batch Scripts\Prerequisites"

COPY /B /V /Y /Z "\\internal.hussmann.com\sites\Apps\Rulestream\Config\PROD\Deployment\Shortcut Batch Scripts\*.bat"  "C:\ProgramData\RuleStream\8.16.4\Batch Scripts"
COPY /B /V /Y /Z "\\internal.hussmann.com\sites\Apps\Rulestream\Config\PROD\Deployment\Shortcut Batch Scripts\Prerequisites\EnableLinkedConnections.reg" "C:\ProgramData\RuleStream\8.16.4\Batch Scripts\Prerequisites"
COPY /B /V /Y /Z "\\internal.hussmann.com\sites\Apps\Rulestream\Config\PROD\Deployment\Shortcut Batch Scripts\Prerequisites\shortcutCreator.bat" "C:\ProgramData\RuleStream\8.16.4\Batch Scripts\Prerequisites"

CALL "C:\ProgramData\RuleStream\8.16.4\Batch Scripts\Prerequisites\shortcutCreator.bat"
regedit.exe /s "C:\ProgramData\RuleStream\8.16.4\Batch Scripts\Prerequisites\EnableLinkedConnections.reg"

RMDIR /S /Q "C:\ProgramData\RuleStream\8.16.4\Batch Scripts\Prerequisites"
PAUSE