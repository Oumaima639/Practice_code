def binary_search(list,target):
    #for this method to be relevent the list has to be sorted 
    first = 0
    last = len(list) - 1

    while first < last :
        midpoint = (first + last)//2 #flour division operator
        if midpoint == target :
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else :
            last = midpoint - 1
    return None

trial = binary_search([1,2,3,4,5,6,7],5)
print(trial)

