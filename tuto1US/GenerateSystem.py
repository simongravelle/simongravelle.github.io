from math import *
typat=3; # 3 types of atom in total (hydrogen, oxygen and carbon)
typbo=1; # 1 type of bond (O-H)
typan=1; # 1 type of angle (H-O-H)
mH=1.00794; # hydrogen mass in grams per mole
mO=15.9994; # oxygen mass in grams per mole
mC = 12.01; # carbon mass in grams per mole
alpha=104.5*pi/180; # O-H-O angle (TIP4P/2005) in radian
r=0.9584; # O-H bond distance (TIP4P/2005) in angstrom
qO=-1.1128; # oxygen charge (TIP4P/2005) in multiple of electron charge
qH=0.5564; # hydrogen charge (TIP4P/2005) in multiple of electron charge
dOO=3.1589; # typical O-O distance in angstrom
dCC=1.418; # distance C-C
beta=30*pi/180; # graphene angle
Rtube=9*(2*dCC*cos(beta))/(2*pi); # radius nanotube
print(Rtube)
Ltube=8*(2*(dCC*sin(beta)+dCC)); # length nanotube
Rres=dOO*10; # size reservoir along z

txlo=-12*(dCC*cos(beta)); txhi=-txlo;
tylo=-6*(dCC*sin(beta)+dCC); tyhi=-tylo;
tzlo=-10-Rres-Ltube/2; tzhi=-tzlo;

cptAtom=0; # for atom counting
cptCar=0; # for carbon counting
cptBond=0; # for bond counting
cptAngle=0; # for angle counting
cptMolecule=0; # for molecule counting

fichier = open("temp", "w")
fichier.write(str(txlo) + " " + str(txhi) + " xlo xhi \n");
fichier.write(str(tylo) + " " + str(tyhi) + " ylo yhi \n");
fichier.write(str(tzlo) + " " + str(tzhi) + " zlo zhi \n");
fichier.write("\n");
fichier.write("Masses \n \n")
fichier.write("1 " + str(mH) + "\n");
fichier.write("2 " + str(mO) + "\n");
fichier.write("3 " + str(mC) + "\n");
fichier.write("\n");

fichier.write("Atoms \n \n")

# creation carbon membrane

membrane_locations=[-Ltube/2-Rres,-Ltube/2, Ltube/2,Ltube/2+Rres]; 
for z in membrane_locations:
	x=txlo;
	y=tylo;
	while y < tyhi:
		while x < txhi:
			if x < txhi and y < tyhi:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar)+" 0 "+"3"+" 0 "+str(x)+" "+str(y)+" "+str(z)+" "+"\n");
			if x < txhi and y+dCC < tyhi:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar)+" 0 "+"3"+" 0 "+str(x)+" "+str(y+dCC)+" "+str(z)+" "+"\n");
			if x+dCC*cos(beta) < txhi and y+dCC*sin(beta)+dCC < tyhi:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar)+" 0 "+"3"+" 0 "+str(x+dCC*cos(beta))+" "+str(y+dCC*sin(beta)+dCC)+" "+str(z)+" "+"\n");
			if x+dCC*cos(beta) < txhi and y+dCC*sin(beta)+2*dCC<tyhi:
				cptAtom += 1; cptCar += 1;
				fichier.write(str(cptCar)+" 0 "+"3"+" 0 "+str(x+dCC*cos(beta))+" "+str(y+dCC*sin(beta)+2*dCC)+" "+str(z)+" "+"\n");
			x=x+2*dCC*cos(beta);
		x=txlo;
		y=y+2*dCC*sin(beta)+2*dCC;

# creation carbon nanotube

nbr=(2*pi*Rtube)/(2*dCC*cos(beta));
z=-Ltube/2;
while z<Ltube/2:
	betaF=0;
	while betaF < 360:
		beta2=betaF+dCC*cos(beta)*180/(Rtube*pi);
		x=Rtube*cos(pi*beta2/180);
		y=Rtube*sin(pi*beta2/180);
		if z<=Ltube/2:
			cptAtom += 1; cptCar += 1;
			fichier.write(str(cptCar) + " 0 " + "3" + " 0 "+ str(x) + " " + str(y) + " " + str(z) + "\n");
		if z+dCC<=Ltube/2:
			cptAtom += 1; cptCar += 1;
			fichier.write(str(cptCar) + " 0 " + "3 " + " 0 "+ str(x) + " " + str(y) + " " + str(z+dCC) + "\n");
		x=Rtube*cos(pi*betaF/180);
		y=Rtube*sin(pi*betaF/180);
		if z+dCC*sin(beta)+dCC<=Ltube/2:
			cptAtom += 1; cptCar += 1;
			fichier.write(str(cptCar) + " 0 " + "3 " + " 0 "+ str(x) + " " + str(y) + " " + str(z+dCC*sin(beta)+dCC) + "\n");
		if z+dCC*sin(beta)+2*dCC<=Ltube/2:
			cptAtom += 1; cptCar += 1;
			fichier.write(str(cptCar) + " 0 " + "3 " + " 0 "+ str(x) + " " + str(y) + " " + str(z+dCC*sin(beta)+2*dCC) + "\n");
		betaF=betaF+360/nbr;
	z=z+2*dCC*(1+sin(beta));

# water molecules

x=txlo+dOO/2;
y=tylo+dOO/2;
z=-Ltube/2-Rres+dOO;
while x <= txhi-dOO/2:
	while y <= tyhi-dOO/2:
		while z <= -Ltube/2-dOO:
			cptMolecule+=1;
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 2 "+str(qO)+" "+str(x)+" "+str(y)+" "+str(z) + "\n");
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 1 "+str(qH)+" "+str(r+x)+" "+str(y)+" "+str(z) + "\n");
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 1 "+str(qH)+" "+str(r*sin(alpha)+x)+ " "+str(r*sin(alpha)+y)+" "+ str(z)+"\n");
			z=z+dOO;
		y=y+dOO;
		z=-Ltube/2-Rres+dOO;
	x=x+dOO;
	y=tylo+dOO/2;

x=txlo+dOO/2;
y=tylo+dOO/2;
z=Ltube/2+dOO;
while x <= txhi-dOO/2:
	while y <= tyhi-dOO/2:
		while z <=Ltube/2+Rres-dOO:
			cptMolecule+=1;
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 2 "+str(qO)+" "+str(x)+" "+str(y)+" "+str(z) + "\n");
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 1 "+str(qH)+" "+str(r+x)+" "+str(y)+" "+str(z) + "\n");
			cptAtom+=1;
			fichier.write(str(cptAtom)+" "+str(cptMolecule)+" 1 "+str(qH)+" "+str(r*sin(alpha)+x)+ " "+str(r*sin(alpha)+y)+" "+ str(z)+"\n");
			z=z+dOO;
		y=y+dOO;
		z=Ltube/2+dOO;
	x=x+dOO;
	y=tylo+dOO/2;
fichier.write("\n"); 

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
