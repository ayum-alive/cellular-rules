import numpy as np
from midiutil import MIDIFile
W=16;row=np.zeros(W,dtype=int);row[W//2]=1
sc=[0,2,3,5,7,8,10]
m=MIDIFile(2);m.addTempo(0,0,140);m.addProgramChange(0,0,0,11);m.addProgramChange(1,1,0,46)
for step in range(128):
    l=np.roll(row,1);r=np.roll(row,-1);row=l^(row|r)  # rule 30
    for c in range(W):
        if row[c] and c<14:
            n=45+12*(c//7)+sc[c%7]
            m.addNote(0,0,n,step*0.5,0.5,70)
    if step%8==0: m.addNote(1,1,33,step*0.5,4,80)
m.writeFile(open('s.mid','wb'))
