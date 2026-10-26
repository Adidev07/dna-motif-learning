"""Learn short-sequence statistics for an artificial motif recognition task without functional genomic claims."""
from kit import *
TITLE='Synthetic DNA Motif Classifier'
LIVE=False

from itertools import product
TAG='ACGTAC'
def validate_sequence(sequence):
    if not isinstance(sequence,str) or not sequence or set(sequence)-set('ACGT'):raise ValueError('Nonempty uppercase ACGT sequence required')
def dinucleotides(sequence):
    validate_sequence(sequence);pairs=[''.join(p) for p in product('ACGT',repeat=2)];count={p:0 for p in pairs}
    for i in range(len(sequence)-1):count[sequence[i:i+2]]+=1
    return np.array([count[p]/max(1,len(sequence)-1) for p in pairs])
def generate(seed,n):
    rng=np.random.default_rng(seed);sequences=[];y=rng.integers(0,2,n)
    for label in y:
        letters=rng.choice(list('ACGT'),60).tolist()
        if label:letters[20:20+len(TAG)]=list(TAG)
        sequences.append(''.join(letters))
    return sequences,y
def run(d,a):
    seq,y=generate(a.seed,900);test,truth=generate(a.seed+1,300);x=np.array([dinucleotides(s) for s in seq]);xt=np.array([dinucleotides(s) for s in test]);mean,scale=standardize_fit(x);w=fit_softmax((x-mean)/scale,y,2);pred=softmax(np.column_stack([np.ones(len(test)),(xt-mean)/scale])@w).argmax(axis=1)
    return dict(ml_metrics=classification(truth,pred),exact_tag_baseline=classification(truth,np.array([TAG in s for s in test])),tag=TAG,scope='Artificial sequence classification; no functional genomic inference'),dict(weights=w,mean=mean,scale=scale,test_sequences=np.array(test),test_labels=truth)

if __name__=="__main__":main(run)
