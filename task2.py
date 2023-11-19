add = lambda x , y : x+y
sub = lambda x , y : x-y
mul = lambda x , y : x*y
def div(x , y):
    if y != 0:
        return (x/y)
    else:
        print("denominater is zero")
        
num1 = float(input("Enter the num:  "))
num2 = float(input("Enter the num:  "))

print("Choose the operation")
print("1.Addition") 
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")

choise = int(input("Enter the choise 1/2/3/4/5: "))

if choise == 1:
    print(add(num1,num2))
    
elif choise == 2:
    print(sub(num1,num2)) 
    
elif choise == 3:
    print(mul(num1,num2))    
    
elif choise == 4:
    print(div(num1,num2))    
else:
    print("invalid input")
        
