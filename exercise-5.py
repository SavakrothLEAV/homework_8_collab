num = [5, 7, 10, 4, 2, 7, 8, 1, 3]

def reverse_ascending(num):
    #create a list that stores the values for returning
    answer = []

    #create a temporary list
    temp = []

    #add extra element to allow comparison the last element for the list
    num.append(num[-1])

    #Starting loop from 1 to compare to the previous element one by one
    for i in range(1, len(num)):
        if num[i] > num[i-1]:
            temp.append(num[i-1])
        else:
            temp.append(num[i-1])
            temp.sort(reverse=True)
            for i in temp:
                answer.append(i)
            temp.clear()

    return answer

print(reverse_ascending(num))
