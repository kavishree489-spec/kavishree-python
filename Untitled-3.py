def normalise(text):

    text = text.replace(" ", "")
    text = text.replace("-", "")

    return text.upper()


def is_valid(reg):

    if len(reg) not in (9, 10):
        return False

    state = reg[0:2]
    district = reg[2:4]

    if not state.isalpha():
        return False

    if not district.isdigit():
        return False

    if len(reg) == 9:
        series = reg[4:5]
        number = reg[5:9]

    else:
        series = reg[4:6]
        number = reg[6:10]

    if not series.isalpha():
        return False

    if not number.isdigit():
        return False

    return True


def format_number(reg):

    return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


inputs = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB"
]

for raw in inputs:

    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "valid")
        print("Formatted:", format_number(reg))

    else:
        print(raw, "->", reg, "INVALID")