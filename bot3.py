import sys
from asmutils import *
# Get file from arguments
file = sys.argv[1]
file = asm(file)
# Print info from file
file.printInfo()

# Test usage of add
try: assert 'add' in file.opcodes, '⚠️ add not used'
except AssertionError as e: print(e)

# Test usage of any variation of jump
try: assert 'jbe' in file.opcodes or 'jz' in file.opcodes \
    or 'jae' in file.opcodes or 'je' in file.opcodes \
    or 'jmp' in file.opcodes, '⚠️ jump not used'
except AssertionError as e: print(e)

# Test if labels are used
try: assert len(file.labels) > 0, '⚠️ No labels used'
except AssertionError as e: print(e)

# Check if there is memory
try: assert file.mem, '⚠️ No memory allocated for registers'
except AssertionError as e: print(e)

print('Expect 0x109E82 (1099778)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()
