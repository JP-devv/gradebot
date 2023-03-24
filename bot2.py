import sys
from asmutils import *
# Get file from arguments
name = sys.argv[1]
file = asm(name)
# Print info from file
file.printInfo()

try:
    # Test if is an ASM file
    assert '.asm' in name, '⚠️ Not an ASM file'
    # Test usage of add
    assert 'add' in file.opcodes, '⚠️ add not used'
    # Test usage of mul
    assert 'mul' in file.opcodes or 'imul' in file.opcodes, '⚠️ mul not used'
    # Test usage of cdq
    assert 'cdq' in file.opcodes, '⚠️ cdq not used'
    # Test usage of div
    assert 'div' in file.opcodes or 'idiv' in file.opcodes, '⚠️ div not used'
    # Check if there is memory
    assert file.mem, '⚠️ No memory allocated for registers'
except AssertionError as e:
    print(e)

print('Expect 0x00000049 (73)')

# Replace file with new data if test argument isn't given
if len(sys.argv) == 2:
    file.replace()
