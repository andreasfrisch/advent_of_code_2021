import math

with open("input.txt", "r") as input:
    increase_count = 0
    line_count = 0
    previous_measurement = math.inf
    for line in input:
        line_count += 1
        measurement = int(line.strip())
        if measurement > previous_measurement:
            increase_count += 1
        previous_measurement = measurement

    print("Numbers increased %d times" % increase_count)
    print("%d lines traversed" % line_count)
