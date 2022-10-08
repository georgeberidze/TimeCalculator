
def add_time(start, duration, *args):
    new_time = ""
    day_limit = 1439
    time_now = {} # holds all information we need for the final output

    week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    # parse input string into dictionary key-values
    time_now['format'] = start.split(' ')[1]
    time_now['hour'] = int(start.split(':')[0])
    time_now['minute'] = int(start.split(':')[1].split(' ')[0])
    
    # converts hours into minutes in a 24hr system. Counting starts at 12:00 AM which is 0 minute and day ends on minute 1440
    if time_now['format'] == 'AM' and time_now['hour'] == 12:
        time_now['converted'] = (time_now['hour'] * 0) + time_now['minute']
    elif time_now['format'] == 'PM' and time_now['hour'] != 12:
        time_now['converted'] = ((time_now['hour']+12) * 60) + time_now['minute']
    else:
        time_now['converted'] = (time_now['hour']* 60) + time_now['minute']
        
    add_converted_time = int(duration.split(':')[0])*60 + int(duration.split(':')[1])

    # count how many days passed
    new_time_converted = time_now['converted'] + add_converted_time
    time_now['days_passed'] = new_time_converted // day_limit

    # keep track of weekday (if day is passed in the argument)
    if args: 
        time_now['old_day'] = args[0].lower().capitalize()
        sum_days = week.index(time_now['old_day'])+time_now['days_passed']
        try:
            time_now['new_day'] = week[sum_days]
        except:
            time_now['new_day'] = week[(sum_days-(len(week)*(sum_days//7)))]

    # find what are new hours and minutes
    time_now['new_hour'] = new_time_converted - ((day_limit+1)*time_now['days_passed'])
    time_now['new_minute'] = (new_time_converted % 60)

    # convert 24 hr back to 12 hr format
    if (time_now['new_hour'] // 60) >= 12:
         time_now['new_hour'] = (time_now['new_hour'] // 60) - 12
         time_now['new_format'] = 'PM'
    else:
        time_now['new_hour'] = time_now['new_hour'] // 60
        time_now['new_format'] = 'AM'

    # displays hour 12 as hour 00
    if time_now['new_hour'] == 0:
        time_now['new_hour'] = 12

    # builds the final result string to match instructions
    new_time = f"{time_now['new_hour']}:"
    if time_now['new_minute'] < 10:
        new_time += "0"
    new_time += f"{time_now['new_minute']} {time_now['new_format']}"

    if 'new_day' in time_now:
        new_time += f", {time_now['new_day']}"

    if time_now['days_passed'] == 1:
        new_time += f" (next day)"
    elif time_now['days_passed'] > 1:
        new_time += f" ({time_now['days_passed']} days later)"

    return new_time