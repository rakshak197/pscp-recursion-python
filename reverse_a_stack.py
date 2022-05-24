def insert(stack, key):
    if not stack:
        stack.append(key)
        return
    top = stack[-1]
    stack.pop()
    insert(stack, key)
    stack.append(top)
    
    

def reverse_a_stack(stack):
    """
    Reverse a stack
    """
    if not stack:
        return 
    top = stack[-1]
    stack.pop()
    reverse_a_stack(stack)
    insert(stack, top)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]
    reverse_a_stack(x)
    print(x)



