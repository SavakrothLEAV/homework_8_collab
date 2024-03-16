def replace_last(numbers):
    if len(numbers)<2:
        return numbers
    else:
        else:
        numbers.insert(0, numbers[-1])
        numbers.pop()
        return numbers
