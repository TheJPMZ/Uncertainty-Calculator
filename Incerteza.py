import math

class variable:
    def __init__(self,x,dx) -> None:
        self.value = x
        self.d_value = dx
        
    def display(self):
        print("{} ± {}".format(self.value, self.d_value))

add_sub = lambda dx, dy: math.sqrt(dx*2 + dy*2)
mul_div = lambda x, y, dx, dy: math.sqrt((dx/x)*2+(dy/y)*2)

def sumar(x:variable, y:variable):
    res = x.value + y.value
    d_res = add_sub(x.d_value, y.d_value)
    return variable(res,d_res)

def restar(x:variable, y:variable):
    res = x.value - y.value
    d_res = add_sub(x.d_value, y.d_value)
    return variable(res, d_res)

def multiplicar(x:variable, y:variable):
    res = x.value * y.value
    d_res = mul_div(x.value, y.value, x.d_value, y.d_value)
    return variable(res, d_res)

def dividir(x:variable, y:variable):
    res = x.value / y.value
    d_res = mul_div(x.value, y.value, x.d_value, y.d_value)
    return variable(res, d_res)

def userinput(message):
    while True:
       
        try:
            inner = float(input(message))
            return inner
        except ValueError:
            print("Not a number")
        


#* Lectura


def managestring(string):
    for x in string:
        
        lista.append(x)
        
        if x.isalpha() and x not in variables: 
            
            ex = userinput("Value of {}\n>".format(x))
            dex = userinput("Enter uncertainty of {}\n".format(x))
            
            variables.update({x:variable(ex,dex)}) 

#* Operaciones

def next_value(lista):
    
    try:
        x = lista.pop(0) 
    except IndexError:
        print("Incomplete expresion, check and try again")
    
    if x == "(":
        substack = []
        x = next_value(lista)
        while x != ")":
            substack.append(x)
            x = next_value(lista)
        return evaluate(substack)

    if x in variables:
        return variables[x]
    else: 
        return x

def evaluate(lista):
        
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
        
main()