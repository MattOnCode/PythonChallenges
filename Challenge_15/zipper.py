def zipper(a, b):
    """
    Zips the two lists 'a' and 'b' together. The lists must be of
    equal length.
    :param a: The first list to be zipped.
    :param b: The second list to be zipped.
    :return: The newly generated list of 'a' and 'b' zipped.
    """
    if len(a) != len(b):
        print("Lists are not the same length!")
        return
    new_list = []
    for element in a:
        new_list.append([element, b[a.index(element)]])
    return new_list


# Testing the function
print(zipper([1, 2, 3, 4, 5], ['A', 'B', 'C', 'D', 'E']))
