def read_fasta(filename):
    file = open(filename,"r")
    header = file.readline().strip()
    sequence = file.readline().strip()
    file.close()
    return sequence

def find_variants(reference, read):
    variants = []
    for i in range(len(read)):
        if read[i] != reference [i]:
            variants.append({ "Position": i + 1,"Reference": reference[i],"Alternate": read[i] })
    return variants

def write_variants(filename, variants):
    variants_file = open(filename, "w")
    variants_file.write("Position\tReference\tAlternate\n")
    for variant in variants:
        variants_file.write(str(variant["Position"]) + "\t" + variant["Reference"] + "\t" + variant["Alternate"] + "\n")
    variants_file.close()

def main():
    reference = read_fasta("reference.fasta")
    read = read_fasta("read.fasta")
    variants = find_variants(reference, read)
    write_variants("variants.vcf", variants)
    print(variants)

if __name__ == "__main__":
    main()
