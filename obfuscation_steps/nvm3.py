
program = """
rand 0
set A
add 1
set B
add 1
set C
arr D
rand B
add C
set C
sub 1
set E
rand A
set F
read É
set M
read F
cmp C
jt U
rand 9
push D
read F
add 1
set F
read M
set É
read É
set U
arr G
rand 0
set F
read É
set Z
read F
cmp E
jt À
rand 1
push G
read F
add 1
set F
read Z
set É
read É
set À
rand 0
read D
set E
rand 0
add 1
set F
read É
set Ã
read F
cmp C
jt T
read F
read D
set H
read F
sub B
read G
cmp B
jt V
read E
sub H
set E
read Y
set É
read É
set V
read E
add H
set E
read É
set Y
read F
add 1
set F
read Ã
set É
read É
set T
arr H
read C
sub 1
set I
rand I
set I
read D
set J
read È
set K
read J
read *
set J
rand J
sub 1
read K
set J
rand 0
set F
read É
set X
read F
cmp C
jt R
read F
cmp I
jt N
read F
read D
push H
read Â
set É
read É
set N
rand 0
add 1
read J
push H
read É
set Â
read F
add 1
set F
read X
set É
read É
set R
arr D
rand 0
read J
set I
cmp A
jt P
read I
cmp B
jt Á
read n
push D
read q
push D
read q
push D
read O
set É
read É
set Á
read e
push D
read r
push D
read z
push D
read b
push D
read i
push D
read r
push D
read O
set É
read É
set P
read z
push D
read b
push D
read i
push D
read r
push D
read É
set O
read Ä
push D
read b
push D
read a
push D
read r
push D
read Ä
push D
read z
push D
read n
push D
read g
push D
read p
push D
read u
push D
read f
push D
read g
push D
read v
push D
read p
push D
read x
push D
read Ä
push D
read g
push D
read b
push D
read Ä
push D
read z
push D
read n
push D
read x
push D
read r
push D
read Ä
push D
read g
push D
read u
push D
read r
push D
read Ä
push D
read r
push D
read d
push D
read h
push D
read n
push D
read g
push D
read v
push D
read b
push D
read a
push D
read Ä
push D
read g
push D
read e
push D
read h
push D
read r
push D
arr A
rand 0
read H
push A
rand 0
add 1
set F
read É
set W
read F
cmp C
jt Q
read Ä
push A
read F
sub 1
read G
cmp B
jt S
read Å
push A
read L
set É
read É
set S
read Æ
push A
read É
set L
read Ä
push A
read F
read H
push A
read F
add 1
set F
read W
set É
read É
set Q
read Ä
push A
read Ç
push A
read Ä
push A
read E
push A
"""

import random
from this import d

mini_dic = {
    ' ': ['  ', '  ', '  ', '  '],
    '0': [' _  ', '/ \\ ', '\\_/ ', '    '],
    '4': ['     ', '|_|  ', '  |  ', '     '],
    '8': [' _  ', '(_) ', '(_) ', '    '],
    '+': ['    ', '_|_ ', ' |  ', '    '],
    '3': ['_  ', '_) ', '_) ', '   '],
    '7': ['__ ', '  |', '  |', '   '],
    '2': ['_  ', ' ) ', '/_ ', '   '],
    '6': [' _  ', '|_  ', '|_) ', '    '],
    '-': ['   ', '__ ', '   ', '   '],
    '1': ['   ', ' | ', ' | ', '   '],
    '5': [' _  ', '|_  ', ' _| ', '    '],
    '9': [' _  ', '|_| ', ' _| ', '    '],
    '=': ['   ', '-- ', '-- ', '   ']
}



class CustomLanguageInterpreter:
    def __init__(self):
        self.variables = {
            "Ä": " ", # space
            "Å": "-", # minus
            "Æ": "+", # plus
            "Ç": "=", # assign
            "È": [    # Transitions
                [(1, 8)],
                [(1, 7)],
                [(0, 3), (1, 7)],
                [(0, 5), (0, 2), (1, 9)],
                [(1, 9)],
                [(1, 9), (1, 6), (0, 3)],
                [(0, 9), (1, 8), (2, 5)],
                [(2, 1)],
                [(2, 0), (2, 6), (2, 9)],
                [(0, 6), (1, 8), (2, 3), (2, 4), (2, 5)],
            ],
            "É": 0, # PC
        }

    def scan_labels(self, program):
        lines = program.split('\n')
        for idx, line in enumerate(lines):
            line = line.strip()
            if line and line.startswith('2 É'):
                label_name = lines[idx + 1].strip().split()[1]
                self.variables[label_name] = idx

    def interpret(self, program):
        self.variables.update(d)
        self.variables["*"] = [len(i) for i in self.variables["È"]]
        self.scan_labels(program)
        lines = program.split('\n')

        while self.variables["É"] < len(lines):
            line = lines[self.variables["É"]].strip()
            if line:
                tokens = line.split()
                command = tokens[0]
                args = tokens[1:]
                if command == '1':  # rand
                    if args[0] in self.variables:
                        self.variables["result"] = random.randint(0, int(self.variables[args[0]]))
                    else:
                        self.variables["result"] = random.randint(0, int(args[0]))
                elif command == '0': # add
                    if args[0] in self.variables:
                        self.variables["result"] += int(self.variables[args[0]])
                    else:
                        self.variables["result"] += int(args[0])
                elif command == '3': # sub
                    if args[0] in self.variables:
                        self.variables["result"] -= int(self.variables[args[0]])
                    else:
                        self.variables["result"] -= int(args[0])
                elif command == 'D': # push
                    self.variables[args[0]].append(self.variables["result"])
                elif command == 'A': # cmp
                    self.variables["result"] = int(self.variables["result"] == self.variables[args[0]])
                elif command == 'P': # jt
                    if self.variables["result"]:
                        self.variables["É"] = self.variables[args[0]]
                        continue
                elif command == '2': # read
                    v = self.variables[args[0]]
                    if isinstance(v, list) or isinstance(v, tuple):
                        self.variables["result"] = v[self.variables["result"]]
                    else:
                        self.variables["result"] = v
                elif command == 'C': # set
                    self.variables[args[0]] = self.variables["result"]
                elif command == 'B': # arr
                    self.variables[args[0]] = list()

            self.variables["É"] += 1

        return f'{"".join(self.variables["D"])}\n{chr(10).join("".join(mini_dic[x][i] for x in [c for e in self.variables["A"] for c in [*str(e)]]) for i in range(4))}'

def strip_instructions(program):
    inst_map = {
        "rand": "1",
        "add": "0",
        "sub": "3",
        "push": "D",
        "cmp": "A",
        "jt": "P",
        "read": "2",
        "set": "C",
        "arr": "B"
    }
    output = ""
    for line, command, args in get_program_lines(program):
        if command in inst_map:
            output += f"{inst_map[command]} {args[0]}\n"
        else:
            output += f"{line}\n"

    return output

def get_program_lines(program):
    lines = program.split("\n")
    for line in lines:
        line = line.strip()
        if line:
            tokens = line.split()
            command = tokens[0]
            args = tokens[1:]
            yield line, command, args

def test(program):
    for i in range(1000):
        interpreter = CustomLanguageInterpreter()
        try:
            res = interpreter.interpret(program)
            print(res)
        except Exception as e:
            print("vars:", interpreter.variables)
            raise e

if __name__ == "__main__":
    program = strip_instructions(program)
    print(program)
    #test(program)