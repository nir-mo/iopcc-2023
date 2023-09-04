import abc
import copy
import dataclasses
import random
from typing import List

import art

OPERATORS = ('+', '-')

mini_dic = {
    ' ': ['  ', '  ', '  ', '  ', ''],
    '0': [' _  ', '/ \\ ', '\\_/ ', '    ', ''],
    '4': ['     ', '|_|_ ', '  |  ', '     ', ''],
    '8': [' _  ', '(_) ', '(_) ', '    ', ''],
    '+': ['    ', '_|_ ', ' |  ', '    ', ''],
    '3': ['_  ', '_) ', '_) ', '   ', ''],
    '7': ['__ ', ' / ', '/  ', '   ', ''],
    '2': ['_  ', ' ) ', '/_ ', '   ', ''],
    '6': [' _  ', '|_  ', '|_) ', '    ', ''],
    '-': ['   ', '__ ', '   ', '   ', ''],
    '1': ['   ', ' | ', ' | ', '   ', ''],
    '5': [' _  ', '|_  ', ' _) ', '    ', ''],
    '9': [' _  ', '(_| ', '  | ', '    ', ''],
    '=': ['   ', '-- ', '-- ', '   ', '']
}



class Transition(abc.ABC):
    def __init__(self, value):
        self.value = value

    @abc.abstractmethod
    def opposite(self):
        raise NotImplementedError()


class Move(Transition):
    def opposite(self):
        return "move"


class Add(Transition):
    def opposite(self):
        return "remove"


class Remove(Transition):
    def opposite(self):
        return "add"


@dataclasses.dataclass
class Equation:
    components: List[int]
    operators: List[str]
    result: int

    def __str__(self):
        expr = str(self.components[0])
        for i in range(1, len(self.components)):
            expr += " "
            expr += self.operators[i - 1]
            expr += " "
            expr += str(self.components[i])

        return f"{expr} = {self.result}"


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


def annotate_equation(equation: Equation):
    """
    Annotate the equation by changing one match!

    :param equation: predefined `Equation`.
    :return: New annotated equation.
    """
    transitions = {
        0: (Add(8),),
        1: (Add(7),),
        2: (Move(3), Add(7)),
        3: (Move(5), Move(2), Add(9)),
        4: (Add(9),),
        5: (Add(9), Add(6), Move(3)),
        6: (Move(9), Add(8), Remove(5)),
        7: (Remove(1),),
        8: (Remove(0), Remove(6), Remove(9)),
        9: (Move(6), Add(8), Remove(3), Remove(4), Remove(5)),
    }

    new_equation = copy.deepcopy(equation)

    # pick a random component
    random_component_index = random.randint(0, len(new_equation.components) - 1)
    random_component = new_equation.components[random_component_index]
    possible_transitions = transitions[random_component]

    # pick transition
    t = possible_transitions[random.randint(0, len(possible_transitions) - 1)]
    new_equation.components[random_component_index] = t.value
    return new_equation, t


def compile_annotations(annotations: List[Transition]):
    move = 0
    add = 0
    remove = 0
    for a in annotations:
        if isinstance(a, Add):
            add += 1
        elif isinstance(a, Remove):
            remove += 1
        else:
            move += 1

    convert_to_move = min(add, remove)
    move += convert_to_move
    add -= convert_to_move
    remove -= convert_to_move

    return move, add, remove


def print_art(equation_str):
    print("\n".join("".join(mini_dic[e][i] for e in equation_str) for i in range(5)))


if __name__ == "__main__":
    # TODO: Add complexity level..
    number_of_transitions = random.randint(1, 2)
    annotated_equation = generate_matchstick_equation()
    transitions = []
    for i in range(number_of_transitions):
        annotated_equation, transition = annotate_equation(annotated_equation)
        transitions.append(transition)

    move, add, remove = compile_annotations(transitions)
    if move:
        print(f"Move {move} match to fix this equation")

    if add:
        print(f"Remove {add} match to fix this equation")

    if remove:
        print(f"Add {remove} match to fix this equation")

    Art = art.text2art(str(annotated_equation), "mini")
    print(Art)
