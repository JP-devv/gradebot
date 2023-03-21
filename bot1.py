import sys
from asmutils import *
# Get file from arguments
file = sys.argv[1]
file = asm(file)
# Compute with data here
file.printInfo()
# Test usage of mov
assert 'mov' in file.opcodes, 'mov not used'
# Test usage of add 
assert 'add' in file.opcodes, 'add not used'
# Test usage of sub 
assert 'sub' in file.opcodes, 'sub not used'
# Check if there is memory
assert file.mem, 'No memory allocated for registers'
print('Expect 0xFFFFFFB (-5)')
# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
  print('')
  file.replace()