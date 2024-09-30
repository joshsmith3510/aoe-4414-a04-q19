# ecef_to_eci.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Josh Smith
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137
w=7.292115*(10**(-5))

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year=float('nan')
month=float('nan')
day=float('nan')
hour=float('nan')
minute=float('nan')
second=float('nan')
ecef_x_km=float('nan')
ecef_y_km=float('nan')
ecef_z_km=float('nan')

# parse script arguments
if len(sys.argv)==10:
   year = float(sys.argv[1])
   month = float(sys.argv[2])
   day = float(sys.argv[3])
   hour = float(sys.argv[4])
   minute = float(sys.argv[5])
   second = float(sys.argv[6])
   ecef_x_km = float(sys.argv[7])
   ecef_y_km = float(sys.argv[8])
   ecef_z_km = float(sys.argv[9])
   ...
else:
   print(\
      'Usage: '\
        'python3 year month day hour minute second ecef_x_km ecef_y_km ecef_z_km ...'\
        )
   exit()

# write script below this line
JD=math.floor(day-32075+1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4)
JDmid=JD-0.5
Dfrac=(second+60*(minute+60*hour))/86400
JDfrac=JDmid+Dfrac
T_UT1=(JDfrac-2451545.0)/36525
theta_gmst_sec=67310.54841+(876600*60*60+8640184.812866)*T_UT1+0.093104*(T_UT1**2)+(-6.2*10**(-6))*T_UT1**3
#theta_gmst_rad=theta_gmst_sec*(2*math.pi/86400)
theta_gmst_rad=math.fmod((theta_gmst_sec%86400)*w,2*math.pi)

c=math.cos(-theta_gmst_rad)
s=math.sin(-theta_gmst_rad)

R=[[c,s,0],[-s,c,0],[0,0,1]]
eci=[ecef_x_km*c+ecef_y_km*s+0,ecef_x_km*-s+ecef_y_km*c+0,0+0+ecef_z_km]
eci_x_km,eci_y_km,eci_z_km=eci


print(eci_x_km)
print(eci_y_km)
print(eci_z_km)