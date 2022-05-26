def permutation(n, out, nbit_list):
    if n==0:
        nbit_list.append(out)
        return
    permutation(n-1, out+[0], nbit_list)
    permutation(n-1, out+[1], nbit_list)

n = 3
nbit_list = []
permutation(3, [], nbit_list)
print(nbit_list)
