def get_divider(hours):
    if hours == 36:
        divider = 180
    elif hours == 40:
        divider = 200
    elif hours == 44:
        divider = 220

    return int(divider)