no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]

def unique_list(l):
#complete the function's body to return the unique list of numbers
    list=[]
    for x in no_list:
        if x not in list:
            list.append(x)
    return sorted(list)

print(unique_list(no_list))
