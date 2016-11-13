index = 0.5
r = int(255 * (1-index))
g = int(255 * index)
if (g > 128):
    g = 255-g

b = int(255 * index)

rhex = int(r,16)
ghex = int(g,16)
bhex = int(b,16)
print(str(rhex)+str(ghex)+str(bhex))
