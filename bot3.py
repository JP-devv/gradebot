import sys
from asmutils import *

# Get file from arguments
name = sys.argv[1]
file = Asm(name)

# Print info from file
file.print_info()

# Test if is an ASM file
if '.asm' not in name:
    print('⚠️ Not an ASM file')

# Test usage of add
if 'add' not in file.opcodes:
    print('⚠️ add not used')

# Test usage of any variation of jump
if 'jbe' not in file.opcodes and 'jz' not in file.opcodes and \
    'jae' not in file.opcodes and 'je' not in file.opcodes and \
    'jmp' not in file.opcodes:
    print('⚠️ jmp not used')

# Test if labels are used
if len(file.labels) == 0:
    print('⚠️ No labels used')

# Check if there is memory
if not file.mem:
    print('⚠️ No memory allocated for registers')

print('Expect 0x109E82 (1099778)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()
