from collections import deque

graph = dict()

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def has_mandarin(name):
    people_who_has_a_mandarin = ["peggy", "jonny", "claire"]
    return name in people_who_has_a_mandarin


def breadth_first_search(given_graph):
    queue = deque()
    queue += given_graph["you"]
    searched = []
    while queue:
        person = queue.popleft()
        if person not in searched:
            if has_mandarin(person):
                print(f"{person} has a mandarin!")
                return True
            else:
                queue += given_graph[person]
                searched.append(person)


def main():
    breadth_first_search(graph)


if __name__ == "__main__":
    main()
