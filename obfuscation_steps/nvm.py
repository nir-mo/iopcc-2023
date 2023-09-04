# Nirmo's VM

from this import d

docs = """
    - rand max_value ; Generate a random number between 0 and max_value and store it in `result`
    - ADD value      ; Add the specified value to `result`: `result = result + value`
    - SUB value      ; Subtract the specified value from `result`: `result = result - value`
    - label value    ; Define a new label with the name value.
    - push arr_name  ; push result into arr_name: arr_name.append(result)
    - cmp value      ; cmp value with result, if equals then result = 1 otherwise result = 0. 
    - jt label_name  ; jump to label_name if result is 1.
    - read var_name  ; read var_name into result.
    - jump label_name; jump to label_name. 
"""

"""
The following NVM program is equivalent to the following function while the interpreter is set with these predefined 
variables: {"components": [], "operators": [], "plus": 1}

```
def generate_matchstick_equation() -> Equation:
    # Create equation left side components..
    number_of_components = random.randint(2, 3)
    components = [random.randint(0, 9) for _ in range(number_of_components)]

    # generate left side operators
    number_of_operators = number_of_components - 1
    operators = [random.choice(OPERATORS) for _ in range(number_of_operators)]

    equation_result = components[0]
    for i in range(1, len(components)):
        if operators[i - 1] == "+":
            equation_result += components[i]
        else:
            equation_result -= components[i]

    return Equation(components, operators, equation_result)
```
"""

generate_equation_program = """
    rand 1                           ; result = random.randint(0, 1)   
    add 2                            ; result = result + 2 -> result = random.randint(2, 3) 
    set number_of_components         ; number_of_components = random.randint(2, 3) 
    
    sub 1                            ; result = result - 1
    set number_of_operators          ; number_of_operators = number_of_components - 1
    
    rand 0                           ; result = 0
    set I                            ; i = 0
    label init_components
    read I                          ; result = i
    cmp number_of_components        ; result = int(i == number_of_components)
    jt init_components_end
    
    rand 9
    push components                 ; components.append(random.randint(0, 9))
    
    read I                          ; result = i
    add 1                           ; result += 1
    set I                           ; i = i = 1
    jump init_components
    label init_components_end
    
    ;;;;;;;;;;;;;;;;;;;;;;; Init operators ;;;;;;;;;;;;;;;;;;;;;;;;
    
    rand 0                           ; result = 0
    set I                            ; i = 0
    label init_operators
    read I                          ; result = i
    cmp number_of_operators         ; result = int(i == number_of_operators)
    jt init_operators_end
    
    rand 1
    push operators                  ; operators.append(random.randint(0, 1))
    
    read I                          ; result = i
    add 1                           ; result += 1
    set I                           ; i = i = 1
    jump init_operators
    label init_operators_end
    
    ;;;;;;;;;;;;;;;;;;;;;;; Calculate equation result ;;;;;;;;;;;;;;;;;;;;;;;;
    
    rand 0
    read components                 ; result = components[0]
    set equation_result             ; equation_result = components[0]
    
    rand 0
    add 1
    set I                           ; i = 1
    
    label eq_result_loop_start
    read I
    cmp number_of_components
    jt eq_result_loop_end
    
    read I
    read components
    set component_i             ; component_i = component[i]
    
    read I
    sub 1
    read operators              ; result = operators[i - 1]
    cmp plus                    ; if (operators[i - 1] != +): 
    jt plus
    
    ; Perform minus calculation    
    read equation_result
    sub component_i              
    set equation_result         ;       equation_result = equation_result - component[i]
    jump eq_result_loop_inc
    label plus                  ; else:
    
    ; Perform plus calculation    
    read equation_result
    add component_i              
    set equation_result         ;       equation_result = equation_result + component[i]
    
    label eq_result_loop_inc
    read I
    add 1
    set I
    jump eq_result_loop_start
    label eq_result_loop_end
    
    ;;;;;;;;;;;;;;;;;;;;;;; Annotate equation ;;;;;;;;;;;;;;;;;;;;;;;;
    read number_of_components
    sub 1
    set number_of_components_len
    rand number_of_components_len
    set component_to_change_index
    read components             
    set component_to_change      ; component_to_change = components[rand(0, number_of_components)]
    read transitions            
    set possible_transitions     ; possible_transitions = transitions[component_to_change]
    read component_to_change
    read lengths
    set possible_transitions_len ; possible_transitions_len = lengths[component_to_change]
    
    rand possible_transitions_len
    sub 1
    read possible_transitions
    set transition              ; transition = possible_transitions[rand(0, possible_transitions_len - 1)]
    
    rand 0
    set I
    label start_build_new_equation_loop
    read I
    cmp number_of_components
    jt end_build_new_equation_loop
    
    read I
    cmp component_to_change_index
    jt replace_element
    read I
    read components
    push new_equation           ; new_equation.append(components[i])
    jump inc_build_new_equation_loop  
        
    label replace_element
    rand 0
    add 1
    read transition
    push new_equation           ; new_equation.append(transition[1])
        
    label inc_build_new_equation_loop
    read I
    add 1
    set I                      ; i = i + 1
    jump start_build_new_equation_loop
    label end_build_new_equation_loop
    
    ;;;;;;;;;;;;;;;;;;;;;;; Build instructions for the user (the player) ;;;;;;;;;;;;;;;;;;;;;;;;
    ;;; Should build the string:
    ;;;  {Move/Add/Remove} one matchstick to make the equation true")
    rand 0
    read transition
    set transition_type
    cmp move
    jt write_move
    read transition_type
    cmp add
    jt write_add
    read n
    push msg
    read q
    push msg
    read q
    push msg
    jump write_rest
    
    label write_add
        ;; write remove
    read e
    push msg
    read r
    push msg
    read z
    push msg
    read b
    push msg
    read i
    push msg
    read r
    push msg
    jump write_rest
    
    label write_move
        read z
    push msg
    read b
    push msg
    read i
    push msg
    read r
    push msg
    
    label write_rest
    read space
    push msg
    read b
    push msg
    read a
    push msg
    read r
    push msg
    read space
    
    push msg
    read z
    push msg
    read n 
    push msg
    read g
    push msg
    read p
    push msg
    read u
    push msg
    read f
    push msg
    read g
    push msg
    read v
    push msg
    read p
    push msg
    read x
    push msg
    read space
    
    push msg
    read g
    push msg
    read b
    push msg
     read space
     
     push msg
     read z
     push msg
     read n
     push msg
     read x
     push msg
     read r
     push msg
      read space
      
      push msg
      read g
      push msg
      read u
      push msg
      read r
      push msg
      read space
      push msg
      
       read r
       push msg
       read d
       push msg
       read h
       push msg
       read n
       push msg
       read g
       push msg
       read v
       push msg
       read b
       push msg
       read a
       push msg
        read space
        
        push msg 
        read g
        push msg
        read e
        push msg
        read h
        push msg
        read r
        push msg
    
    ;;;;;;;;;;;;;;;;;;;;;;; Build an equation string ;;;;;;;;;;;;;;;;;;;;;;;;
    ;; The equation is an array of strings and integers:
    ;;;;;
    
    rand 0
    read new_equation
    push new_equation_str ; new_equation_str.append(new_equation[0])
    
    rand 0
    add 1
    set I
    label start_new_equation_str
    read I
    cmp number_of_components
    jt end_new_equation_str
    
    read space
    push new_equation_str
    
    read I
    sub 1
    read operators
    cmp plus
    jt add_plus
    read minus_str
    jump continue_new_equation_str
    label add_plus
    read plus_str
    
    label continue_new_equation_str
    push new_equation_str       ; new_equation_str.append('+' if operators[i - 1] else '-')
    
    read space
    push new_equation_str
    
    read I
    read new_equation
    push new_equation_str       ; new_equation_str.append(new_equation[i])
    
    read I
    add 1
    set I
    jump start_new_equation_str
    label end_new_equation_str
    
    read space
    push new_equation_str
    read assign
    push new_equation_str   ; new_equation_str.append('=')
    read space
    push new_equation_str
    read equation_result
    push new_equation_str   ; new_equation_str.append(equation_result)
    
    ;;;;;;;;;;;;;;;;;;;;;;; print everything ;;;;;;;;;;;;;;;;;;;;;;;;
    print msg
    mini_print new_equation_str
"""


import random

mini_dic = {
    ' ': ['  ', '  ', '  ', '  ', ''],
    '0': [' _  ', '/ \\ ', '\\_/ ', '    ', ''],
    '4': ['     ', '|_|  ', '  |  ', '     ', ''],
    '8': [' _  ', '(_) ', '(_) ', '    ', ''],
    '+': ['    ', '_|_ ', ' |  ', '    ', ''],
    '3': ['_  ', '_) ', '_) ', '   ', ''],
    '7': ['__ ', '  |', '  |', '   ', ''],
    '2': ['_  ', ' ) ', '/_ ', '   ', ''],
    '6': [' _  ', '|_  ', '|_) ', '    ', ''],
    '-': ['   ', '__ ', '   ', '   ', ''],
    '1': ['   ', ' | ', ' | ', '   ', ''],
    '5': [' _  ', '|_  ', ' _| ', '    ', ''],
    '9': [' _  ', '|_| ', ' _| ', '    ', ''],
    '=': ['   ', '-- ', '-- ', '   ', '']
}
class CustomLanguageInterpreter:
    def __init__(self):
        self.variables = {
            "components": [],
            "operators": [],
            "new_equation": [],
            "new_equation_str": [],
            "msg": [],
            "plus": 1,
            "move": 0,
            "add": 1,
            "space": " ",
            "remove": 2,
            "minus_str": "-",
            "plus_str": "+",
            "assign": "=",
            "transitions": [
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
            "lengths": [1, 1, 2, 3, 1, 3, 3, 1, 3, 5]
        }
        self.labels = {}
        self.pc = 0  # Program counter

    def scan_labels(self, program):
        lines = program.split('\n')
        for idx, line in enumerate(lines):
            line = line.strip()
            if line and line.startswith('label'):
                label_name = line.split()[1]
                self.labels[label_name] = idx

    def interpret(self, program):
        self.variables.update(d)
        self.scan_labels(program)
        lines = program.split('\n')
        while self.pc < len(lines):
            line = lines[self.pc].strip()
            comment = line.find(";")
            if comment != -1:
                line = line[:line.find(";")]
                line = line.strip()

            if line:
                tokens = line.split()
                command = tokens[0]
                args = tokens[1:]
                if command == 'rand':
                    if args[0] in self.variables:
                        self.variables["result"] = random.randint(0, int(self.variables[args[0]]))
                    else:
                        self.variables["result"] = random.randint(0, int(args[0]))
                elif command == 'add':
                    if args[0] in self.variables:
                        self.variables["result"] += int(self.variables[args[0]])
                    else:
                        self.variables["result"] += int(args[0])
                elif command == 'sub':
                    if args[0] in self.variables:
                        self.variables["result"] -= int(self.variables[args[0]])
                    else:
                        self.variables["result"] -= int(args[0])
                elif command == 'label':
                    self.labels[args[0]] = self.pc
                elif command == 'push':
                    self.variables[args[0]].append(self.variables["result"])
                elif command == 'cmp':
                    self.variables["result"] = int(self.variables["result"] == self.variables[args[0]])
                elif command == 'jt':
                    if self.variables["result"]:
                        self.pc = self.labels[args[0]]
                        continue
                elif command == 'read':
                    v = self.variables[args[0]]
                    if isinstance(v, list) or isinstance(v, tuple):
                        self.variables["result"] = v[self.variables["result"]]
                    else:
                        self.variables["result"] = v
                elif command == 'jump':
                    self.pc = self.labels[args[0]]
                    continue
                elif command == 'set':
                    self.variables[args[0]] = self.variables["result"]
                elif command == 'print':
                    print("".join(self.variables[args[0]]))
                elif command == 'mini_print':
                    print("\n".join("".join(mini_dic[x][i] for x in [c for e in self.variables[args[0]] for c in [*str(e)]]) for i in range(5)))

            self.pc += 1


for i in range(1000):
    interpreter = CustomLanguageInterpreter()
    try:
        interpreter.interpret(generate_equation_program)
    except Exception as e:
        print("vars:", interpreter.variables)
        raise e
