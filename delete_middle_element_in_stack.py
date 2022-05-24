from copy import deepcopy


def get_size(stack):
    if not stack:
        return 0
    stack.pop()
    return get_size(stack) + 1
    

def delete_middle_element_in_stack(stack, size):
    if size == 1:
        stack.pop()
        return
    top = stack[-1]
    stack.pop()
    delete_middle_element_in_stack(stack, size-1)
    stack.append(top)


if __name__   == "__main__":
    stack = [2,1,3,4,6,5,8,7,9]
    stack_copy = deepcopy(stack)
    size = get_size(stack_copy) 
    k = (size)//2 + 1
    delete_middle_element_in_stack(stack, k)
    print(stack)