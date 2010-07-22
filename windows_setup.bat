@echo off
set PYTHONPATH=%PYTHONPATH%;C:\Python26\Lib\site-packages
set PATH=%PATH%;C:\Python26;C:\Python26\Scripts
python setup.py install

> "%USERPROFILE%\Desktop\wtqt.bat" (
@echo.@echo off
@echo.set PYTHONPATH=%%PYTHONPATH%%;C:\Python26\Lib\site-packages
@echo.set PATH=%%PATH%%;C:\Python26;C:\Python26\Scripts
@echo.cmd 
)