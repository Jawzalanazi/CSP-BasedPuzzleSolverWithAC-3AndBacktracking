from itertools import product
from queue import Queue

def is_valid_operation(group, operation, target, values):
    """Check if the operation on the group satisfies the target."""
    if operation == '+':
        return sum(values) == target
    elif operation == '-':
        return abs(values[0] - values[1]) == target
    elif operation == '*':
        result = 1
        for value in values:
            result *= value
        return result == target
    elif operation == '/':
        return max(values) / min(values) == target
    return False

def ac3(variables, domains, neighbors):
    """AC-3 algorithm for enforcing arc-consistency."""
    queue = Queue()
    for xi in variables:
        for xj in neighbors[xi]:
            queue.put((xi, xj))

    while not queue.empty():
        xi, xj = queue.get()
        if revise(xi, xj, domains):
            if not domains[xi]:
                print(f"AC-3 failed, empty domain for {xi}")
                return False
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.put((xk, xi))
    return True

def revise(xi, xj, domains):
    """Revise domains of xi based on xj."""
    revised = False
    for x in set(domains[xi]):
        if not any(x != y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised

def select_unassigned_variable(assignment, variables, domains):
    """Select variable using Minimum Remaining Values (MRV) heuristic."""
    unassigned = [var for var in variables if var not in assignment]
    return min(unassigned, key=lambda var: len(domains[var]))

def forward_checking(assignment, var, value, domains, neighbors):
    """Perform forward checking after assigning value to var."""
    for neighbor in neighbors[var]:
        if neighbor not in assignment:
            domains[neighbor] = [v for v in domains[neighbor] if v != value]

def backtrack(assignment, variables, domains, neighbors, groups):
    """Backtracking search with MRV and forward checking."""
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment, variables, domains)
    print(f"Selecting variable: {var} with domain: {domains[var]}")  # Debug: Print selected variable and its domain
    for value in domains[var]:
        if all(value != assignment.get(neighbor) for neighbor in neighbors[var] if neighbor in assignment):
            assignment[var] = value
            forward_checking(assignment, var, value, domains, neighbors)

            result = backtrack(assignment, variables, domains, neighbors, groups)
            if result:
                return result

            del assignment[var]
    return None

def solve_puzzle(grid_size, groups):
    """Solve the puzzle using CSP approach."""
    variables = [(i, j) for i in range(grid_size) for j in range(grid_size)]
    domains = {var: list(range(1, grid_size + 1)) for var in variables}
    neighbors = {
        var: [(var[0], col) for col in range(grid_size) if col != var[1]] +
             [(row, var[1]) for row in range(grid_size) if row != var[0]]
        for var in variables
    }

    if not ac3(variables, domains, neighbors):
        return None

    assignment = {}
    return backtrack(assignment, variables, domains, neighbors, groups)

# Example usage
if __name__ == "__main__":
    grid_size = int(input("Enter the grid size: "))  # User input for grid size
    groups = [
        ({(0, 0), (0, 1)}, '+', 10),  # Changed from 5 to 10
        ({(1, 0), (1, 1)}, '*', 12),  # Changed from 6 to 12
        ({(2, 2), (3, 2)}, '-', 3),   # Changed from 1 to 3
    ]

    solution = solve_puzzle(grid_size, groups)
    if solution:
        for i in range(grid_size):
            print([solution[(i, j)] for j in range(grid_size)])
    else:
        print("No solution found.")
