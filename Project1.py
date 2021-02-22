import numpy as np

#defining the stack class
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

def removing_from_queue():
    check = queue1.remove()
    return check


def check_if_visited(check):
    for i in range(len(visited_list)):
        if check.current == visited_list[i].current:
            print("visited")
            return None
    visited_list.append(check)
    print("not visited")
    return check


#locates the zero element in the matrix called inside super_move_function
def locate_0(current):
    location = np.where(current == 0)
    return location[0][0], location[1][0]

def moveleft(node1):
    if locy == 0:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx][locy - 1]
        child[locx][locy - 1] = node1[locx][locy]
        #print(currentnode)
        return child


def moveright(node1):
    if locy != sh[1] -1:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx][locy + 1]
        child[locx][locy + 1] = node1[locx][locy]
        #print(currentnode)
        return child

def moveup(node1):
    if locx != 0:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx - 1][locy]
        child[locx - 1][locy] = node1[locx][locy]
        #print(currentnode)
        return child

def movedown(node1):
    if locx != sh[0]-1:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx + 1][locy]
        child[locx + 1][locy] = node1[locx][locy]
        #print(currentnode)
        return child
