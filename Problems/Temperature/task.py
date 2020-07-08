FAH_TO_C = "F"
C_TO_FAH = "C"


def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def type_unit(type_t):
    types = {"F": "C", "C": "F"}
    return types[type_t]


def choice(type_t, temp):
    if type_t == FAH_TO_C:
        return fahrenheit_to_celsius(temp)
    elif type_t == C_TO_FAH:
        return celsius_to_fahrenheit(temp)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    new_temp = choice(unit, int(temperature))
    new_unit = type_unit(unit)
    print(f"{new_temp} {new_unit}")
