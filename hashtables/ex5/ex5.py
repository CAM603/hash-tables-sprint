# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}

    for file in files:
        split_txt = file.split('/')[1:]

        for txt in split_txt:
            if not cache.get(txt):
                cache[txt] = []
            cache[txt].append(file)

    result = []

    for x in queries:
        if cache.get(x):
            if len(cache[x]) > 1:
                for path in cache[x]:
                    result.append(path)
            else:
                result.append(cache[x][0])

    return result


# files = []

# for i in range(10):
#     files.append(f"/dir{i}/file{i}")

# for i in range(10):
#     files.append(f"/dir{i}/dirb{i}/file{i}")

# queries = []

# for i in range(5):
#     queries.append(f"nofile{i}")

# queries += [
#     "file3",
#     "file2",
#     "file9",
#     "file8"
# ]

# print(finder(files, queries))
if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        'nofile'
    ]
    queries = [
        "foo",
        "qux",
        "baz",
        "nofile"
    ]
    print(finder(files, queries))
