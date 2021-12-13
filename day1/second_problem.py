from math import inf

inputs = []
with open("input.txt", "r") as input:
    for line in input:
        measurement = int(line.strip())
        inputs.append(measurement)

current_measurement = inf
count_measurements = 0
count_increases = 0
for i in range(len(inputs)-2):
    measurement = sum(inputs[i:i+3]) # The last number in a slice is not included
    if measurement > current_measurement:
        print("Sum %d of %s is larger than %d" % (measurement, inputs[i:i+3], current_measurement))
        count_increases += 1
    count_measurements += 1
    current_measurement = measurement

print("Measurements increased %d times" % count_increases)
print("%d measurements in total" % count_measurements)
