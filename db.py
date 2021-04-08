#!/usr/bin/ env python3
# 05/03/2020
# @uthor Drake Greeott
# Create a program that allows you to store the data for players of a game.

import sqlite3
from contextlib import closing

from business import Player


def connect():
    global conn
    # connect to the database and set the row factory
    conn = sqlite3.connect("player_db.sqlite")
    conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_player(row):
    return Player(row["playerID"], row["name"], row["wins"], row["losses"], row["ties"])

def get_stats():
    with closing(conn.cursor()) as c:
        query = '''SELECT * from Player
                    ORDER BY wins DESC'''
        c.execute(query)
        results = c.fetchall()

    player = []
    for row in results:
           player.append(make_player(row))
    return player  
        

def add_player(new_add):
    sql = '''INSERT INTO Player (name, wins, losses, ties)
                    VALUES (?, ?, ?, ?)'''

    # execute an INSERT statemnet
    with closing(conn.cursor()) as c:
        c.execute(sql, (new_add.name, new_add.wins, new_add.losses, new_add.ties))
        conn.commit()

def delete_player(name):
    # execute a DELETE statement
    with closing(conn.cursor()) as c:
        sql = '''DELETE FROM Player
                 WHERE name = ?'''
        c.execute(sql, (name,))
        conn.commit()

