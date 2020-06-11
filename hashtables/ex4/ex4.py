def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Loop through list
    # If positive, add to cache
    # If negative, change to positive
    cache = {}
    for num in a:
        num = abs(num)
        # if not cache.get(abs(num)):
        #     cache[abs(num)] = 1
        # cache[abs(num)] += 1
        if not num in cache.keys():
            cache[num] = 1
        else:
            cache[num] += 1

    my_list = [x[0] for x in list(cache.items()) if x[1] > 1]

    return my_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
