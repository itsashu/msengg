REM make build an copy files

set TopDir=..\..\..\build
set WebDir= ..\..\..\build\web
if not exist %TopDir%\web md %TopDir%\web
if not exist %TopDir%\conf md %TopDir%\conf

echo === removing old build dir ====
if exist build rmdir /Q /S build

echo === building files ===
python setup.py || exit /B 1
echo === copying files ===


if not exist %TopDir%\conf\webappconfig.xml xcopy /Y webappconfig.xml %TopDir%\conf || exit /B 7
if not exist %WebDir%\static xcopy /Y /i /s /e static %WebDir%\static || exit /B 12
if not exist %WebDir%\templates xcopy /Y /i templates %WebDir%\templates || exit /B 13

