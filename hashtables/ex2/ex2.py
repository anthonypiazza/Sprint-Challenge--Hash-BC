#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    target = None

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        if ticket.source == "NONE":
            target = ticket.destination
            del route[0]
            route.append(ticket.destination)
    
    while route[0] is None:
        destination = hash_table_retrieve(hashtable, target)
        target = destination
        del route[0]
        route.append(destination)

    return route
