import argparse
from math import sqrt

def gravitational_time_dilation(M, r, t):
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    c = 299792458  # Speed of light in meters per second
    factor = sqrt(1 - (2 * G * M) / (r * c**2))  # Gravitational time dilation factor
    observer_time = t * factor  # Time experienced by the observer
    object_time = t  # Time experienced by the object (proper time)
    return observer_time, object_time

def main():
    parser = argparse.ArgumentParser(description="Calculate gravitational time dilation based on mass, distance, and time interval.")
    parser.add_argument("--mass", type=float, help="Mass of the gravitating object in kilograms.")
    parser.add_argument("--distance", type=float, help="Distance from the mass in meters.")
    parser.add_argument("--time", type=float, help="Time interval in years.")

    args = parser.parse_args()

    if args.mass is None:
        M = float(input("Enter the mass of the gravitating object in kilograms: "))
    else:
        M = args.mass

    if args.distance is None:
        r = float(input("Enter the distance from the mass in meters: "))
    else:
        r = args.distance

    if args.time is None:
        t_years = float(input("Enter the time interval in years: "))
    else:
        t_years = args.time

    # Converting the time interval from years to seconds
    t = t_years * 365 * 24 * 60 * 60

    # Calculating gravitational time dilation
    observer_time, object_time = gravitational_time_dilation(M, r, t)
    print(f"Observer's time experienced: {observer_time / (365 * 24 * 60 * 60)} years")
    print(f"Object's time experienced: {object_time / (365 * 24 * 60 * 60)} years")

if __name__ == "__main__":
    main()
