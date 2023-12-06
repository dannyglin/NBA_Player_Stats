import requests

def get_player_stats(player_name):
    # Format the player's name for the API request
    formatted_name = player_name.replace(' ', '_')

    # URL for the basketball-reference.com API
    url = f"https://www.balldontlie.io/api/v1/players?search={formatted_name}"

    # Make a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['data']:
            player_id = data['data'][0]['id']
            player_info_url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}"

            # Get player's season averages
            player_stats_response = requests.get(player_info_url)
            if player_stats_response.status_code == 200:
                stats_data = player_stats_response.json()
                if stats_data['data']:
                    player_stats = stats_data['data'][0]
                    points_per_game = player_stats['pts']
                    assists_per_game = player_stats['ast']
                    rebounds_per_game = player_stats['reb']
                    field_goal_percentage = player_stats['fg_pct']

                    # Display player statistics
                    print(f"Player: {player_name}")
                    print(f"- Points per game: {points_per_game}")
                    print(f"- Assists per game: {assists_per_game}")
                    print(f"- Rebounds per game: {rebounds_per_game}")
                    print(f"- Field goal percentage: {field_goal_percentage}%")
                else:
                    print("No statistics found for this player.")
            else:
                print("Failed to fetch player statistics.")
        else:
            print("Player not found.")
    else:
        print("Failed to fetch player information.")

# Get user input for player name
player_name_input = input("Please input a basketball player's name: ")

# Call the function with the provided player name
get_player_stats(player_name_input)
