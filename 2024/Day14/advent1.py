import sys
import math 


def read_robots_from_file(file_path):
    """
    Read a file containing robot data and create a list of Robot instances.

    Each line in the file should be formatted as:
    p=X,Y v=VX,VY

    :param file_path: Path to the input file.
    :return: List of Robot instances.
    """
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                start_position = parts[0].split('=')[1]
                velocity = parts[1].split('=')[1]

                start_x, start_y = map(int, start_position.split(','))
                velocity_x, velocity_y = map(int, velocity.split(','))

                robots.append(Robot(start_x, start_y, velocity_x, velocity_y))
    return robots

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

class Robot:
    def __init__(self, start_x, start_y, velocity_x, velocity_y):
        """
        Initialize the Robot with a starting position and velocity.

        :param start_x: Initial X position of the robot.
        :param start_y: Initial Y position of the robot.
        :param velocity_x: Velocity in the X direction.
        :param velocity_y: Velocity in the Y direction.
        """
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.vx = velocity_x
        self.vy = velocity_y
        self.quadrant = None

    def move(self):
        """
        Update the position of the robot based on its velocity.
        """
        self.x += self.vx
        self.y += self.vy

    def reset_position(self):
        """
        Reset the robot's position to its starting point.
        """
        self.x = self.start_x
        self.y = self.start_y

    def update_quadrant(self, wide, tall):
        if self.x < int(wide/2):
            if self.y > int(tall/2) :
                self.quadrant = "SW"
            elif self.y < int(tall/2):            
                self.quadrant = "NW"
            else:
                self.quadrant="line"
        elif self.x > int(wide/2):
            if self.y > int(tall/2) :
                self.quadrant = "SE"
            elif self.y < int(tall/2):     
                self.quadrant = "NE"
            else:
                self.quadrant="line"
        else:
            self.quadrant="line"

    def __str__(self):
        """
        Return a string representation of the robot's current state.
        """
        return f"Robot(Position: ({self.x}, {self.y}), Velocity: ({self.vx}, {self.vy}, Quadrant: {self.quadrant}))"

def one_sec_movement(robot, wide, tall):
    """
    Compute the robot's position in the next simulation step.
    If the robot goes beyond the bounds (wide, tall, or 0), it loops to the other side.

    :param robot: The Robot instance to simulate.
    :param wide: The width of the simulation area.
    :param tall: The height of the simulation area.
    """
    robot.x = (robot.x + robot.vx) % wide
    robot.y = (robot.y + robot.vy) % tall

    robot.update_quadrant(wide, tall)

def print_robots(robots, wide, tall):
    """
    Print a drawing of the simulation area with robots' positions.

    Each position in the grid will show:
      - '.' if no robot is present.
      - The number of robots present at that position.

    :param robots: List of Robot instances.
    :param wide: The width of the simulation area.
    :param tall: The height of the simulation area.
    """
    grid = [[0 for _ in range(wide)] for _ in range(tall)]

    # Count robots in each position
    for robot in robots:
        grid[robot.y][robot.x] += 1

    # Print the grid
    for row in grid:
        print("".join(str(cell) if cell > 0 else '.' for cell in row))

if __name__ == "__main__":
    """
    Main function to execute the script
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    robots = read_robots_from_file(filename)
    for robot in robots:
        print(robot)

    sec = 100
    wide= 101
    tall= 103
    #print_robots(robots, wide, tall)
    for i in range(0, sec):
        print(f" number of sec : {i+1}")
        for robot in robots:
            one_sec_movement(robot, wide, tall)
            #print(robot)
    print_robots(robots, wide, tall)

    #for robot in robots:
    #    print(robot)
    totNE =0
    totSE =0
    totNW =0
    totSW =0
    for robot in robots:
        if robot.quadrant == "NE":
            totNE +=1
        if robot.quadrant == "SE":
            totSE +=1
        if robot.quadrant == "NW":
            totNW +=1
        if robot.quadrant == "SW":
            totSW +=1
        else:
            "ERROR"

    print(f"NW: {totNW}")
    print(f"NE: {totNE}")
    print(f"SW: {totSW}")
    print(f"SE: {totSE}")
    print(f"Result: {totNE*totSE*totNW*totSW}")
