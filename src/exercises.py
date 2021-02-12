def reverse_list(input_list):
    new_lst = input_list[::-1] 
    return new_lst

def count_digits(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return Count
