from collections import defaultdict
import helpers
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_scenario_01():

    pass

    # # Figure 1 - T_trim coarse values

    # fig = plt.figure().suptitle("Scenario 01 - Trim \n (T_trim Coarse Values)")

    # ax1 = plt.subplot(1,2,1, title="Vertical Speed vs Time", xlabel="Time [s]", ylabel="Vertical Speed [m/s]")
    # ax2 = plt.subplot(1,2,2, title="Airspeed Rate vs Time", xlabel="Time [s]", ylabel="Airspeed Rate [m/s^2]", xlim = (10,200), ylim = (-20,20))

    # log_file_names = ["T_trim_0.50.txt", "T_trim_0.60.txt", "T_trim_0.70.txt", "T_trim_0.80.txt", "T_trim_0.90.txt"]

    # for f in log_file_names:

    #    params = f.rstrip(".txt")
    #    helpers.DroneAttributes(f).local_velocity.vz.plot(ax = ax1, label=params)
    #    helpers.DroneAttributes(f).airspeed_rate.mag.plot(ax = ax2, label=params)
    
    # for ax in [ax1, ax2]:
    #     ax.axhline(y=0, c="k"); ax.set_xlabel("Time [s]"); ax.legend()

    # # Figure 2 - T_trim fine values

    # fig = plt.figure().suptitle("Scenario 01 - Trim \n (T_trim Fine Values)")

    # ax1 = plt.subplot(1,2,1, title="Vertical Speed vs Time", ylabel="Vertical Speed [m/s]")
    # ax2 = plt.subplot(1,2,2, title="Airspeed Rate vs Time", ylabel="Airspeed Rate [m/s^2]", xlim=(10,200), ylim=(-20,20))

    # log_file_names = ["T_trim_0.60.txt", "T_trim_0.62.txt", "T_trim_0.64.txt", "T_trim_0.66.txt", "T_trim_0.68.txt", "T_trim_0.70.txt"]

    # for f in log_file_names:

    #    params = f.rstrip(".txt")
    #    helpers.DroneAttributes(f).local_velocity.vz.plot(ax = ax1, label=params)
    #    helpers.DroneAttributes(f).airspeed_rate.mag.plot(ax = ax2, label=params)
    
    # for ax in [ax1, ax2]:
    #     ax.axhline(y=0, c="k"); ax.set_xlabel("Time [s]"); ax.legend()

    # # Show all figures

    # plt.show()


def plot_scenario_02():

    # Figure 1 - Pitch Hold Controller - k_p_theta and k_d_theta

    fig = plt.figure().suptitle("Scenario 02 - Altitude Hold \n Pitch Hold Controller")

    ax1 = plt.subplot(1,2,1, title="Altitude vs Time", xlabel="Time [s]", ylabel="Altitude [m]")
    ax2 = plt.subplot(1,2,2, title="Altitude vs Time", xlabel="Time [s]", ylabel="Altitude [m]")

    # Left ax

    log_file_names = []
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_000.00_k_d_theta_000.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_001.00_k_d_theta_000.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_002.00_k_d_theta_000.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_003.00_k_d_theta_000.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_004.00_k_d_theta_000.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_005.00_k_d_theta_000.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_010.00_k_d_theta_000.00.txt")

    for f in log_file_names:

       params = f.replace("./scenario_02_-_altitude_hold/","").replace(".txt","")
       helpers.DroneAttributes(f).global_position.alt.plot(ax = ax1, label=params)


    # Right ax

    log_file_names = []
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_004.00_k_d_theta_-05.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_004.00_k_d_theta_-02.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_004.00_k_d_theta_-01.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_004.00_k_d_theta_000.00.txt")
    log_file_names.append("./scenario_02_-_altitude_hold/k_p_theta_004.00_k_d_theta_001.00.txt")

    for f in log_file_names:

       params = f.replace("./scenario_02_-_altitude_hold/","").replace(".txt","")
       helpers.DroneAttributes(f).global_position.alt.plot(ax = ax2, label=params)

    # Draw legends, target values and x-labels on axes
    for ax in [ax1, ax2]:
        ax.axhline(y=450, c="g", label="Target altitude")
        ax.set_xlabel("Time [s]")
        ax.legend()


    # Figure 2 - Altitude Hold (With Pitch) Hold Controller - k_p_z and k_i_z

    fig = plt.figure().suptitle("Scenario 02 - Altitude Hold \n Altitude Hold (With Pitch) Controller")

    ax = plt.subplot(1,1,1, title="Altitude vs Time", xlabel="Time [s]", ylabel="Altitude [m]")

    # Left ax

    log_file_names_set_1 = []
    #log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_000.00_k_i_z_000.00.txt")
    #log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_000.10_k_i_z_000.00.txt")
    #log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_000.50_k_i_z_000.00.txt")
    #log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_001.00_k_i_z_000.00.txt")
    #log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_002.00_k_i_z_000.00.txt")
    #log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_003.00_k_i_z_000.00.txt")
    #log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_004.00_k_i_z_000.00.txt")
    log_file_names_set_1.append("./scenario_02_-_altitude_hold/k_p_z_005.00_k_i_z_000.00.txt")

    for f in log_file_names_set_1:

       params = f.replace("./scenario_02_-_altitude_hold/","").replace(".txt","")
       helpers.DroneAttributes(f).global_position.alt.plot(ax = ax, label=params)

    log_file_names_set_2 = []
    #log_file_names_set_2.append("./scenario_02_-_altitude_hold/k_p_z_005.00_k_i_z_000.01.txt") 
    #log_file_names_set_2.append("./scenario_02_-_altitude_hold/k_p_z_005.00_k_i_z_000.10.txt") 
    log_file_names_set_2.append("./scenario_02_-_altitude_hold/k_p_z_005.00_k_i_z_001.00.txt")  
    log_file_names_set_2.append("./scenario_02_-_altitude_hold/k_p_z_005.00_k_i_z_001.00_a.txt") 
    log_file_names_set_2.append("./scenario_02_-_altitude_hold/k_p_z_005.00_k_i_z_001.00_b.txt") 
    #log_file_names_set_2.append("./scenario_02_-_altitude_hold/k_p_z_005.00_k_i_z_010.00.txt")  

    for f in log_file_names_set_2:

       params = f.replace("./scenario_02_-_altitude_hold/","").replace(".txt","")
       helpers.DroneAttributes(f).global_position.alt.plot(ax = ax, label=params, linestyle="--")

    # Draw legends, target values and x-labels on axes
    ax.axhline(y=450, c="g", label="Target altitude")
    ax.set_xlabel("Time [s]")
    ax.legend()


    # Show all figures
    plt.show()   


if __name__ == "__main__":

    plot_scenario_02()

