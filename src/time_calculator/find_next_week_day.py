def find_next_week_day(week_day, days_later) :
    if not week_day :
        return ''
    elif week_day and not days_later :
        return week_day

    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    week_day_index = week_days.index(week_day.lower())
    new_day_index = (week_day_index + days_later) % 7
    return week_days[new_day_index]
