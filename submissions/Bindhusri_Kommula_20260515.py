#  Write  a  program  to  convert  prefix  to  postfix

def prefix_to_postfix(prefix):

    s = []
    prefix = prefix[::-1]
    for ch in prefix:
        if not is_operator(ch):
            s.append(ch)
        else:
            op1 = s.pop()
            op2 = s.pop()
            temp = op1 + op2 + ch
            s.append(temp)

    return s.pop()


prefix = input()
print("Prefix :", prefix)
print("Postfix:", prefix_to_postfix(prefix))