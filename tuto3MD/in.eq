# LAMMPS input file

variable	T equal 300 # temperature
variable	dt equal 0.0005 # timestep
variable	p0 equal 1e5 # desired pressure - Pa

units           metal
boundary        p p p
atom_style      full
bond_style      harmonic
angle_style     harmonic
pair_style  	hybrid/overlay airebo 2.5 1 1 lj/cut/tip4p/long 8 9 1 1 0.1546 10.0
kspace_style	pppm/tip4p 1.0e-4

read_data	data.lammps

bond_coeff      1 0.0 0.9572
angle_coeff     1 0.0 104.52

set 		type 1*7 charge 0
set 		type 8 charge -1.1128
set 		type 9 charge 0.5564

pair_coeff 	* * 	airebo ./CH.airebo C C C C NULL NULL NULL NULL NULL
pair_coeff      * * 	lj/cut/tip4p/long 0 0
pair_coeff      1*5 8 	lj/cut/tip4p/long 0.00494351 3.28 # Amber
pair_coeff 	6*7 8 	lj/cut/tip4p/long 0.02693779 3.2664 # C-O AMBER96 force field
pair_coeff 	8 8 	lj/cut/tip4p/long 0.008031034 3.1589 # TIP4P Water

group		wat type 8 9
group		pst type 7
group	 	gra type 1 2 3 4
group	 	grt type 1 2 3
group	 	gr1 type 1

neighbor        2.0 bin
neigh_modify    delay 0
neigh_modify	exclude group pst pst

dump 		dp1 all atom 5000 dump.eq.lammpstrj

variable	nb equal count(pst) 		# number of atom in the piston
variable	area equal lx*ly*1e-20 		# m2
variable	force equal ${p0}*${area} 	# Pa*m2 = N 
variable	fperat equal ${force}/${nb}	# N (force per atom)
variable	f0 equal ${fperat}*6.24e8	# eV/A
fix    		afp pst aveforce NULL NULL -${f0}
fix 		sfp pst setforce 0.0 0.0 NULL

fix             s1 wat shake 1.0e-4 200 0 b 1 a 1
velocity 	wat create ${T} 5658732 # give initiate velocity to water molecules

fix		nvl wat nve
fix		nvw pst nve
fix		nvg grt nve

compute		tpw wat temp
fix 		myber wat temp/berendsen ${T} ${T} 0.1
fix_modify	myber temp tpw

timestep	${dt}
thermo		100
run		150000

write_restart  restart.eq


