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
    print('⚠️ _convertc2f not called')

# Test usage of call
if 'call' not in file.opcodes:
    print('⚠️ call not used')
    
# Test usage of push
if 'push' not in file.opcodes:
    print('⚠️ push not used')

# Check if there is memory
if not file.mem:
    print('⚠️ No memory allocated for registers')

print('Expect 0x109E82 (1099778)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()