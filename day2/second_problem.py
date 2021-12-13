
def parse_input_line(line):
    tokens = line.strip().split(' ')
    if len(tokens) > 2:
        print("WARNING >> Received too plentiful input: %s" % tokens)
    return tokens[0].strip(), int(tokens[1].strip())

depth = 0
horizontal_position = 0
aim = 0
with open("input.txt", "r") as input:
    for line in input:
        command, value = parse_input_line(line.strip())
        if command == "up":
            aim -= value
        elif command == "down":
            aim += value
        elif command == "forward":
            horizontal_position += value
            depth += aim * value
        else:
            print("WARNING >> Illegal command: %s" % command)

print("Program Completed:\n\tDepth: %d\n\tPosition: %d\n\tProduct: %d" % (depth, horizontal_position, depth*horizontal_position))
