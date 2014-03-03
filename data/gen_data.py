import csv
from nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader,stopwords
MAX_WORDS = 4
NUM_WORDS = 100
wordlist = PlaintextCorpusReader('', 'ofk(_chap_[1234])?\.txt')

sents = wordlist.sents('ofk.txt')
seqs = []

def clean_sent(sent):
    sent = filter(lambda w: w.isalpha() or w in ['.', '!', '?'], sent)
    out = []
    for i in range(len(sent)):
        if sent[i] == 't':
            out[-1] += "'t"
        else:
            out.append(sent[i])
    return out

sents= map(clean_sent, sents)

for sent in sents:
    output = []
    for i in range(len(sent)):
        output.append(sent[i])
        if len(output) >= MAX_WORDS:
            break
    if output:
        seqs.append(output)

output = map(lambda s: '-'.join(s), seqs)
freq = FreqDist(output)
output_seq = [(k, freq[k]) for k in freq]

data = sorted(output_seq, reverse=True, key=lambda x: x[1])[:NUM_WORDS]


with open('data.csv', 'w') as outfile:
    datawriter = csv.writer(outfile)
    datawriter.writerows(data)
