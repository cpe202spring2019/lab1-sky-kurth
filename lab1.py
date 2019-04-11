
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == []:
        return none
    elif int_list == None:
        raise ValueError
    else:
        highest = int_list[0]
        for i in int_list:
            if i > highest:
                highest = i
        return highest

def reverse_rec(int_list):   # must use recursion
    if int_list == None:
        raise ValueError
    if int_list == [] :
        return []
    else:
        return [int_list[-1]] + reverse_rec(int_list[:len(int_list)

def bin_search(target, low, high, int_list):  # must use recursion
    if int_list == None:
        raise ValueError
        
    test_index = int(low + (high - low) / 2)
    if int_list[test_index] == target:
        return test_index
    elif high - low == 1:
        if int_list[test_index + 1] == target:
            return test_index + 1
        else:
            return None
    elif int_list[test_index] > target:
        high = test_index
        return bin_search(target, low, high, int_list)
    elif int_list[int(high / 2)] < target:
        low = test_index
        return bin_search(target, low, high, int_list)
