# Function Assignment Grader

import sys
from asmutils import *

# Get file from arguments
file = sys.argv[1]
standardize(file)

# Standard Parsing
#
# Data is grabbed from .data section as 2D array
# is32 is a boolean whether 32 bit or 64 bit 
# names is a list of functions that we have
is32 = is32(file)

# Compute with data here
print('DATA')
for line in getVar(file):
  print(line)
print('')

print('MEMORY')
mem = getMem(file)
for line in mem:
  print(line)
print('')

print('OPCODES')
opcodes = getOp(file)
print(opcodes,'\n')

# Test usage of add 
assert 'add' in opcodes, 'add not used'

# Test usage of mul
assert 'mul' in opcodes or 'imul' in opcodes, 'mul not used'

# Test usage of cdq 
assert 'cdq' in opcodes, 'cdq not used'

# Test usage of div
assert 'div' in opcodes or 'idiv' in opcodes, 'div not used'

# Check if there is memory
assert mem, 'No memory allocated for registers'

print('Expect 0x00000049 (73)')

if len(sys.argv) == 2:
  print('')
  replace(file)
