# Arithmetic Formatter
#
# input: list of string(s)
#        (optional) boolean
#            True  = solve arithmetic problem(s)
#            False = don't solve arithmetic problem(s)
#
# output: arithmetic problem(s) printed onto terminal line
#         formatted vertically
#             (optional) answer to arithmetic problems
#             added to vertical formatting

def arithmetic_formatter(problems: list = [], solve: bool = False) -> None:
    if not problems:
        return
    
    if len(problems) > 5:
        print('Error: Too many problems.')
        return

    l1 = []
    l2 = []
    l3 = []
    l4 = []

    for i, problem in enumerate(problems):
        if '*' in problem or '/' in problem:
            print("Error: Operator must be '+' or '-'.")
            return
        
        if '+' in problem:
            parts = problem.split('+')
            op = '+'
        else:
            parts = problem.split('-')
            op = '-'
        
        max_digits = max(map(len, parts)) - 1
        if max_digits > 4:
            print('Error: Numbers cannot be more than four digits.')
            return

        try:
            parts[0] = int(parts[0].strip())
            parts[1] = int(parts[1].strip())
        except ValueError:
            print('Error: Numbers must only contain digits.')
            return
        
        if solve:
            if '+' in problem:
                parts.append(parts[0] + parts[1])
            else:
                parts.append(parts[0] - parts[1])
        
        l1.append(' ' * (max_digits - len(str(parts[0])) + 2) + str(parts[0]))
        l2.append(f'{op} ' + ' ' * (max_digits - len(str(parts[1]))) + str(parts[1]))
        l3.append('-' * (max_digits + 2))
        if solve:
            l4.append(' ' * (max_digits - len(str(parts[2])) + 2) + str(parts[2]))

    print(*l1, sep='    ')
    print(*l2, sep='    ')
    print(*l3, sep='    ')
    if solve: 
        print(*l4, sep='    ')

if __name__ == '__main__':
    # Expected output:
    #   32         1      9999      523
    # +  8    - 3801    + 9999    -  49
    # ----    ------    ------    -----
    #   40     -3800     19998      474
    arithmetic_formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

    print()

    # Expected output:
    #    32      3801      45      123
    # + 698    -    2    + 43    +  49
    # -----    ------    ----    -----
    arithmetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])