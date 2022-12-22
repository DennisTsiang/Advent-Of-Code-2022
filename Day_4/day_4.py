def is_assignment_pair_full_of_dupe_work(pair1, pair2):
    (pair1_min_range, pair1_max_range) = pair1
    (pair2_min_range, pair2_max_range) = pair2
    if (pair2_min_range >= pair1_min_range and pair2_max_range <= pair1_max_range) or \
        (pair1_min_range >= pair2_min_range and pair1_max_range <= pair2_max_range):
        return True
    return False


def find_number_of_duped_work(pairs):
    count = 0
    for pair in pairs:
        if is_assignment_pair_full_of_dupe_work(pair[0], pair[1]):
            count += 1
    print(count)


def contains_overlapping_work(pair1, pair2):
    (pair1_min_range, pair1_max_range) = pair1
    (pair2_min_range, pair2_max_range) = pair2
    if is_assignment_pair_full_of_dupe_work(pair1, pair2) or \
        (pair2_min_range >= pair1_min_range and pair2_min_range <= pair1_max_range) or \
        (pair2_max_range >= pair1_min_range and pair2_max_range <= pair1_max_range):
        return True
    return False


def find_number_of_overlapping_work(pairs):
    count = 0
    for pair in pairs:
        if contains_overlapping_work(pair[0], pair[1]):
            count += 1
    print(count)


text = open("input.txt", "r")
pairs = []
for line in text:
    (pair1, pair2) = line.strip().split(",")
    (pair1_min_range, pair1_max_range) = map(int, pair1.split("-"))
    (pair2_min_range, pair2_max_range) = map(int, pair2.split("-"))
    pairs.append([(pair1_min_range, pair1_max_range),
                  (pair2_min_range, pair2_max_range)])

find_number_of_duped_work(pairs)
find_number_of_overlapping_work(pairs)
