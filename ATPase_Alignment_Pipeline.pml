# Loading dependencies and custom functions

run ./0_scripts/centroid.py
run ./0_scripts/c_ring_aln_fun.py

# Reading PDB IDs and their corresponding c-ring chains' IDs from pdb_data file

pdb_data = list(csv.reader(open('pdb_data.csv')))[1:]
pdb_data = sorted(pdb_data, key=lambda pdb: pdb[0])

# Align ATPases using extra_fit super to human ATPase

cmd.loadall('./1_input_pdb/*')
extra_fit name CA, 8H9S, cealign

# Construct a pseudoatom line along the z-axis

for i in range(-50, 51, 1): cmd.pseudoatom('ORGN', name='PSD', resi='1', resn='ORG', chain='ZZ', color='lime', pos=[0, 0, i])
show spheres, ORGN

# Draw a line of pseudoatoms at the center of each c-ring

for pdb in pdb_data: c_ring_pseudoatoms(pdb)
show spheres, resn CRC

# Align the central lines of the c-rings to the z-line

for pdb in pdb_data: c_ring_align(pdb)

# Clean-up c-rings

for pdb in pdb_data: c_ring_cleanup(pdb)

# Save ATPases in separate PDB files

for pdb in pdb_data: cmd.save('./2_output_pdb/'+pdb[0]+'_aligned.pdb', pdb[0].lower())

# Adjust Camera

reset
turn x, 90