
def insert(stack, val):
    """
    Inserting value at right place in the sorted stackay.
    """
    if len(stack)==0 or stack[-1]<=val:
        stack.append(val)
        return 
    top_el = stack[-1]
    stack.pop()
    insert(stack, val)
    stack.append(top_el)

def sort(stack):
    """
    Sort stackay using recursion.
    """
    if not stack:
        return
    top = stack[-1]
    stack.pop()
    sort(stack) 
    insert(stack, top)

if __name__ == "__main__":
    x= [2,1,3,4,6,5,8,7,9]
    sort(x)
    print(x)