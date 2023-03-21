# Helpful utilities when grading ASM
import os

class asm:
  file = None
  var = None
  mem = None
  ins = None
  opcodes = None
  lines = None
  def __init__(self, file):
    self.file = file
    self.standardize()
    with open(self.file) as file:
      self.lines = file.readlines()
    newinst = self.lines.copy()
    self.var = self.getVar()
    print(self.lines == newinst)
    self.mem = self.getMem()
    self.ins = self.getIns()
    self.opcodes = self.getOp()
  # Get variables from data section
  def getVar(self):
    # Store data in a list
    data = []
    # Only get code between .data and .code
    is_past_data = False
    for line in self.lines:
      line = line.casefold()
      if not is_past_data and '.data' in line:
        is_past_data = True
        continue
      elif is_past_data and '.code' in line:
        is_past_data = False
        break
      elif is_past_data and line[0] != ';' and line[0] != '\n':
        mark = len(line) if ';' not in line else line.find(';')
        bits = line[:mark].split()
        if len(bits) > 2:
          data.append(bits)
      return data

  # Get specific memory variable
  def getMem(self):
    # Filter from data, we know memory will start as 0 or ?
    new_data = []
    for elem in self.var:
      if elem[2] == '0' or elem[2] == '?':
        new_data.append(elem)
    return new_data

  # Get instructions from code section
  def getIns(self):
    # Store data in a list
    data = []
    # Only get code between .data and .code
    is_past_code = False
    for line in self.lines:
      line = line.casefold().replace(',', ' ')
      if not is_past_code and 'main proc' in line:
        is_past_code = True
        continue
      elif is_past_code and 'invoke' in line:
        is_past_code = False
        break
      elif is_past_code and line[0] != ';' and line[0] != '\n':
        mark = len(line) if ';' not in line else line.find(';')
        bits = line[:mark].split()
        if len(bits) > 0:
          data.append(bits)
      return data

  # Get opcodes only 
  def getOp(self):
    data = []
    for elem in self.ins:
      data.append(elem[0])
    return set(data)
      
  # Determine if 32 bit or 64 bit program
  def is32(self):
    for line in self.lines:
      if '.386' in line:
        print('32 BIT PROGRAM\n')
        return True
      print('WARNING: 64 BIT SYSTEM CODE DETECTED, ADAPT VS AS NECESSARY\n')
      return False
        
  # Gets function names
  def getFunction(self):
    # Store functions as string list
    names = []
    for line in self.lines:
      if 'endp'.casefold() in line.casefold():
        names.append(line.split()[0])
      return names

  # Standardize linker
  def standardize(self):
    os.system(f'sed -i "" "s/^main/_main/" "{self.file}"')
    os.system(f'sed -i "" "s/END main/END _main/" "{self.file}"')

  # Copy file to clipboard and delete
  def replace(self):
    os.system(f'cat "{self.file}" | pbcopy && rm "{self.file}"')
    print(f'Replaced {self.file} onto clipboard successfully')
