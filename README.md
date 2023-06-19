# Fractal Plant - L-System Simulation

This repository contains an implementation of an L-system to simulate fractal plant.
The L-system is defined by the following parameters:

## Symbols

- X: Auxiliary symbol
- F: Go forward and draw a line
- +: Rotate by 25 degrees
- -: Rotate by -25 degrees
- [: Push the current state
- ]: Pop the state

## Initial Word

The initial word is set to X.

## Rules

- Rule P1: X → F+[[X]-X]-F[-FX]+X
- Rule P2: F → FF+

## Initial Values

The initial position is set to (x=0, y=0). The initial angle is set to 25 degrees (alpha = 25°).

## Usage

1. Run the program.
2. Observe the output, which includes the generated graphical representation of the fractal plant on the plot.
