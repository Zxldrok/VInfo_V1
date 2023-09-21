@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "PYTHON_EXE=%SCRIPT_DIR%runtime\python.exe"
set "SCRIPT_FILE=%SCRIPT_DIR%main.py"

echo "Chemin de l'interpréteur Python : %PYTHON_EXE%"
echo "Chemin du fichier main.py : %SCRIPT_FILE%"

"%PYTHON_EXE%" "%SCRIPT_FILE%"

if errorlevel 1 (
    echo "Une erreur s'est produite."
) else (
    echo "Exécution terminée avec succès."
)

endlocal
