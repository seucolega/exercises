from rna_codon_table import codons_and_proteins


def strand_to_codons(series: str) -> list:
    length = 3
    return [series[index * length:index * length + length] for index in range(0, len(series) // length)]


def codon_to_protein(codon: str) -> str:
    for codons_and_protein in codons_and_proteins:
        if codon in codons_and_protein[0]:
            return codons_and_protein[1]


def proteins(strand: str) -> list:
    codons = strand_to_codons(strand)
    result = []
    for codon in codons:
        protein = codon_to_protein(codon)
        if protein == 'STOP':
            break
        result.append(protein)
    return result
