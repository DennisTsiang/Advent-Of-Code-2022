def update_tail(current_head: tuple[int, int], current_tail: tuple[int, int]):
    diff_x = current_head[0] - current_tail[0]
    diff_y = current_head[1] - current_tail[1]
    update_x = 1 if diff_x > 0 else -1 if diff_x < 0 else 0
    update_y = 1 if diff_y > 0 else -1 if diff_y < 0 else 0
    return (current_tail[0] + update_x, current_tail[1] + update_y)


def update_positions(current_head: tuple[int, int], tails: list[tuple[int, int]], direction: str, distance: int, visited_spots: set):
    for _ in range(distance):
        if direction == "U":
            current_head = (current_head[0], current_head[1] + 1)
        elif direction == "D":
            current_head = (current_head[0], current_head[1] - 1)
        elif direction == "L":
            current_head = (current_head[0] - 1, current_head[1])
        else:
            current_head = (current_head[0] + 1, current_head[1])
        prev_knot = current_head
        for index, knot in enumerate(tails):
            if (abs(prev_knot[0] - knot[0]) > 1) or (abs(prev_knot[1] - knot[1]) > 1):
                tails[index] = knot = update_tail(prev_knot, knot)
            prev_knot = knot
        visited_spots.add(tails[-1])
    return (current_head, tails)


def find_number_of_visited_spots(movements: list[str], tail_knots: int):
    visited_spots = set()
    visited_spots.add((0, 0))
    current_head = (0, 0)
    tail_rope = [(0, 0) for _ in range(tail_knots)]
    for line in movements:
        direction, distance = line.split()
        current_head, tail_rope = update_positions(current_head, tail_rope, direction, int(distance), visited_spots)
    return len(visited_spots)


file = open("input.txt", "r", encoding="utf-8")
input_text = file.read().splitlines()
file.close()
print(find_number_of_visited_spots(input_text, 1))
print(find_number_of_visited_spots(input_text, 9))