
# Class definition for Race
class Race:
    # Initialization function
    def __init__(self, time, distance):
        # Time taken for the race
        self.time = time
        # Distance to beat
        self.distance_to_beat = distance
        # Minimum time to hold
        self.min_time_to_hold = 0
        # Minimum time check infimum
        self.min_time_check_inf = [0]
        # Minimum time check supremum
        self.min_time_check_sup = [time]
        # Maximum time to hold
        self.max_time_to_hold = time
        # Maximum time check infimum
        self.max_time_check_inf = [0]
        # Maximum time check supremum
        self.max_time_check_sup = [time]

    # Compute the number of possible winning
    def number_of_possible_winning(self):
        return self.max_time_to_hold - self.min_time_to_hold + 1

    # Check if the distance is beaten
    def is_beaten(self, distance):
        return distance > self.distance_to_beat

    # Check if the distance is just beaten
    def is_just_beaten(self, time_holding):
        return not self.is_beaten(self.compute_distance(time_holding - 1))

    # Check if the distance is beaten just now
    def is_beaten_just(self, time_holding):
        return self.is_beaten(self.compute_distance(time_holding - 1))

    # Compute the distance
    def compute_distance(self, speed):
        return speed * (self.time - speed)

    # Look for the infimum
    def look_inf(self):
        time_holding = int((min(self.min_time_check_sup) + max(self.min_time_check_inf)) / 2)
        while time_holding in self.min_time_check_inf:
            time_holding += 1
        distance_t0 = self.compute_distance(time_holding)
        distance_t1 = self.compute_distance(time_holding + 1)

        if distance_t1 - distance_t0 >= 0 and not self.is_beaten(distance_t0):
            self.min_time_check_inf.append(time_holding)
            self.look_inf()

        elif distance_t1 - distance_t0 >= 0 and self.is_beaten(distance_t0):
            if self.is_just_beaten(time_holding):
                self.min_time_to_hold = time_holding
                return
            else:
                self.min_time_check_sup.append(time_holding)
                self.look_inf()

        elif distance_t1 - distance_t0 < 0:
            self.min_time_check_sup.append(time_holding)
            self.look_inf()

    # Look for the supremum
    def look_sup(self):
        time_holding = int((min(self.max_time_check_sup) + max(self.max_time_check_inf)) / 2)
        while time_holding in self.max_time_check_inf:
            time_holding += 1
        distance_t0 = self.compute_distance(time_holding)
        distance_t1 = self.compute_distance(time_holding + 1)

        if distance_t1 - distance_t0 < 0 and self.is_beaten(distance_t0):
            self.max_time_check_inf.append(time_holding)
            self.look_sup()

        elif distance_t1 - distance_t0 < 0 and not self.is_beaten(distance_t0):
            if self.is_beaten_just(time_holding):
                self.max_time_to_hold = time_holding - 1
                return
            else:
                self.max_time_check_sup.append(time_holding)
                self.look_sup()

        elif distance_t1 - distance_t0 >= 0:
            self.max_time_check_inf.append(time_holding)
            self.look_sup()

# Test cases
#race = Race(71530, 940200)
race = Race( 54817088, 446129210351007)
race.look_inf()
race.look_sup()
tot = race.number_of_possible_winning()

print("The multiplication of all the possible winnings is : %s" % tot)
