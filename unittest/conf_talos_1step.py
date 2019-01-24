from crocoddyl import getTalosPathFromRos
import pinocchio
import pickle
import os
#---------------------------------------------------------
MODEL_PATH = getTalosPathFromRos()
MESH_DIR = MODEL_PATH+'/../'
URDF_FILENAME = "talos_reduced.urdf"
URDF_MODEL_PATH = MODEL_PATH + "/robots/" + URDF_FILENAME
robot = pinocchio.robot_wrapper.RobotWrapper.BuildFromURDF(URDF_MODEL_PATH, [MESH_DIR],
                                                           pinocchio.JointModelFreeFlyer())
#---------------------------------------------------------

DISPLAY = True

#-------------------------INITIAL TRAJECTORY----------
TRAJ_DIR = os.getcwd()+"/traj_1step/"

X_init = pickle.load( open(TRAJ_DIR+"X_init.out","rb")) #loads the state x
U_init = pickle.load( open(TRAJ_DIR+"U_init.out","rb")) # loads the control u

#loads the forces ("lambda") in the local frame in order LF, RF
#where lf: 'leg_left_6_joint', 'rf' : 'leg_right_6_joint'
f_init = pickle.load( open(TRAJ_DIR+"f_init.out","rb")) 
ddq_init = pickle.load( open(TRAJ_DIR+"ddq_init.out","rb")) #loads the acceleration
