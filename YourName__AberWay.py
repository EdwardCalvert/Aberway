from aberway_background_code import create, update, main_loop
import time
import heapq
import random


ColourFlip = False

    
screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)


# --- SET THESE VALUES TO AN EXAMPLE ---
startPos = 0
listOfNodesToPass = [10,11,14]
length = 676.75
error = 0.06

def path_update():
    ListOfNodeId = [] #set the value of this to the nodes that your path takes
    start = time.time_ns() # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------

    import math

    # local aliases from outer scope
    start_node = startPos
    required_nodes = listOfNodesToPass[:]  # list of ints
    target_length = length
    tol = error

    # quick handle: if no required nodes, just try to reach end (assume end is last in required list?)
    # The code assumes 'start' and 'end' are provided. In your starter you gave only startPos and a listOfNodesToPass.
    # We will treat the last element of required_nodes as end if that's intended; otherwise we assume end is the last required node.
    if len(required_nodes) == 0:
        # nothing required: trivial shortest-path style; but we don't have an explicit separate 'end' variable.
        # We'll return empty path (no moves).
        ListOfNodeId = []
        end = time.time_ns()
        # ---------- ---------- END OF YOUR CODE ---------- ----------
        end = time.time_ns()
        update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error, end - start)
        return

    # In the problem description earlier you had a start and an end; the starter code doesn't include an explicit `end` var.
    # We'll treat the last required node as the final destination to be visited (common pattern). If you have a different end,
    # replace 'final_goal' with the correct node id.
    final_goal = required_nodes[-1]  # treat last required node as destination
    required_set = set(required_nodes)

    # Build adjacency using lineList weights (symmetric)
    adj = {i: [] for i in range(len(nodeList))}
    edge_weight = {}
    for line in lineList:
        pair = line[4]
        u, v = pair[0], pair[1]
        w = float(line[5])
        edge_weight[(u, v)] = w
        edge_weight[(v, u)] = w
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Map required nodes to bit indices for mask
    req_index = {}
    for i, n in enumerate(sorted(required_set)):
        req_index[n] = i
    req_count = len(req_index)

    # helper: mask for a set of required nodes
    def mask_of(node, mask):
        if node in req_index:
            return mask | (1 << req_index[node])
        return mask

    # Heuristic: bias to be near proportional length according to fraction of required nodes visited.
    # If zero required nodes remain, heuristic is abs(remaining_length_to_target).
    def heuristic(current_length, visited_mask):
        visited_count = bin(visited_mask).count("1")
        # fraction target we expect to have reached by visiting visited_count required nodes
        # +1 denominator avoids division by zero if req_count = 0
        fraction = (visited_count) / max(1, req_count)
        expected_length_so_far = fraction * target_length
        return abs(current_length - expected_length_so_far)

    # Priority queue: (priority, current_length, node, visited_mask, parent_key)
    # We'll store parent mapping keyed by (node, mask, length_rounded) to reconstruct path
    pq = []
    start_mask = 0
    start_mask = mask_of(start_node, start_mask)
    start_len = 0.0
    start_len_r = round(start_len, 2)
    start_key = (start_node, start_mask, start_len_r)
    start_priority = heuristic(start_len, start_mask)
    heapq.heappush(pq, (start_priority, start_len, start_node, start_mask))

    # parent and visited bookkeeping
    parent = {}  # key: (node,mask,length_r) -> (prev_node, prev_mask, prev_length_r)
    seen_best = {}  # best (minimal) length achieved for (node,mask); used to prune worse paths
    # Use a small epsilon for float comparisons when storing best lengths
    EPS = 1e-6

    found = False
    goal_state = None

    # limit iterations to avoid runaway in pathological cases
    MAX_ITERS = 5_000_000
    iters = 0

    while pq and iters < MAX_ITERS:
        iters += 1
        priority, cur_len, node, mask = heapq.heappop(pq)

        # Discretize length for state keys
        cur_len_r = round(cur_len, 2)
        state_key = (node, mask)

        # prune: if we already reached (node,mask) with a length that is strictly better (closer to expected)
        prev_best = seen_best.get(state_key)
        if prev_best is not None and cur_len >= prev_best - EPS:
            continue
        seen_best[state_key] = cur_len

        # Check goal: visited all required nodes & at destination & length within tolerance
        visited_all = (mask == ( (1 << req_count) - 1 ))
        if visited_all and node == final_goal:
            if abs(cur_len - target_length) <= tol:
                # success
                goal_state = (node, mask, cur_len_r)
                found = True
                break
            # else: continue exploring to find a length within tolerance

        # Expand neighbors
        for (nbr, w) in adj[node]:
            new_len = cur_len + w
            # prune if new_len exceeds target + tol (we never want to go that far unless you allow overshoot)
            # But because we might approach target exactly by going longer then shorter isn't possible (paths accumulate),
            # so prune if exceed. This keeps search manageable.
            if new_len > target_length + tol:
                continue

            new_mask = mask_of(nbr, mask)
            new_len_r = round(new_len, 2)

            # parent key for reconstruction
            child_key = (nbr, new_mask, new_len_r)
            parent[child_key] = (node, mask, cur_len_r)

            # priority: combine heuristics:
            # 1) how close current length is to expected fraction (encourage matching)
            # 2) small additive term favoring shorter paths so we don't explore extremely long detours
            h = heuristic(new_len, new_mask)
            pr = h + 0.01 * new_len  # small tie-breaker by length

            heapq.heappush(pq, (pr, new_len, nbr, new_mask))

    # Reconstruct path if found
    if found and goal_state is not None:
        node_g, mask_g, len_g = goal_state
        path_rev = []
        cur = goal_state
        while True:
            cur_node, cur_mask, cur_len_r = cur
            path_rev.append(cur_node)
            if cur_node == start_node and cur_mask == start_mask and round(0.0,2) == round(0.0,2):
                break
            prev = parent.get(cur)
            if prev is None:
                # try to stop if we reached start differently (defensive)
                break
            cur = prev
        path_rev.reverse()
        # update ListOfNodeId with path excluding the starting node because `update` prepends startPos
        if len(path_rev) >= 1 and path_rev[0] == start_node:
            ListOfNodeId = path_rev[1:]
        else:
            ListOfNodeId = path_rev

    else:
        # not found: fall back to a simple greedy route connecting required nodes sequentially (best-effort)
        # This will at least produce a contiguous route that visits required nodes in given order.
        ListOfNodeId = []
        cur = start_node
        for req in required_nodes:
            # move along adjacency by always choosing neighbor that reduces Euclidean distance to target req (greedy)
            # This is naive but ensures contiguity.
            # We'll run simple BFS to find a shortest hop path (by edge count) from cur to req.
            from collections import deque
            q = deque()
            q.append(cur)
            prev_map = {cur: None}
            found_bfs = False
            while q and not found_bfs:
                x = q.popleft()
                if x == req:
                    found_bfs = True
                    break
                for (y, _) in adj[x]:
                    if y not in prev_map:
                        prev_map[y] = x
                        q.append(y)
            if found_bfs:
                # reconstruct
                temp = []
                at = req
                while at is not None:
                    temp.append(at)
                    at = prev_map[at]
                temp.reverse()
                # append everything except current node (cur) because it's already in path
                if temp and temp[0] == cur:
                    ListOfNodeId.extend(temp[1:])
                else:
                    ListOfNodeId.extend(temp)
                cur = req
            else:
                # cannot reach required node, skip
                cur = req

        # final ListOfNodeId should end at final_goal; ensure it does
        if not ListOfNodeId or ListOfNodeId[-1] != final_goal:
            ListOfNodeId.append(final_goal)



    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error, end - start)

path_update()
main_loop()
