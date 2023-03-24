import sys
from asmutils import *
# Get file from arguments
name = sys.argv[1]
file = asm(name)
# Print info from file
file.printInfo()

# Test if is an ASM file
try: assert '.asm' in name, '⚠️ Not an ASM file'
except AssertionError as e: print(e)

# Test usage of add
try: assert 'add' in file.opcodes, '⚠️ add not used'
except AssertionError as e: print(e)

# Test usage of mul
try: assert 'mul' in file.opcodes or 'imul' in file.opcodes, '⚠️ mul not used'
except AssertionError as e: print(e)

# Test usage of cdq
try: assert 'cdq' in file.opcodes, '⚠️ cdq not used'
except AssertionError as e: print(e)

# Test usage of div
try: assert 'div' in file.opcodes or 'idiv' in file.opcodes, '⚠️ div not used'
except AssertionError as e: print(e)

# Check if there is memory
try: assert file.mem, '⚠️ No memory allocated for registers'
except AssertionError as e: print(e)


print('Expect 0x00000049 (73)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()
