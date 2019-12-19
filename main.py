#library setup
#------------------------------
import stability as st
import fly as fl
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
#------------------------------

plot = 1 # flag for plot

# Define the aircraft geometry
#------------------------------
root_chord = 62e-3 #[m]
tip_chord = 30e-3 #[m]
wing_span = 460e-3 #[m]
Lv = 250e-3 #[m] Vertical tail moment arm
Lh = 240e-3 #[m] horizontal tail moment arm
airfoil ='S4094.dat' # airfoil name with the extension(.dat / .out)
alpha = 0 #[degree] angle of attack
#------------------------------

# Criteria Constants
#------------------------------
'''
B > 5 , spirally stable
B = 5 , spirally neutral
B < 5 , spirally unstable

Vv = 0.02 ... 0.05

Vh = 0.30 ... 0.60

VB = 0.10 ... 0.2
'''
B = 5
Vv = 0.035
Vh = 0.45

#------------------------------

#Flight sumulation setting
#------------------------------
v_start = 10 #[m/s]
v_final = 30 #[m/s]
Thrust = 10 #[N]
step_fly = 1 #[m/s]
#------------------------------
aircraft = [root_chord,
            tip_chord,
            wing_span]


airplane = st.stab(aircraft)
S = airplane.wing_area() # [m^2]
c = airplane.average_chord() # [m]
MAC = airplane.mean_aerodynamic_chord() #[m]
gamma = airplane.dihedral_angle(B,Lv) # [degree]
VB = airplane.roll_control(B,Vv)
Sv = airplane.vertical_tail_area(Vv,Lv)
Sh = airplane.horizontal_tail_area(Vh,Lh)

#Show the realtion Sv/lv
#------------------------------------------
V_coef = [0.02 ,0.035 ,0.05]
airplane.vertical_volume(V_coef,50e-3,Lv*1.15)
#------------------------------------------

#Show the realtion Sh/lh
#------------------------------------------
H_coef = [0.30 ,0.45 ,0.60 ]
airplane.horizontal_volume(H_coef,50e-3,Lh*1.15)
#------------------------------------------

#Flight Analisys
#------------------------------------------
V = 10
takeoff_angle = 45 #[degree]
a_takeoff = 500 #[m/s^2] initial acceletation
fly = fl.flight()
L,D,Cl,Cd = fly.flight_forces(V,airfoil,4,S,MAC) #L = lift and D = Drag
m = 0.02
fly.performance(v_start,v_final,Thrust,step_fly,airfoil,alpha,S,MAC)
#------------------------------------------
plt.figure(101)
plt.plot((Lh,Lh),(Sh,Sh),label = "Current Confinguration",marker = ".", markersize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.figure(100)
plt.plot((Lv,Lv),(Sv,Sv),label = "Current Confinguration",marker = ".", markersize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

distance = quad(fly.distance,V,0, args = ( m, D))


#output
print('\nWing Area:',S,' m^2')
print('Vertical tail area:', round(Sv,6), 'm^2')
print('Horizontal tail area:', round(Sh,6), 'm^2')
print('Dihedral angle:',round(gamma,2), ' degree')
print('VvB:',round(VB,2))
print('Estimated flight distance:', round(distance[0],2),'m')


#------------------------------------------
if plot:
    plt.show()
