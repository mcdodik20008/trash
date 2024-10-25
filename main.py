def get_baza(arr):
    lng = 0
    sm = 0
    for a in arr:
        if int(a) % 2 == 0 and int(a) > 0:
            lng += 1
            sm += int(a)
    return lng, sm

