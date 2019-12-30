#!/usr/bin/python


def divide_number(num, divide_by):
    return num / divide_by


divider_lam = lambda my_number, divider: my_number / divider

print(divider_lam(10, 2))

my_list = ["34", "12", "4452", "78", "9"]
my_list.sort(key=lambda x: int(x[len(x)-1]))
print(my_list)

num_list = [1, 2, 3, 4, 5]
filtered_list = filter(lambda x: x/2, num_list)
print(list(filtered_list))


# TODO
# for x = [(1, 2), (4, 7), (9,10), ....]
# return all tuples which their sum is divided by 3

def get_divs_by_3(list_of_tuples):
    return list(filter(lambda x: (x[0] + x[1]) % 3 == 0, list_of_tuples))


some_tuple = [(1, 2), (4, 7), (9,10), (4, 5)]
print(get_divs_by_3(some_tuple))
