def parse_input(start, duration, *args):
    [time, noon] = start.split()
    [hours, minutes] = time.split(':')
    [add_hours, add_minutes] = duration.split(':')
    week_day = ''
    if (len(args) > 0) :
        week_day = args[0]
    return [noon, hours, add_hours, minutes, add_minutes, week_day]
