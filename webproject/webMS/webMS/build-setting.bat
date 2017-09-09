REM make build an copy files

set TopDir=..\..\..\..\..\build

if not exist %TopDir%\webMS md %TopDir%\webMS
if not exist %TopDir%\webMS\apache md %TopDir%\webMS\apache

echo === removing old MedNet dir ====
if exist webMS rmdir /Q /S webMS

echo === building files ===
python Settingsetup.py || exit /B 1



