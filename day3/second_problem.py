

line_tokens = []
with open("input.txt", "r") as input:
    for line in input:
        line_tokens.append(list(line.strip()))

def column_majority(lines_tokens, column):
    sum = 0
    break_point = len(lines_tokens)/2
    for line in lines_tokens:
        sum += int(line[column])
    return sum, break_point


def filter_line_tokens(index, line_tokens, metric):
    sum, break_point = column_majority(line_tokens, index)
    target = ""
    if metric == "oxygen":
        target = "1" if sum >= break_point else "0"
    elif metric == "co2":
        target = "0" if sum >= break_point else "1"
    else:
        print("WARN >> Illegal metric: %s" % metric)
        exit(0)

    filtered_tokens = [tokens for tokens in line_tokens if tokens[index] == target]
    return filtered_tokens

def find_rating(line_tokens, metric):
    modified_tokens = line_tokens
    index = 0
    while len(modified_tokens) > 1:
        modified_tokens = filter_line_tokens(index, modified_tokens, metric)
        index += 1

    return int("".join(modified_tokens[0]), 2)

oxygen_rating = find_rating(line_tokens, "oxygen")
print("Oxygen Rating: %d" % oxygen_rating)
co2_scrubber_rating = find_rating(line_tokens, "co2")
print("CO2 Scrubber Rating: %d" % co2_scrubber_rating)

print("Product: %d" % (oxygen_rating*co2_scrubber_rating))

