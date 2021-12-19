def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

dict_symb_func_names = {"+": "add",
"-": subtract,
"*": multiply,
"/": divide
}

num1 = (int(input("What's the first number? ")))
num2 = (int(input("What's the second number? ")))

for symb in dict_symb_func_names:
  print (symb)
operation_symb = input("Pick an operation from the line above: ")

if operation_symb in dict_symb_func_names:
  


print(f"{num1} {operation_symbol} {num2} = {answer}")