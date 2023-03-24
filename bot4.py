import sys
from asmutils import *

# Get file from arguments
name = sys.argv[1]
file = asm(name)

# Print info from file
file.printInfo()

# Test if is an ASM file
if '.asm' not in name:
    print('⚠️ Not an ASM file')

# Test usage of _convertC2F
if '_convertc2f' not in file.functions:
    print('⚠️ _convertc2f as a function not called')

# Test usage of call
if 'call' not in file.opcodes:
    print('⚠️ call not used')
    
# Test usage of push
if 'push' not in file.opcodes:
    print('⚠️ push not used')

# Test usage of add
if 'add' not in file.opcodes:
    print('⚠️ add not used')

# Test usage of mul
if 'mul' not in file.opcodes and 'imul' not in file.opcodes:
    print('⚠️ mul not used')

# Test usage of cdq
if 'cdq' not in file.opcodes and 'dword' == file.var[0][1]:
    print('⚠️ cdq not used')

# Test usage of cwd
if 'cwd' not in file.opcodes and 'word' == file.var[0][1]:
    print('⚠️ cwd not used')

# Test usage of div
if 'div' not in file.opcodes and 'idiv' not in file.opcodes:
    print('⚠️ div not used')

# Check if there is memory
if not file.mem:
    print('⚠️ No memory allocated for registers')

# Calculate expected value
if len(file.var) != 2:
    print('⚠️ Warning, expected value could be incorrect')
    
celsius = int(file.var[0][2])
flag = True
for item in file.var:
    # Looking for the celsius variable, it should contain the letter 'c'
    if item[2] != 0 and 'c' in item[0]:
        celsius = int(item[2])
        flag = False
fahrenheit = int(celsius * (9/5) + 32) if celsius != -1.1 else -1.1
if flag or len(file.var) != 2:
    print('⚠️ Warning, expected value could be incorrect')
print(f'Expect {hex(fahrenheit)} ({fahrenheit})')
    

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()