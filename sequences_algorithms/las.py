import sys, copy

def define_las_array (lenX):
    return [0 for j in range(lenX)]

def col (x):
    if x < 5:
        return 'r'
    elif x > 10:
        return 'g'
    else:
        return 'b'


def draw_array (array):
    out = ""
    for i in array:
        out += str(i) + " "
    out += "\n"
    return out

def las(X):

    tempX = copy.copy(X)
    tempX.insert(0, None)
    c = define_las_array(len(tempX))
    m = len(tempX)

    max_ = 0
    for i in range(1, m):
        xi = tempX[i]
        temp = 0
        for h in range(1, i):
            xh = tempX[h]
            if temp < c[h] and col(xi) != col(xh):
                temp = c[h]
        c[i] = 1 + temp

        if max_ < c[i]:
            max_ = c[i]
    print(draw_array(c))
    return max_

if __name__ == "__main__":
    print("This is a libray, load it as a module:\n\
            import las as l\n\
            l.las(Seq)")
