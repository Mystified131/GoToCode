@ECHO OFF
MD C:\ProgramData\RuleStream\8.16.4\Applications\Prod
COPY /B /V /Y /Z "\\internal.hussmann.com\sites\apps\Rulestream\Config\PROD\Deployment\*.dll"  "C:\ProgramData\RuleStream\8.16.4\Applications\Prod" /B
PAUSE
EXIT