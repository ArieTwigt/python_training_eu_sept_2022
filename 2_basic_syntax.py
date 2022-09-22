# assigning a variable in Python
name = "Arie"
city = 'Amsterdam'
place = "Arie's"

# integer variable
age = 50

# float, numerics with decimals
length = 1.95

# boolean
raining=True
smoking=False
print("hello")

# every variable in Python is an object
# an object has:
# * methods (actions)
# * attributes (aspects)

## () --> used to call a function or method
name.upper()

## Functions --> global
# e.g. global conversion functions
#str()
#int()
#float()
#
#list()
#dict()

## Operators '+'

## lists (in others programming languages = arrays)
my_list = ['Arie', 'Rose', 'James', 'Anne']
my_list.append('John')

# code conventions
# lowercase letters
MyName = 'Jim' # non-convention --> reserved for Objects
my_name = 'Arie' # convention

# descriptive variable names
age = 10
num_times = 100 


sentence = "Hello" + " " + name

# format
sentence = "Hello {}, you are {} years old.".format(name, age)

# f-string
sentence = f"Hello {name}, you are {age} years old."