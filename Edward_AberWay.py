from aberway_background_code import create, update, main_loop
import time
import heapq
import random
import math


ColourFlip = False


screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)


# --- SET THESE VALUES TO AN EXAMPLE ---
startPos = 47
listOfNodesToPass = [34, 19, 0, 12]
length = 2044.79
error = 0.14


def path_update():
    ListOfNodeId = []  # set the value of this to the nodes that your path takes
    start = time.time_ns()  # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------

    possible_paths = []
    def find_paths(start, path=[], current_length=0):
        path = path + [start]

        if current_length >= length - error and current_length <= length + error:
            possible_paths.append(path)
            return

        if current_length > length + error:
            return

        neighbors = nodeList[start][3]
        for neighbor in neighbors:
            dist =  math.dist(nodeList[start][0], nodeList[neighbor][0])
            if neighbor not in path:  # avoid cycles, if required
                find_paths(neighbor, path, current_length + dist)

    find_paths(startPos)

    for path in possible_paths:
        if set(listOfNodesToPass).issubset(path):
            print(f"Valid: {path}")
            ListOfNodeId = path
            pass
    #ListOfNodeId = [0, 2, 10, 13, 11, 14, 15]
    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos,
           listOfNodesToPass, length, error, end - start)


path_update()
main_loop()
