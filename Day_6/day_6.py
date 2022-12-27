def find_marker(marker_size: int, input: str):
    for i in range(0, len(input) - marker_size):
        buffer = input[i:i + marker_size]
        charactersSet = set(buffer)
        if (len(charactersSet) == marker_size):
            return i + marker_size


def find_start_of_packet_marker(input: str):
    PACKET_MARKER_SIZE = 4
    return find_marker(PACKET_MARKER_SIZE, input)


def find_start_of_message_marker(input: str):
    MESSAGE_MARKER_SIZE = 14
    return find_marker(MESSAGE_MARKER_SIZE, input)


input = open("input.txt", "r", encoding="utf-8").read().split("\n")
for line in input:
    print(find_start_of_packet_marker(line))
    print(find_start_of_message_marker(line))
