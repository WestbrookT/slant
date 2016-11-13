index = 0.5
r = int(255 * (1-index))
g = int(255 * index)
if (g > 128):
    g = 255-g

b = int(255 * index)

rhex = format(r,'x')
ghex = format(g,'x')
bhex = format(b,'x')
print(str(rhex)+str(ghex)+str(bhex))
