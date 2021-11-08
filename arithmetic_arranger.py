import re


def solve_one_problem(problem):
    match = re.match(r"^\s*(\d+)\s*([-+])\s*(\d+)\s*$", problem).groups()

    num1 = match[0]
    sign = match[1]
    num2 = match[2]
    length = max(len(num1), len(num2))
    rjust1 = num1.rjust(length + 2)
    rjust2 = num2.rjust(length + 1)
    retval = rjust1 + '\n' + sign + rjust2 + '\n' + '-' * (length + 2)
    return retval


def arithmetic_arranger(problems):
    resultaat1 = ''
    resultaat2 = []
    for problem in problems:
        one_ready = solve_one_problem(problem)
        line1 = one_ready.splitlines()[0]
        line2 = one_ready.splitlines()[1]
        line3 = one_ready.splitlines()[2]
        resultaat2.append(line1)
        resultaat2.append(line2)
        resultaat2.append(line3)
    resultaat_line1 = resultaat2[0] + '    ' + resultaat2[3]
    resultaat_line2 = resultaat2[1] + '    ' + resultaat2[4]
    resultaat_line3 = resultaat2[2] + '    ' + resultaat2[5]
    echten_resultaat = resultaat_line1 + '\n' + resultaat_line2 + '\n' + resultaat_line3
    return echten_resultaat
    TE_KRIJGEN = (
        '  3801      123\n'
        '-    2    +  49\n'
        '------    -----'
    )

