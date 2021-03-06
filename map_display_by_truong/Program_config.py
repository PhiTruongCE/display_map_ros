import numpy as np
import math
from enum import Enum

'''
CONTROL SIGNALs FOR SHOWING OR HIDING PLOT EMELENTS
'''
show_animation = True
show_map = True
show_world = False

show_traversal_sight = True

show_open_sight = True
show_closed_sight = True
show_circle_range = True

show_ref_sight = True

show_sketelon_path = True
show_approximately_shortest_path = True
show_critical_line_segments = True
show_cls_orderednumber = True  # show ordered number of critical line segments

show_visited_path = True
show_visible_graph = True

show_active_openpt = True
show_next_point = True

show_robot = True
show_goal = True
show_start = True
show_text_goal = True




'''
PRINT OUT FOR DEBUG
'''
print_boundary_linesegments = True
print_closed_sights = True
print_closed_linesegments = False
print_open_sights = True
print_ref_sight = False
print_ref_csight_linesegments = False
print_csight_linesegments = False
print_traversal_sight = False

'''
LINE STYPE FOR DISPLAY PLOT
'''
ls_is = ":.c"    # intersection
ls_bp = "-r"     # boundary points
ls_ts = "-"      # true sight
cl_ts = "m"      # color true sight
cl_os = "c"
ls_bp = ":g"     # blind sight
ls_map = "-b"    # map 
ls_cs = ":m"     # close sight
ls_os = "c"      # open sight
ls_goal = "*r"   # goal
ls_start = "*b"   # goal
ls_nextpt = "1r" # next points
ls_aopt = ".b"   # active open points
ls_iopt = "ok"   # inactive open_point
ls_em = "-m"     # explored_map
ls_vg = ":k"     # visible graph
ls_vp = "-r"     # visited path
ls_goingp = "-1g" # going path
ls_cls = '--g'      # critical line segment 
ls_sp = "-r"        # shortest skeleton path
ls_asp = "-m"       # approximately shortest path
# Robots configuration
class RobotType(Enum):
    circle = 0
    rectangle = 1

class Config:
    '''
    simulation parameter class
    '''

    def __init__(self):
        # robot parameter
        self.max_speed = 100.0  # [m/s]
        self.min_speed = -100.0  # [m/s]
        self.max_yaw_rate = 40.0 * math.pi / 180.0  # [rad/s]
        self.max_accel = 0.2  # [m/ss]
        self.max_delta_yaw_rate = 40.0 * math.pi / 180.0  # [rad/ss]
        self.v_resolution = 0.01  # [m/s]
        self.yaw_rate_resolution = 0.1 * math.pi / 180.0  # [rad/s]
        self.dt = 0.1  # [s] Time tick for motion prediction
        self.predict_time = 0.1  # [s]
        self.to_goal_cost_gain = 0.15
        self.speed_cost_gain = 1.0
        self.obstacle_cost_gain = 1.0
        self.robot_stuck_flag_cons = 0.001  # constant to prevent robot stucked
        self.robot_type = RobotType.circle
        self.robot_vision = 30 # the range of input vision
        # if robot_type == RobotType.circle
        # Also used to check if goal is reached in both types
        self.robot_radius = 1.0  # [m] for collision check

        # if robot_type == RobotType.rectangle
        self.robot_width = 0.5  # [m] for collision check
        self.robot_length = 1.2  # [m] for collision check
        # obstacles [x(m) y(m), ....]
        #self.ob = np.array([[-1, -1],
        
        self.max_speed = 1.0  # [m/s]
        self.min_speed = -0.5  # [m/s]
        self.max_yaw_rate = 40.0 * math.pi / 180.0  # [rad/s]
        self.max_accel = 0.2  # [m/ss]
        self.max_delta_yaw_rate = 40.0 * math.pi / 180.0  # [rad/ss]
        self.v_resolution = 0.01  # [m/s]
        self.yaw_rate_resolution = 0.1 * math.pi / 180.0  # [rad/s]
        self.dt = 0.1  # [s] Time tick for motion prediction
        self.predict_time = 3.0  # [s]
        self.to_goal_cost_gain = 0.15
        self.speed_cost_gain = 1.0
        self.obstacle_cost_gain = 1.0
        self.robot_stuck_flag_cons = 0.001  # constant to prevent robot stucked
        self.robot_type = RobotType.circle

        # if robot_type == RobotType.circle
        # Also used to check if goal is reached in both types
        self.robot_radius = 1.0  # [m] for collision check

        # if robot_type == RobotType.rectangle
        self.robot_width = 0.5  # [m] for collision check
        self.robot_length = 1.2  # [m] for collision check
        #                    [0, 2],
        #                    [4.0, 2.0],
        #                    [5.0, 4.0],
        #                    [5.0, 5.0],
        #                    [5.0, 6.0],
        #                    [5.0, 9.0],
        #                    [8.0, 9.0],
        #                    [7.0, 9.0],
        #                    [8.0, 10.0],
        #                    [9.0, 11.0],
        #                    [12.0, 13.0],
        #                    [12.0, 12.0],
        #                    [15.0, 15.0],
        #                    [13.0, 13.0]
        #                    ])
        #
        #self.ob = np.random.randint(100, size=(1,2))
    @property
    def robot_type(self):
        return self._robot_type

    @robot_type.setter
    def robot_type(self, value):
        if not isinstance(value, RobotType):
            raise TypeError("robot_type must be an instance of RobotType")
        self._robot_type = value
