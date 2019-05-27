fichier = open("temp", "w")

from math import *
import os

typat=2;	#type d atomes
typbo=1;	#type de bond
typan=1;	#type d angle


massH=1.008;
massO=16.00;
typeO=1;
typeH=2;
chargeO=-1.1128 ;
chargeH=0.5564;
eOO=3.4; 		# O-O typical distance
r = 0.9572; 		#distance O-H
alpha=104.52*pi/180; 	#H-O-H angle radian

# Boite
xlo=-9*eOO;
xhi=9*eOO;
ylo=-9*eOO;
yhi=9*eOO;
zlo=-30;
zhi=30;

# system creation
fichier.write("# system \n \n")

# box dimension
fichier.write(str(xlo) + " " + str(xhi) + " xlo xhi \n"); 
fichier.write(str(ylo) + " " + str(yhi) + " ylo yhi \n");
fichier.write(str(zlo) + " " + str(zhi) + " zlo zhi \n");
fichier.write("\n");

# Masses
fichier.write("Masses \n \n")
fichier.write("1 " + str(massO) + "\n");
fichier.write("2 " + str(massH) + "\n");
fichier.write("\n");

# Atoms
fichier.write("Atoms \n \n")
x=xlo+eOO/2;
y=ylo+eOO/2;
z=-8;
nbat=0; #nomber of atome
nmol=0; # number of molecule
while z<8:
	while y<yhi:
		while x<xhi:
			nbat += 1; nmol +=1;
			fichier.write(str(nbat)+" "+str(nmol)+" "+str(typeO)+" "+str(chargeO)+" "+str(x)+" "+str(y)+" "+str(z) + "\n"); 
			nbat += 1;
			fichier.write(str(nbat)+" "+str(nmol)+" "+str(typeH)+" "+str(chargeH)+" "+str(x+r)+" "+str(y)+" "+str(z) + "\n"); 
			nbat += 1;
			fichier.write(str(nbat)+" "+str(nmol)+" "+str(typeH)+" "+str(chargeH)+" "+str(x+r*cos(alpha))+" "+str(y+r*sin(alpha))+" "+str(z) + "\n"); 
			x=x+eOO;
		y=y+eOO;
		x=xlo+eOO/2;
	z=z+eOO;
	y=ylo+eOO/2;
fichier.write("\n");

# Bonds
fichier.write("Bonds \n \n")
cptBond=0; # number of bond (/2)
while cptBond <= nbat/3-1:
	fichier.write(str(cptBond*2+1)+" 1 "+str(cptBond*3+1)+" "+str(cptBond*3+2)+"\n");
	fichier.write(str(cptBond*2+2)+" 1 "+str(cptBond*3+1)+" "+str(cptBond*3+3)+"\n"); 
	cptBond +=1;
fichier.write("\n");

# Angles
fichier.write("Angles \n \n")
cptAngle=0; #nombre d angle
while cptAngle <= nbat/3-1 :
	fichier.write(str(cptAngle+1) + " 1 " + str(3*cptAngle+2) + " " + str(3*cptAngle+1) + " " + str(3*cptAngle+3) + "\n");
	cptAngle +=1;
fichier.write("\n");
fichier.close()
# writing the data file

source = open("temp", "r")
txt = source.read()
source.close()
os.remove("temp")
fichier = open("data.lammps", "w")
# Introduction
fichier.write("#  Data file"+ "\n"+ "\n")
fichier.write(str(nbat) + " " + "atoms"+ "\n");
fichier.write(str(cptBond*2) + " " + "bonds"+ "\n");
fichier.write(str(cptAngle) + " " + "angles"+ "\n");
fichier.write("\n");
fichier.write(str(typat) + " " + "atom types"+ "\n");
fichier.write(str(typbo) + " " + "bond types"+ "\n");
fichier.write(str(typan) + " " + "angle types"+ "\n");
fichier.write("\n"); 
fichier.write(str(txt));
fichier.close()
