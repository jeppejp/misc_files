import math


with open("100points.txt", "w") as fp:
    for i in range(0,100):
        fp.write("%d %d\n"%(i, int(math.sin(i)*60)))
