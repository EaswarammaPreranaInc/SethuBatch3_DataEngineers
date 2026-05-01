#1
'''
Write  a  program  to  delete  a  directory.
Input  is  either  directory  name  (or)  path  of  the  directory
'''
import os
try:
    x = input('Enter the directory name or path of directory that is to be deleted:')
    os . rmdir(f'{x}')
    print(f'Directory {x} is deleted')

except FileNotFoundError:
    print(f'{x} Directory does not exist')
except OSError:
    print(f'{x} is Non-Empty')


#2
'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
import os
try:
    x = input('Enter the path of directories to be deleted:')
    os . removedirs(f'{x}')
    print('Directory or Directories are deleted')

except FileNotFoundError:
    print('Directory does not exist')
except OSError:
    print('Last Directory is Non-Empty')


#  Write  a  program  to  rename  a  file
import os
try:
    a = input('Enter the file name to be changed:')
    b = input('Enter the name to be changed into:')
    os . rename(a , b)

except FileNotFoundError:
    print(f'{a} does not exist')
except FileExistsError:
    print(f'{b} already exists, cannot give {a} the existing name {b}')
    


# Write  a  program  to  rename  a  directory
import os
try:
    x = input('Enter the directory name to be changed:')
    y = input('Enter the name to be changed into:')
    os . rename(x , y)

except FileNotFoundError:
    print(f'{x} does not exist')
except FileExistsError:
    print(f'{y} already exists, cannot give {x} the existing name {y}')


#3
'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
import os
try:
    x = input('Enter the director or path ("." for Current Working Directory):')
    l = os . listdir(f'{x}')
    s = []
    f = []

    for y in l:
        if '.' in y:
            f . append(y)
        else:
            s . append(y)

    print('Sub-Directories:' , s)
    print('Files:' , f)
except FileNotFoundError:
    print('The given files does not exist')




# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
import os

x = input('Enter the name of the directory to be iterated through:')
g = os . walk(f'{x}')

while True:
    try:
        tpl = next(g)
        print('Directory Path:' , tpl[0])
        print('Sub-Directories:' , tpl[1])
        print('Files:' , tpl[2])
        os . system('pause')
        os . system('cls')
    except StopIteration:
        break
