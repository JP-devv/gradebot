# Helpful utilities when grading ASM
import os


class asm:
    file = None
    var, mem, ins, opcodes, functions, labels, lines = None, None, None, None, None, None, None

    # Constructor will get all necessary information from file
    # and will organize it to be easily accessable for whatever you need
    def __init__(self, file):
        self.file = file
        self.__standardize()  # Cleans file to uniform format
        with open(self.file) as file:  # Get content from file
            self.lines = file.readlines()
            for i in range(len(self.lines)):
                self.lines[i] = self.lines[i].casefold().replace(',', ' ')
        self.__is32()  # Determines if 32 bit or 64 bit program
        self.functions = self.__getFunction()  # Get function names
        self.var = self.__getVar()  # Get variables from data section
        self.mem = self.__getMem()  # Get variable selected for memory
        self.ins = self.__getIns()  # Get ASM instructions
        self.opcodes = self.__getOp()  # Get unique opcodes uses in file
        self.labels = self.__getlabels()  # Get labels used in file

    # Gets variables from data section
    def __getVar(self):
        # Store data in a list
        data = []
        # Only get code between .data and .code
        is_past_data = False
        for line in self.lines:
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
    def __getMem(self):
        # Filter from data, we know memory will start as 0 or ?
        new_data = []
        for elem in self.var:
            if elem[2] == '0' or elem[2] == '?':
                new_data.append(elem)
        return new_data

    # Get instructions from code section
    def __getIns(self):
        # Store data in a list
        data = []
        # Only get code between .data and .code
        is_past_code = False
        for line in self.lines:
            if not is_past_code and 'main proc' in line:
                is_past_code = True
                continue
            elif is_past_code and 'invoke' in line:
                is_past_code = False
                break
            elif is_past_code and line[0] != ';' and line[0] != '\n' and ':' not in line:
                mark = len(line) if ';' not in line else line.find(';')
                bits = line[:mark].split()
                if len(bits) > 0:
                    data.append(bits)
        return data

    # Get opcodes only
    def __getOp(self):
        data = []
        for elem in self.ins:
            data.append(elem[0])
        return set(data)

    # Get instructions from code section
    def __getlabels(self):
        # Store data in a list
        data = []
        # Only get code between .data and .code
        is_past_code = False
        for line in self.lines:
            if not is_past_code and 'main proc' in line:
                is_past_code = True
                continue
            elif is_past_code and 'invoke' in line:
                is_past_code = False
                break
            elif is_past_code and line[0] != ';' and line[0] != '\n' and ':' in line:
                mark = len(line) if ';' not in line else line.find(';')
                bits = line[:mark].split()
                if len(bits) > 0:
                    data.append(bits[-1])
        return data

    # Determine if 32 bit or 64 bit program
    def __is32(self):
        for line in self.lines:
            if '.386' in line:
                print('32 BIT PROGRAM\n')
                return True
        print('WARNING: 64 BIT SYSTEM CODE DETECTED, ADAPT AS NECESSARY\n')
        return False

    # Gets function names
    def __getFunction(self):
        # Store functions as string list
        names = []
        for line in self.lines:
            if 'endp' in line:
                names.append(line.split()[0])
            return names

    # __standardize linker
    def __standardize(self):
        os.system(f'sed -i "" "s/^main/_main/" "{self.file}"')
        os.system(f'sed -i "" "s/END main/END _main/" "{self.file}"')

    # Copy file to clipboard and delete
    def replace(self):
        print('')
        os.system(f'cat "{self.file}" | pbcopy && rm "{self.file}"')
        print(f'Replaced {self.file} onto clipboard successfully')

    # Print all information
    def printInfo(self):
        print('DATA')
        for line in self.var:
            print(line)
        print('')
        print('OPCODES')
        print(self.opcodes, '\n')
        if self.labels:
            print('LABLES')
            print(self.labels, '\n')
