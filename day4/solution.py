input = open("./input.txt")
xmas_array = []

def checkXmas(array):
    rows = len(array)
    cols = len(array[0])
    count = 0
    x_mas_count = 0
    
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_word(x, y, dx, dy):
        if not all(is_valid(x + i*dx, y + i*dy) for i in range(4)):
            return False
        word = ''.join(array[x + i*dx][y + i*dy] for i in range(4))
        return word == 'XMAS'
    
    def check_string(x, y, dx, dy):
        if not all(is_valid(x + i*dx, y + i*dy) for i in range(3)):
            return False
        
        chars = [array[x + i*dx][y + i*dy] for i in range(3)]
        forward = ''.join(chars)
        backward = ''.join(chars[::-1])
        return forward == 'MAS' or forward == 'SAM' or backward == 'MAS' or backward == 'SAM'

    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1

    for i in range(rows-2):
        for j in range(cols-2):
            diagonal1 = check_string(i, j, 1, 1)
            diagonal2 = check_string(i, j+2, 1, -1)
            
            if diagonal1 and diagonal2:
                x_mas_count += 1
    
    return count, x_mas_count

for line in input.readlines():
    xmas_array.append(line.strip("\n"))

print(checkXmas(xmas_array))
