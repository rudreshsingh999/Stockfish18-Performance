# Stockfish 17 vs 18 Tournament

## Quick Setup

### 1. Install chess library
Open Command Prompt and run:
```
pip install chess
```

### 2. Download Stockfish Engines
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

## What You'll See

The tournament will:
- Run 100 games (alternating colors for fairness)
- Show live progress for each game
- Display running scores
- Save detailed results to JSON when done
