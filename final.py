import math
import time as TIME
from matplotlib import lines, pyplot as plt
import numpy as np


T_INTERVAL = 1

#Taking input from a text file

def read_file(input_file):

    with open(input_file) as f:
        [r_0, del_rudder, t, upto_rudder, psi_0, initial_rudder, k_coeff, t_coeff,
            x_0, y_0, velocity] = [float(val) for val in f.readline().split(',')]

        t = int(t)

    return r_0, del_rudder, t, upto_rudder, psi_0, initial_rudder, k_coeff, t_coeff, x_0, y_0, velocity

#Plotting Function

def plot_figure(x, y):
    plt.scatter(x, y, color = "red")
    plt.autoscale(enable=True, axis='both', tight=True)
    plt.xlabel('x component of Ship Trajectory (meter)')
    plt.ylabel('y component of Ship Trajectory (meter)')
    plt.title('Ship Trajectory')
    plt.pause(1)

#Assigning the image out of "plot_figure" function so that computation power is minimized

im = plt.imread("rampal1.png")
plt.imshow(im, extent=[0, 870, 0, 1350], aspect='auto')

#Function that solves "Nomoto model" using Runge-Kutta 2nd Order Method

def ship_trajectory(r_initial, rudder_change, time, rudder_angle, psi_initial, initial_rudder_angle, k_index, T_index, x_0, y_0, velocity):
    interval = 1

    rudder_temp = initial_rudder_angle

    for _ in range(time):
        if rudder_temp < rudder_angle:
            rudder_temp += rudder_change * interval

            k1 = (k_index/T_index*rudder_temp-r_initial/T_index)*interval

            k2 = (k_index/T_index*rudder_temp -
                  ((1/T_index)*(r_initial+k1)))*interval

        elif rudder_temp > rudder_angle:
            rudder_temp -= (rudder_change*interval)

            k1 = (k_index/T_index*rudder_temp-r_initial/T_index)*interval

            k2 = (k_index/T_index*rudder_temp -
                  ((1/T_index)*(r_initial+k1)))*interval

        else:
            rudder_temp = rudder_angle

            k1 = (k_index/T_index*rudder_temp-r_initial/T_index)*interval

            k2 = (k_index/T_index*rudder_temp -
                  ((1/T_index)*(r_initial+k1)))*interval

        r_initial += (0.5*k1+0.5*k2)

        current_rate = r_initial

        psi_initial += interval * current_rate

        current_psi = psi_initial

        x_0 += velocity*math.cos(current_psi*math.pi/180)*T_INTERVAL
        y_0 += velocity*math.sin(current_psi*math.pi/180)*T_INTERVAL

        plot_figure(x_0, y_0)


if __name__ == "__main__":
    r_0, del_rudder, t, upto_rudder, psi_0, initial_rudder, k_coeff, t_coeff, x_0, y_0, velocity = read_file(
        'input/input1.txt')

    ship_trajectory(r_0, del_rudder, t, upto_rudder, psi_0,
                    initial_rudder, k_coeff, t_coeff, x_0, y_0, velocity)

    plt.show()