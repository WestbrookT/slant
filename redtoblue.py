index = 0.5
r = int(255 * (1-index))
g = int(255 * index)
if (g > 128):
    g = 255-g

b = int(255 * index)

rhex = hex(r)
ghex = hex(g)
bhex = hex(b)
print(str(rhex)+str(ghex)+str(bhex))
