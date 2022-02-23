"""Create a function which translates a given DNA string into RNA"""
def dna_to_rna(dna):
    rna = ''
    for i in dna:
        if i=='T':
            rna +='U'
        else:
            rna += i
    return rna
