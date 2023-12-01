from time_calculator.switch_noon import switch_noon

def calculate_hours_and_noon(hours, added_hours, additional_hours, noon):
    result_hours = int(hours) + int(added_hours) + additional_hours
    result_noon = noon
    times_to_change = 0
    if (result_hours == 12) :
        result_noon = switch_noon(noon)
    elif (result_hours > 12) :
        times_to_change = int(result_hours / 12)
        if (times_to_change % 2 != 0) :
            result_noon = switch_noon(noon)
        result_hours = abs(result_hours - times_to_change * 12)
        result_hours = result_hours if result_hours > 0 else 12
    days_later = 0
    if (noon == 'PM' and result_noon == 'AM' and times_to_change == 1) :
        days_later = 1
    elif (times_to_change) :
        days_later = round(times_to_change / 2)    
    return [result_hours, result_noon, days_later]