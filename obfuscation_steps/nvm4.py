"""
TODO: 4) DONE! read two chars each time, no more new lines, ignore spaces and new lines.
"""

program = """
1 0
C A
0 1
C B
0 1
C C
B D
1 B
0 C
C C
3 1
C E
1 A
C F
2 É
C M
2 F
A C
P U
1 9
D D
2 F
0 1
C F
2 M
C É
2 É
C U
B G
1 0
C F
2 É
C Z
2 F
A E
P À
1 1
D G
2 F
0 1
C F
2 Z
C É
2 É
C À
1 0
2 D
C E
1 0
0 1
C F
2 É
C Ã
2 F
A C
P T
2 F
2 D
C H
2 F
3 B
2 G
A B
P V
2 E
3 H
C E
2 Y
C É
2 É
C V
2 E
0 H
C E
2 É
C Y
2 F
0 1
C F
2 Ã
C É
2 É
C T
B H
2 C
3 1
C I
1 I
C I
2 D
C J
2 È
C K
2 J
2 *
C J
1 J
3 1
2 K
C J
1 0
C F
2 É
C X
2 F
A C
P R
2 F
A I
P N
2 F
2 D
D H
2 Â
C É
2 É
C N
1 0
0 1
2 J
D H
2 É
C Â
2 F
0 1
C F
2 X
C É
2 É
C R
B D
1 0
2 J
C I
A A
P P
2 I
A B
P Á
2 n
D D
2 q
D D
2 q
D D
2 O
C É
2 É
C Á
2 e
D D
2 r
D D
2 z
D D
2 b
D D
2 i
D D
2 r
D D
2 O
C É
2 É
C P
2 z
D D
2 b
D D
2 i
D D
2 r
D D
2 É
C O
2 Ä
D D
2 b
D D
2 a
D D
2 r
D D
2 Ä
D D
2 z
D D
2 n
D D
2 g
D D
2 p
D D
2 u
D D
2 f
D D
2 g
D D
2 v
D D
2 p
D D
2 x
D D
2 Ä
D D
2 g
D D
2 b
D D
2 Ä
D D
2 z
D D
2 n
D D
2 x
D D
2 r
D D
2 Ä
D D
2 g
D D
2 u
D D
2 r
D D
2 Ä
D D
2 r
D D
2 d
D D
2 h
D D
2 n
D D
2 g
D D
2 v
D D
2 b
D D
2 a
D D
2 Ä
D D
2 g
D D
2 e
D D
2 h
D D
2 r
D D
B A
1 0
2 H
D A
1 0
0 1
C F
2 É
C W
2 F
A C
P Q
2 Ä
D A
2 F
3 1
2 G
A B
P S
2 Å
D A
2 L
C É
2 É
C S
2 Æ
D A
2 É
C L
2 Ä
D A
2 F
2 H
D A
2 F
0 1
C F
2 W
C É
2 É
C Q
2 Ä
D A
2 Ç
D A
2 Ä
D A
2 E
D A
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
        for idx in range(0, len(program) - 2, 2):
            line = program[idx:idx+2]
            if line == '2É':
                label_name = program[idx + 3]
                self.variables[label_name] = idx

    def interpret(self, program):
        self.variables.update(d)
        self.variables["*"] = [len(i) for i in self.variables["È"]]
        self.scan_labels(program)

        while self.variables["É"] < len(program):
            line = program[self.variables["É"]: self.variables["É"] + 2]
            command = line[0]
            arg = line[1]
            if command == '1':  # rand
                if arg in self.variables:
                    self.variables["_"] = random.randint(0, int(self.variables[arg]))
                else:
                    self.variables["_"] = random.randint(0, int(arg))
            elif command == '0': # add
                if arg in self.variables:
                    self.variables["_"] += int(self.variables[arg])
                else:
                    self.variables["_"] += int(arg)
            elif command == '3': # sub
                if arg in self.variables:
                    self.variables["_"] -= int(self.variables[arg])
                else:
                    self.variables["_"] -= int(arg)
            elif command == 'D': # push
                self.variables[arg].append(self.variables["_"])
            elif command == 'A': # cmp
                self.variables["_"] = int(self.variables["_"] == self.variables[arg])
            elif command == 'P': # jt
                if self.variables["_"]:
                    self.variables["É"] = self.variables[arg]
                    continue
            elif command == '2': # read
                v = self.variables[arg]
                if isinstance(v, list) or isinstance(v, tuple):
                    self.variables["_"] = v[self.variables["_"]]
                else:
                    self.variables["_"] = v
            elif command == 'C': # set
                self.variables[arg] = self.variables["_"]
            elif command == 'B': # arr
                self.variables[arg] = list()

            self.variables["É"] += 2

        return f'{"".join(self.variables["D"])}\n{chr(10).join("".join(mini_dic[x][i] for x in [c for e in self.variables["A"] for c in [*str(e)]]) for i in range(4))}'

def inline_program(program):
    output = ""
    for line, command, args in get_program_lines(program):
        output += f"{command}{args[0]}"

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
    program = inline_program(program)
    print(program)
    #test(program)
