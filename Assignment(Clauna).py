Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(5, 55, 5):
	print(i)

	
5
10
15
20
25
30
35
40
45
50
>>> for n (-10, 11, 1):
	
SyntaxError: invalid syntax
>>> for n in range(-10, 11, 1):
	print(n)

	
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
1
2
3
4
5
6
7
8
9
10
>>> for p in range(10, -11, -1):
	p

	
10
9
8
7
6
5
4
3
2
1
0
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
>>> import turtle
>>> aaron = turtle.Turtle()
>>> aaron
<turtle.Turtle object at 0x03D25630>
>>> def drawSpiral(myTurtle, maxside):
	for sidelength in range(1, maxside+1, 5):
		myTurtle.forward(sidelength)
		myTurtle.right(69)

		
>>> drawSpiral(aaron, 69)
>>> mejia = turtle.Turtle()
>>> mejia
<turtle.Turtle object at 0x011613D0>
>>> def drawOpposite(oTurtle, oMaxside):
	for side in range(1, maxside+1, 5):
		oTurtle.forward(side)
		oTurtle.left(69)

		
>>> drawOpposite(mejia, 69)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    drawOpposite(mejia, 69)
  File "<pyshell#25>", line 2, in drawOpposite
    for side in range(1, maxside+1, 5):
NameError: name 'maxside' is not defined
>>> def drawOpposite(oTurtle, oMaxside):
	for side in range(1, oMaxside+1, 5):
		oTurtle.forward(side)
		oTurtle.left(69)

		
>>> drawOpposite(mejia, 69)
>>> 
