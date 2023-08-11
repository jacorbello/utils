# Heat Transfer

This utility allows you to calculate heat transfer through conduction. You can specify the thermal conductivity, cross-sectional area, temperature difference, and distance, either through command-line arguments or interactive prompts.

## Prerequisites

python
```
Python 3.x
```

## Installation

Clone the repository or download the script.

## Usage
### Command-Line Arguments

You can run the script with the following command-line arguments:

`--conductivity`: Thermal conductivity in W/m*K
`--area`: Cross-sectional area in square meters
`--temp-difference`: Temperature difference in Kelvin
`--distance`: Distance in meters

Example:

```bash
python main.py --conductivity 50 --area 0.01 --temp-difference 100 --distance 0.05

# returns
Heat transfer rate: 10000.0 W
```

## Interactive Prompts

If you run the script without any arguments, it will prompt you to enter the required information interactively:

```bash
python main.py
```

## Understanding Heat Transfer

Heat transfer through conduction is a process where heat is transferred within a solid material without the movement of the material itself. The formula for calculating heat transfer through conduction is given by:

$ q = \frac{{k \cdot A \cdot \Delta T}}{{d}} $

Where:

- `q`: Heat transfer rate (W)
- `k`: Thermal conductivity (W/m*K)
- `A`: Cross-sectional area (m^2)
- `dT`: Temperature difference (K)
- `d`: Distance (m)

In the context of this script, you can specify the thermal conductivity, cross-sectional area, temperature difference, and distance. The script then calculates the heat transfer rate using the above formula.
