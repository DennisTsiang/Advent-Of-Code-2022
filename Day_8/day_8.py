def find_number_of_visible_trees(grid: list[list[int]]):
    visible = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if row == 0 or row == len(grid) - 1 or col == 0 or col == len(
                    grid[row]) - 1:
                visible += 1
                continue
            tree = grid[row][col]
            up = max([grid[y][col] for y in range(0, row)])
            down = max(grid[y][col] for y in range(row + 1, len(grid)))
            right = max([grid[row][x] for x in range(col + 1, len(grid[row]))])
            left = max([grid[row][x] for x in range(0, col)])
            if tree > up or tree > down or tree > right or tree > left:
                visible += 1
    return visible


def compute_score(tree: int, trees: list[int]):
    score = 0
    for tree_view in trees:
        if tree_view < tree:
            score += 1
        else:
            score += 1
            break
    return score


def find_highest_scenic_score(grid):
    highest_score = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if row == 0 or row == len(grid) - 1 or col == 0 or col == len(
                    grid[row]) - 1:
                continue  # score would be 0 for edges
            tree = grid[row][col]
            up = [grid[y][col] for y in range(0, row)]
            up.reverse()
            up_score = compute_score(tree, up)

            down = [grid[y][col] for y in range(row + 1, len(grid))]
            down_score = compute_score(tree, down)

            right = [grid[row][x] for x in range(col + 1, len(grid[row]))]
            right_score = compute_score(tree, right)

            left = [grid[row][x] for x in range(0, col)]
            left.reverse()
            left_score = compute_score(tree, left)

            score = up_score * down_score * right_score * left_score
            highest_score = max(score, highest_score)
    return highest_score


input_text = open("input.txt", "r", encoding="utf-8").read().splitlines()
grid = []
for line in input_text:
    row = []
    for char in line:
        row.append(int(char))
    grid.append(row)
print(find_number_of_visible_trees(grid))
print(find_highest_scenic_score(grid))