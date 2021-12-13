

line_tokens = []
with open("input.txt", "r") as input:
    for line in input:
        line_tokens.append(list(line.strip()))

binary_sum = [0]*len(line_tokens[0])
for binary in line_tokens:
    for index, digit in enumerate(binary):
        binary_sum[index] += int(digit)

break_point = len(line_tokens)/2
gamma_rate = "".join(["1" if x > break_point else "0" for x in binary_sum])
gamma_rate_decimal = int(gamma_rate, 2)
epsilon_rate = "".join(["1" if x < break_point else "0" for x in binary_sum])
epsilon_rate_decimal = int(epsilon_rate, 2)

print("Binary Sum: %s" % binary_sum)
print("Gamma: %s, which is %d" % (gamma_rate, gamma_rate_decimal))
print("Epsilon: %s, which is %d" % (epsilon_rate, epsilon_rate_decimal))
print("Gamma x Epsilon product = %d" % (gamma_rate_decimal*epsilon_rate_decimal))
