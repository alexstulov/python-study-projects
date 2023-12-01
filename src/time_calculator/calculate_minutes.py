def calculate_minutes(minutes, added_minutes):
    result_minutes = int(added_minutes) + int(minutes)
    additional_hours = 0
    if (result_minutes >= 60) :
        additional_hours = round(result_minutes / 60)
        result_minutes = result_minutes - additional_hours * 60
    
    result_minutes = str(result_minutes)
    if (len(result_minutes) < 2) :
        result_minutes = "0" + result_minutes
    return [additional_hours, result_minutes]