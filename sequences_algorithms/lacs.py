import sys, copy

def define_lacs_matrix (lenX, lenY):
    return [[0 for i in range(lenY)] for j in range(lenX)]

def draw_matrix (matrix):
    out = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            out += str(matrix[i][j]) + " "
        out += "\n"
    return out

def col (x):
    if x < 5:
        return 'r'
    elif x > 10:
        return 'g'
    else:
        return 'b'

def lacs (X, Y):
    tempX = copy.copy(X)
    tempY = copy.copy(Y)
    # insert dumb values to align list to index 1 as start index
    tempX.insert(0, None)
    tempY.insert(0, None)

    # define a matrix c of len(X) rows and len(Y) columns and
    # intialize all elements to 0
    c = define_lacs_matrix(len(tempX), len(tempY))
    m = len(tempX)
    n = len(tempY)

    max_ = 0
    for i in range(1, m):
        xi = tempX[i]
        for j in range(1, n):
            yj = tempY[j]

            if yj == xi:
                temp = 0

                for s in range(1, i):
                    xs = tempX[s]
                    for t in range(1, j):
                        yt = tempY[t]
                        if temp < c[s][t] and col(xi) != col(xs):
                            temp = c[s][t]
                c[i][j] = 1 + temp
            else:
                c[i][j] = 0

            if c[i][j] > max_:
                max_ = c[i][j]

    print(draw_matrix(c))

    # be sure to put to get_lacs_sequence tempX
    # because it's a one based modified version
    # of X
    print str(get_lacs_sequence(c, tempX))
    return max_

# Given the lacs matrix and the first sequence
# give the lacs sequence by going through the lacs matrix
# and pushing to the sequence the first character which
# correspond to an increment in the matrix
def get_lacs_sequence (lacs_matrix, X):
    lacs_sequence = []
    increment = 0

    # we exclude 0
    for i in range(1, len(lacs_matrix)):
        for j in range(1, len(lacs_matrix[0])):
            if lacs_matrix[i][j] > increment:
                increment += 1
                lacs_sequence.append(X[i])

    return lacs_sequence


if __name__ == "__main__":
    print("This is a libray, load it as a module:\n\
            import lacs as l\n\
            l.lacs(Seq1, Seq2)")
