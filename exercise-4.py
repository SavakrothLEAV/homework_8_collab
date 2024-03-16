def chunking_by(numbers, chunck):
    
    chunck_list = []
    
    for i in range(0, len(numbers), chunck):
        
        chunck_list.append(numbers[i:i + chunck])
    
    return chunck_list
print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
print(chunking_by([3, 4, 5], 1))