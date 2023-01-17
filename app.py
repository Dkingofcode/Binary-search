# a function that takes a list and target parameter
# multiple variables : middle, start, end, steps
# recursion or while loop
# increase steps each time a split is done
# conditions to track target position

def binarySearch(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Steps", steps, ":" , str(list[start:end+1]))

        steps = steps +  1
        middle = (start + end) // 2

        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1        
     
    return -1





















