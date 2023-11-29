from arithmetic_arranger.prepare_arithmetic_problem import prepare_arithmetic_problem

def arithmetic_arranger(problems, with_answer = False) :
    # handle errors
    if len(problems) > 5 :
        return "Error: Too many problems."

    for problem in problems :
        [first_operand, operator, second_operand] = problem.split()
        if operator != '+' and operator != '-' :
            return "Error: Operator must be '+' or '-'."
        if len(first_operand) > 4 or len(second_operand) > 4 :
            return "Error: Numbers cannot be more than four digits."
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        try :
            first_operand = int(first_operand)
            first_operand = int(first_operand)
        except :
            return "Error: Numbers must only contain digits."
    # prepare problems
    prepared_problems = []
    for problem in problems :
        prepared_problems.append(prepare_arithmetic_problem(problem))

    result_strings = ["","","",""]
    for prepared_problem in prepared_problems :
        for index, result_string in enumerate(result_strings) :
                result_strings[index] += prepared_problem[index] + " " * 4
            
    # form result
    result = result_strings[0].rstrip() + '\n' + result_strings[1].rstrip() + '\n' + result_strings[2].rstrip()
    
    if with_answer :
        result += '\n' + result_strings[3].rstrip()
    
    return result