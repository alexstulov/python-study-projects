def prepare_arithmetic_problem(arithmetic_problem) :
    # parse data
    answer = str(eval(arithmetic_problem))
    arithmetic_problem = arithmetic_problem.split();
    first_operand = arithmetic_problem[0]
    operator = arithmetic_problem[1]
    second_operand = arithmetic_problem[2]
    first_operand_length = len(first_operand)
    second_operand_length = len(second_operand)
    # organize first two strings
    first_string = first_operand
    second_string = second_operand
    length_difference = 0
    if first_operand_length > second_operand_length :
        length_difference = first_operand_length - second_operand_length
        first_string = first_operand
        second_string = " " * length_difference + second_operand
    elif first_operand_length < second_operand_length :
        length_difference = second_operand_length - first_operand_length
        first_string = " " * length_difference + first_operand
        second_string = second_operand
    first_string = "  " + first_string
    second_string = operator + " " + second_string
    # organize last two strings
    max_length = max(first_operand_length, second_operand_length)
    dashes_amount = max_length + 2
    dashes_string = "-" * dashes_amount
    answer_string = " " * (dashes_amount - len(answer)) + answer
    # organize result
    return [
        first_string,
        second_string,
        dashes_string,
        answer_string
    ]