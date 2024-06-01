from pymol import cmd
import string
import csv

def generate_numeric_range(start, end): return '+'.join(str(i) for i in range(int(start), int(end) + 1))

def generate_alpha_range(start, end): return '+'.join(chr(i) for i in range(ord(start), ord(end) + 1))

def generate_mixed_range(start, end): return '+'.join(f'{start[0]}{i}' for i in range(int(start[1:]), int(end[1:]) + 1))

def c_subunit_chains(pdb):
    initial = pdb[1]
    terminal = pdb[2]

    if initial.isdigit() and terminal.isdigit():
        pdb[1] = generate_numeric_range(initial, terminal)
    elif len(initial) == 1 and len(terminal) == 1 and initial.isalpha() and terminal.isalpha():
        pdb[1] = generate_alpha_range(initial, terminal)
    elif len(initial) > 1 and len(terminal) > 1 and initial[0].isalpha() and terminal[0].isalpha():
        pdb[1] = generate_mixed_range(initial, terminal)
    
    return pdb

def c_subunit_number(pdb):
    chain_ids = pdb[1].split('+')
    pdb[2] = len(chain_ids)
    #print PDB ID has X chains
    
    return pdb


cmd.extend("c_subunit_chains", c_subunit_chains)
cmd.extend("c_subunit_number", c_subunit_number)