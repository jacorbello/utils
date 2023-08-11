import argparse

def heat_transfer(k, A, dT, d):
    """
    Calculate heat transfer through conduction.

    :param k: Thermal conductivity (W/m*K)
    :param A: Cross-sectional area (m^2)
    :param dT: Temperature difference (K)
    :param d: Distance (m)
    :return: Heat transfer rate (W)
    """
    return (k * A * dT) / d

def main():
    parser = argparse.ArgumentParser(description="Calculate heat transfer through conduction.")
    parser.add_argument("--conductivity", type=float, help="Thermal conductivity in W/m*K.")
    parser.add_argument("--area", type=float, help="Cross-sectional area in square meters.")
    parser.add_argument("--temp-difference", type=float, help="Temperature difference in Kelvin.")
    parser.add_argument("--distance", type=float, help="Distance in meters.")

    args = parser.parse_args()

    k = args.conductivity if args.conductivity else float(input("Enter the thermal conductivity in W/m*K: "))
    A = args.area if args.area else float(input("Enter the cross-sectional area in square meters: "))
    dT = args.temp_difference if args.temp_difference else float(input("Enter the temperature difference in Kelvin: "))
    d = args.distance if args.distance else float(input("Enter the distance in meters: "))

    # Calculating heat transfer
    q = heat_transfer(k, A, dT, d)
    print(f"Heat transfer rate: {q} W")

if __name__ == "__main__":
    main()
