def palindrome(input_list):
    print(input_list)
    if not input_list:
        return "palindrome"
    if input_list[0] != input_list[len(input_list)-1]:
        return "Not a palindrome"
    else:
        return(palindrome(input_list[1:-1]))


list_string = [x for x in input()]
print(palindrome(list_string))