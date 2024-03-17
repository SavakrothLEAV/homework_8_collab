def remove_all_after(numbers, n):
    size = len(numbers)

    if size == 0:
        return numbers
    
    else: 

        if n in numbers:
            result = []
            ind = numbers.index(n)
            result = numbers[:ind]
            return result 

        else: 
            return numbers
   
