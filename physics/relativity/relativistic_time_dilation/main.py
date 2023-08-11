import argparse
from math import sqrt

def relativistic_time_dilation(v, t):
    c = 299792458  # Speed of light in meters per second
    gamma = 1 / sqrt(1 - (v**2 / c**2))  # Lorentz factor
    observer_time = t * gamma  # Time experienced by the observer
    object_time = t  # Time experienced by the object (proper time)
    return observer_time, object_time

def main():
    parser = argparse.ArgumentParser(description="Calculate time dilation based on relative velocity and time interval.")
    parser.add_argument("--velocity", type=float, help="Relative velocity as a percentage of the speed of light (e.g., 98 for 98%).")
    parser.add_argument("--time", type=float, help="Time interval in years.")

    args = parser.parse_args()

    if args.velocity is None:
        v_percentage = float(input("Enter the relative velocity as a percentage of the speed of light (e.g., 98 for 98%): "))
    else:
        v_percentage = args.velocity

    if args.time is None:
        t_years = float(input("Enter the time interval in years: "))
    else:
        t_years = args.time

    # Converting the input values
    c = 299792458  # Speed of light in meters per second
    v = v_percentage / 100 * c  # Converting percentage to actual speed
    t = t_years * 365 * 24 * 60 * 60  # Converting years to seconds

    # Calculating time dilation
    observer_time, object_time = relativistic_time_dilation(v, t)
    print(f"Observer's time experienced: {observer_time / (365 * 24 * 60 * 60)} years")
    print(f"Object's time experienced: {object_time / (365 * 24 * 60 * 60)} years")

if __name__ == "__main__":
    main()
