# Stockfish 17 vs 18 Tournament - Quick Fix Guide

## The Problem You Had
The old version had inconsistent parameter names causing a TypeError.

## This Version is Fixed!
- Clean, tested code with consistent parameter naming
- Uses `seconds_per_move=0.5` throughout
- Games will finish in 30-60 seconds each
- Total tournament time: 50-100 minutes for 100 games

## Quick Setup

### 1. Install Python (if needed)
- Download from https://www.python.org/downloads/
- **CHECK "Add Python to PATH" during installation!**
- Restart Command Prompt after installing

### 2. Install chess library
Open Command Prompt and run:
```
pip install chess
```

### 3. Download Stockfish Engines
**Stockfish 17:**
- Go to: https://github.com/official-stockfish/Stockfish/releases/tag/sf_17
- Download: `stockfish-windows-x86-64-avx2.zip`
- Extract and rename the .exe to `stockfish-17.exe`
- Put it in this folder

**Stockfish 18:**
- Go to: https://github.com/official-stockfish/Stockfish/releases/tag/sf_18
- Download: `stockfish-windows-x86-64-avx2.zip`
- Extract and rename the .exe to `stockfish-18.exe`
- Put it in this folder

### 4. Run Tournament
Double-click: `run_tournament.bat`

OR from Command Prompt:
```
python chess_tournament.py stockfish-17.exe stockfish-18.exe
```

## Adjusting Game Speed

To change how long each game takes, edit `chess_tournament.py` line 210:

```python
tournament = TournamentManager(engine1_path, engine2_path, games=100, seconds_per_move=0.5)
```

Change `seconds_per_move`:
- `0.1` = Ultra-fast (10-20 sec/game)
- `0.5` = Fast (30-60 sec/game) ← **default**
- `1.0` = Medium (1-2 min/game)
- `2.0` = Slower (2-3 min/game)
- `5.0` = Very slow (5-8 min/game)

## What You'll See

The tournament will:
- Run 100 games (alternating colors for fairness)
- Show live progress for each game
- Display running scores
- Save detailed results to JSON when done
