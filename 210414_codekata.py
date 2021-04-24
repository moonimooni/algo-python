def dfs(i, j, grid, weight, candidates):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid):
        return
    
    weight += grid[i][j]
    
    if i+1 == len(grid) and j+1 == len(grid):
        candidates.append(weight)
        return


    dfs(i+1, j, grid, weight, candidates)
    dfs(i, j+1, grid, weight, candidates)

def min_path_sum(grid):
    candidates = []

    dfs(0, 0, grid, 0, candidates)

    return min(candidates)