input = open("./input.txt")

def createInputMap(input, map):
    first, second = input.strip("\n").split("|")
    if map.get(first) is None:
        map[first] = [second]
    else:
        map[first].append(second) 
    return

def correctInput(input_array, map):
    graph = {}
    all_pages = set(input_array)
    
    for page in all_pages:
        graph[page] = set()
    
    for page in all_pages:
        if page in map:
            for after_page in map[page]:
                if after_page in all_pages:
                    graph[page].add(after_page)
    
    def topological_sort():
        visited = set()
        temp = set()
        order = []
        
        def visit(page):
            if page in temp:
                return False
            if page in visited:
                return True
            
            temp.add(page)
            
            for next_page in graph[page]:
                if not visit(next_page):
                    return False
            
            temp.remove(page)
            visited.add(page)
            order.insert(0, page)
            return True
        
        for page in graph:
            if page not in visited:
                if not visit(page):
                    return None
        
        return order
    
    correct_order = topological_sort()
    if correct_order is None:
        return 0
    
    final_order = [page for page in correct_order if page in input_array]
    
    return int(final_order[len(final_order) // 2])

def chcekInput(input, map):
    input_array = input.strip("\n").split(",")

    for i in range(len(input_array) - 1):
        check = input_array[i + 1:-1]
        map_array = map.get(input_array[i])
        if input_array[i] != input_array[-1] and map_array is None:
            return 0
        for number in check:
            if map_array == None or number not in map_array:
                return 0
    
    return int(input_array[len(input_array) // 2])

def checkWrongInput(input, map):
    input_array = input.strip("\n").split(",")
    
    is_correct = True
    for i in range(len(input_array) - 1):
        check = input_array[i + 1:]
        map_array = map.get(input_array[i])
        if map_array is not None:
            for number in check:
                if number not in map_array:
                    return correctInput(input_array, map)

    return 0


page_map = {}
verify = False
count = 0
wrong_count = 0

for line in input.readlines():
    if line == "\n":
        verify = True
        continue
    if verify == False:
        createInputMap(line, page_map)
    else:
        count += chcekInput(line, page_map)
        wrong_count += checkWrongInput(line, page_map)

print(count)
print(wrong_count)