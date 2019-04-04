from math import *

typat=2; # 2 types of atom in total (hydrogen and oxygen) 
typbo=1; # 1 type of bond (O-H) 
typan=1; # 1 type of angle (H-O-H) 
mH=1.00794; # hydrogen mass in grams per mole 
mO=15.9994; # oxygen mass in grams per mole 
alpha=104.5*pi/180; # O-H-O angle (TIP4P/2005) in radian 
r=0.9584; # O-H bond distance (TIP4P/2005) in angstrom 
qO=-1.1128; # oxygen charge (TIP4P/2005) in multiple of electron charge 
qH=0.5564; # hydrogen charge (TIP4P/2005) in multiple of electron charge 
dOO=3.1589; # typical O-O distance in angstrom 

txlo=-15; txhi=15;
tylo=-15; tyhi=15;
tzlo=-15; tzhi=15;

cptAtom=0; # for atom counting 
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
fichier.write("\n"); 

fichier.write("Atoms \n \n") 
x=txlo+dOO/2;
y=tylo+dOO/2;
z=tzlo+dOO/2;
while x <= txhi-dOO/2:
	while y <= tyhi-dOO/2:
		while z <= tzhi-dOO/2:
			cptMolecule+=1;
			fichier.write(str(cptAtom+1)+" "+str(cptMolecule)+" 2 "+str(qO)+" "+str(x)+" "+str(y)+" "+str(z) + "\n");cptAtom+=1;
			fichier.write(str(cptAtom+1)+" "+str(cptMolecule)+" 1 "+str(qH)+" "+str(r+x)+" "+str(y)+" "+str(z) + "\n");cptAtom+=1;
			fichier.write(str(cptAtom+1)+" "+str(cptMolecule)+" 1 "+str(qH)+" "+str(r*sin(alpha)+x)+ " "+str(r*sin(alpha)+y)+" "+ str(z)+"\n");cptAtom+=1;
			z=z+dOO;
		y=y+dOO;
		z=tzlo+dOO/2;
	x=x+dOO;
	y=tylo+dOO/2;
fichier.write("\n");

fichier.write("Bonds \n \n") 
while cptBond < 2*cptAtom/3: 
	fichier.write(str(cptBond+1)+" 1 "+str(cptBond/2*3+1)+" "+str(cptBond/2*3+2)+"\n"); 
	fichier.write(str(cptBond+2)+" 1 "+str(cptBond/2*3+1)+" "+str(cptBond/2*3+3)+"\n"); 
	cptBond+=2;
fichier.write("\n");

fichier.write("Angles \n \n") 
while cptAngle < cptAtom/3: 
	fichier.write(str(cptAngle+1)+" 1 "+str(cptAngle*3+2)+" "+str(cptAngle*3+1)+" "+str(cptAngle*3+3)+"\n"); 
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
