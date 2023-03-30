'''This module consisit of 20 Python Experiments:

1. write a program to demonstrate different number data types in python
2. write a program to perform different Arithmetic Operations on numbers in python
3. write a program to create, concatenate and print a string and accessing sub-string from a given string
4. write a python script to print the current date in the following format "Sun May 29 02:26:23 IST 2017"
5. write a program to create, append and remove lists in python
6. write a program to demonstrate working with tuples in python
7. write a program to demonstrate working with dictionaries in python
8. write a program to find largest of three numbers
9. write a python program to convert temperatures to and from celsius,fahrenheit. [formula: c/5 = f-32/9] 
10. write a python program to conduct the following pattern, using a nested for loop
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
11. write a python script that prints prime numbers less than 20
12. write a python program to find factorial of a number using Recursion
13. write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of other two sides)
14. write a python program to define a module to find Fibnacci Numbers and import the module to another program
15. write a python program to define a module and import a specific function in that module to another program
16. write a script named copyfile.py this script prompt the user for the names of two text files. The contents of the first file should be input and written to second file
17. write a program that inputs a text file.The program should print all of the unique words in the file in alphabetical order
18. write a python class to convert an integer to a roman numeral.
19. write a python class to implement pow(x, n).
20. write a python class to reverse a string word by word

THANK YOU :>
GITHUB : https://github.com/likhith1409
'''


#########################################
import time
from datetime import datetime
import operator

def outputExp1():
    a=50
    print(a,"is of type",type(a))
    b=39.9
    print(b,"is of type",type(b))
    c=10+12j
    print(c,"is of type",type(c))
    d=True
    print(d,"is of type",type(d))
    e="Hi"
    print(e,"is of type",type(e))

def outputExp2():
    a=int(input("Enter the value a:"))
    b=int(input("Enter the value b:"))
    print("Line 1 - value of a+b is",a+b)
    print("Line 2 - value of a+b is",a-b)
    print("Line 3 - value of a+b is",a*b)
    print("Line 4 - value of a+b is",a/b)
    print("Line 5 - value of a+b is",a%b)
    print("Line 6 - value of a+b is",a**b)

def outputExp3():
    str1="Hello"
    print(str1)
    str2="welcome"
    print(str2)
    str3='''How are you'''
    print(str2)

def outputExp4():
    n = datetime.now()

    day= n.strftime("%a")
    month= n.strftime("%b")
    d = n.strftime("%d")
    time = n.strftime("%H:%M:%S")
    year = n.strftime("%Y")
    print(day,month,d,time,"IST",year)

def outputExp5():
    prog = ["JAVA","PYTHON","C"]
    print(prog)
    print("***appending***")
    a=input("Enter the string to append:")
    prog.append(a)
    print(prog)
    print("***removing***")
    b=input("Enter the string to remove:")
    prog.remove(b)
    print(prog)

def outputExp6():
    t=(10,20,30,40)
    print(t)
    type(t)
    t.apped    #error
    t.remove(10) 

def outputExp7():
    print("***DICTIONARIES***")

    n = int(input("Enter the limit of the dictionary:"))
    dict = {}

    for i in range(n):
        query = input("Enter the query: ")
        ans = input("Enter the ans: ")

        dict[query] = ans


    print("Original dictionary:", dict)

    sorted_dict = sorted(dict.items(),key=operator.itemgetter(0))
    print("Dictionary in ascending order by value:",sorted_dict)
    sorted_dict = sorted(dict.items(),key=operator.itemgetter(0),reverse=True)
    print("Dictionary in descending order by value:",sorted_dict)

def outputExp8():
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    num3=int(input("Enter num3:"))
    n=[num1,num2,num3]
    print("The largest of 3 numbers is:",max(n))
    print("The smallest of 3 numbers is:",min(n))
    avg=sum(n)/len(n)
    print("The average of 3 numbers is:",avg)

def outputExp9():
    while(True):

        print("Press 1.Celsius to Fahrenheit")
        print("Press 2.Fahrenheit to celsius")
        print("Press 3.Exit")
        n=int(input("Enter the number:"))
        if(n==1):
            cel = float(input("Enter the celsius value:"))

            fah = (cel * 1.8)+32

            print("%0.1f degree Celsius is equal to %0.1f degree Fahrenheit"%(cel,fah))

        elif(n==2):
            fah = float(input("Enter the Fahrenheit:"))
            Cel = ((fah-32)*5)/9

            print("%0.1f degree Fahrenheit is equal to %0.1f degree Celsius"%(fah,cel))
        else:
            exit(0)

def outputExp10():
    max_stars = 5
    for i in range(1, max_stars+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

    for i in range(max_stars-1, 0, -1):
        for j in range(1, i+1):
             print("*", end=" ")
        print()

def outputExp11():
    n = int(input("Enter the limit:"))

    for i in range(2,n):
        isPrime = True
        for j in range(2,i//2+1):
            if(i%j==0):
                isPrime = False
        if isPrime:
            print(i)


def outputExp12():
    def fact(n):
        if n==0:
            result = 1
        else:
            result=n*fact(n-1)
        return result
    n = int(input("Enter the number to check Factorial:"))
    for i in range(1,n):
        factorial = fact(n)
    print(factorial)


def outputExp13():
    a= int(input("Enter the side1:"))
    b= int(input("Enter the side2:"))
    c= int(input("Enter the side3:"))


    if (a^2+b^2)==c^2:
        print("Right Angled Triangle")
    else:
        print("Not Right Angled Triangle")


def outputExp14():
    n = int(input("Enter the limit of Fibnoci series:"))
    def fib(n):
        f1=0
        f2=1
        print(f1)
        print(f2)
        while(n-2>0):
            f3 = f1+f2
            print(f3)
            f1 = f2
            f2 = f3
            n = n-1

    print(fib(n))


def outputExp15():
    import math
    print("Value of Pi is",math.pi)


def outputExp16():
    f1 = input("Enter the input file:")
    f2 = input("Enter the Output file:")


    file1 = open(f1, "w")
    data = input("Enter the Data:")
    file1.write(data)
    file1.close()


    file2 = open(f2,"w")
    file1 = open(f1, "r")
    file2.write(file1.read())
    file1.close()
    file2.close()


    print("File copyed Succesfully!!")


def outputExp17():
    f1 = input("Enter the file name:")
    file = open(f1,"r")


    contents = file.read()
    words = contents.split()
    words.sort()


    for word in words:
        print(word)


def outputExp18():
    class RomanConvert:
        def Roman_num(self,num):
            roman_no = {
                1000:"M",
                900:"CM",
                500:"D",
                400:"CD",
                100:"C",
                90:"XC",
                50:"L",
                40:"XL",
                10:"X",
                9:"IX",
                5:"V",
                4:"IV",
                1:"I"
            }


            result = ''
            for value,symbol in roman_no.items():
                while num >= value:
                    result += symbol
                    num -= value
            return result


    convert = RomanConvert()
    print(convert.Roman_num(900))

def outputExp19():
    class powcalic:
        def powcal(self,x,n):
            if n<0:
                x = 1/x
                n = -n
            result = 1


            while n:
                if n & 1:
                    result *= x
                x *= x
                n >>= 1
            return result


    calic = powcalic()
    print(calic.powcal(2,3))


def outputExp20():
    class reversestr:
        def revstr(self, s):
            return ' '.join(reversed(s.split()))


    rev = reversestr()
    print(rev.revstr('Hello World'))




#####################################################################################
##-> for Printing the inputs

def inputExp1():
    a='''
        a=50
        print(a,"is of type",type(a))
        b=39.9
        print(b,"is of type",type(b))
        c=10+12j
        print(c,"is of type",type(c))
        d=True
        print(d,"is of type",type(d))
        e="Hi"
        print(e,"is of type",type(e))
    '''
    print(a)

def inputExp2():
    a='''
    a=int(input("Enter the value a:"))
    b=int(input("Enter the value b:"))
    print("Line 1 - value of a+b is",a+b)
    print("Line 2 - value of a+b is",a-b)
    print("Line 3 - value of a+b is",a*b)
    print("Line 4 - value of a+b is",a/b)
    print("Line 5 - value of a+b is",a%b)
    print("Line 6 - value of a+b is",a**b)
    '''
    print(a)

def inputExp3():
    a='''
        str1="Hello"
        print(str1)
        str2="welcome"
        print(str2)
        str3='How are you'---> use triple quotes in this line!!!!!
        print(str2)
    '''
    print(a)

def inputExp4():
    a='''
        n = datetime.now()

        day= n.strftime("%a")
        month= n.strftime("%b")
        d = n.strftime("%d")
        time = n.strftime("%H:%M:%S")
        year = n.strftime("%Y")
        print(day,month,d,time,"IST",year)
    '''
    print(a)


def inputExp5():
    a='''
        prog = ["JAVA","PYTHON","C"]
        print(prog)
        print("***appending***")
        a=input("Enter the string to append:")
        prog.append(a)
        print(prog)
        print("***removing***")
        b=input("Enter the string to remove:")
        prog.remove(b)
        print(prog)
    '''
    print(a)


def inputExp6():
    a='''
        t=(10,20,30,40)
        print(t)
        type(t)
        <class 'tuple'> #error
        t.apped    #error
        t.remove(10) 
    '''
    print(a)


def inputExp7():
    a='''
        print("***DICTIONARIES***")

        n = int(input("Enter the limit of the dictionary:"))
        dict = {}

        for i in range(n):
            query = input("Enter the query: ")
            ans = input("Enter the ans: ")

            dict[query] = ans


        print("Original dictionary:", dict)

        sorted_dict = sorted(dict.items(),key=operator.itemgetter(0))
        print("Dictionary in ascending order by value:",sorted_dict)
        sorted_dict = sorted(dict.items(),key=operator.itemgetter(0),reverse=True)
        print("Dictionary in descending order by value:",sorted_dict)
    '''
    print(a)


def inputExp8():
    a='''
        num1=int(input("Enter num1:"))
        num2=int(input("Enter num2:"))
        num3=int(input("Enter num3:"))
        n=[num1,num2,num3]
        print("The largest of 3 numbers is:",max(n))
        print("The smallest of 3 numbers is:",min(n))
        avg=sum(n)/len(n)
        print("The average of 3 numbers is:",avg)
    '''
    print(a)


def inputExp9():
    a='''
        while(True):

            print("Press 1.Celsius to Fahrenheit")
            print("Press 2.Fahrenheit to celsius")
            print("Press 3.Exit")
            n=int(input("Enter the number:"))
            if(n==1):
                cel = float(input("Enter the celsius value:"))

                fah = (cel * 1.8)+32

                print("%0.1f degree Celsius is equal to %0.1f degree Fahrenheit"%(cel,fah))

            elif(n==2):
                fah = float(input("Enter the Fahrenheit:"))
                Cel = ((fah-32)*5)/9

                print("%0.1f degree Fahrenheit is equal to %0.1f degree Celsius"%(fah,cel))
            else:
                exit(0)
    '''
    print(a)


def inputExp10():
    a='''
        max_stars = 5
        for i in range(1, max_stars+1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()

        for i in range(max_stars-1, 0, -1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()
    '''
    print(a)


def inputExp11():
    a='''
        n = int(input("Enter the limit:"))

        for i in range(2,n):
            isPrime = True
            for j in range(2,i//2+1):
                if(i%j==0):
                    isPrime = False
            if isPrime:
                print(i)
    '''
    print(a)



def inputExp12():
    a='''
    def fact(n):
        if n==0:
            result = 1
        else:
            result=n*fact(n-1)
        return result
    n = int(input("Enter the number to check Factorial:"))
    for i in range(1,n):
        factorial = fact(n)
    print(factorial)
    '''
    print(a)



def inputExp13():
    a='''
    a= int(input("Enter the side1:"))
    b= int(input("Enter the side2:"))
    c= int(input("Enter the side3:"))


    if (a^2+b^2)==c^2:
        print("Right Angled Triangle")
    else:
        print("Not Right Angled Triangle")
    '''
    print(a)



def inputExp14():
    a='''
    n = int(input("Enter the limit of Fibnoci series:"))
    def fib(n):
        f1=0
        f2=1
        print(f1)
        print(f2)
        while(n-2>0):
            f3 = f1+f2
            print(f3)
            f1 = f2
            f2 = f3
            n = n-1

    print(fib(n))
    '''
    print(a)



def inputExp15():
    a='''
    import math
    print("Value of Pi is",math.pi)
    '''
    print(a)



def inputExp16():
    a='''
    f1 = input("Enter the input file:")
    f2 = input("Enter the Output file:")


    file1 = open(f1, "w")
    data = input("Enter the Data:")
    file1.write(data)
    file1.close()


    file2 = open(f2,"w")
    file1 = open(f1, "r")
    file2.write(file1.read())
    file1.close()
    file2.close()


    print("File copyed Succesfully!!")
    '''
    print(a)



def inputExp17():
    a='''
    f1 = input("Enter the file name:")
    file = open(f1,"r")


    contents = file.read()
    words = contents.split()
    words.sort()


    for word in words:
        print(word)
    '''
    print(a)



def inputExp18():
    a='''
    class RomanConvert:
        def Roman_num(self,num):
            roman_no = {
                1000:"M",
                900:"CM",
                500:"D",
                400:"CD",
                100:"C",
                90:"XC",
                50:"L",
                40:"XL",
                10:"X",
                9:"IX",
                5:"V",
                4:"IV",
                1:"I"
            }


            result = ''
            for value,symbol in roman_no.items():
                while num >= value:
                    result += symbol
                    num -= value
            return result


    convert = RomanConvert()
    print(convert.Roman_num(900))
    '''
    print(a)


def inputExp19():
    a='''
    class powcalic:
        def powcal(self,x,n):
            if n<0:
                x = 1/x
                n = -n
            result = 1


            while n:
                if n & 1:
                    result *= x
                x *= x
                n >>= 1
            return result


    calic = powcalic()
    print(calic.powcal(2,3))
    '''
    print(a)



def inputExp20():
    a='''
    class reversestr:
        def revstr(self, s):
            return ' '.join(reversed(s.split()))


    rev = reversestr()
    print(rev.revstr('Hello World'))
    '''
    print(a)


