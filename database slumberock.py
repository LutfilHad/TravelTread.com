import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('slumberock_game.db')
cursor = conn.cursor()

# Create Players table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Players (
    player_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
def add_player(name, email):
    conn = sqlite3.connect('slumberock_game.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Players (name, email) VALUES (?, ?)
    ''', (name, email))
    conn.commit()
    conn.close()

# Create Scores table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Scores (
    score_id INTEGER PRIMARY KEY,
    player_id INTEGER,
    score INTEGER,
    game_mode TEXT,
    score_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES Players (player_id)
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

# Adding a new player
add_player('Ali', 'ali@example.com')
add_player('abu', 'abu@example.com')

# Adding scores for players
add_score(1, 1500, 'Single Player')
add_score(2, 2000, 'Multiplayer')
add_score(1, 1800, 'Multiplayer')

# Retrieving high scores
high_scores = get_high_scores(5)
for score in high_scores:
    print(score)

# Commit the changes and close the connection
conn.commit()
conn.close()