import random

def find_all_zero_groups(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    all_groups = []

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 0 and (x, y) not in visited:
                stack = [(x, y)]
                group = []

                while stack:
                    cx, cy = stack.pop()
                    if (cx, cy) in visited:
                        continue
                    visited.add((cx, cy))
                    group.append((cx, cy))

                    for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 0 and (nx, ny) not in visited:
                            stack.append((nx, ny))

                all_groups.append(group)

    return all_groups

def connect_zero_groups(matrix):
    rows, cols = len(matrix), len(matrix[0])

    while True:
        # Identify all zero groups in the current matrix
        zero_groups = find_all_zero_groups(matrix)
        
        # Stop when there's only one group of zeros
        if len(zero_groups) <= 1:
            break

        min_distance = float('inf')
        closest_pairs = []

        # Find the closest pairs of zeros between different groups
        for i in range(len(zero_groups)):
            for j in range(i + 1, len(zero_groups)):
                group1, group2 = zero_groups[i], zero_groups[j]
                
                for x1, y1 in group1:
                    for x2, y2 in group2:
                        distance = abs(x1 - x2) + abs(y1 - y2)
                        if distance < min_distance:
                            min_distance = distance
                            closest_pairs = [(x1, y1, x2, y2)]
                        elif distance == min_distance:
                            closest_pairs.append((x1, y1, x2, y2))

        # Randomly select a pair among the closest pairs
        x1, y1, x2, y2 = random.choice(closest_pairs)

        # Randomly choose a position along the line between (x1, y1) and (x2, y2)
        if abs(x1 - x2) > abs(y1 - y2):
            best_position = (random.randint(min(x1, x2), max(x1, x2)), y1)
        else:
            best_position = (x1, random.randint(min(y1, y2), max(y1, y2)))

        # Update the matrix by turning the selected `1` into a `0`
        if best_position:
            x, y = best_position
            matrix[x][y] = 0  # Turn the selected `1` into a `0` to connect groups

    return matrix
DefaultGrid = [
    [1,1,1,1,1,1],
    [1,0,0,0,0,1],
    [1,1,0,1,1,1],
    [1,0,0,0,0,1],
    [1,1,1,1,1,1],
    ]

print(connect_zero_groups(DefaultGrid))
[[1, 1, 1, 1, 1, 1], 
 [1, 0, 0, 0, 0, 1], 
 [1, 1, 0, 1, 1, 1], 
 [1, 0, 0, 0, 0, 1], 
 [1, 1, 1, 1, 1, 1]]