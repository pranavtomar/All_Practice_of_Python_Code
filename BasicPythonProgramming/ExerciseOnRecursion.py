def human_pyramid(no_of_people):
    #remove pass and place the recursive code the you had written earlier for this function
    if no_of_people == 1: 
        return 50
    else:
        return 50 + 2 * human_pyramid(no_of_people-2)


def find_maximum_people(max_weight):
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable
    total_weight = 0
    n = 1
    while True:
        weight_added = human_pyramid(n)
        if total_weight + weight_added <= max_weight:
            total_weight += weight_added
            n += 2
        else:
            break
    return n-2

    

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)