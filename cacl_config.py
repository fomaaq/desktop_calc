buttons = {'C': {'formula': '0'},
           'del': {'formula': lambda formula: formula[0: -1]},
           'X^2': {'formula': lambda formula: str((eval(formula)) ** 2)},
           '/': {'formula': '/'},
           '7': {'formula': '7'},
           '8': {'formula': '8'},
           '9': {'formula': '9'},
           '*': {'formula': '*'},
           '4': {'formula': '4'},
           '5': {'formula': '5'},
           '6': {'formula': '6'},
           '-': {'formula': '-'},
           '1': {'formula': '1'},
           '2': {'formula': '2'},
           '3': {'formula': '3'},
           '+': {'formula': '+'},
           '+/-': {'formula': lambda formula: str((eval(formula)) * -1)},
           '0': {'formula': '0'},
           '.': {'formula': '.'},
           '=': {'formula': lambda formula: str(eval(formula))}}
