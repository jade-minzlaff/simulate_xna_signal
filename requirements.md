requirements for simulate_xna_signal.py
Required packages:
Pandas, NumPy, MatPlotLib

Pandas is used to read data from a .csv file containing a library of possible 4mers and their associated experimental nanopore signal into Python. 
NumPy is used for numerical operations involved in signal processing and in the generation of synthetic noise. This uses data imported by Pandas. 
MatPlotLib is used to generate the step function plot which is output by the package, dependent on numerical operations and data accomplished by Pandas and NumPy. 