"""
You have a table with all available goods in the store. The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first
argument and the whole data as the second one

Input: int and list of dicts. Each dicts has two keys "name" and "price"

Output: the same as the second Input argument.

EXAMPLE:
bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
]

bigger_price(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}]
"""


def bigger_price(num_of_returns: int, list_of_dicts: list) -> list:
    results_list = []
    while len(results_list) < num_of_returns:
        max_price = 0
        max_index = 0
        for index, dictionary in enumerate(list_of_dicts):
            if dictionary['price'] > max_price:
                max_price = dictionary['price']
                max_index = index
        results_list.append(list_of_dicts[max_index])
        list_of_dicts.pop(max_index)
    return results_list


def better_bigger_price(num_returns, list_of_dicts):
    return sorted(list_of_dicts, key=lambda d: d['price'], reverse=True)[:num_returns]
