
import re

coordinate_pairs = []


largest_x = 0
largest_y = 0

def pprint_grid(grid):
    print("---------------------------------")
    for row in grid:
        print(row)
    print("---------------------------------")

def sum_intersections(grid):
    return sum([len([x for x in y if x >= 2]) for y in grid])

with open("input.txt", "r") as file:
    for line in file:
        x1, y1, x2, y2 = tuple([int(x) for x in re.findall(r"\d+", line)])

        loc_max_x = max(x1, x2)
        if loc_max_x > largest_x:
            largest_x = loc_max_x
        loc_max_y = max(y1, y2)
        if loc_max_y > largest_y:
            largest_y = loc_max_y

        coordinate_pairs.append((x1, y1, x2, y2))

print("grid size: %d x %d" % (largest_x, largest_y))

#grid = [[0]*(largest_x+1)]*(largest_y+1)
grid = []
for y in range(largest_y+1):
    grid.append([0]*(largest_x+1))


for (x1, y1, x2, y2) in coordinate_pairs:
    #print("coordinates: (%d,%d) -> (%d,%d)" % (x1, y1, x2, y2))
    if y1 == y2: # all on the same row
        #print("same row")
        delta_x = abs(x1-x2)
        min_x = min(x1, x2)
        for x in range(min_x, min_x+delta_x+1):
            grid[y1][x] += 1
    elif x1 == x2: # all in the same coloumn
        #print("same coloumn")
        delta_y = abs(y1-y2)
        min_y = min(y1, y2)
        for y in range(min_y, min_y+delta_y+1):
            grid[y][x1] += 1
    else:
        print("diagonal: (%d,%d)->(%d,%d))" % (x1, y1, x2, y2))
        delta_x = abs(x1-x2)
        min_x = min(x1, x2)
        delta_y = abs(y1-y2)
        min_y = min(y1, y2)
        ys = list(range(min_y, min_y+delta_y+1))
        if y1 > y2:
            ys.reverse()
        xs = list(range(min_x, min_x+delta_x+1))
        if x1 > x2:
            xs.reverse()
        coords = zip(xs, ys)
        for x, y in coords:
            grid[y][x] += 1

intersections = sum_intersections(grid)
print("Intersections with 2 or more: %d" % intersections)
