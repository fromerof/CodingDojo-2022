num1 = 42 # variable and number
num2 = 2.3 # variable and number
boolean = True #  var and boolean
string = 'Hello World' # variable as string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # array 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana') # tuple
print(type(fruit)) #print and type 
print(pizza_toppings[1]) #print and type 
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #access value
person['name'] = 'George' #change value to
person['eye_color'] = 'blue' #change value
print(fruit[2]) #initialize
"""conditional and print 
if num1 > 45:  
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
"""
"""for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
"""
""" while loop
x = 0
while(x < 5):
    print(x)
    x += 1
"""
pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value

print(person)#initialize
person.pop('eye_color') #delete value
print(person)#initialize

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') #print 
    if topping == 'Olives':
        break 

def print_hello_ten_times(): #function
    for num in range(10): #for loop, argument and parameter
        print('Hello') #argument 

print_hello_ten_times() #return
def print_hello_x_times(x): #function
    for num in range(x): #for loop and parameter
        print('Hello') #paramenter

print_hello_x_times(4) #return

def print_hello_x_or_ten_times(x = 10): #function with x ass argument and 10 ass parameter
    for num in range(x): #for loop and parameter
        print('Hello') #parameter

print_hello_x_or_ten_times() #return
print_hello_x_or_ten_times(4) #return giving an argument 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)