#!/usr/bin/python3

"""This module contains a function that returns the perimeter of the island
described in 'grid'"""


def island_perimeter(grid):
    """This function returns the perimeter of the island described in
    'grid'"""
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell is land
            if grid[i][j] == 1:
                # Add 4 to the perimeter initially
                perimeter += 4

                # Check adjacent cells and subtract 1 for
                # each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
