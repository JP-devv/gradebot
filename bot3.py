import sys
from asmutils import *
# Get file from arguments
file = sys.argv[1]
file = asm(file)
# Print info from file
file.printInfo()

# Test usage of add 
assert 'add' in file.opcodes, 'add not used'
# Test usage of mul
assert 'jbe' in file.opcodes or 'jz' in file.opcodes, 'jump not used'
# Test if labels are used
assert len(file.labels) > 0, 'No labels used'
# Check if there is memory
assert file.mem, 'No memory allocated for registers'
print('Expect 0x109E82 (1099778)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
  file.replace()