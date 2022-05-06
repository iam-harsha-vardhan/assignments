#!/usr/bin/env python
# coding: utf-8

# # Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[1]:


def arrCount(arr, n, sum):
 
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if int(arr[i]) + int(arr[j]) == sum:
                count += 1
    return count
 
arr =list(input("enter numbers with comas").split(","))
n = len(arr)
sum = int(input("enter sum value"))
print("Count of pairs is",arrCount(arr, n, sum))


# # Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# In[4]:


def reverse(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
 

a =list(input("enter numbers with comas").split(","))
n=len(a)
print(a)
reverse(a, 0, n-1)
print("Reversed list is")
print(a)


# # Write a program to check if two strings are a rotation of each other?

# In[6]:


def check(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return 0
    temp = string1 + string1
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
 

string1 =str( input('enter 1st string'))
string2 =str( input('enter 2st string'))
 
if check(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")


# # Write a program to print the first non-repeated character from a string?

# In[14]:


s = str( input('enter string:'))
while s != "":
   slen0 = len(s)
   ch = s[0]
   s = s.replace(ch, "")
   slen1 = len(s)
   if slen1 == slen0-1:
      print ("First non-repeating character is: ",ch)
      break;


# In[ ]:


# Read about the Tower of Hanoi algorithm. Write a program to implement it 


# In[15]:


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         

n = int(input("Enter the number of disks"))
TowerOfHanoi(n, 'A', 'C', 'B')


# # Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
# 

# In[18]:


def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convert postfix to Prefix expression
 
 
def postToPre(post_exp):
 
    s = []
 
   
    length = len(post_exp)
 
    
    for i in range(length):
 
       
        if (isOperator(post_exp[i])):
 
            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            # concat the operands and operator
            temp = post_exp[i] + op2 + op1
 
            # Push string temp back to stack
            s.append(temp)
 
      
        else:
 
            # push the operand to the stack
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 

if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    # Function call
    print("Prefix : ", postToPre(post_exp))


# # Write a program to convert prefix expression to infix expression.

# In[19]:


def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))
     


# 
# # Write a program to check if all the brackets are closed in a given code snippet.

# In[20]:


def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
if __name__ == "__main__":
    expr = "{()}[]"
 
    
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


#  # Write a program to reverse a stack.

# In[22]:


class  Stack_to_reverse  :
    # Creates  an  empty  stack.
    def __init__(  self  ):
        self.items  =  list()
        self.size=-1

    
    def  isEmpty(  self  ):
        if(self.size==-1):
            return True
        else:
            return False

    
    def  pop(  self  ):
        if  self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
            self.size-=1

    def  push(  self,  item  ):
        self.items.append(item)
        self.size+=1

    def reverse(self,string):
        n = len(string)

        for i in range(0,n):
            S.push(string[i])

        string=""

 

        for i in range(0,n):
            string+=S.pop()
        return string

S=Stack_to_reverse()
seq=input("Enter a string to reversed")
sequence = S.reverse(seq)
print("Reversed string is " + sequence)


# # Write a program to find the smallest number using a stack.

# In[24]:


class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min


# In[25]:


m = MinStack()
m.push(5)
m.push(32)
m.push(23)


# In[26]:


print(m.getMin())


# In[27]:


m.pop()
print(m.top())
print(m.getMin())


# In[ ]:




