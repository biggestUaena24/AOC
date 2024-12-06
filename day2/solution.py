def checkSafe(array):
    if all(array[i] < array[i + 1] for i in range(len(array) - 1)):
        pass
    elif all(array[i] > array[i + 1] for i in range(len(array) - 1)):
        pass
    else:
        return False
    
    for i in range(len(array) - 1):
        diff = abs(array[i + 1] - array[i])
        if diff < 1 or diff > 3:
            return False

    return True

def checkSafeTolerant(array):
    if checkSafe(array):
        return True

    for i in range(len(array)):
        reduced_array = array[:i] + array[i + 1:]
        if checkSafe(reduced_array):
            return True

    return False

    


file = open("./input.txt")
safe = 0
safe_tolerate = 0

for line in file.readlines():
    data = line.split()
    data = [int(num) for num in data]
    
    safe_check = checkSafe(data)
    safe_tolerate_check = checkSafeTolerant(data)

    if safe_check:
        safe += 1
    if safe_tolerate_check:
        safe_tolerate += 1

print(safe, safe_tolerate)
