def merge(list_one, list_two):
    """
    Takes two sorted lists and merges them in order to return a list that
    contains the contents of the two lists merged.
    :param list_one: The first sorted list of numbers.
    :param list_two: The second sorted list of numbers.
    :return: A list containing the values of te two lists merged together.
    """
    merged = []

    while len(list_one) > 0 and len(list_two) > 0:
        if list_one[0] < list_two[0]:
            merged.append(list_one.pop(0))
        else:
            merged.append(list_two.pop(0))

    merged = merged + list_one + list_two
    return merged


# Testing the function
listA = [1, 5, 6, 7]
listB = [2, 3, 8]
print("A = {}\nB = {}".format(listA, listB))
print("Merged list = {}".format(merge(listA, listB)))
