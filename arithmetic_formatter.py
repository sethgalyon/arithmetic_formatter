# Arithmetic Formatter
#
# input:  list of string(s)
#         (optional) boolean
#             True  = solve arithmetic problem(s)
#             False = don't solve arithmetic problem(s)
#
# output: return arithmetic problem(s) string formatted vertically
#         (optional) answer to arithmetic problems
#             added to vertical formatting

def arithmetic_formatter(problems: list = [], solve: bool = False) -> str:
    if not problems:
        return 'Error: No problems provided.'
    
    if len(problems) > 5:
        return 'Error: Too many problems.'

    l1, l2, l3, l4 = [], [], [], []

    for problem in problems:
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
    
        if '+' in problem:
            nums = problem.replace(' ', '').split('+')
            op = '+'
        else:
            nums = problem.replace(' ', '').split('-')
            op = '-'
        
        max_digits = max(map(len, nums))
        if max_digits > 4:
            return 'Error: Numbers cannot be more than four digits.'

        try:
            nums[0] = int(nums[0])
            nums[1] = int(nums[1])
            nums.append(0)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        
        l1.append(' ' * (max_digits - len(str(nums[0])) + 2) + str(nums[0]))
        l2.append(f'{op} ' + ' ' * (max_digits - len(str(nums[1]))) + str(nums[1]))
        l3.append('-' * (max_digits + 2))

        if solve:
            if op == '+':
                nums[2] = nums[0] + nums[1]
            else:
                nums[2] = nums[0] - nums[1]
            l4.append(' ' * (max_digits - len(str(nums[2])) + 2) + str(nums[2]))

    l1 = '    '.join(l1)
    l2 = '    '.join(l2)
    l3 = '    '.join(l3)
    if solve: 
        l4 = '    '.join(l4)
        return '\n'.join([l1, l2, l3, l4])
    else:
        return '\n'.join([l1, l2, l3])

if __name__ == '__main__':
    # Expected output:
    #   32         1      9999      523
    # +  8    - 3801    + 9999    -  49
    # ----    ------    ------    -----
    #   40     -3800     19998      474
    print(arithmetic_formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

    print()

    # Expected output:
    #    32      3801      45      123
    # + 698    -    2    + 43    +  49
    # -----    ------    ----    -----
    print(arithmetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

    print()

    # Expected output:
    #    32      3801      45      123
    # + 698    -    2    + 43    +  49
    # -----    ------    ----    -----
    #   730      3799      88      172
    print(arithmetic_formatter(["32+698", "3801-2", "45+43", "123+49"], True))
