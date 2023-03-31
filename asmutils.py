import os
import subprocess


class Asm:
    """A class for analyzing Assembly language (ASM) code."""

    def __init__(self, file):
        """Initialize an instance of the Asm class."""
        self.file = file
        self._standardize()
        with open(self.file) as file:
            self.lines = [line.casefold().replace(',', ' ')
                          for line in file.readlines()]
        self._is32()
        self.functions = self._get_functions()
        self.var = self._get_var()
        self.mem = self._get_mem()
        self.ins = self._get_ins()
        self.opcodes = self._get_opcodes()
        self.labels = self._get_labels()

    def _get_var(self):
        """Retrieve variables from the data section."""
        data = []
        is_past_data = False
        for line in self.lines:
            if not is_past_data and '.data' in line:
                is_past_data = True
                continue
            elif is_past_data and '.code' in line:
                is_past_data = False
                break
            elif is_past_data and line[0] != ';' and line[0] != '\n':
                comment_position = len(
                    line) if ';' not in line else line.find(';')
                tokens = line[:comment_position].split()
                if len(tokens) > 2:
                    data.append(tokens)
        return data

    def _get_mem(self):
        """Retrieve specific memory variables with a value of '0' or '?'."""
        return [elem for elem in self.var if elem[2] in ('0', '?')]

    def _get_ins(self):
        """Retrieve instructions from the code section."""
        data = []
        is_past_code = False
        for line in self.lines:
            if not is_past_code and 'main proc' in line:
                is_past_code = True
                continue
            elif is_past_code and 'invoke' in line:
                is_past_code = False
                break
            elif is_past_code and line[0] != ';' and line[0] != '\n' and ':' not in line:
                comment_position = len(
                    line) if ';' not in line else line.find(';')
                tokens = line[:comment_position].split()
                if len(tokens) > 0:
                    data.append(tokens)
        return data

    def _get_opcodes(self):
        """Retrieve unique opcodes from the instructions."""
        return {elem[0] for elem in self.ins}

    def _get_labels(self):
        """Retrieve labels from the code section."""
        data = []
        is_past_code = False
        for line in self.lines:
            if not is_past_code and 'main proc' in line:
                is_past_code = True
                continue
            elif is_past_code and 'invoke' in line:
                is_past_code = False
                break
            elif is_past_code and line[0] != ';' and line[0] != '\n' and ':' in line:
                comment_position = len(
                    line) if ';' not in line else line.find(';')
                tokens = line[:comment_position].split()
                if len(tokens) > 0:
                    data.append(tokens[-1])
        return data

    def _is32(self):
        """Determine if the assembly code is for a 32-bit or 64-bit program."""
        for line in self.lines:
            if '.386' in line:
                print('32 BIT PROGRAM\n')
                return True
        print('WARNING: 64 BIT SYSTEM CODE DETECTED, ADAPT AS NECESSARY\n')
        return False

    def _get_functions(self):
        """Retrieve function names from the assembly code."""
        return [line.split()[0] for line in self.lines if 'endp' in line]

    def _standardize(self):
        """Standardize the assembly code by updating labels and directives."""
        subprocess.run(['sed', '-i', '""', 's/^main/_main/', self.file])
        subprocess.run(['sed', '-i', '""', 's/END main/END _main/', self.file])

    def replace(self):
        """Copy the content of the assembly code file to the clipboard and delete the file."""
        print('')
        subprocess.run(['cat', self.file, '|', 'pbcopy'])
        os.remove(self.file)
        print(f'Replaced {self.file} onto clipboard successfully')

    def print_info(self):
        """Print gathered information about the assembly code."""
        print('DATA')
        for line in self.var:
            print(line)
        print('')
        print('OPCODES')
        print(self.opcodes, '\n')
        if self.labels:
            print('LABELS')
            print(self.labels, '\n')
        if self.functions and len(self.functions) > 1:
            print('FUNCTIONS')
            print(self.functions, '\n')