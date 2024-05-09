def decimalToBinary(input_number):
    x = input_number
    binary_list = []
    while x > 0:
        if x % 2 != 0:
            binary_list.append('1')
        else:
            binary_list.append('0')
        print(binary_list,x)
        x = x // 2
    
    if input_number != 0:
        #binary_list.append('1')
        binary_list.reverse()
        binaryOutput = ''.join(binary_list)
    else:
        return 0
    return binaryOutput

input_number = int(input())
print(decimalToBinary(input_number))
