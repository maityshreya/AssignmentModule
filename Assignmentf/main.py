import constants

def calculate_circumference(radius):
    return 2 * constants.PI * radius

def calculate_energy(mass):
    return mass * constants.SPEED_OF_LIGHT ** 2

def main():
    radius = 5
    mass = 1  # in kg

    circumference = calculate_circumference(radius)
    energy = calculate_energy(mass)

    print(f"The circumference of a circle with radius {radius} is {circumference:.2f}")
    print(f"The energy equivalent of mass {mass} kg is {energy:.2e} J")

if __name__ == "__main__":
    main()