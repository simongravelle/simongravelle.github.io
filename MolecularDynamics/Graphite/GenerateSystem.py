fichier = open("temp", "w")

from math import *
typat = 6; #type d atomes
# graphene properties
mC = 12.01; # mass carbon
d=1.4; # distance C-C
beta=30*pi/180; # angle between atoms
c=3.4; # interlayer distance
# box properties
xhi=10*d*cos(beta); xlo=-xhi;
yhi=3*(2*d+2*d*sin(beta)); ylo=-yhi;
zhi=c*3.05; zlo=-zhi;

# Creation systeme
fichier.write("# System \n \n")
fichier.write(str(xlo) + " " + str(xhi) + " xlo xhi \n"); 
fichier.write(str(ylo) + " " + str(yhi) + " ylo yhi \n");
fichier.write(str(zlo) + " " + str(zhi) + " zlo zhi \n");
fichier.write("\n");
fichier.write("Masses \n \n")
fichier.write("1 " + str(mC) + "\n");
fichier.write("2 " + str(mC) + "\n");
fichier.write("3 " + str(mC) + "\n");
fichier.write("4 " + str(mC) + "\n");
fichier.write("5 " + str(mC) + "\n");
fichier.write("6 " + str(mC) + "\n");
fichier.write("\n");
fichier.write("Atoms \n \n")
# generate seven layers of graphene
typ=1;
x=xlo;
y=ylo;
z=zlo+c/2;
cptat=0; #counter atome
while z<zhi-c/2:
	while y < yhi:
		while x < xhi:
			cptat += 1;
			fichier.write(str(cptat) + " " + str(typ) + " " + str(x+d*cos(beta)*(-1)**typ/2) + " " + str(y) + " " + str(z) + "\n");
			cptat += 1;
			fichier.write(str(cptat) + " " + str(typ) + " " + str(x+d*cos(beta)*(-1)**typ/2) + " " + str(y+d)  + " " + str(z) + "\n");
			cptat += 1;
			fichier.write(str(cptat) + " " + str(typ) + " " + str(x+d*cos(beta)+d*cos(beta)*(-1)**typ/2) + " " + str(y+d*sin(beta)+d) + " " + str(z) + "\n");
			cptat += 1;
			fichier.write(str(cptat) + " " + str(typ) + " " + str(x+d*cos(beta)+d*cos(beta)*(-1)**typ/2) + " " + str(y-d*sin(beta)) + " " + str(z) + "\n");
			x=x+2*d*cos(beta);
		x=xlo;
		y=y+2*d*sin(beta)+2*d;
	z=z+c;
	y=ylo;
	typ=typ+1;
fichier.write("\n");
fichier.close()
source = open("temp", "r")
txt = source.read()
source.close()
import os
os.remove("temp")
fichier = open("data.lammps", "w")
fichier.write("#  System"+ "\n"+ "\n")
fichier.write(str(cptat) + " " + "atoms"+ "\n");
fichier.write("\n");
fichier.write(str(typat) + " " + "atom types"+ "\n");
fichier.write("\n"); 
fichier.write(str(txt));
fichier.close()
