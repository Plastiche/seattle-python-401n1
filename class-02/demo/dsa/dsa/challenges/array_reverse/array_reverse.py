# swap elements
# slice the last index and itterate backwards
# user a loop with range start at last element append to a new list
# pop and append
# .reverse()
# ::-1


def reverse_list1(new_list):
    """
    TThis function will reverse an array using swap method
    """
    for i in range(len(new_list)//2):
        new_list[i], new_list[-i-1] = new_list[-i-1], new_list[i]
    return new_list


def reverse_list2(new_list):
    """
    This function will reverse an array using a loop
    """
    answer = []
    for i in range(len(new_list) - 1, -1, -1):
        answer.append(new_list[i])
    return answer


def reverse_list3(new_list):
    """
    This function will reverse an array
    """
    new_list.reverse()
    return new_list


def reverse_list4(new_list):
    """
    This function will reverse an array
    """
    return new_list[::-1]


if __name__ == '__main__':
    print(reverse_list4([1, 2, 3, 4, 5]))
    print(reverse_list4([1, 2, 3, 4, 5, 6]))
    print(reverse_list4([1]))
    print(reverse_list4([]))

