#!/usr/bin/ env python3
# 05/03/2020
# @uthor Drake Greeott
# Create a program that allows you to store the data for players of a game.

class Player():
    def __init__(self, playerID=0, name=None, wins=0, losses=0,
                 ties=0, games=0):
        self.playerID = playerID
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.games = (self.wins + self.losses + self.ties)

        
