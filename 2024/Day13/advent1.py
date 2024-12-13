import sys
import math 

def read_and_parse_file(file_path):
    """
    Reads a file containing button and prize sequences and parses it into a structured format.

    :param file_path: Path to the input file.
    :return: A list of dictionaries containing parsed data for each group.
    """
    import re

    # Define regular expressions to match button and prize lines
    button_pattern = r"Button ([A-Z]): X\+(-?\d+), Y\+(-?\d+)"
    prize_pattern = r"Prize: X=(-?\d+), Y=(-?\d+)"

    parsed_data = []

    with open(file_path, 'r') as file:
        current_group = {"buttons": {}, "prize": None}
        line_counter = 0

        for line in file:
            line_counter += 1
            line = line.strip()

            # Match button lines
            button_match = re.match(button_pattern, line)
            if button_match:
                button_name = button_match.group(1)
                x_offset = int(button_match.group(2))
                y_offset = int(button_match.group(3))
                current_group["buttons"][button_name] = {"X": x_offset, "Y": y_offset}

            # Match prize line
            prize_match = re.match(prize_pattern, line)
            if prize_match:
                x_prize = int(prize_match.group(1))
                y_prize = int(prize_match.group(2))
                current_group["prize"] = {"X": x_prize, "Y": y_prize}

            # Every 4 lines, assume the group is complete
            if line_counter % 4 == 0:
                parsed_data.append(current_group)
                current_group = {"buttons": {}, "prize": None}

        # Add the last group if it contains data
        if current_group["buttons"] or current_group["prize"]:
            parsed_data.append(current_group)

    return parsed_data

def compute_token(game):
    """
    Computes the number of times Button A and Button B should be pushed to reach the prize values.

    :param game: A dictionary containing button offsets and prize values.
    :return: A tuple (times_A, times_B) or None if no solution exists.
    """
    buttons = game.get("buttons", {})
    prize = game.get("prize", {})

    if not buttons or not prize:
        return 0

    x_target = prize.get("X")
    y_target = prize.get("Y")

    a_x = buttons.get("A", {}).get("X", 0)
    a_y = buttons.get("A", {}).get("Y", 0)
    b_x = buttons.get("B", {}).get("X", 0)
    b_y = buttons.get("B", {}).get("Y", 0)

    # Resolve equations to compute A and B
    try:
        A = (x_target - y_target * (b_x / b_y)) / (a_x - (b_x / b_y) * a_y)
        B = (x_target - y_target * (a_x / a_y)) / (b_x - (a_x / a_y) * b_y)
    except ZeroDivisionError:
        return 0

    token = math.floor(A * 3 + B)

    if 0.00001 > abs(A - int(A)) and 0.00001 > abs(B - int(B)):
        if 0 <= A < 100 and 0 <= B < 100:
            print(f"Token: {token}, A: {A}, B: {B}")
            return token
    return 0

# The length of the final list is printed as the result.
if __name__ == "__main__":
    """
    Main function to execute the script
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    parsed_data = read_and_parse_file(filename)
    print(parsed_data)

    tokens = 0
    for i, elem in enumerate(parsed_data):
        print(f"Processing group {i + 1}...")
        tokens += compute_token(elem)

    print(f"Result: {tokens}")
