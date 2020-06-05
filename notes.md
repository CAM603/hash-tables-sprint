# Hashing Functions

-   A function where the input is any data and the output is a number. Maps data to a number
-   Must be deterministic (consistent). The same input must return the same output
-   Different input data should return different numbers (not always)
-   Must return numbers that are within a specific range
-   To convert input data to an integer, hashing functions operate on the individual characters that make up the string
    -   We can encode strings into their bytes with .encode() method
-   Usually sum all the integer values and % the value by the size of the list
    -   This ensures the max return value is the last index of the list
-   Use hashing functions to map strings/data to an index in the list and then store a value
    -   We can in turn retrieve the value using the hash function

# Collision Resolution

-   Open addressing with linear probing: start at the collision location and move sequentially through the slots until there is an empty one.
    -   Method causes clustering when collisions occur in the same area. We want even distribution. You can minimize clustering by skipping slots when searching
    -   Limited to the size of the list
-   Chaning: Allow each slot to hold a reference to a collection (or chain) of items.
    -   Each slot is likely to have very few items so our operations are still efficient.

# Performance of Basic Hash Table Operations

-   Search: O(1)
-   Insert: O(1)
-   Delete: O(1)
-   Resizing: O(1)
-   The computation takes the same amount of time to search for an item in a list of 10 and for a list of 1000000
-   Worst case: all become O(n)
    -   This is if every hash table entry were placed inside a linked list that was referenced by a single index
-   Average case: O(1)
    -   If collisions are handled well, the hashing function spreads data evenly, and a low load factor is maintained

# Load Factor

-   The number of items stored in the hash table divided by the number of slots
-   As the load factor increases, so does the likelihood of a collision, which reduces the performance
-   Need to monitor the load factor and resize the hash table when it gets too large
-   When load factor is > 0.7

# Automatic Resizing

-   Hash table automatically resizes based on the load factor
-   Common to double the size of the hash table
-   When resizing, you need to re-insert all of the items into this new hash table
-   Each item has to be rerun through the hashing function because the hashing function takes into account the size of the hash table when determining the index that it returns
-   Resizing: O(1)
-   One way is to compute the load factor whenever an item is inserted or deleted. If too high or too low then you need to resize

# Various Use Cases

Use as a cache
Use as a lookup table
