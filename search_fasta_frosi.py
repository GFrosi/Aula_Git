import pickle


def search(fasta, start, end, gene_name):
    index = pickle.load(open(fasta + '.fai', "rb"))


    with open(fasta, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()


            # if the line num was indexed
            if line_num in index[gene_name].keys():
                # print(start, index[gene_name][line_num][0], end , index[gene_name][line_num][1])

                if start >= index[gene_name][line_num][0] and start <= index[gene_name][line_num][1]:  # find the starting line
                    start_pos = start - index[gene_name][line_num][0]

                    #start and end on the same line
                    if end <= index[gene_name][line_num][1]:
                        end_pos = end + index[gene_name][line_num][0] -1
                        #troquei o seq para o yield
                        yield line[start_pos:end_pos]
                        break

                    # starts in this line but ends in another line
                    elif end > (index[gene_name][line_num][1]):
                        #removi o seq e coloquei o yield
                        yield line[start_pos:]



                # The start was in another line and the end might be or not in this line (:. len(seq) >0)
                if start < index[gene_name][line_num][0]:

                    # seq extends beyond this line
                    if end > index[gene_name][line_num][1]:

                        yield line[:]


                    # seq ends in this line
                    elif end<= index[gene_name][line_num][1]:
                        end_pos = end - index[gene_name][line_num][0]
                        yield line[:end_pos]
                        break



def len(fasta, gene_name=None):
    index = pickle.load(open(fasta + '.fai', "rb"))

    if gene_name is None:

        for name in index.keys():
            last_index_line = sorted(index[name].keys())[-1] # key of the last line of the index file
            print(name, index[name][last_index_line][1])

    # Get the index[1] of the last tuple of the last line
    else:
        last_index_line = sorted(index[gene_name].keys())[-1]
        print(gene_name, index[gene_name][last_index_line][1])



def splice(fasta, range, gene_name):
    for r in range:
        start, end = r.split('-')
        start = int(start)
        end = int(end)

        sequence = search(fasta, start, end, gene_name)

        for s in sequence:
            print(s, end='')
    print()













