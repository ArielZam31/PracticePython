def busc_eco(seq):
    ecoRI = ["GAATTC", "AAGCTT", "GCGGCCGC"]
    res_ecoRI = []

    for seq_corte in ecoRI:
        while True:
            sitio = seq.find(seq_corte)
            if sitio >= 0:
                presencia = "Si"
                res_ecoRI.append([seq, len(seq), presencia, sitio])
                seq = seq[sitio + len(seq_corte):]
            else:
                presencia = "No"
                res_ecoRI.append([seq, len(seq), presencia, sitio])
                break

    return res_ecoRI
