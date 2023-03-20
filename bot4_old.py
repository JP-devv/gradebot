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
data = getvar(file)
is32 = is32(file)
names = getfunction(file)

# Announce program type
print(f'Program Type: {32 if is32 else 64} BIT')

# Convert celsius to fahrenheit
fahrenheit = int(int(data[0][2]) * (9/5) + 32)

# Test function
assertt('Has Function', '_convertC2F', names)
# Test call
assertt('Has Call Instruction', 'True', usescommand(file, 'call'))
# Print expected outcome
print(f'Expecting: {hex(fahrenheit)} ({fahrenheit})\n')
#replace(file)
