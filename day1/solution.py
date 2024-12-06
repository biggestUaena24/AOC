# Reading input
file = open("./input.txt")

# Getting the first and second list from input
first_location = []
second_location = []

for line in file.readlines():
    temp = line.split()
    first_location.append(int(temp[0]))
    second_location.append(int(temp[1]))

first_location.sort()
second_location.sort()

# Part 1 and Part 2
total_distance = 0
similarity_score = 0
for i in range(len(first_location)):
    total_distance += abs(first_location[i] - second_location[i])
    similarity_score += first_location[i] * second_location.count(first_location[i])

print(total_distance)
print(similarity_score)