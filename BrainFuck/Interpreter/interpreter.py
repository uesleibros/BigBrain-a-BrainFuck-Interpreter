"""
BrainFuck Interpreter
--------------------------------

- A Simple interpreter for the programming language (BrainFuck)

*Copyright: (c) 2022-UesleiDev
*License: MIT,  see more details (https://opensource.org/licenses/MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the Interpreter), to deal in the Interpreter without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Interpreter, and to permit persons to whom the Interpreter is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Interpreter.

THE INTERPRETER IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE INTERPRETER.
"""
import sys

#==[SAVE BYTES]==#
cells = [0]
guide = 0
loop = 0
ip = 0
ptr = 0
loop_stack = {}
loop_table = []
debbuger = True

def Debbuger(deb):
	global debbuger
	debbuger = deb

#==[INTERPRETER]==#
def run_interpreter(filename=""):
    global guide
    global cells
    global loop
    global ip
    global ptr
    global loop_stack
    global loop_table
    
    #==[TOKENS]==#
    BRAIN_MINUS = '-'
    BRAIN_SUM = '+'
    BRAIN_UPPER = '>'
    BRAIN_LOWER = '<'
    BRAIN_TILDE = '~'
    BRAIN_DIVISION = '/'
    BRAIN_POINT = '.'
    BRAIN_LCASE = '['
    BRAIN_RCASE = ']'
    	
    if not filename.endswith(('.b', '.bfk', '.bf', '.brainf', '.fuck')):
    	print(f"BigBrain[Interpreter FileSys]: A extension (.{filename.split('.')[-1]}) is not supported, Supported extensions: [.b, .bfk, .bf, .brainf, .fuck].")
    	sys.exit(0)

    try:
    	file = open(filename).read()
    except IOError as e:
    	print(f"BigBrain[Interpreter FileSys]: Directory/File not founded: {filename}")
    	sys.exit(0)
    
    while ip < len(file):
        sy = file[ip] #sy -> symbol
        
        #==PREVENT NEGATIVE POSITION==#
        if guide < 0:
        	guide = 0

        #==[TOKENS]==#
        if sy == BRAIN_SUM:
            if cells[guide] > 256:
                cells[guide] = 0
            else:
                cells[guide] = cells[guide] + 1
            
        elif sy == BRAIN_MINUS:
            if cells[guide] < 0:
                print(f"Memory[{guide}]: Cannot be less than 0.")
                sys.exit(0)
            else:
                cells[guide] = cells[guide] - 1
            
        elif sy == BRAIN_UPPER:
            cells.append(0)
            guide += 1
            
        elif sy == BRAIN_LOWER:
            guide -= 1
            
        elif sy == BRAIN_POINT:
            print(chr(cells[guide]), end="")
            
        elif sy == BRAIN_TILDE:
            if cells[guide] > 256:
                cells[guide] = 0
            else:
                cells[guide] = cells[guide] + 15
                
        elif sy == BRAIN_DIVISION:
            if cells[guide] < 0:
                print(f"Memory[{guide}]: Cannot be less than 0.")
                sys.exit(0)
            else:
                cells[guide] = cells[guide] - 15

        elif sy == ',':
          inp = input('\nInput Requested [Type just one letter]:  ')
          cells[guide] = ord(inp[0])
          
        #==[LOOP FUCK]==#
        elif sy == BRAIN_LCASE:
        	if cells[guide] == 0:
        		openCase = 1
        		while openCase > 0:
        			ip += 1
        			if file[ip] == BRAIN_LCASE:
        				openCase += 1
        			elif file[ip] == BRAIN_RCASE:
        				openCase -= 1
        				
        elif sy == BRAIN_RCASE:
        	openCase = 1
        	while openCase > 0:
        		ip -= 1
        		if file[ip] == BRAIN_LCASE:
        			openCase -= 1
        		elif file[ip] == BRAIN_RCASE:
        			openCase += 1	
        	ip -= 1
        	
        ip += 1
          
    if debbuger == True:
    	des = 0
    	print("\nMemory's Bytes:")
    	print(cells) # <- Debbuger: You can turn off, just use: Debbuger(False)
    	print("\n-> Memory Spaces:", len(cells))
    	for c in cells:
    		if c == 0:
    			des += 1
    	print("-> Empty memory spaces:", des)
