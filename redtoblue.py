def indextohex(index):
    r = int(255 * (1-index))
    g = int(255 * index)
    if (g > 128):
        g = 255-g
    b = int(255 * index)
    rhex = format(r,'02x')
    ghex = format(g,'02x')
    bhex = format(b,'02x')
    return(str(rhex)+str(ghex)+str(bhex))

print(indextohex(0))
print(indextohex(.2))
print(indextohex(.5))
print(indextohex(.8))
print(indextohex(1))
