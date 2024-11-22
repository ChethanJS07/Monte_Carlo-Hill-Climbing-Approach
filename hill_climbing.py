import numpy as np
from copy import deepcopy

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):  # Tile numbers 1 to 8
        x1, y1 = np.where(state == i)
        x2, y2 = np.where(goal == i)
        distance += abs(x1[0] - x2[0]) + abs(y1[0] - y2[0])  # Extract scalar values
    return distance

# Function to find possible moves
def find_moves(state):
    moves = []
    x, y = np.where(state == 0)
    x, y = x[0], y[0]  # Blank space (0) location
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Valid move
            new_state = deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

# Hill Climbing algorithm
def hill_climbing(initial_state, goal_state):
    current_state = np.array(initial_state)
    current_cost = manhattan_distance(current_state, goal_state)
    steps = [current_state]

    while current_cost != 0:
        next_states = find_moves(current_state)
        next_states_with_cost = [(state, manhattan_distance(state, goal_state)) for state in next_states]
        next_states_with_cost.sort(key=lambda x: x[1])  # Sort by heuristic value (cost)

        best_next_state, best_next_cost = next_states_with_cost[0]

        if best_next_cost < current_cost:
            current_state = best_next_state
            current_cost = best_next_cost
            steps.append(current_state)
        else:  # Stuck at local maxima or plateau
            return steps, False

    return steps, True

# Display function
def display_state(state):
    print("\n".join([" ".join(map(str, row)) for row in state]))
    print()

initial_state = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 0, 8]])

goal_state = np.array([[1, 2, 3],
                       [4, 5, 0],
                       [7, 8, 6]])

# Solve the puzzle
steps, success = hill_climbing(initial_state, goal_state)

# Print results
if success:
    print("Solution found!")
    for step in steps:
        display_state(step)
else:
    print("Failed to find solution. Stuck at a local maxima or plateau.")
    print("Steps taken:")
    for step in steps:
        display_state(step)

# Limitations
if not success:
    print("Analysis:")
    print("- Hill Climbing can get stuck at local maxima, plateaus, or ridges.")
    print("- It does not backtrack or explore alternative paths, limiting its ability to escape suboptimal states.")
    print("- Random restarts or stochastic approaches can mitigate these issues but are not part of basic Hill Climbing.")