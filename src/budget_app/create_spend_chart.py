def generate_row(names, i):
    row = ''
    for index, _ in enumerate(names):
        if len(names[index]) > i:
            row += names[index][i] + ' ' * 2
        else:
            row += ' ' * 3
    return row

def get_vertical_names(categories):
    names = []
    for category in categories:
        names.append(category.name)
    max_category_name_length = len(max(names, key=len))
    prefix = " " * 5
    vertical_names = []
    character_index = 0
    while character_index < max_category_name_length:
        vertical_names.append(prefix + generate_row(names, character_index))
        character_index+=1
    return vertical_names

def get_category_parts_in_spends(categories):
    total_withdrawals = 0
    for category in categories:
        total_withdrawals += category.get_withdrawals_total()
    percents = []
    for category in categories:
        category_part = category.get_withdrawals_total() / total_withdrawals * 100
        if category_part > 10:
            category_part = int(round(category_part / 10) * 10)
        else:
            category_part = 0
        percents.append(category_part)
    return percents

def add_category_parts_string(result, category_parts, percent):
    temp_result = result
    for category_part in category_parts:
        if (percent <= category_part):
            temp_result += ' o '
        else:
            temp_result += '   '
    temp_result += " \n"
    return temp_result

def get_chart_string(category_parts):
    result = ''
    percent = 100
    while percent >= 0:
        num = str(percent)
        if len(num) < 3:
           num = " " * (3 - len(num)) + num
        result += num + "|"
        result = add_category_parts_string(result, category_parts, percent)
        percent-=10
    return result

def get_separator(categories):
    categories_amount = len(categories)
    spacer = (1 + categories_amount * 3)
    return " " * 4 + "-" * spacer + "\n"

def create_spend_chart(categories):
    vertical_names = get_vertical_names(categories)
    category_parts = get_category_parts_in_spends(categories)
    
    result = "Percentage spent by category\n"
    result += get_chart_string(category_parts)
    
    result += get_separator(categories)
    result += '\n'.join(vertical_names)
    
    return result