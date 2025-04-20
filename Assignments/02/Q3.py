import time
from collections import deque
from ortools.sat.python import cp_model

def read_puzzle_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines[0].strip(), lines

def write_solution_to_file(filename, solution, lines, line_number):
    if len(lines) > line_number:
        lines[line_number] = solution + "\n"
    else:
        while len(lines) < line_number:
            lines.append("\n")
        lines.append(solution + "\n")
    with open(filename, "w") as f:
        f.writelines(lines)

def string_to_grid(puzzle_str):
    return [[int(puzzle_str[r * 9 + c]) for c in range(9)] for r in range(9)]

def grid_to_string(grid):
    return "".join(str(cell) for row in grid for cell in row)

# Version 1: CSP + AC3 + Backtracking
def get_peers(row, col):
    peers = set()
    for i in range(9):
        peers.add((row, i))
        peers.add((i, col))
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            peers.add((r, c))
    peers.discard((row, col))
    return peers

def initialize_domains(grid):
    domains = {}
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                domains[(row, col)] = set(range(1, 10))
            else:
                domains[(row, col)] = {grid[row][col]}
    return domains

def ac3(domains):
    queue = deque([(xi, xj) for xi in domains for xj in get_peers(*xi)])
    while queue:
        xi, xj = queue.popleft()
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in get_peers(*xi):
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(domains, xi, xj):
    revised = False
    if len(domains[xj]) == 1:
        val = next(iter(domains[xj]))
        if val in domains[xi] and len(domains[xi]) > 1:
            domains[xi].discard(val)
            revised = True
    return revised

def select_unassigned_variable(domains):
    unassigned = [v for v in domains if len(domains[v]) > 1]
    return min(unassigned, key=lambda var: len(domains[var]), default=None)

def is_complete(domains):
    return all(len(domains[v]) == 1 for v in domains)

def is_consistent(value, var, domains):
    for peer in get_peers(*var):
        if len(domains[peer]) == 1 and value == next(iter(domains[peer])):
            return False
    return True

def backtrack(domains):
    if is_complete(domains):
        return domains
    var = select_unassigned_variable(domains)
    if not var:
        return None
    for value in sorted(domains[var]):
        if is_consistent(value, var, domains):
            new_domains = {v: set(domains[v]) for v in domains}
            new_domains[var] = {value}
            if ac3(new_domains):
                result = backtrack(new_domains)
                if result:
                    return result
    return None

def domains_to_grid(domains):
    grid = [[0] * 9 for _ in range(9)]
    for (row, col), val in domains.items():
        grid[row][col] = next(iter(val))
    return grid

def run_csp_solver(puzzle_str, lines):
    grid = string_to_grid(puzzle_str)
    domains = initialize_domains(grid)
    start = time.time()
    ac3(domains)
    result = backtrack(domains)
    end = time.time()
    if result:
        solution_grid = domains_to_grid(result)
        solution_str = grid_to_string(solution_grid)
        write_solution_to_file("Q3.txt", solution_str, lines, 1)
        print("-> CSP + AC3 + Backtracking Solver finished in ", round(end - start, 6), "seconds.")
    else:
        print("CSP Solver failed.")

# Version 2: OR-Tools Solver
def run_or_tools_solver(puzzle_str, lines):
    grid = string_to_grid(puzzle_str)
    model = cp_model.CpModel()
    cells = [[model.NewIntVar(1, 9, f"cell_{r}_{c}") for c in range(9)] for r in range(9)]
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                model.Add(cells[r][c] == grid[r][c])
    for i in range(9):
        model.AddAllDifferent(cells[i])
        model.AddAllDifferent([cells[r][i] for r in range(9)])
    for block_r in range(3):
        for block_c in range(3):
            block = []
            for r in range(3):
                for c in range(3):
                    block.append(cells[3*block_r + r][3*block_c + c])
            model.AddAllDifferent(block)
    solver = cp_model.CpSolver()
    start = time.time()
    status = solver.Solve(model)
    end = time.time()
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        solved_grid = [[solver.Value(cells[r][c]) for c in range(9)] for r in range(9)]
        solution_str = grid_to_string(solved_grid)
        write_solution_to_file("Q3.txt", solution_str, lines, 2)
        print("-> OR-Tools Solver finished in ", round(end - start, 6), "seconds.")
    else:
        print("OR-Tools failed.")

# Version 3: GPT Solver (Basic Backtracking)
def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    return True

def solve_basic(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_basic(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def run_gpt_solver(puzzle_str, lines):
    grid = string_to_grid(puzzle_str)
    start = time.time()
    solve_basic(grid)
    end = time.time()
    solution_str = grid_to_string(grid)
    write_solution_to_file("Q3.txt", solution_str, lines, 3)
    print("-> GPT Solver finished in ", round(end - start, 6), "seconds.")

# Main 
def main():
    puzzle_str, lines = read_puzzle_from_file("Q3.txt")
    run_csp_solver(puzzle_str, lines)
    run_or_tools_solver(puzzle_str, lines)
    run_gpt_solver(puzzle_str, lines)

if __name__ == "__main__":
    main()

"""
Qs: Can you improve time on your version?

To improve time in my CSP version, I should use MRV with Degree heuristic, apply 
Least Constraining Value for value ordering, avoid deep copying domains by using a change stack, 
and run AC3 only on affected arcs.

"""