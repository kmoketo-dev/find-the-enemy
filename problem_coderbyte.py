def find_closest_enemy(game_grid):
    num_rows = len(game_grid)
    num_cols = len(game_grid[0]) if num_rows > 0 else 0

    player_position = None
    enemy_positions = []

    for row in range(num_rows):
        for col in range(num_cols):
            if game_grid[row][col] == 1:
                player_position = (row, col)
            elif game_grid[row][col] == 2:
                enemy_positions.append((row, col))

    if not enemy_positions:
        return 0

    distances_to_enemies = []

    for enemy_position in enemy_positions:

        direct_horizontal_dist = abs(player_position[1] - enemy_position[1])
        wrapped_horizontal_dist = num_cols - direct_horizontal_dist
        min_horizontal_dist = min(direct_horizontal_dist, wrapped_horizontal_dist)

        direct_vertical_dist = abs(player_position[0] - enemy_position[0])
        wrapped_vertical_dist = num_rows - direct_vertical_dist
        min_vertical_dist = min(direct_vertical_dist, wrapped_vertical_dist)

        total_distance = min_horizontal_dist + min_vertical_dist
        distances_to_enemies.append(total_distance)

    return min(distances_to_enemies)
