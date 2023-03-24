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

print('Expect 0x00000049 (73)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()
