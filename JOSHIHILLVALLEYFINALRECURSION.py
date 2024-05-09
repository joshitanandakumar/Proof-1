'''

def joshirecursion(x):
    if x == 0:
        return 0
    else:
        print(x-1)
        return(joshirecursion(x - 1) )

input_num = int(input())
joshirecursion(input_num)

'''

def checkasc(input_list):

    if len(input_list) <= 1:
        return(True)
    if input_list[0] < input_list[1]:
        return checkasc(input_list[1:])
    else:
        return(False)
#input_list = [int(x) for x in input().split()]
#checkasc(input_list)


def checkdesc(input_list):
    
    if len(input_list) <= 1:
        return(True)
    if input_list[0] > input_list[1]:
        return checkdesc(input_list[1:])
    else:
        return(False)
#input_list = [int(x) for x in input().split()]
#checkdesc(input_list)

def hillvalleycheck(input_list):
    for i in range(2, len(input_list)-1):
        if checkasc(input_list[:i]) == True:
            '''
            if checkasc(input_list[i:]) == True:
                print('Not a hill nor valley.')
                break
            '''
            if checkdesc(input_list[i:]) == True:
                print('It is a hill')
                return
            else:
                continue

        elif checkdesc(input_list[:i]) == True:
            '''
            if checkdesc(input_list[i:]) == True:
                print('Not a hill nor valley.')
                break
            '''
            if checkasc(input_list[i:]) == True:
                print('It is a valley.')
                return
            else:
                continue
    print("It is neither hil nor valley")

input_list = [int(x) for x in input().split()]
hillvalleycheck(input_list)