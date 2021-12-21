import math

class variable:
    """A format for all the data in the expresion
    """
    def __init__(self,x,dx) -> None:
        self.value = x
        self.d_value = dx
        
    def display(self):
        """Prints the value and the uncertainty in a correct format
        """
        print("{} ± {}".format(self.value, self.d_value))

add_sub = lambda dx, dy: math.sqrt(dx*2 + dy*2)
mul_div = lambda x, y, dx, dy: math.sqrt((dx/x)*2+(dy/y)*2)

def sumar(x:variable, y:variable) -> variable:
    """Adds two values with uncertainty

    Args:
        x (variable): Variable with value and uncertainty
        y (variable): Variable with value and uncertainty

    Returns:
        variable: The addition of the two values
    """
    res = x.value + y.value
    d_res = add_sub(x.d_value, y.d_value)
    return variable(res,d_res)

def restar(x:variable, y:variable) -> variable:
    """Substracts two numbers and gives the uncertainty

    Args:
        x (variable): Variable with value and uncertainty 
        y (variable): Variable with value and uncertainty

    Returns:
        variable: The substraction of the two values
    """
    res = x.value - y.value
    d_res = add_sub(x.d_value, y.d_value)
    return variable(res, d_res)

def multiplicar(x:variable, y:variable) -> variable:
    """The multiplication of two numbres and gives uncertainty

    Args:
        x (variable): Variable with value and uncertainty
        y (variable): Variable with value and uncertainty

    Returns:
        variable: The product of the two numbers
    """
    res = x.value * y.value
    d_res = mul_div(x.value, y.value, x.d_value, y.d_value)
    return variable(res, d_res)

def dividir(x:variable, y:variable) -> variable:
    """Divides two numbers and gives the uncertainty

    Args:
        x (variable): Dividend a variable with value and uncertainty
        y (variable): Divisor a variable with value and uncertainty, shuoldn't be 0

    Returns:
        variable: The division of the two values
    """
    res = x.value / y.value
    d_res = mul_div(x.value, y.value, x.d_value, y.d_value)
    return variable(res, d_res)

def userinput(message):
    """Asks the user for a float value and manages exceptions

    Args:
        message (string): Message displayed when prompting the user

    Returns:
        float: Number chosen by the user
    """
    while True:
       
        try:
            inner = float(input(message))
            return inner
        except ValueError:
            print("Not a number")

def managestring(string):
    """Reads the initial ecuation string provided by the user
    and isolates the variables for correct value asignations

    Args:
        string (string): Formmula entered by the user
    """
    for x in string:
        
        lista.append(x)
        
        if x.isalpha() and x not in variables: 
            
            ex = userinput("Value of {}\n>".format(x))
            dex = userinput("Enter uncertainty of {}\n>".format(x))
            
            variables.update({x:variable(ex,dex)}) 

def next_value(lista):
    """Returns the next value fron the original expresion and checks
    if it should start a substack

    Args:
        lista (list): Initial expresion converted to a list

    Returns:
        string: The next value of the list, while deleting itself from the list
    """
    
    try:
        x = lista.pop(0) 
    except IndexError:
        print("Incomplete expresion, check and try again")
    
    if x == "(": #If it detects a parenthesis it isolates the part inside the parenthesis and append the result of that
        substack = []
        x = next_value(lista)
        while x != ")":
            substack.append(x)
            x = next_value(lista)
        return evaluate(substack)

    if x in variables:
        return variables[x] #If the value is a variable it returns instead the object
    else: 
        return x

def evaluate(lista):
    """Evaluates the expresion, first it starts putting everything into a stack
    if it finds a multiplication it pushes the product of the operation to the stack 
    parenthesis are taken into account in nextvalue()

    Args:
        lista (list): The expresion turned into a list

    Returns:
        variable: The result of the whole expresion in variable form
    """
        
    stack = []
    
    while lista:

        x = next_value(lista)
        
        if x == "*" or x == "/": 
            
            y = stack.pop()
            z = next_value(lista)
            
            if x == "*":
                res = multiplicar(y,z)
            elif x == "/":
                res = dividir(y,z)
                
            stack.append(res)
        else:       
            stack.append(x)
        
    now =  next_value(stack)

    while stack:
        
        x = next_value(stack)
        
        if x == "+":
            now = sumar(now, next_value(stack))
        elif x == "-":
            now = restar(now, next_value(stack))
        else:
            print("Unacceptable character found")
            
    return now

def main():
    global variables, lista
    
    print("##- Welcome to the uncertainty calculator -##")
    
    def new_expresion():
        """Makes sure the formula entered by the user is in a correct format
        and wont explode the code

        Raises:
            ValueError: If the string is empty
            NameError: If there variables with more than 1 character
            KeyError: If there is an unaccounted value

        Returns:
            string: The formula in a correct format
        """
        symbols = "+-*/()"
        while True:
            try: 
                string = input("Type in the formula: ")
                if not string: raise ValueError

                listedstring = []
                for x in string:
                    listedstring.append(x)
                    
                    if not x.isalpha():
                        
                        if x not in symbols:
                            raise NameError
                    
                for x in range(len(listedstring)-1):
                    if listedstring[x].isalpha() and listedstring[x+1].isalpha(): raise KeyError
    
            except ValueError:
                print(">ERROR> Empty strings are not allowed\n")
            except KeyError:
                print(">ERROR> Variables should only be 1 character, for multiplication use '*'\n")
            except NameError:
                print(">ERROR> Don't use numbers. The only operators allowed are: {}".format(symbols))
            else:
                return string
                
    expresion = new_expresion()
    
    try:
        while True:
            lista = []
            variables = {}
            managestring(expresion)
            evaluate(lista).display()
            if "1" != input("\nExit the program with 'ctrl+C'\n\t[1] - Keep the current formula: '{}'\n\t[2] - New Formula\n>".format(expresion)):
                expresion = new_expresion()    
    except KeyboardInterrupt:
        exit("\n=-= Bye =-=")
        
if __name__ == "__main__":
    main()
