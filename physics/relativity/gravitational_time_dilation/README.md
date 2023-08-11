# Gravitational Time Dilation Calculator

This script allows you to calculate gravitational time dilation based on the mass of the gravitating object, the distance from the mass, and the time interval. You can specify these values either through command-line arguments or interactive prompts.
## Prerequisites

python
```bash
Python 3.x
```
## Installation

Clone the repository or download the script.
## Usage
### Command-Line Arguments

You can run the script with the following command-line arguments:

`--mass`: Mass of the gravitating object in kilograms
`--distance`: Distance from the mass in meters
`--time`: Time interval in years

### Example:

```bash
python main.py --mass 5.972e24 --distance 6371000 --time 5

# returns
Observer's time experienced: 4.999999996519461 years
Object's time experienced: 5.0 years
```

### Interactive Prompts

If you run the script without any arguments, it will prompt you to enter the required information interactively:

```bash
python main.py
```
## Understanding Gravitational Time Dilation

Gravitational time dilation is a difference in the elapsed time measured by two observers, due to a difference in gravitational potential between their locations. This effect is described by the general theory of relativity, and the formula for gravitational time dilation is given by:

$t' = t \sqrt{1 - \frac{2GM}{rc^2}}$

Where:

- `t'`: Time experienced by the observer (dilated time).
- `t`: Proper time experienced by the object (time interval in the object's rest frame).
- `G`: Gravitational constant, approximately 6.67430×10−11 m3 kg−1 s−26.67430×10−11m3kg−1s−2.
- `M`: Mass of the gravitating object in kilograms.
- `r`: Distance from the mass in meters.
- `c`: Speed of light in a vacuum, approximately 299,792,458 meters per second.

In the context of this script, you can specify the mass of the gravitating object, the distance from the mass, and the time interval in years. The script then calculates the time experienced by an observer and an object, applying the above formula.