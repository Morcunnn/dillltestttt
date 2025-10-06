@echo off
setlocal enabledelayedexpansion

rem Detect Python launcher
set "PY_CMD=py -3"
%PY_CMD% --version >nul 2>nul || set "PY_CMD=python"

echo [1/4] Creating virtual environment (.venv)...
%PY_CMD% -m venv .venv || (echo Failed to create venv & exit /b 1)

echo [2/4] Installing dependencies...
".venv\Scripts\python.exe" -m pip install --upgrade pip || exit /b 1
".venv\Scripts\python.exe" -m pip install -r requirements.txt || exit /b 1
".venv\Scripts\python.exe" -m pip install pyinstaller || exit /b 1

echo [3/4] Building onefile executable...
".venv\Scripts\pyinstaller.exe" --noconsole --onefile --name "TEDIL" --hidden-import=tkinter "run_tedil.py" || exit /b 1

echo Built: dist\TEDIL.exe

echo [4/4] Creating installer (optional, requires NSIS 'makensis' in PATH)...
where makensis >nul 2>nul
if %errorlevel%==0 (
  makensis /DAPP_VERSION=1.0.0 installer.nsi || exit /b 1
  echo Installer created: dist\TEDIL_Setup_1.0.0.exe
) else (
  echo NSIS not found. To create installer, install NSIS and re-run this script.
)

echo Done.
exit /b 0
