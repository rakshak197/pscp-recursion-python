n=5
k=4
index = 0
inp = list(range(1, n+1))
print(inp)

def jos(inp, index):
    if  len(inp) == 1:
        return inp
    index = (index + k)% len(inp)
    print(inp[index])
    inp.pop(index)
    jos(inp, index)

jos(inp, index)

print(inp)