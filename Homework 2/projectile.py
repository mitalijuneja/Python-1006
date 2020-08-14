import matplotlib.pyplot as plt

####
# Mitali Juneja (mj2944)
# Homework 2b Problem 1 = contains the functions for the projectile
# simulation
####

gravity = 9.81
G = 6.6742*10**-11
Me = 5.9736*10**24
Re = 6371000

def s_standard(t, v_0):
    """uses the standard formula to calculate the position"""
    
    standard_pos = -0.5 * gravity * (t ** 2) + v_0 * t
    return standard_pos

def s_sim(t, v_0, s_0, delta_t):
    """uses the simulation method to calculate the position, this is
    done the standard way without using lists and calculates the
    relevant quantities after every delta_t seconds"""
    
    t_curr = 0
    while t_curr < t:
        t_curr += delta_t
        
        # round the time to 2 decimal places to avoid rounding
        # errors (eg. 2.9995 instead of 3, etc) which mess up the 
        # while loop condition
        t_curr = round(t_curr,2)
        next_pos = s_next(s_0, v_0, delta_t)
        next_vel = v_next(v_0, grav(s_0), delta_t)
        s_0 = next_pos
        v_0 = next_vel
    return s_0

def s_sim_lst(t, delta_t, pos, vel, t_init):
    """uses the simulation method to calculate the position, this is 
    done using lists to save the previous values each time they are 
    calculated so that values are not continuously recalculated"""
   
    t_curr = t_init
    while t_curr < t:
        t_curr += delta_t
        
        # round the time to 2 decimal places to avoid rounding
        # errors (eg. 2.9995 instead of 3, etc) which mess up the 
        # while loop condition
        t_curr = round(t_curr,2)
        next_pos = s_next(pos[-1], vel[-1], delta_t)
        next_vel = v_next(vel[-1], grav(pos[-1]), delta_t)
        
        # store the previous positions and velocities in lists to
        # avoid recalculating
        pos.append(next_pos)
        vel.append(next_vel)
    return pos[-1]

def s_next(s, v, delta_t):
    """ uses the formula to calculate the next position delta_t seconds
    later"""
    
    next_pos = s + delta_t * v
    return next_pos


def v_next(v, g, delta_t):
    """ uses the formula to calculate the next velocity delta_t seconds
    later"""
    
    next_vel = v - delta_t * g
    return next_vel

def grav(s):
    """ uses the formula to calculate the value of g given the height"""
    
    g = G * Me/((Re + s) ** 2)
    return g


def plot_trajectories(v_0, s_0, delta_t):
    """ collects the times, standard positions, and simulation positions
    in lists in order to plot them"""
    
    t_curr = 0
    pos_curr = s_0
    times = [t_curr]
    sim_pos = [s_0]
    formula_pos = [s_0]
    vel = [v_0]
   
    # collect the time and position data to be plotted
    while pos_curr >= 0:
        t_curr += delta_t
        t_curr = round(t_curr, 2)
        times.append(t_curr)
        formula_pos.append(s_standard(t_curr, v_0))
        pos_curr = s_sim_lst(t_curr, delta_t, sim_pos, vel, t_curr - delta_t)
  
    # calculate the differences between the simulation and standard positions
    diffs = []
    for i in range(len(formula_pos)):
        diffs.append(sim_pos[i] - formula_pos[i])
        
    # create 2 subplots
    f, (ax1, ax2) = plt.subplots(2, 1, sharex = True)
    # plot the trajectories
    ax1.plot(times, formula_pos, c = 'r')
    ax1.plot(times, sim_pos, c = 'b')
    # plot the differences
    ax2.plot(times, diffs, c = 'g')
    # show plot
    plt.show()
    return
    
    

