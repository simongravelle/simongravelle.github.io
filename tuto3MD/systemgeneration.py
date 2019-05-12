from math import *
typat=9; # 9 types of atom in total
typbo=1; # 1 type of bond (O-H)
typan=1; # 1 type of angle (H-O-H)
mH=1.00794; # hydrogen mass in grams per mole
mO=15.9994; # oxygen mass in grams per mole
mC = 12.01; # carbon mass in grams per mole
alpha=104.5*pi/180; # O-H-O angle (TIP4P/2005) in radian
r=0.9584; # O-H bond distance (TIP4P/2005) in angstrom
qO=-1.1128; # oxygen charge (TIP4P/2005) in multiple of electron charge
qH=0.5564; # hydrogen charge (TIP4P/2005) in multiple of electron charge
qC=0; # carbon charge in multiple of electron charge
dOO=3.1589; # typical O-O distance in angstrom
dCC=1.4; # distance C-C airebo
beta=30*pi/180; # graphene angle
cptAtom=0; # for atom counting
cptCar=0; # for carbon counting
cptBond=0; # for bond counting
cptAngle=0; # for angle counting
cptMolecule=0; # for molecule counting
pos_wall=60; # for piston location
dX=6;
c=6.696/2; # distance graphene-graphene
txlo=-10*dCC*cos(beta);
txhi=10*dCC*cos(beta);
tylo=-3*(2*dCC*sin(beta)+2*dCC);
tyhi=3*(2*dCC*sin(beta)+2*dCC);
tzlo=-c/2-c-10;
tzhi=int(pos_wall)+20;
sigma=3.374; #A
unit=2*sigma/sqrt(2); # for the piston dimension


fichier = open("temp", "w")

# Creation systeme
fichier.write("# System \n \n")
fichier.write(str(txlo) + " " + str(txhi) + " xlo xhi \n"); 
fichier.write(str(tylo) + " " + str(tyhi) + " ylo yhi \n");
fichier.write(str(tzlo) + " " + str(tzhi) + " zlo zhi \n");
fichier.write("\n");
fichier.write("Masses \n \n")
fichier.write("1 " + str(mC) + "\n");
fichier.write("2 " + str(mC) + "\n"); 
fichier.write("3 " + str(mC) + "\n"); 
fichier.write("4 " + str(mC) + "\n"); 
fichier.write("5 " + str(mC) + "\n"); 
fichier.write("6 " + str(mC) + "\n"); 
fichier.write("7 " + str(mC) + "\n"); 
fichier.write("8 " + str(mO) + "\n");
fichier.write("9 " + str(mH) + "\n");
fichier.write("\n");

fichier.write("Atoms \n \n")
# creation graphite membrane 
graphene_locations=[c/2+c, c/2, -c/2, -c/2-c]; 
idxC=0;
for z in graphene_locations: 
	x=txlo;
	y=tylo;
	idxC=idxC+1;
	while y < tyhi:
		while x < txhi:
			if y<tyhi and y>=tylo:
			       	x0=x;
				y0=y;
				z0=z;
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + str(idxC) + " " + str(qC) + " " + str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			if y<tyhi and y>=tylo:
			       	x0=x;
				y0=y+dCC;
				z0=z;
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + str(idxC) + " " + str(qC) + " " + str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			if y<tyhi and y>=tylo:
			       	x0=x+dCC*cos(beta);
				y0=y+dCC+dCC*sin(beta);
				z0=z;
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + str(idxC) + " " + str(qC)+ " " + str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			if y<tyhi and y>=tylo:
			       	x0=x+dCC*cos(beta);
				y0=y+2*dCC+dCC*sin(beta);
				z0=z;
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + str(idxC) + " " + str(qC) + " " + str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			x=x+2*dCC*cos(beta);
		x=txlo;
		y=y+2*dCC*sin(beta)+2*dCC;

# creation piston 
x=txlo+unit/4;
y=tylo+unit/4;
z=pos_wall+dX;
p=sqrt(2)*unit/2*0.7071067811865476;
nwall=0;
while y < tyhi:
	while x < txhi:
		while z <= pos_wall+unit*1.1+dX:
			x0=x;
			y0=y;
			z0=z+unit/2;
			if x0<txhi and x0>=txlo and y0<tyhi and y0>=tylo:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + "7 " + " 0 "+ str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			x0=x;
			y0=y+unit/2;
			z0=z;
			if x0<txhi and x0>=txlo and y0<tyhi and y0>=tylo:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + "7 " + " 0 "+ str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			x0=x+unit/2;
			y0=y;
			z0=z;
			if x0<txhi and x0>=txlo and y0<tyhi and y0>=tylo:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + "7 " + " 0 "+ str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			x0=x+unit/2;
			y0=y+p;
			z0=z+p;
			if x0<txhi and x0>=txlo and y0<tyhi and y0>=tylo:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar) + " 0 " + "7 " + " 0 "+ str(x0) + " " + str(y0) + " " + str(z0) + " " + "\n");
			z=z+unit;
		x=x+unit;
		z=pos_wall+dX;
	x=txlo+unit/4;
	y=y+unit;

# creation water reservoir
x=txlo+dOO/2;
y=tylo+dOO/2;
z=c/2+c+e;
while x <= txhi-dOO/2:
	while y <= tyhi-dOO/2:
		while z <= pos_wall-e/2:
			cptMolecule+=1;
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 8 "+str(qO)+" "+str(x)+" "+str(y)+" "+str(z) + "\n");
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 9 "+str(qH)+" "+str(r+x)+" "+str(y)+" "+str(z) + "\n");
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 9 "+str(qH)+" "+str(r*sin(alpha)+x)+ " "+str(r*sin(alpha)+y)+" "+ str(z)+"\n");
			z=z+dOO;
		y=y+dOO;
		z=c/2+c+e;
	x=x+dOO;
	y=tylo+dOO/2;
fichier.write("\n"); 
fichier.write("Bonds \n \n")
while cptBond < 2*(cptAtom-cptCar)/3:
	fichier.write(str(cptBond+1)+" 1 "+str(cptCar+cptBond/2*3+1)+" "+str(cptCar+cptBond/2*3+2)+"\n");
	fichier.write(str(cptBond+2)+" 1 "+str(cptCar+cptBond/2*3+1)+" "+str(cptCar+cptBond/2*3+3)+"\n");
	cptBond+=2;
fichier.write("\n");
fichier.write("Angles \n \n")
while cptAngle < (cptAtom-cptCar)/3:
	fichier.write(str(cptAngle+1)+" 1 "+str(cptCar+cptAngle*3+2)+" "+str(cptCar+cptAngle*3+1)+" "+str(cptCar+cptAngle*3+3)+"\n");
	cptAngle+=1;

fichier.close() 

# writing of data file	
source = open("temp", "r")
txt = source.read()
source.close()
import os
os.remove("temp")
fichier = open("data.lammps", "w")
fichier.write("# Data file LAMMPS"+ "\n"+ "\n")
fichier.write(str(cptAtom)+" "+"atoms"+"\n");
fichier.write(str(cptBond)+" "+"bonds"+"\n");
fichier.write(str(cptAngle)+" "+"angles"+"\n");
fichier.write("\n");
fichier.write(str(typat)+" "+"atom types"+"\n");
fichier.write(str(typbo)+" "+"bond types"+"\n");
fichier.write(str(typan)+" "+"angle types"+"\n");
fichier.write("\n");
fichier.write(str(txt));
fichier.close() 




