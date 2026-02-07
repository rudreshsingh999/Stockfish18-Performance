#!/usr/bin/env python3
"""
Stockfish 17 vs Stockfish 18 Tournament Manager
Runs 100 games with fast time control (0.5 seconds per move)
"""

import chess
import chess.engine
import os
import sys
import time
from pathlib import Path
from datetime import datetime
import json

class TournamentManager:
    def __init__(self, engine1_path, engine2_path, games=100, seconds_per_move=0.5):
        self.engine1_path = Path(engine1_path)
        self.engine2_path = Path(engine2_path)
        self.total_games = games
        self.seconds_per_move = seconds_per_move
        
        self.results = {
            'stockfish17_wins': 0,
            'stockfish18_wins': 0,
            'draws': 0,
            'games': []
        }
        
    def play_game(self, game_num, white_engine_path, black_engine_path, white_name, black_name):
        """Play a single game between two engines"""
        board = chess.Board()
        
        # Open engines
        white_engine = chess.engine.SimpleEngine.popen_uci(white_engine_path)
        black_engine = chess.engine.SimpleEngine.popen_uci(black_engine_path)
        
        # Set time limit per move
        time_control = chess.engine.Limit(time=self.seconds_per_move)
        
        moves_played = 0
        
        try:
            while not board.is_game_over():
                if board.turn == chess.WHITE:
                    result = white_engine.play(board, time_control)
                else:
                    result = black_engine.play(board, time_control)
                
                board.push(result.move)
                moves_played += 1
                
                # Progress indicator every 10 moves
                if moves_played % 10 == 0:
                    print(f"  Move {moves_played}...", end='\r')
            
            # Determine result
            outcome = board.outcome()
            if outcome.winner == chess.WHITE:
                winner = white_name
            elif outcome.winner == chess.BLACK:
                winner = black_name
            else:
                winner = "Draw"
            
            game_result = {
                'game_number': game_num,
                'white': white_name,
                'black': black_name,
                'winner': winner,
                'moves': moves_played,
                'termination': outcome.termination.name
            }
            
            return game_result
            
        finally:
            white_engine.quit()
            black_engine.quit()
    
    def run_tournament(self):
        """Run the complete tournament"""
        print("=" * 60)
        print("STOCKFISH 17 vs STOCKFISH 18 TOURNAMENT")
        print("=" * 60)
        print(f"Games: {self.total_games}")
        print(f"Time Control: {self.seconds_per_move} seconds per move")
        print(f"Estimated time per game: ~30-60 seconds")
        print("=" * 60)
        print()
        
        start_time = time.time()
        
        for game_num in range(1, self.total_games + 1):
            # Alternate colors each game
            if game_num % 2 == 1:
                white_path = self.engine1_path
                black_path = self.engine2_path
                white_name = "Stockfish 17"
                black_name = "Stockfish 18"
            else:
                white_path = self.engine2_path
                black_path = self.engine1_path
                white_name = "Stockfish 18"
                black_name = "Stockfish 17"
            
            print(f"Game {game_num}/{self.total_games}: {white_name} (White) vs {black_name} (Black)")
            
            game_result = self.play_game(game_num, white_path, black_path, white_name, black_name)
            
            # Update results
            self.results['games'].append(game_result)
            
            if game_result['winner'] == "Stockfish 17":
                self.results['stockfish17_wins'] += 1
            elif game_result['winner'] == "Stockfish 18":
                self.results['stockfish18_wins'] += 1
            else:
                self.results['draws'] += 1
            
            # Print game result
            print(f"  Result: {game_result['winner']} ({game_result['moves']} moves)")
            print(f"  Current Score - SF17: {self.results['stockfish17_wins']} | "
                  f"SF18: {self.results['stockfish18_wins']} | "
                  f"Draws: {self.results['draws']}")
            print()
        
        elapsed_time = time.time() - start_time
        self.print_final_results(elapsed_time)
        self.save_results()
    
    def print_final_results(self, elapsed_time):
        """Print final tournament results"""
        print()
        print("=" * 60)
        print("FINAL RESULTS")
        print("=" * 60)
        print(f"Stockfish 17 Wins: {self.results['stockfish17_wins']}")
        print(f"Stockfish 18 Wins: {self.results['stockfish18_wins']}")
        print(f"Draws: {self.results['draws']}")
        print(f"Total Games: {self.total_games}")
        print()
        
        sf17_score = self.results['stockfish17_wins'] + (self.results['draws'] * 0.5)
        sf18_score = self.results['stockfish18_wins'] + (self.results['draws'] * 0.5)
        
        print(f"Points (Win=1, Draw=0.5):")
        print(f"  Stockfish 17: {sf17_score}")
        print(f"  Stockfish 18: {sf18_score}")
        print()
        
        if sf17_score > sf18_score:
            print(f"Winner: Stockfish 17 (+{sf17_score - sf18_score})")
        elif sf18_score > sf17_score:
            print(f"Winner: Stockfish 18 (+{sf18_score - sf17_score})")
        else:
            print("Result: Tied!")
        
        print()
        print(f"Tournament Duration: {elapsed_time/60:.2f} minutes")
        print("=" * 60)
    
    def save_results(self):
        """Save results to JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tournament_results_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\nDetailed results saved to: {filename}")


def main():
    # Check if engine paths are provided
    if len(sys.argv) < 3:
        print("Usage: python chess_tournament.py <stockfish17_path> <stockfish18_path>")
        print("\nExample:")
        print("  python chess_tournament.py stockfish-17.exe stockfish-18.exe")
        sys.exit(1)
    
    engine1_path = sys.argv[1]
    engine2_path = sys.argv[2]
    
    # Verify engines exist
    if not os.path.exists(engine1_path):
        print(f"Error: Stockfish 17 not found at {engine1_path}")
        sys.exit(1)
    
    if not os.path.exists(engine2_path):
        print(f"Error: Stockfish 18 not found at {engine2_path}")
        sys.exit(1)
    
    # Create and run tournament
    # 0.5 seconds per move = fast games (~30-60 seconds each)
    # Adjust seconds_per_move if you want longer/shorter games
    tournament = TournamentManager(engine1_path, engine2_path, games=100, seconds_per_move=0.5)
    tournament.run_tournament()


if __name__ == "__main__":
    main()
