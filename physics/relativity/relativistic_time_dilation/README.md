# Time Dilation Calculator

This script allows you to calculate time dilation based on relative velocity and time interval. You can specify the relative velocity as a percentage of the speed of light and the time interval in years, either through command-line arguments or interactive prompts.
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

`--velocity`: Relative velocity as a percentage of the speed of light (e.g., 98 for 98%)
`--time`: Time interval in years

Example:

```bash

python main.py --velocity 98 --time 5

# returns
Observer's time experienced: 25.125945381480275 years
Object's time experienced: 5.0 years
```


## Interactive Prompts

If you run the script without any arguments, it will prompt you to enter the required information interactively:

```bash
python main.py
```
## Understanding Time Dilation

Time dilation is a difference in the elapsed time measured by two observers, due to a relative velocity between them. This effect is described by the special theory of relativity, and the formula for time dilation is given by:

$t' = \frac{t}{\sqrt{1 - \frac{v^2}{c^2}}}$​

​t​

Where:

- `t′`: Time experienced by the observer (dilated time).
- `t`: Proper time experienced by the object (time interval in the object's rest frame).
- `v`: Relative velocity between the observer and the object.
- `c`: Speed of light in a vacuum, approximately 299,792,458299,792,458 meters per second.

The factor $\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$

​1​ is known as the Lorentz factor, and it quantifies how much time dilation occurs. As the relative velocity vv approaches the speed of light cc, the Lorentz factor increases, leading to greater time dilation.

In the context of this script, you can specify the relative velocity as a percentage of the speed of light and the time interval in years. The script then calculates the time experienced by an observer and an object moving at the given velocity, applying the above formula.