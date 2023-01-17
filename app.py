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
        print(start)
        print(end)
        if target == list[middle]:
            print(start)
            print(end)
            return middle
        if target < list[middle]:
            print(start)
            print(end)
            end = middle - 1
        else:
            start = middle + 1        
            print(start)
            print(end)
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
target = 34

binarySearch(my_list, target)



















