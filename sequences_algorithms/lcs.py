import sys, copy

def define_lcs_matrix (lenX, lenY):
    return [[0 for i in range(lenY)] for j in range(lenX)]

def draw_matrix (matrix):
    out = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            out += str(matrix[i][j]) + " "
        out += "\n"

    return out

def lcs (X, Y):
    tempX = copy.copy(X)
    tempY = copy.copy(Y)
    # insert dumb values to align list to index 1 as start index
    tempX.insert(0, 0)
    tempY.insert(0, 0)

    # define a matrix c of len(X) rows and len(Y) columns and
    # intialize all elements to 0
    c = define_lcs_matrix(len(tempX), len(tempY))
    m = len(tempX)
    n = len(tempY)

    for i in range(1, m):
        for j in range(1, n):

            xi = tempX[i]
            yj = tempY[j]
            if xi == yj:
                c[i][j] = 1 + c[i - 1][j - 1]
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    print draw_matrix(c)

    return c[m - 1][n - 1]

if __name__ == "__main__":
    print("This is a libray, load it as a module:\n\
            import lcs as l\n\
            l.lcs(Seq1, Seq2)")
