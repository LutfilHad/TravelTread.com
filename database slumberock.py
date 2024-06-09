import pygame
import requests

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame with Ranking System")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define player properties
player_pos = [400, 300]
player_size = 50

# Function to add or update player in the database
def add_or_update_player(name, score):
    url = 'http://localhost:3000/add-or-update-player'
    data = {'name': name, 'score': score}
    response = requests.post(url, json=data)
    return response.json()

# Function to get the leaderboard
def get_leaderboard():
    url = 'http://localhost:3000/leaderboard'
    response = requests.get(url)
    return response.json()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Add or update player in the database when space is pressed
                response = add_or_update_player("Player1", 100)
                print(response)
            elif event.key == pygame.K_l:
                # Get the leaderboard when 'l' is pressed
                leaderboard = get_leaderboard()
                print("Leaderboard:")
                for player in leaderboard:
                    print(f"{player['name']}: {player['score']}")

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()