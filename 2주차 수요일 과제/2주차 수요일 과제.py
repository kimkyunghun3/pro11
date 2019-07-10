Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
t.shape('turtle')

SyntaxError: multiple statements found while compiling a single statement
>>> import turtle as t
t.shape('turtle')
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> import turtle as t
t.shape('turtle')

SyntaxError: multiple statements found while compiling a single statement
>>> import turtle as t
t.shape('turtle')

SyntaxError: multiple statements found while compiling a single statement
>>> import turtle as t
t.shape('turtle')

SyntaxError: multiple statements found while compiling a single statement
>>> import turtle as t
t.shape('turtle')
SyntaxError: multiple statements found while compiling a single statement
>>> import turtle as t
>>> t.shape('turtle')
>>> t.foward(100)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.foward(100)
AttributeError: module 'turtle' has no attribute 'foward'
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(100)
>>> t.left(90)
>>> 
>>> 
>>> for i in range(4):
	t.forward(100)
	t.right(90)

	
>>> 
>>> for i in range(4):
	t.forward(100)
	t.right(90)

	
>>> a=[10,20,30]
a.insert(2,500)
SyntaxError: multiple statements found while compiling a single statement
>>> a=[10,20,30]
>>> a.insert(2,500)
>>> a
[10, 20, 500, 30]
>>> len(a)
4
>>> a=[10,20,30]
a.insert(1,[500,600])

SyntaxError: multiple statements found while compiling a single statement
>>> a=[10,20,30]
>>> a.insert(1,[500,600])
>>> a
[10, [500, 600], 20, 30]
>>> a.pop()
30
>>> a
[10, [500, 600], 20]
>>> del a[2]
>>> a
[10, [500, 600]]
>>> a.remove(10)
>>> a
[[500, 600]]
>>> from collections import deque
>>> a=deque([10,20,30])
>>> a
deque([10, 20, 30])
>>> a.append(500)
>>> a
deque([10, 20, 30, 500])
>>> a.popleft()
10
>>> a
deque([20, 30, 500])
>>> a.appendleft(25)
>>> a
deque([25, 20, 30, 500])
>>> a.index(30)
2
>>> a.count(30)
1
>>> a.reverse()
>>> 
>>> a
deque([500, 30, 20, 25])
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.sort()
AttributeError: 'collections.deque' object has no attribute 'sort'
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.sort()
AttributeError: 'collections.deque' object has no attribute 'sort'
>>> if len(seq)
SyntaxError: invalid syntax
>>> a=[0,0,0,0,0]
>>> b=a.copy()
>>> 
>>> a
[0, 0, 0, 0, 0]
>>> b
[0, 0, 0, 0, 0]
>>> a is b
False
>>> a==b
True
>>> a=[39.21.53.52.10]
SyntaxError: invalid syntax
>>> a=[39,21,53,52,10]
>>> a
[39, 21, 53, 52, 10]
>>> for i in a:
	print(i)

	
39
21
53
52
10
>>> a=[39,21,53,52,10]
>>> for index, value in enumerate(a):
	print(index,value)

	
0 39
1 21
2 53
3 52
4 10
>>> for index, value in enumerate(a):
	print(index+1,value)

	
1 39
2 21
3 53
4 52
5 10
>>> for index, value in enumerate(a, start=1):
	print(index+1,value)

	
2 39
3 21
4 53
5 52
6 10
>>> for index, value in enumerate(a, start=1):
	print(index,value)

	
1 39
2 21
3 53
4 52
5 10
>>> a=[38,21,53,51,55]
>>> for i in range(len(a)):
	
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	print(a[i])

	
38
21
53
51
55
>>> a=[38,21,53,51,55]
>>> smallest=a[0]
>>> f
>>> 
>>> 
>>> for i in a:
	if i< smallest:
		smallest=i

		
>>> smallest
21
>>> a.sort()
>>> 
>>> 
>>> a[0]
21
>>> a[2]
51
>>> a.sort(reverse=True)
>>> a[0]
55
>>> min(a)
21
>>> max(a)
55
>>> sum(a)
218
>>> a=[i for i in range(10)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> c=[i+5 for i in range(10)]
>>> c
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> d=[i*2 for i in range(10)]
>>> d
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> a=[i for i in range(10) if i%2==0]
>>> a
[0, 2, 4, 6, 8]
>>> a=[i*j for j in range(2,10) for i in range(1,10)]
>>> a
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
>>> a=[1.2,2.5,3.6,4.7]
>>> for i inn range(len(a)):
	
SyntaxError: invalid syntax
>>> a=[1.2,2.5,3.6,4.7]for i inn range(len(a)):
	
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	a[i]=int(a[i])

	
>>> 
>>> a
[1, 2, 3, 4]
>>> a=[1.2,2.5,3.6,4.7]
>>> a=list(map(int,a))
>>> a
[1, 2, 3, 4]
>>> a=list(map(str,range(1)))
>>> a
['0']
>>> a=list(map(str,range(10)))
>>> a
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> a=input().split()

>>> 10 20
SyntaxError: invalid syntax
>>> a
[]
>>> a=input(10 20).split()
SyntaxError: invalid syntax
>>> a=input(10,20).split()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    a=input(10,20).split()
TypeError: input expected at most 1 arguments, got 2
>>> a=input().split()

>>> a
[]
>>> list(a)
[]
>>> 
>>> 
>>> a
[]
>>> a=map(int,input().split())
a
>>> a=map(int,input().split())
10 20
SyntaxError: multiple statements found while compiling a single statement
>>> a
<map object at 0x10353fda0>
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    list(a)
ValueError: invalid literal for int() with base 10: 'a'
>>> a,b=[10,20]
>>> a
10
>>> b
20
>>> a=(33,22,11,44,55)
>>> a.index(11)
2
>>> a.count(44)
1
>>> for i in a
SyntaxError: invalid syntax
>>> for i in a:
	print(i,end='')

	
3322114455
>>> a=(1.2,3.4,5.6)
>>> a=tuple(map(int,a))
>>> a
(1, 3, 5)
>>> max(a)
5
>>> min(a)
1
>>> sum(a)
9
>>> a,b=map(int,input().split())
for i in range(start, stop+1)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    a,b=map(int,input().split())
ValueError: invalid literal for int() with base 10: 'for'
>>> a,b=map(int,input().split())
for i in range(start, stop+1):
	
SyntaxError: multiple statements found while compiling a single statement
>>> a,b=map(int,input().split())
for i in range(start, stop+1)
SyntaxError: multiple statements found while compiling a single statement
>>> a=[[10,20],[30,40]]
>>> b=a
>>> b[0][0]=500
>>> a
[[500, 20], [30, 40]]
>>> b
[[500, 20], [30, 40]]
>>> table=str.maketrans('aeiou','12345')
>>> 'apple'.translate(table)
'1ppl2'
>>> 'apple pear mango banana'.split()
['apple', 'pear', 'mango', 'banana']
>>> ''.join(['apple','pear','grape'])
'applepeargrape'
>>> ' '.join(['apple','pear','grape'])
'apple pear grape'
>>> '-'.join(['apple','pear','grape'])
'apple-pear-grape'
>>> 'python'.upper()
'PYTHON'
>>> '{0:0<10}'.format(15)
'1500000000'
>>> {key: 0 for key in dict.fromkeys(['a','b','c','d']).key()}
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    {key: 0 for key in dict.fromkeys(['a','b','c','d']).key()}
AttributeError: 'dict' object has no attribute 'key'
>>> {key:0 for key in dict.fromkeys(['a','b','c','d']).key()}
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    {key:0 for key in dict.fromkeys(['a','b','c','d']).key()}
AttributeError: 'dict' object has no attribute 'key'
>>> with opne('words.txt','r') as file:
	print(line.strip('\n'))
	for i in range(len(world)//2):
		if word[i] !=word[-l-i]:
		if word==word[::-1]
		
SyntaxError: expected an indented block
>>> with opne('words.txt','r') as file:
	print(line.strip('\n'))
	for i in range(len(world)//2):
		if word[i] !=word[-l-]
		
SyntaxError: invalid syntax
>>> 
>>> def calc(a,b):
	return a+b,a-b,a*b,a/b

>>> 
>>> def print_numbers(*args):
	    for arg in args:
	         print(arg)

>>> print_numbers(10)
10
>>> 
>>> print_numbers(10,20,30,40)
10
20
30
40
>>> def get_max_score(*args)
SyntaxError: invalid syntax
>>> def ge_min_score(*args):
def get_max_score, get_min_score, get_average_score (*args):
    print max,min,average(*args)
 30과
 
SyntaxError: expected an indented block
>>> def factorial(n):
    if n == 1:      # n이 1일 때
        return 1
    return n * factorial(n - 1)
print(factorial(5))
SyntaxError: invalid syntax
>>> 
>>> lambda x: x+10
<function <lambda> at 0x1079e2048>
>>> plus_ten =lambda x:x+10
>>> plus_ten(1)
11
>>> input()
Hello, world!
'Hello, world!'
>>> a=int(input(''))
b=int(input(''))
c=input('')
SyntaxError: multiple statements found while compiling a single statement
>>> 
a,b,c,d=map(int,input().split())
print((a+b+c+d)//4)
Traceback (most recent call last):
  File "<pyshell#221>", line 2, in <module>
    a,b,c,d=map(int,input().split())
ValueError: invalid literal for int() with base 10: 'print((a+b+c+d)//4)'
>>> print(a=>90 and b>80 and c>85 and d>=80)
