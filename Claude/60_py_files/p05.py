"""Problem 5: Ohm's law: current and power"""


def p05():
    voltage, resistance = 12.0, 4.0        # volts, ohms
    current = voltage / resistance          # I = V / R
    power = voltage * current               # P = V * I
    print(f"V = {voltage} V, R = {resistance} ohm")
    print(f"Current I = {current} A, Power P = {power} W")


if __name__ == "__main__":
    p05()
