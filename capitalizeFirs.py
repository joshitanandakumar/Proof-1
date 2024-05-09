'''def capitalize(input_string):
    for x in range(input_string[0]):
        x.upper()
        firstLetter = x.upper()
        return firstLetter
    rest = len(input_string)
    
    

capitalize(input_string)
input_string = input()
'''

def capitalizeFirst(word):
    word[0] = word[0].upper()
    newWord = ''.join(word)
    return newWord
       
word = [x for x in input()]
print(capitalizeFirst(word))