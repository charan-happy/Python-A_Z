# wrong type conversion

num1 = 25 # int
num2 = "45" # string
result = num1+ num2
print(result)

"""
# output

Traceback (most recent call last):
  File "/workspaces/Python-A_Z/python-basics/programming-basics/code-practice/5-typeconverstion-1.py", line 5, in <module>
    result = num1+ num2
             ~~~~^~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

