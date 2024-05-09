'''
def sum_odd_numbers(input_list):
    if not input_list:
        return 0
    elif input_list[0] % 2 == 0:
        return sum_odd_numbers(input_list[1:])
    else:
        return input_list[0] + sum_odd_numbers(input_list[1:])

input_list = [int(x) for x in input().split()]
print(sum_odd_numbers(input_list))
'''



def oddEven(input_list):
    if not input_list:
        return 0
    elif input_list[0] % 2 != 0:
        return input_list[0] + oddEven(input_list[1:]) 
    else:
        return oddEven(input_list[1:]) - input_list[0]
    
input_list = [int(x) for x in input().split()]
print(oddEven(input_list))
        
print(djd )