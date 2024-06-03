import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('slumberock_game.db')
cursor = conn.cursor()

# Create Players table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

def add_player(name):
    conn = sqlite3.connect('slumberock_game.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Players (name) VALUES (?)
    ''', (name,))
    conn.commit()
    conn.close()

# Create Scores table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Scores (
    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    score INTEGER,
    game_mode TEXT,
    score_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES Players(player_id)
)
''')

def add_score(player_id, score, game_mode):
    conn = sqlite3.connect('slumberock_game.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Scores (player_id, score, game_mode) VALUES (?, ?, ?)
    ''', (player_id, score, game_mode))
    conn.commit()
    conn.close()

def get_high_scores(limit=10):
    conn = sqlite3.connect('slumberock_game.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT Players.name, Scores.score, Scores.game_mode, Scores.score_date
    FROM Scores
    JOIN Players ON Scores.player_id = Players.player_id
    ORDER BY Scores.score DESC
    LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Create Characters table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_name TEXT NOT NULL
)
''')

def add_character(character_name):
    conn = sqlite3.connect('slumberock_game.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Characters (character_name) VALUES (?)
    ''', (character_name,))
    conn.commit()
    conn.close()

# Adding a new player
add_player('Ali')
add_player('Abu')

# Adding scores for players
add_score(1, 1500, 'Single Player')
add_score(2, 2000, 'Multiplayer')
add_score(1, 1800, 'Multiplayer')

# Adding characters for players to choose
add_character('Character 1')
add_character('Character 2')
add_character('Character 3')

# Retrieving high scores
high_scores = get_high_scores(5)
for score in high_scores:
    print(score)

# Commit the changes and close the connection
conn.commit()
conn.close()