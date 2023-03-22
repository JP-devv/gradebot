import sys
from asmutils import *
# Get file from arguments
name = sys.argv[1]
file = asm(name)
# Print info from file
file.printInfo()

# Test if is an ASM file
assert '.asm' in name, 'Not an ASM file'
# Test usage of add 
assert 'add' in file.opcodes, 'add not used'
# Test usage of any variation of jump
assert 'jbe' in file.opcodes or 'jz' in file.opcodes \
  or 'jae' in file.opcodes or 'je' in file.opcodes \
  or 'jmp' in file.opcodes, 'jump not used'
# Test if labels are used
assert len(file.labels) > 0, 'No labels used'
# Check if there is memory
assert file.mem, 'No memory allocated for registers'
print('Expect 0x109E82 (1099778)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
  file.replace()