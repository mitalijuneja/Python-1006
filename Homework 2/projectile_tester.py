# *********************************************
# Mitali Juneja (mj2944)
# projectile_tester
# this prgram tests the functions in the
# projectile module
# *********************************************

import projectile


def main():

    # set up intitial values
    v_0 = 300
    s_0 = 0
    t = 0
    delta_t = .05
    pos = [s_0]
    vel = [v_0]
    
    
    s = s_0 #start s off at s_0

    # print a table with values computed both ways for positive positions

    print('seconds \t distance_sim \t \t distance_formula')
    print('-----------------------------------------------------------')
    while s >= 0:
        s_formula = projectile.s_standard(t, v_0)
        print(f'{t} \t \t {s} \t \t {s_formula}')
        t = t + 1
        # modification using lists
        s = projectile.s_sim_lst(t,delta_t, pos, vel, t - 1)   
        # original s_sim method
        #s = projectile.s_sim(t, v_0, s_0, delta_t)
    projectile.plot_trajectories(v_0, s_0, delta_t)

# now run main()
main()