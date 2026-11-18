import numpy as np
W,H=401,200
def run(rule):
    row=np.zeros(W,dtype=np.uint8);row[W//2]=1;g=[row]
    for _ in range(H-1):
        l=np.roll(row,1);r=np.roll(row,-1);idx=l*4+row*2+r
        row=np.array([(rule>>int(i))&1 for i in idx],dtype=np.uint8);g.append(row)
    return np.array(g)
tiles=[run(r) for r in (30,90,110,150)]
img=np.concatenate([np.concatenate(tiles[:2],1),np.concatenate(tiles[2:],1)],0)
rgb=np.stack([20+img*230,20+img*150,40+img*60],-1).astype(np.uint8)
open('r.ppm','wb').write(b'P6 %d %d 255\n'%(img.shape[1],img.shape[0])+rgb.tobytes())
