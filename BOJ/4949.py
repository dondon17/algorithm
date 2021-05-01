while True:
    str = input()
    if str == '.':
        break
    stack = []
    flag = 0

    for ch in str:
        if ch == '(' or ch == '[':
            stack.append(ch)

        elif ch == ')':
            if not stack or stack[-1] == '[':
                flag = -1
                break;
            elif stack[-1] == '(':
                stack.pop()
        elif ch == ']':
            if not stack or stack[-1] == '(':
                flag = -1
                break;
            elif stack[-1] == '[':
                stack.pop()
        else: 
            continue
    
    if flag == 0 and not stack:
        print("yes")
    else:
        print("no")
