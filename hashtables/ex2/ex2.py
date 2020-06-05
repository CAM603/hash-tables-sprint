#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source  # starting airport
        self.destination = destination  # next airport


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = []
    # key = starting location
    # value = destination location
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # loop through tickets
    # start with the ticket whose source is None
    # Prev is ticket with None as source
    # Cur is ticket with key that matches prev's destination
    prev = cache['NONE']
    cur = cache[prev]

    for _ in range(length):
        route.append(prev)
        prev = cur
        cur = cache[cur]

    return route


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))
