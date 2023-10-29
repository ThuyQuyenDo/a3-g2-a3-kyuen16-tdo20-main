def find_path(maze, from_cell, to_cell):
    def helper(maze, current, to_cell, path, visit_ed):
        if current == to_cell:
            return path + [to_cell]
        
        visit_ed = visit_ed + [current]
        neighbors = [maze.get_left(current), maze.get_right(current), maze.get_up(current), maze.get_down(current)]
        for neighbor in neighbors:
            if neighbor != -1 and neighbor not in visit_ed:
                result = helper(maze, neighbor, to_cell, path + [current], visit_ed)
                if result is not None:
                    return result
        return None

    result = helper(maze, from_cell, to_cell, [], [])
    if result is not None:
        return result
    else:
        return []
