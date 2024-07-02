import csv
from pymol import cmd
from pymol import stored

def c_ring_pseudoatoms(pdb):
    print('Processing PDB ID: '+pdb[0])
    cmd.select(pdb[0].lower()+'_c_ring', '('+'chain '+pdb[1].replace(',','+')+') and '+pdb[0])
    chain_ids = pdb[1].split(',')
    myspace = {'residues': []}          # This is a user defined PyMOL namespace dictionary
    cmd.iterate_state(-1, pdb[0].lower()+' and polymer.protein and chain '+chain_ids[0], 'residues.append(resv)', space=myspace)
    seq_start = sorted(set(myspace['residues']))[0]
    seq_end = sorted(set(myspace['residues']))[-1]    
    for res in range(seq_start, (seq_end + 1)): cmd.pseudoatom(pdb[0].lower(), name='PSD', resi='1', resn='CRC', chain='ZZ', color='hotpink', pos=centroid(pdb[0]+'_c_ring and resi '+str(res)+' and name CA'))

def c_ring_align(pdb):
    cmd.select(pdb[0].lower()+'_c_ring_cen_axs', 'resn CRC and '+pdb[0])
    cmd.align(pdb[0].lower()+'_c_ring_cen_axs', 'ORGN')

def c_ring_cleanup(pdb):
    cmd.remove(pdb[0].lower()+'_c_ring_cen_axs')
    cmd.delete(pdb[0].lower()+'_c_ring_cen_axs')


cmd.extend("c_ring_pseudoatoms", c_ring_pseudoatoms)
cmd.extend("c_ring_align", c_ring_align)
cmd.extend("c_ring_cleanup", c_ring_cleanup)