def kth_symbol_in_grammer(n, k):
    """Given a grammar, find the kth symbol in the grammar.
    Grammer: 0 -> 01, 1 -> 10
    N=1:
    Grammer: 0
    N=2:
    Grammer: 01
    N=3:
    Grammer: 0110
    N=4:
    Grammer: 01101001
    Args:
        n (int): Nth string in grammer
        k (int): kth symbol in the string

    Returns:
        bool: Nth string, kth symbol in the grammer
    """
    if n==1 and k==1:
        return 0
    mid = pow(2, n-1)//2
    if k <=mid:
        return kth_symbol_in_grammer(n-1, k)
    else:
        return not kth_symbol_in_grammer(n-1, k-mid)
    
if __name__ == "__main__":
    print(kth_symbol_in_grammer(4,8))