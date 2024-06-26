print("Creating Hash Table...")

graph = {}

graph["you"] = ["Alice", "Bob", "Claire"]
graph["Alice"] = ["Peggy"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Peggy"] = []
graph["Anuj"] = []
graph["Thom"] = []
graph["Jonny"] = []

# print(graph)

# for i in graph:
    # print(i)
    # print("\n")

# Queue / Dequeu in action. It adds and removes from a Hash Table in FIFO order (First In, First Out)

from collections import deque

search_q = deque()
search_q += graph["you"]

def person_is_seller(name):
    return name[-1] == "m" # If the person name's ends [-1] with an -m, then we say its a Seller

while search_q: # While its not empty...
    person = search_q.popleft() # Grabs the first item to the left (First In, First Out)
    if person_is_seller(person):
        print(person + " is a seller!")
    else: 
        print("This person (" + person + ") is not a seller")
        search_q += graph[person] # Adds the nodes from that person to the queue. And since it takes from the left, the order is not modified (we want to first check all first degree nodes)

# However this has a big problem. We can see that Peggy is added twice because its in the relationships of Alice but also Bob. This could lead to an infinite loop
# To handle this kind of situation, we need to make sure to somehow mark each person as "already searched" when we iterate through them
# A Set is a good data structure for this task since duplicates are not allowed

print("----------------------")

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a seller!")
                return True
            else:
                print(person + " is not a seller")
                search_queue += graph[person]
                searched.add(person)
        print(searched)
    return False

search("you")









