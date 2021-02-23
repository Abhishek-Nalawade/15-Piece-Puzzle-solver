import numpy as np

#defining the queue class to use as a data structure
class queue():
    def __init__(self):
        self.pending = list()

    def add(self, child):
        self.pending.insert(0, child)

    def remove(self):
        if self.pending:
            return self.pending.pop()
        return None

    def peek(self):
        if self.pending:
            return self.pending[-1]

    def size(self):
        return len(self.pending)

#created node class in order to save current node and it's parent
class node():
    def __init__(self, current, parent):
        self.current = current
        self.parent = parent


def convert_matrix_to_string(matrix):
    final = str()
    for i in range(sh[0]):
        for j in range(sh[1]):
            if matrix[i][j] < 10:
                st = '0'
                st1 = '{}'.format(matrix[i][j])
                final = final + st + st1
            else:
                st1 = '{}'.format(matrix[i][j])
                final = final + st1
    return final


def convert_string_to_matrix(string1):
    li = list()
    a = str()
    count = 0
    for i in string1:
        a = a + i
        count += 1
        if count%2 == 0:
            li.append(int(a))
            a = ''
            count = 0
    matrix = np.array(li)
    matrix = np.reshape(matrix, (sh[0], sh[1]))
    return matrix


#removes from the queue
def removing_from_queue():
    check = queue1.remove()
    return check


#checking if the node has been visited previously and then appending to the visited_list
def check_if_visited(check):
    for i in range(len(visited_list)):
        if check.current == visited_list[i].current:
            #print("visited")
            return None
    visited_list.append(check)
    #print("not visited")
    return check


#locates the zero element in the matrix called inside super_move_function
def locate_0(current):
    location = np.where(current == 0)
    return location[0][0], location[1][0]


#this function performs actions and gets children and calls the locate_0 function as well
def super_move_function(currentnode):

    def moveleft(node1):
        child = node1.copy()
        child[locx][locy] = node1[locx][locy - 1]
        child[locx][locy - 1] = node1[locx][locy]
        #print(currentnode)
        return child

    def moveright(node1):
        child = node1.copy()
        child[locx][locy] = node1[locx][locy + 1]
        child[locx][locy + 1] = node1[locx][locy]
        return child

    def moveup(node1):
        child = node1.copy()
        child[locx][locy] = node1[locx - 1][locy]
        child[locx - 1][locy] = node1[locx][locy]
        return child

    def movedown(node1):
        child = node1.copy()
        child[locx][locy] = node1[locx + 1][locy]
        child[locx + 1][locy] = node1[locx][locy]
        return child

    node = convert_string_to_matrix(currentnode.current)
    locx, locy = locate_0(node)
    new_child = list()
    if locy != 0:
        new_child.append(moveleft(node))
    if locy != sh[1] -1:
        new_child.append(moveright(node))
    if locx != 0:
        new_child.append(moveup(node))
    if locx != sh[0]-1:
        new_child.append(movedown(node))

    return new_child, node


#compares new children with goal state and adds them to the queue
def compare_with_goal(children, parent):
    child_str = list()
    parent_str = convert_matrix_to_string(parent)

    #converting matrix to string to check with goal state
    for i in children:
        child_str.append(convert_matrix_to_string(i))

    for child in child_str:
        if goal == child:
            print("\n Goal has been reached \n")
            return child, parent_str
        else:
            queue1.add(node(child, parent_str))


#main body of the program
visited_list = list()
goal = '01020304050607080910111213141500'
test_case_1 = np.array([[1, 2, 3, 4],[5, 6, 0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]])
test_case_2 = np.array([[1, 0, 3, 4],[5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]])
test_case_3 = np.array([[0, 2, 3, 4],[1, 5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]])
test_case_4 = np.array([[5, 1, 2, 3],[0, 6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]])
test_case_5 = np.array([[1, 6, 2, 3], [9, 5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]])
sh = test_case_1.shape
initial_str = convert_matrix_to_string(test_case_5)
first_node = node(initial_str, None)
queue1 = queue()
queue1.add(first_node)


while True:
    new_parent = None
    while new_parent is None:
        new_node = removing_from_queue()
        new_parent = check_if_visited(new_node)
    children_list, parent = super_move_function(new_parent)
    child_parent = compare_with_goal(children_list, parent)
    if child_parent is not None:
        break

parent_info = child_parent[1]
#print(len(visited_list))


#tracing back the parent node
route = list()
while parent_info is not None:
    for i in range(len(visited_list)):
        if parent_info == visited_list[i].current:
            parent_info = visited_list[i].parent
            route.append(i)
            break

file = list()

print("The path from the given test case to the goal state is as follows:")
#prints the path and also creates a list in order to write the path to the nodePath.txt file
for i in range(len(route)):
    z = visited_list[route[len(route)-1-i]].current
    mtx = convert_string_to_matrix(z)
    print(mtx)
    counter = 0
    for i in mtx:
        for j in i:
            file.append(str(j))
            file.append("  ")
            counter += 1
            if counter%4 == 0:
                file.append("\n")
            if counter == 16:
                file.append("\n")
                file.append("\n")


#creates a list of required matrices to write in the nodePath.txt file
goal_mtx = convert_string_to_matrix(goal)
print(goal_mtx)
counter = 0
for i in goal_mtx:
    for j in i:
        file.append(str(j))
        file.append("  ")
        counter += 1
        if counter%4 == 0:
            file.append("\n")


#attaches the goal state to the nodePath.txt file
fh = open("nodePath_test_case_5.txt", 'w')
for i in file:
    fh.write(i)
fh.close()
