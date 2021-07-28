from collections import defaultdict
import helpers
import matplotlib.pyplot as plt
import numpy as np
import os


if __name__ == "__main__":

    # Figure 1 - T_trim coarse values

    fig = plt.figure().suptitle("Scenario 01 - Trim \n (T_trim Coarse Values)")

    ax1 = plt.subplot(1,2,1, title="Vertical Speed vs Time", xlabel="Time [s]", ylabel="Vertical Speed [m/s]")
    ax2 = plt.subplot(1,2,2, title="Airspeed Rate vs Time", xlabel="Time [s]", ylabel="Airspeed Rate [m/s^2]", xlim = (10,200), ylim = (-20,20))

    log_file_names = ["T_trim_0.50.txt", "T_trim_0.60.txt", "T_trim_0.70.txt", "T_trim_0.80.txt", "T_trim_0.90.txt"]

    for f in log_file_names:

       params = f.rstrip(".txt")
       helpers.DroneAttributes(f).local_velocity.vz.plot(ax = ax1, label=params)
       helpers.DroneAttributes(f).airspeed_rate.mag.plot(ax = ax2, label=params)
    
    for ax in [ax1, ax2]:
        ax.axhline(y=0, c="k"); ax.set_xlabel("Time [s]"); ax.legend()

    # Figure 2 - T_trim fine values

    fig = plt.figure().suptitle("Scenario 01 - Trim \n (T_trim Fine Values)")

    ax1 = plt.subplot(1,2,1, title="Vertical Speed vs Time", ylabel="Vertical Speed [m/s]")
    ax2 = plt.subplot(1,2,2, title="Airspeed Rate vs Time", ylabel="Airspeed Rate [m/s^2]", xlim=(10,200), ylim=(-20,20))

    log_file_names = ["T_trim_0.60.txt", "T_trim_0.62.txt", "T_trim_0.64.txt", "T_trim_0.66.txt", "T_trim_0.68.txt", "T_trim_0.70.txt"]

    for f in log_file_names:

       params = f.rstrip(".txt")
       helpers.DroneAttributes(f).local_velocity.vz.plot(ax = ax1, label=params)
       helpers.DroneAttributes(f).airspeed_rate.mag.plot(ax = ax2, label=params)
    
    for ax in [ax1, ax2]:
        ax.axhline(y=0, c="k"); ax.set_xlabel("Time [s]"); ax.legend()

    # Show all figures

    plt.show()



