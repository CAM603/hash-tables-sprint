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
            if len(answer) == 1:
                if len(cache[limit - weight]) > 1:
                    answer.insert(0, cache[weight][1])
                elif answer[0] >= cache[weight][0]:
                    answer.append(cache[weight][0])
                elif answer[0] and answer[0] < cache[weight][0]:
                    answer.insert(0, cache[weight][0])
            elif len(answer) == 0:
                answer.append(cache[weight][0])

    if len(answer) == 2:
        return answer
    else:
        return None


my_weights = [4, 4]


print(get_indices_of_item_weights(my_weights, 2, 8))
