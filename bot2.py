# Function Assignment Grader

import sys
from asmutils import *

# Get file from arguments
file = sys.argv[1]
file = asm(file)

# Standard Parsing
#
# Data is grabbed from .data section as 2D array
# is32 is a boolean whether 32 bit or 64 bit 
# names is a list of functions that we have
is32 = file.is32()
# Compute with data here
print('DATA')
for line in file.var:
  print(line)
print('')

print('MEMORY')
for line in file.mem:
  print(line)
print('')

print('OPCODES')
print(file.opcodes,'\n')

# Test usage of add 
assert 'add' in file.opcodes, 'add not used'

# Test usage of mul
assert 'mul' in file.opcodes or 'imul' in file.opcodes, 'mul not used'

# Test usage of cdq 
assert 'cdq' in file.opcodes, 'cdq not used'

# Test usage of div
assert 'div' in file.opcodes or 'idiv' in file.opcodes, 'div not used'

# Check if there is memory
assert file.mem, 'No memory allocated for registers'

print('Expect 0x00000049 (73)')

if len(sys.argv) == 2:
  print('')
  file.replace()
