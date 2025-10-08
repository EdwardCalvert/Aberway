from aberway_background_code import create, update, main_loop
import time
import heapq
import random
import math


ColourFlip = False


screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)


# --- SET THESE VALUES TO AN EXAMPLE ---
startPos = 0
listOfNodesToPass = [34, 27, 17]
length = 758.97
error = 0.06


def path_update():
    ListOfNodeId = []  # set the value of this to the nodes that your path takes
    start = time.time_ns()  # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------

    def calculate_distance_between_nodeList_elements(from_node, to_node):

        pass

    def find_paths(start, path=[], current_length=0):
        path = path + [start]

        if current_length >= length - error and current_length <= length + error:
            print("=====>Found path:", path)

        if current_length > length + error:
            # print(f"Path too long: {current_length}")
            return

        neighbors = nodeList[start][3]
        # print(neighbors)
        for neighbor in neighbors:

            totalDist = 0
            for line in lineList:
                l = line[4]
                
                if l == [start, neighbor]:
                    # add the distance that has been traveled
                    if line[1] != None:
                        totalDist += math.dist(line[0], line[1])
                    else:
                        totalDist += math.dist(line[0][-1], line[0][0])
                    
                l.reverse()
                if l == [start, neighbor]:

                    # add the distance that has been traveled
                    if line[1] != None:
                        totalDist += math.dist(line[0], line[1])
                    else:
                        totalDist += math.dist(line[0][-1], line[0][0])


            if neighbor not in path:  # avoid cycles, if required
                find_paths(neighbor, path, current_length + totalDist)

    find_paths(0)

    ListOfNodeId = [0, 2, 10, 13, 11, 14, 15]
    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos,
           listOfNodesToPass, length, error, end - start)


path_update()
main_loop()
