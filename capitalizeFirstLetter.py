def palindrome(input_string):
    
    new = input_string[::-1]
    first = ''.join(input_string)
    last = ''.join(new)    
    if first == last:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

def palin(input_string):
    mid = len(input_string)//2
    last = len(input_string)-1

    for i in range(0,mid+1):
        if input_string[i] == input_string[last]:

            if i == mid:
                 return
            last = last-1    
            continue
    print("It is not palindrome")

input_string =   
palindrome(input_string)
palin(input_string)


palin  