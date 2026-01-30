def seconds_since_midnight(seconds):
    if not isinstance(seconds, int):
        return "Invalid input.Seconds must be an integer."
    hours24 = seconds//3600
    remaining = seconds%3600
    minutes = remaining//60
    secs = remaining%60

    if hours24 <12:
        period = "AM"
    else:
        period = "PM"
    hours12 = hours24 %12
    if hours12 ==0:
        hours_12 = 12

    return f"{hours12:02d} {minutes:02d} {secs:02d} {period}"

##done (double)

