def permutation(n, out, permutations):
    if n==0:
        permutations.append(out)
        return
    permutation(n-1, out+[0], permutations)
    permutation(n-1, out+[1], permutations)

n = 3
permutations = []
permutation(3, [], permutations)
print(permutations)
