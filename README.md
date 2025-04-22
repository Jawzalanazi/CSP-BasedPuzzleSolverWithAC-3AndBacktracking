# CSP-Based Puzzle Solver with AC-3 and Backtracking

This project provides a **Constraint Satisfaction Problem (CSP)** solver for grid-based puzzles. It uses the **AC-3** (Arc-Consistency) algorithm for enforcing constraints and a **Backtracking** algorithm for variable assignment. The solver aims to assign values to grid cells while satisfying a set of mathematical constraints like addition, subtraction, multiplication, and division.

## Features:
- **AC-3 Algorithm**: Enforces arc-consistency by revising variable domains.
- **Backtracking Search**: Uses **Minimum Remaining Values (MRV)** heuristic and **forward checking** for pruning invalid values during the search.
- **Mathematical Constraints**: The solver can handle various operations such as sum, difference, product, and ratio to check if the assigned values satisfy the target.

## How It Works:
1. **AC-3 Algorithm**: 
   - Ensures that each variable has valid values that do not violate any constraints with its neighbors. If a variable's value becomes inconsistent with its neighbors, it is removed from the domain.
   
2. **Backtracking Search**: 
   - After enforcing arc-consistency, the program uses backtracking to try different variable assignments. If an assignment fails, it backtracks and tries another value until it finds a valid solution or determines no solution exists.

3. **Constraint Validation**: 
   - For each group of variables, the solver checks if the values assigned satisfy the operation-based constraints (addition, subtraction, multiplication, or division).

## How to Use:
1. **Input**: 
   - The solver asks for the **grid size** (e.g., `4` for a 4x4 grid) and the **number of groups** to be satisfied with the constraints.
   
2. **Output**: 
   - If the solver finds a valid solution, it prints the grid configuration. If no solution exists, it informs the user.

### Steps to Run:
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    ```

2. Navigate to the project folder:
    ```bash
    cd your-repository-name
    ```

3. Run the program:
    ```bash
    python puzzle_solver.py
    ```

4. Enter the required **grid size** and **number of groups** when prompted.

## Example:
### Input:
```
Enter the number of groups: 3
```

### Output:
```
Solution found:
[ [2, 3, 1, 4], 
  [3, 1, 4, 2],
  [1, 4, 2, 3],
  [4, 2, 3, 1] ]
```

## Notes:
- The program is designed for puzzles where the constraints are relatively simple and do not create contradictions.
- For larger grids or more complex constraints, the solution time may increase as the algorithm explores more possibilities.

## License:
This project is provided for educational purposes.
Feel free to use or adapt it with credit.
