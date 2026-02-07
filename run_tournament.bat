@echo off
echo ========================================
echo Stockfish 17 vs 18 Tournament Manager
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Check if chess library is installed
python -c "import chess" >nul 2>&1
if errorlevel 1 (
    echo Installing required chess library...
    pip install chess
    if errorlevel 1 (
        echo ERROR: Failed to install chess library
        pause
        exit /b 1
    )
)

REM Check if Stockfish engines exist
if not exist "stockfish-17.exe" (
    echo ERROR: stockfish-17.exe not found in current directory
    echo Please download Stockfish 17 and place it here
    echo See README.md for instructions
    pause
    exit /b 1
)

if not exist "stockfish-18.exe" (
    echo ERROR: stockfish-18.exe not found in current directory
    echo Please download Stockfish 18 and place it here
    echo See README.md for instructions
    pause
    exit /b 1
)

echo All checks passed! Starting tournament...
echo.
echo This will run 100 games with 0.5 seconds per move
echo Estimated time: 50-100 minutes (games are ~30-60 sec each)
echo.
echo Press Ctrl+C to cancel, or
pause

python chess_tournament.py stockfish-17.exe stockfish-18.exe

echo.
echo Tournament complete!
pause
