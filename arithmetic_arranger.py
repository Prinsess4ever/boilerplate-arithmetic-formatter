import re


def solve_one_problem(problem, with_solution=False):
    match = re.match(r"^\s*([a-z0-9]+)\s*(.)\s*([a-z0-9]+)\s*$", problem).groups()

    num1 = match[0]
    sign = match[1]
    num2 = match[2]

    length = max(len(num1), len(num2))

    if sign != '+' and sign != '-':
        return "Error: Operator must be '+' or '-'."
    if length > 4:
        return "Error: Numbers cannot be more than four digits."
    if not num1.isdigit() or not num2.isdigit():
        return "Error: Numbers must only contain digits."

    getal1 = num1.rjust(length + 2)
    getal2 = num2.rjust(length + 1)
    streepje = '-' * (length + 2)

    if with_solution:
        oplossing = int(num1) + int(num2) if sign == '+' else int(num1) - int(num2)

        getal3 = str(oplossing).rjust(length + 2)
        
        return getal1 + '\n' + sign + getal2 + '\n' + streepje + '\n' + getal3

    return getal1 + '\n' + sign + getal2 + '\n' + streepje


def arithmetic_arranger(problems, with_solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    resultaat2 = []

    for problem in problems:
        one_ready = solve_one_problem(problem , with_solution)
        if one_ready.startswith('Error'):
            return one_ready

        resultaat2.extend(one_ready.splitlines())

    aantal_lijnen = 4 if with_solution else 3
    line1 = '    '.join(x for x in resultaat2[0::aantal_lijnen])
    line2 = '    '.join(x for x in resultaat2[1::aantal_lijnen])
    line3 = '    '.join(x for x in resultaat2[2::aantal_lijnen])
    if with_solution:
        line4 = '    '.join(x for x in resultaat2[3::aantal_lijnen])
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3

    #
    #     resultaat2.append(one_ready.splitlines())
    #
    # x = []
    # for line in zip(*resultaat2):
    #     x.append('    '.join(line))
    #
    # return '\n'.join(x)

