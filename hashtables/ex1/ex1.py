def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    answer = []
    # Loop through weights
    for i in range(len(weights)):
        # if not in cache store it
        # key = weight
        # value = weights list index
        if not cache.get(weights[i]):
            cache[weights[i]] = []
        cache[weights[i]].append(i)

    for weight in weights:
        if cache.get(limit - weight):
            # if there is an index in answer already
            if len(answer) == 1:
                # if there is a nested value for the key
                if len(cache[limit - weight]) > 1:
                    # if index value in answer is greater
                    # insert the index after
                    if answer[0] >= cache[weight][1]:
                        answer.append(cache[weight][1])
                    elif answer[0] < cache[weight][1]:
                        answer.insert(0, cache[weight][1])
                # if index value in answer is greater
                # add new index after it
                elif answer[0] >= cache[weight][0]:
                    answer.append(cache[weight][0])
                # if index value in answer is less
                # add new index before it
                elif answer[0] and answer[0] < cache[weight][0]:
                    answer.insert(0, cache[weight][0])
            # if answer is empty
            elif len(answer) == 0:
                answer.append(cache[weight][0])
    # if there are two indexes in answer
    # we have an answer!
    if len(answer) == 2:
        return answer
    # else there is no solution!
    else:
        return None


my_weights = [4, 4]


print(get_indices_of_item_weights(my_weights, 2, 8))
