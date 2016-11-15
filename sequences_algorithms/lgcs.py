import sys, copy

def define_lgcs_matrix (lenX, lenY):
    return [[0 for i in range(lenY)] for j in range(lenX)]

def draw_matrix (matrix):
    out = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            out += str(matrix[i][j]) + " "
        out += "\n"

    return out

def lgcs (X, Y):
    tempX = copy.copy(X)
    tempY = copy.copy(Y)
    # insert dumb values to align list to index 1 as start index
    tempX.insert(0, None)
    tempY.insert(0, None)

    # define a matrix c of len(X) rows and len(Y) columns and
    # intialize all elements to 0
    c = define_lgcs_matrix(len(tempX), len(tempY))
    m = len(tempX)
    n = len(tempY)

    # remember that the range(from, to) function generates
    # all the number from "from" INCLUDED and "to" ESCLUDED
    max_ = 0
    for i in range(1, m):
        xi = tempX[i]
        for j in range(1, n):
            yj = tempY[j]
            if xi != yj:
                c[i][j] = 0
            else:
                temp = 0
                for s in range(1, i):
                    xs = tempX[s]
                    for t in range(1, j):
                        yt = tempY[t]
                        if xs < xi and temp < c[s][t]:
                            temp = c[s][t]
                c[i][j] = 1 + temp
            if max_ < c[i][j]:
                max_ = c[i][j]
    print(draw_matrix(c))
    return max_

if __name__ == "__main__":
    print("This is a libray, load it as a module:\n\
            import lgcs as l\n\
            l.lcs(Seq1, Seq2)")
