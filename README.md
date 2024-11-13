# Optimization DSS Project

## Overview

This project implements a Decision Support System (DSS) to solve the Balanced Transportation Problem using Vogel's Approximation Method. The system uses Python and the Tkinter library for the graphical user interface (GUI). The primary goal is to optimize the allocation of resources from multiple sources to multiple destinations while minimizing transportation cost.

## Features

- **Balanced Transportation Problem**: The system is designed specifically for balanced scenarios, where the total supply equals the total demand.
- **Interactive GUI**: Users can input the cost matrix, supply, and demand values directly into the system's GUI.
- **Real-Time Calculation**: The system calculates and displays the optimal allocation of resources using Vogel's Approximation Method.
- **Error Handling**: The system checks that the total supply equals total demand and provides feedback if they do not match.

## Installation

### Prerequisites

- Python 3.11.2
- Tkinter (typically included with Python)
- NumPy

### Steps

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Shegzimus/optimization-dss-project.git
    ```
2. **Navigate to the Project Directory**:
    ```sh
    cd optimization-dss-project
    ```
3. **Install the Required Python Packages**:
    ```sh
    pip install numpy
    ```
4. **Run the Application**:
    ```sh
    python OptimizationDSS.py
    ```

## Usage

1. **Launching the Application**: Run the Python script `OptimizationDSS.py` to launch the application window.
   
2. **Input Fields**:
   - **Cost Matrix**: Enter the transportation costs between each source and destination.
   - **Supply and Demand**: Enter the supply available at each source and the demand required at each destination.

3. **Calculate**: Click the "Calculate" button to compute the optimal allocation using Vogel's Approximation Method. The results will be displayed in the grid below.

4. **Error Messages**: If the total supply does not match the total demand, an error message will be displayed, prompting you to adjust the inputs.

## Vogel's Approximation Method

The Vogel's Approximation Method is a heuristic for finding a good initial feasible solution for the transportation problem. The method prioritizes routes with the highest penalty (difference between the two lowest costs) to allocate resources, iterating until all supplies and demands are satisfied.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Tkinter**: For providing the GUI components.
- **NumPy**: For the efficient numerical computations.

## Contact

For any queries, please contact [segun.ajet@protonmail.com](mailto:segun.ajet@protonmail.com).
