
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
    if int_list == [] :
        return []
    else:
        return [int_list[-1]] + reverse_rec(int_list[:len(int_list)

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
