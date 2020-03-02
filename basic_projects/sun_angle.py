def sun_angle(time):
    hh = int(time.split(":")[0])
    mm = int(time.split(":")[1])

    if hh <= 6 or hh >= 18:
        return str("I don't see the sun!")

