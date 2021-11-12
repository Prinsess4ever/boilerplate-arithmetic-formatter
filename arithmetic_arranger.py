import re


def solve_one_problem(problem, with_solution=False):
    match = re.match(r"^\s*([a-z0-9]+)\s*(.)\s*([a-z0-9]+)\s*$", problem).groups()

    num1 = match[0]
    sign = match[1]
    num2 = match[2]
    alnum1 = num1.isdigit()
    alnum2 = num2.isdigit()
    length = max(len(num1), len(num2))
    met_oplosing = ''
    if sign != '+' and sign != '-':
        return "Error: Operator must be '+' or '-'."
    elif length > 4:
        return "Error: Numbers cannot be more than four digits."
    elif alnum1 == True and alnum2 == False:
        return "Error: Numbers must only contain digits."
    elif alnum1 == True and alnum2 == False:
        return "Error: Numbers must only contain digits."
    elif with_solution == True and sign == "+":
        met_oplosing = int(num1) + int(num2)
        rjust1 = num1.rjust(length + 2)
        rjust2 = num2.rjust(length + 1)
        rjust3 = str(met_oplosing).rjust(length + 2)
        return rjust1 + '\n' + sign + rjust2 + '\n' + '-' * (length + 2) + '\n' + rjust3
    elif with_solution == True and sign == '-':
        met_oplosing = int(num1) - int(num2)
        rjust1 = num1.rjust(length + 2)
        rjust2 = num2.rjust(length + 1)
        rjust3 = str(met_oplosing).rjust(length + 2)
        return rjust1 + '\n' + sign + rjust2 + '\n' + '-' * (length + 2) + '\n' + rjust3
    else:
        rjust1 = num1.rjust(length + 2)
        rjust2 = num2.rjust(length + 1)
        return rjust1 + '\n' + sign + rjust2 + '\n' + '-' * (length + 2)


def arithmetic_arranger(problems, with_solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    resultaat2 = []
    resultaat_line1 = ''
    resultaat_line2 = ''
    resultaat_line3 = ''
    resultaat_line4 = ''
    echte_resultaat = ''

    for problem in problems:
        one_ready = solve_one_problem(problem , with_solution)
        if one_ready.startswith('Error'):
            return one_ready
        if with_solution == True:
            line1 = one_ready.splitlines()[0]
            line2 = one_ready.splitlines()[1]
            line3 = one_ready.splitlines()[2]
            line4 = one_ready.splitlines()[3]
            resultaat2.append(line1)
            resultaat2.append(line2)
            resultaat2.append(line3)
            resultaat2.append(line4)
        else:
            line1 = one_ready.splitlines()[0]
            line2 = one_ready.splitlines()[1]
            line3 = one_ready.splitlines()[2]
            resultaat2.append(line1)
            resultaat2.append(line2)
            resultaat2.append(line3)
        lengthe_of_lines = one_ready.splitlines()
    if len(lengthe_of_lines) == 4 and with_solution == True:
        if len(problems) == 5:
            resultaat_line1 = resultaat2[0] + '    ' + resultaat2[4] + '    ' + resultaat2[8] + '    ' + resultaat2[12] + '    ' + resultaat2[16]
            resultaat_line2 = resultaat2[1] + '    ' + resultaat2[5] + '    ' + resultaat2[9] + '    ' + resultaat2[13] + '    ' + resultaat2[17]
            resultaat_line3 = resultaat2[2] + '    ' + resultaat2[6] + '    ' + resultaat2[10] + '    ' + resultaat2[14] + '    ' + resultaat2[18]
            resultaat_line4 = resultaat2[3] + '    ' + resultaat2[7] + '    ' + resultaat2[11] + '    ' + resultaat2[15] + '    ' + resultaat2[19]
        elif len(problems) == 4:
            resultaat_line1 = resultaat2[0] + '    ' + resultaat2[4] + '    ' + resultaat2[8] + '    ' + resultaat2[12]
            resultaat_line2 = resultaat2[1] + '    ' + resultaat2[5] + '    ' + resultaat2[9] + '    ' + resultaat2[13]
            resultaat_line3 = resultaat2[2] + '    ' + resultaat2[6] + '    ' + resultaat2[10] + '    ' + resultaat2[14]
            resultaat_line4 = resultaat2[3] + '    ' + resultaat2[7] + '    ' + resultaat2[11] + '    ' + resultaat2[15]
        elif len(problems) == 3:
            resultaat_line1 = resultaat2[0] + '    ' + resultaat2[4] + '    ' + resultaat2[8]
            resultaat_line2 = resultaat2[1] + '    ' + resultaat2[5] + '    ' + resultaat2[9]
            resultaat_line3 = resultaat2[2] + '    ' + resultaat2[6] + '    ' + resultaat2[10]
            resultaat_line4 = resultaat2[3] + '    ' + resultaat2[7] + '    ' + resultaat2[11]
        else:
            resultaat_line1 = resultaat2[0] + '    ' + resultaat2[4]
            resultaat_line2 = resultaat2[1] + '    ' + resultaat2[5]
            resultaat_line3 = resultaat2[2] + '    ' + resultaat2[6]
            resultaat_line4 = resultaat2[3] + '    ' + resultaat2[7]
        echte_resultaat = resultaat_line1 + '\n' + resultaat_line2 + '\n' + resultaat_line3 + '\n' + resultaat_line4
        return echte_resultaat
    elif len(problems) == 5:
        resultaat_line1 = resultaat2[0] + '    ' + resultaat2[3] + '    ' + resultaat2[6] + '    ' + resultaat2[9] + '    ' + resultaat2[12]
        resultaat_line2 = resultaat2[1] + '    ' + resultaat2[4] + '    ' + resultaat2[7] + '    ' + resultaat2[10] + '    ' + resultaat2[13]
        resultaat_line3 = resultaat2[2] + '    ' + resultaat2[5] + '    ' + resultaat2[8] + '    ' + resultaat2[11] + '    ' + resultaat2[14]
    elif len(problems) == 4:
        resultaat_line1 = resultaat2[0] + '    ' + resultaat2[3] + '    ' + resultaat2[6] + '    ' + resultaat2[9]
        resultaat_line2 = resultaat2[1] + '    ' + resultaat2[4] + '    ' + resultaat2[7] + '    ' + resultaat2[10]
        resultaat_line3 = resultaat2[2] + '    ' + resultaat2[5] + '    ' + resultaat2[8] + '    ' + resultaat2[11]
    elif len(problems) == 3:
        resultaat_line1 = resultaat2[0] + '    ' + resultaat2[3] + '    ' + resultaat2[6]
        resultaat_line2 = resultaat2[1] + '    ' + resultaat2[4] + '    ' + resultaat2[7]
        resultaat_line3 = resultaat2[2] + '    ' + resultaat2[5] + '    ' + resultaat2[8]
    else:
        resultaat_line1 = resultaat2[0] + '    ' + resultaat2[3]
        resultaat_line2 = resultaat2[1] + '    ' + resultaat2[4]
        resultaat_line3 = resultaat2[2] + '    ' + resultaat2[5]

    echte_resultaat = resultaat_line1 + '\n' + resultaat_line2 + '\n' + resultaat_line3
    return echte_resultaat
    TE_KRIJGEN = (
        '  3801      123\n'
        '-    2    +  49\n'
        '------    -----'
    )

