#  Write  a  program  to  convert  prefix  to  postfix

from prog1b import stack

def convert(prefix):

    prefix = prefix[::-1]

    s = stack()

    for ch in prefix:

        if ch . isalnum():
            s . push(ch)

        else:
            x = s . pop()
            y = s . pop()

            temp = x + y + ch

            s . push(temp)

    return s . pop()

prefix = input('Enter prefix expression : ')

postfix = convert(prefix)

print('Postfix expression : ' , postfix)
