import pickle


def splice(fasta, range, gene_name):
    index = pickle.load(open(fasta + '.fai', "rb"))



    with open(fasta, 'r') as f:
        for