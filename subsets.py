# cook your dish here

def get_subsets(inp, out, subsets):
    if not inp:
        subsets.append(out)
        return
    get_subsets(inp[1:], out+[inp[0]], subsets)
    get_subsets(inp[1:], out, subsets)

x = ["a","b","c"]
subsets = []
get_subsets(x, [], subsets)
print(subsets)

