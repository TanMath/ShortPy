import math

program = input()

printlist=[]

def tinput():
    return "input()"
def function(name,arg,code):
    variables='qrstuvwxyz'
    return "def "+name+"("+ ','.join(variables[0:n])+"):\n\t"+code
def print(i):
    if program[i+1]='"':
        s = ""
        i+=1
        while i<len(program) and program[i]!='"':
                    s+=program[i]
                    i+=1
        return "print '"+s+"'"
    else: #Assume variable is one character
        return "print"+program[i+1]
funcdict={}

programfile=open("program.py", "w+")

for i in program:
    if printlist.find(i):
        pass
    if i == "I":
        input = tinput()
        program.write(input)
    elif i == "D" :
         #Solve problem with functions - D is for defining a function, but need to find next characters for function definition.
        funcdict[D]=[i]
    elif i=="p":
        print=print(i)
    
        
    
    
