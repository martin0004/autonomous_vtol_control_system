# Series of helper classes and functions specific to this project.

from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


#---------- Classes ---------- #

class DroneAttributes(object):
    """Drone attributes as a function of time, derived from log file data."""


    def __init__(self, log_file_name):

        self._log_file_dict = None
        self._load_log(log_file_name)


    @property
    def log_file_dict(self):
        return self._log_file_dict


    @property
    def airspeed(self):
        array_t = np.array(self.local_velocity.index)        
        array_airspeed_mag = np.linalg.norm(self.local_velocity, axis=1)   
        df = pd.DataFrame(array_airspeed_mag, index=array_t, columns=["mag"])
        df.index.name = "t"
        return df


    @property
    def airspeed_rate(self):

        df = self.airspeed

        # Keep only 1 row out of each 100 rows.
        # This reduces problems of divenging derivatives if dividing by a very small time step.
        df = df.iloc[::100,:]

        t0 = df.index[:-1].values # All values, excluding the last one.
        t1 = df.index[1:].values  # All values, excluding the first one.
        delta_t = t1-t0

        airspeed_t0 = df.mag.iloc[0:-1].values # All values, excluding the last one.
        airspeed_t1 = df.mag.iloc[1:].values   # All values, excluding the first one.
        delta_airspeed = airspeed_t1 - airspeed_t0

        data = np.array([delta_t, delta_airspeed]).T
        df = pd.DataFrame(data, index=t1, columns=["delta_t", "delta_airspeed"])
        df.index.name = "t"

        df = df[df.delta_t != 0] # Drop all lines where delta_t equals 0 (would cause NaN or Inf values)
        df["mag"] = df["delta_airspeed"] / df["delta_t"]
        df = df.drop(columns=["delta_t", "delta_airspeed"])

        return df


    @property
    def global_position(self):
        l = self._log_file_dict["GLOBAL_POSITION"]
        df = pd.DataFrame(l, columns=["t","lat","lon","alt"], dtype=np.float32)
        df = df.set_index("t")
        return(df)    


    @property
    def local_position(self):
        l = self._log_file_dict["LOCAL_POSITION"]
        df = pd.DataFrame(l, columns=["t","x","y","z"], dtype=np.float32)
        df = df.set_index("t")
        return(df) 


    @property
    def local_velocity(self):
        l = self._log_file_dict["LOCAL_VELOCITY"]
        df = pd.DataFrame(l, columns=["t","vx","vy","vz"], dtype=np.float32)
        df = df.set_index("t")
        return(df) 


    def _load_log(self, log_file_name):

        d = defaultdict(list)

        # Load log data into dictionnary
        # (data loaded as lists of string)

        with open(log_file_name, 'r') as f:

            line = f.readline()

            while line:

                # Remove "end of line" symbol and blank spaces.
                line = line.rstrip()
                line = line.replace(" ", "")
                # Split line into list.
                message_data = line.split(",")
                # Remove message name from list.
                message_name = message_data.pop(0)
                # Remove "MsgID" from message name.
                message_name = message_name.replace("MsgID.", "")
                # Append data to log.
                d[message_name].append(message_data)
                # Read new line in file.
                line = f.readline()

        self._log_file_dict = d     


#---------- Functions ---------- #

def get_cwd_txt_files() -> list:
    """Return list of .txt filenames in current working directory."""

    txt_files = []

    cwd = os.getcwd()
    filenames = os.listdir(cwd)

    for filename in filenames:

        filepath = os.path.join(cwd, filename)
        (prefix, extension) = os.path.splitext(filename) 

        if ( os.path.isfile(filepath) ) and ( extension == ".txt" ):

            txt_files.append(filename)

    return txt_files  


#---------- Main ---------- #

if __name__ == "__main__":
    """Function for troubleshooting class."""

    log_file_name = "T_trim_0.68.txt"
    drone_attributes = DroneAttributes(log_file_name)

    print(drone_attributes.global_position)





