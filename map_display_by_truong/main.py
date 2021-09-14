import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from map_display_truong import *
from Robot_csv_lib import *
from Robot_world_lib import *
from Program_config import *
from Robot_control_panel import *

config = Config()



def main():
    menu_result = menu()
    #mapname = menu_result.n
    worldname = menu_result.w
    xstart = [30, 100, 200, 500]
    ystart = [20, 10, 300, 250]
    xgoal = menu_result.gx
    ygoal = menu_result.gy
    read_map_from_world(worldname)
    ob = read_map_csv(worldname + ".csv")
    display(worldname + ".csv", xgoal, ygoal, xstart, ystart)

if __name__ == '__main__':
    main()
