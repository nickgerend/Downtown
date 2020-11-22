import matplotlib.pyplot as plt

#region Functions

def line_slope_intercept(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b # y = mx + b

def two_lines_intercept(m1, b1, m2, b2):
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y

def two_lines_intercept2(p0_x, p0_y, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    s1_x = p1_x - p0_x     
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x
    s2_y = p3_y - p2_y
    #s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
    t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)
    i_x = p0_x + (t * s1_x)
    i_y = p0_y + (t * s1_y)
    return i_x, i_y

#endregion

#region Classes

class building:
    def __init__(self, row, column, path, x, y, tile = -1): 
        self.row = row
        self.column = column
        self.path = path
        self.x = x
        self.y = y
        self.tile = tile

class lines:
    def __init__(self, line, x1, y1, x2, y2): 
        self.line = line
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class intercept:
    def __init__(self, intercept, line1, line2): 
        self.intercept = intercept
        self.x1 = line1.x1
        self.y1 = line1.y1
        self.x2 = line1.x2
        self.y2 = line1.y2
        self.x3 = line2.x1
        self.y3 = line2.y1
        self.x4 = line2.x2
        self.y4 = line2.y2
        self.iPoint_x = 0.0
        self.iPoint_y = 0.0
    def calc_iPoint(self):
        self.iPoint_x, self.iPoint_y = two_lines_intercept2(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)

#endregion

#region Alg
width_height_ratio = 0.5
half_whr = width_height_ratio / 2

V_x = 150.0
V_y = 40.0 #20
columns = 30
floors = 130 #74
col_counter = 1
diag_point = 2

lines_list = []
building_list = []

for i in range(floors):

    lines_list.clear()

    # A1:
    lines_list.append(lines('a1', half_whr, 0.0, half_whr, 1.0))
    lines_list.append(lines('a1_', 0.0, i + 0.0, V_x, V_y))
    A1_i = intercept('A1', lines_list[0], lines_list[1])
    A1_i.calc_iPoint()
    A1_x = A1_i.iPoint_x
    A1_y = A1_i.iPoint_y

    # A2:
    lines_list.append(lines('a2', half_whr, 0.0, half_whr, 1.0))
    lines_list.append(lines('a2_', 0.0, i + 0.5, V_x, V_y))
    A2_i = intercept('A2', lines_list[2], lines_list[3])
    A2_i.calc_iPoint()
    A2_x = A2_i.iPoint_x
    A2_y = A2_i.iPoint_y

    # A3:
    lines_list.append(lines('a3', half_whr, 0.0, half_whr, 1.0))
    lines_list.append(lines('a3_', 0.0, i + 1.0, V_x, V_y))
    A3_i = intercept('A3', lines_list[4], lines_list[5])
    A3_i.calc_iPoint()
    A3_x = A3_i.iPoint_x
    A3_y = A3_i.iPoint_y

    
    building_list.append(building(i + 0.0, 0.0, -1.0, 0.0, i + 0.0)) 
    building_list.append(building(i + 0.5, 0.0, -1.0, 0.0, i + 0.5))
    building_list.append(building(i + 1.0, 0.0, -1.0, 0.0, i + 1.0))
    building_list.append(building(i + 0.0, 0.5, -1.0, A1_x, A1_y))
    building_list.append(building(i + 0.5, 0.5, -1.0, A2_x, A2_y))
    building_list.append(building(i + 1.0, 0.5, -1.0, A3_x, A3_y))

    # if i == 2:
    #     x = [o.x for o in building_list if (o.column % 1 == 0) and (o.row % 1 == 0)]
    #     y = [o.y for o in building_list if (o.column % 1 == 0) and (o.row % 1 == 0)]
    #     plt.scatter(x, y)
    #     plt.show()

    col_counter = 1

    for j in range(2 * columns - 1):
        
        lines_list.clear()

        #region Calc Points
        # A1:
        lines_list.append(lines('a1', building_list[diag_point].x, building_list[diag_point].y, building_list[diag_point + 2].x, building_list[diag_point + 2].y))
        lines_list.append(lines('a1_', 0.0, i + 0.0, V_x, V_y))
        A1_i = intercept('A1', lines_list[0], lines_list[1])
        A1_i.calc_iPoint()
        A1_x = A1_i.iPoint_x
        A1_y = A1_i.iPoint_y

        # A2:
        lines_list.append(lines('a2', A1_x, 0.0, A1_x, 1.0))
        lines_list.append(lines('a2_', 0.0, i + 0.5, V_x, V_y))
        A2_i = intercept('A2', lines_list[2], lines_list[3])
        A2_i.calc_iPoint()
        A2_x = A2_i.iPoint_x
        A2_y = A2_i.iPoint_y

        # A3:
        lines_list.append(lines('a3', A1_x, 0.0, A1_x, 1.0))
        lines_list.append(lines('a3_', 0.0, i + 1.0, V_x, V_y))
        A3_i = intercept('A3', lines_list[4], lines_list[5])
        A3_i.calc_iPoint()
        A3_x = A3_i.iPoint_x
        A3_y = A3_i.iPoint_y
        #endregion

        building_list.append(building(i + 0.0, col_counter, -1.0, A1_x, A1_y))
        building_list.append(building(i + 0.5, col_counter, -1.0, A2_x, A2_y))
        building_list.append(building(i + 1.0, col_counter, -1.0, A3_x, A3_y))

        col_counter += .5
        diag_point += 3

    diag_point += 6

    # Diagram:
    #
    #      1.0 --b----A3----B3---------   \
    #      0.5 --|---A2,b---B2---------    > (x_offset, y_offset) vanishing point
    #  ^   0.0 --|----A1----B1---------   /
    #  y             a,c
    #  x >      0.0 [*/2] [w/h]*

#endregion

#region Display points

# x = [o.x for o in building_list if (o.column % 1 == 0) and (o.row % 1 == 0)]
# y = [o.y for o in building_list if (o.column % 1 == 0) and (o.row % 1 == 0)]
# plt.scatter(x, y)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.show()

#endregion

#region Create polygons
FFR = [o for o in building_list if (o.column % 1 == 0) and (o.row % 1 == 0)] # First Floor Right
building_poly = []
index = 0
i_row = 0
for i in range(1, floors + 1):   
    for j in range(columns):
        index = j * 2 + i_row
        building_poly.append(building(i, j, 0, FFR[index].x, FFR[index].y, 'R'+str(i)+'C'+str(j+1)+'East'))
        building_poly.append(building(i, j, 1, FFR[index+2].x, FFR[index+2].y, 'R'+str(i)+'C'+str(j+1)+'East'))
        building_poly.append(building(i, j, 2, FFR[index+3].x, FFR[index+3].y, 'R'+str(i)+'C'+str(j+1)+'East'))
        building_poly.append(building(i, j, 3, FFR[index+1].x, FFR[index+1].y, 'R'+str(i)+'C'+str(j+1)+'East'))
    i_row = i * (2 * columns + 2)
index = 0
i_row = 0
for i in range(1, floors + 1):   
    for j in range(columns):
        index = j * 2 + i_row
        building_poly.append(building(i, j, 0, -FFR[index].x, FFR[index].y, 'R'+str(i)+'C'+str(j+1)+'West'))
        building_poly.append(building(i, j, 1, -FFR[index+2].x, FFR[index+2].y, 'R'+str(i)+'C'+str(j+1)+'West'))
        building_poly.append(building(i, j, 2, -FFR[index+3].x, FFR[index+3].y, 'R'+str(i)+'C'+str(j+1)+'West'))
        building_poly.append(building(i, j, 3, -FFR[index+1].x, FFR[index+1].y, 'R'+str(i)+'C'+str(j+1)+'West'))
    i_row = i * (2 * columns + 2)
#endregion

# x = [o.x for o in building_poly]
# y = [o.y for o in building_poly]
# plt.scatter(x, y)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.show()

#region Write out file
import csv
import os
with open(os.path.dirname(__file__) + '/building.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['row', 'column', 'path', 'x', 'y', 'tile'])
    for window in building_poly:
        writer.writerow([window.row, window.column, window.path, window.x, window.y, window.tile])
#endregion