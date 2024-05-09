def duplicate(input_list):
    x = 0
    #input_list.sort()
    print(input_list)
    while (True):

        count = input_list.count(input_list[x])
        if count > 1:
            
            while (count > 1):
                input_list.remove(input_list[x])
                count = count-1
        print(x, input_list)
        if x == (len(input_list) - 2):
            break
        x = x+1
        
    return input_list

input_list = [int(x) for x in input().split()]
print(duplicate(input_list))


   