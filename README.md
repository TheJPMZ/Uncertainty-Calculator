# Uncertainty Calculator
**TheJPMZ**

An easy to use calculator that makes arithmetic operations with uncertainty. You can evaluate complex operations that has addition, subtraction, multiplication, division, and can understand parenthesis for correct order.



## How to run?
With python 3 installed on CMD/Console:
- To run the calculator
--```python Uncertainty.py```

## How to use?
### Operations
The calculator allows the basic arithmetic operations

 - Addition: `a+b`
 - Subtraction: `a-b`
 - Multiplication: `a*b`
 - Division: `a/b`
 
 To make the operations the calculator follows classic operation order (Parenthesis -> Multiplication & Division -> Addition * Subtraction)
### Variables
You can declare algebraic variables given it is represented with one character and its a letter.

You can't include numbers so if you need a constant you should declare it as a variable and assign its value like in the following example:

### Example of use
In this case we will be using the following equation:

![imagen](https://user-images.githubusercontent.com/64183934/146873648-deea00b3-ad8f-4a85-9a3d-f3252a069631.png)

The correct way to declare this function would be:  

```c
Type in the formula: "((a+b)/(b*c))-p"
```

Then you would need to register the value and uncertainty of every variable, for example here to declare the $\pi$:
```c
Value of p
>3.141592
Enter uncertainty of p
>0
```
The program would print something like this:
```c
-1.1415000000000002 ± 2.413690382068065
```
Then you can enter another formula or try the same one with different values. 
You can also exit the program with `ctrl+c`
