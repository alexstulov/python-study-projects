from time_calculator.parse_input import parse_input
from time_calculator.find_next_week_day import find_next_week_day
from time_calculator.calculate_minutes import calculate_minutes
from time_calculator.calculate_hours_and_noon import calculate_hours_and_noon
    
def add_time(start, duration, *args):
    [noon, hours, added_hours, minutes, added_minutes, week_day] = parse_input(start, duration, *args)
    [additional_hours, result_minutes] = calculate_minutes(minutes, added_minutes)
    [result_hours, result_noon, days_later] = calculate_hours_and_noon(hours, added_hours, additional_hours, noon)
    result = str(result_hours) + ":" + str(result_minutes) + " " + result_noon
    # add week day if needed
    week_day = find_next_week_day(week_day, days_later)
    if (week_day) :
        result += ", " + week_day.capitalize()
    if (days_later == 1) :
        result += " (next day)"
    elif(days_later > 1) :
        result += " (" + str(days_later) + " days later)"
         
    return result