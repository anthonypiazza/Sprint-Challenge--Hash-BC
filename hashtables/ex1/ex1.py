#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if length <=1:
        return None
    
    else:
        for i in range(0, len(weights)):
            current_weight = weights[i]
            hash_table_insert(ht, current_weight, i)
        
        for i in range(0, len(weights)):
            current_weight = weights[i]
            target_key_value = limit - current_weight
            solution = hash_table_retrieve(ht, target_key_value)

            if solution:
                if solution >= i:
                    return (solution, i)
                else:
                    return (i, solution)
                    
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
