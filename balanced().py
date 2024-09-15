class Stack:
  def __init__(self,n):
    print("Constructer Run")
    self.items = []
    self.n = n

  def push(self,i):
    # Add element
    if len(self.items) < self.n:
      self.items.append(i)
    else:
      print("stack is full")

  def pop(self):
    # Get top elemnt and remove element
    if len(self.items) == 0:
      print("stack is empty")
    else:
      return self.items.pop(-1)

  def top(self):
    # Get top elemnt
    if len(self.items) == 0:
      print("stack is empty")
    else:
      return self.items[-1]
      
  def display(self):
    # Display stack
    print(self.items)
    
  def length(self):
    # Get length
    return len(self.items)
  
  def is_empty(self):
   return len(self.items) == 0




def is_balanced(stringIn):
    stackMain = Stack(20)
    stack2 = Stack(20)
    dict1 = {")":"(","}":"{","]":"["}

    for i in stringIn:
        if i == "(" or i == "{" or i == "[":
            stackMain.push(i)
            
        elif i == ")" or i == "}" or i == "]":
          isTrue = False
          for j in range(stackMain.length()):
              if stackMain.is_empty():
                return False
              if stackMain.top() == dict1[i]:
                stackMain.pop()
                while not stack2.is_empty():
                  stackMain.push(stack2.pop())
                isTrue = True
                break
              else:
                
                stack2.push(stackMain.pop())
                
                
          if not isTrue:
            return False
          
              
          while not stack2.is_empty():
             stackMain.push(stack2.pop())
             
    return stackMain.is_empty()
    


userString = input("Enter a string: ")
if is_balanced(userString):
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")
