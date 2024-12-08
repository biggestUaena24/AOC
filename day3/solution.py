import re
file = open("input.txt")


def getMultiplication(input):
    pattern = r"mul\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    matches = re.findall(pattern, input)
    return sum(int(x) * int(y) for x, y in matches)

def getMultiplicationCondition(input):
    enabled = True
    sections = re.split(r"(do\(\)|don't\(\))", input)
    sum = 0
   
    for section in sections:
        if section == "do()":
            enabled = True
        elif section == "don't()":
            enabled = False

        if enabled:
            sum += getMultiplication(section)
    return sum

mul_sum = 0
mul_sum2 = 0
input = ""

for line in file.readlines():
    input += line

mul_sum += getMultiplication(input)
mul_sum2 += getMultiplicationCondition(input)

print(mul_sum)
print(mul_sum2)