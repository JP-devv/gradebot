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

# Test usage of mov
if 'mov' not in file.opcodes:
    print('⚠️ mov not used')

# Test usage of add
if 'add' not in file.opcodes:
    print('⚠️ add not used')

# Test usage of sub
if 'sub' not in file.opcodes:
    print('⚠️ sub not used')

# Check if there is memory
if not file.mem:
    print('⚠️ No memory allocated for registers')

print('Expect 0xFFFFFFB (-5)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()
