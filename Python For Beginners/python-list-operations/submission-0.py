def check_list_empty(my_list) -> bool:
    return not bool(len(my_list));


def check_element_in_list(my_list, element) -> bool:
    flag = None
    for i in range(0, len(my_list)):
        if my_list[i] == element:
            flag = True
    return bool(flag)
        


# do not modify below this line
print(check_list_empty([]))
print(check_list_empty([1, 2, 3]))

print(check_element_in_list([1, 2, 3], 1))
print(check_element_in_list([1, 2, 3], 4))

print(check_element_in_list(["Apple", "Banana", "Orange"], "Banana"))
print(check_element_in_list(["Apple", "Banana", "Orange"], "Grape"))
