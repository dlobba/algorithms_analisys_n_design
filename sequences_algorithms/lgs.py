import sys, copy

def define_lgs_array (lenX):
    return [0 for j in range(lenX)]

def draw_array (array):
    out = ""
    for i in array:
        out += str(i) + " "
    out += "\n"
    return out

def lgs(X):

    tempX = copy.copy(X)
    tempX.insert(0, None)
    c = define_lgs_array(len(tempX))
    m = len(tempX)

    max_ = 0
    for i in range(1, m):
        xi = tempX[i]
        temp = 0
        for s in range(i):
            xs = tempX[s]
            if xi > xs and temp < c[s]:
                temp = c[s]
        c[i] = 1 + temp
        if c[i] > max_:
            max_ = c[i]

    print draw_array(c)

    return max_

if __name__ == "__main__":
    print("This is a libray, load it as a module:\n\
            import lgs as l\n\
            l.lis(Seq)")
