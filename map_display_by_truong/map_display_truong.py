import matplotlib.pyplot as plt
import sys
import getopt
from Robot_csv_lib import *
from Robot_map_lib import *

def display(mapname,gx,gy,sx,sy):
    ob = read_map_csv(mapname)

    # draw map obstacles 
    map_display(plt, mapname, ob,gx,gy,sx,sy)

    plt.axis("equal")
    plt.grid(True)
    plt.show()

