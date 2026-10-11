def reverseInteger(x: int) -> int:
    rev = 0
    t = -1

    if x < 0:
        x = -x
        t = -1
    else:
        t = 1

    while x > 0:
        rem = x % 10
        rev = rev * 10 + rem
        x = x // 10

    return rev * t 