# Glider-Challenge-2019

## Description

A simple script used to aid design the stability condition and estimated flight distance of a balsa wood handcrafted glider wich was launched with a slingshot across the field.

The scripts follow a simple [stability criteria](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-01-unified-engineering-i-ii-iii-iv-fall-2005-spring-2006/systems-labs-06/spl8.pdf). For the flight distance the script use [**XFOIL**](https://web.mit.edu/drela/Public/web/xfoil/) to determine the aerodynimics coefficients, it's a free program created by *Mark Drella* 

## How to Use

If you use a Debian Linux distribuition you can download **XFOIL** with a simple:
> sudo apt-get install xfoil

If you are using a Windows as operating system you just need to keep the *.exe* file in the same folder of the script.

## Results

At the end of the calculations a couple charts will be ploted, the most relevant for stability is showed in **FIGURE 01**


![Figure](https://github.com/LukMarks/Glider-Challenge-2019/blob/master/image%20source/Figure.png)
<div style="text-align:center;"> FIGURE 01 </div>

The plot show where your current configuration is placed inside of the envelope, once your design is between this lines the vertical and horizontal stability is ensured. Next the values of the aredodynimics coefficients will be displayed:

```
Aerodynimics Coefficiets
cd:  0.01489  cl:  0.2931
Aerodynimics Coefficiets
cd:  0.01464  cl:  0.2904
Aerodynimics Coefficiets
cd:  0.01442  cl:  0.2875
```
In the end of the routine a brief review of your design will be showed with the estimated flight distance.
```
Wing Area: 0.01058  m^2
Vertical tail area: 0.000681 m^2
Horizontal tail area: 0.000456 m^2
Dihedral angle: 2.76  degree
VvB: 0.18
Estimated flight distance: 36.94 m
```

### References
* [Stability Criteria](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-01-unified-engineering-i-ii-iii-iv-fall-2005-spring-2006/systems-labs-06/spl8.pdf)
* [Aerodynimic Theory](https://arc.aiaa.org/doi/pdf/10.2514/1.C034415)
* [Airfoil Database](https://m-selig.ae.illinois.edu/ads/coord_database.html)
