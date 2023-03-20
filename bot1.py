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

# Announce program type
print(f'TYPE: {32 if is32 else 64} BIT')
print('')

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

print('ASSERTIONS')
# Test usage of mov
assertt('Has mov', usesCommand(file, 'mov'))

# Test usage of add 
assertt('Has add', usesCommand(file, 'add'))

# Test usage of sub 
assertt('Has sub', usesCommand(file, 'sub'))

# Check if there is memory
assertt('Has mem', mem)

if len(sys.argv) == 2:
  print('')
  replace(file)
