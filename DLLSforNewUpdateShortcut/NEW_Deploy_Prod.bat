@ECHO OFF
MD C:\ProgramData\RuleStream\8.17.0\Applications\Prod
COPY /B /V /Y /Z "\\internal.hussmann.com\sites\apps\Rulestream\Config\PROD\Deployment\*.dll"  "C:\ProgramData\RuleStream\8.17.0\Applications\Prod" /B
PAUSE
EXIT