# Function Assignment Grader

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
# Check if there is memory
assert file.mem, 'No memory allocated for registers'
print('INSERT ANSWER HERE')

if len(sys.argv) == 2:
  print('')
  file.replace()
