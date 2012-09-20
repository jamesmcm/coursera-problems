#import pycrypto




bytestr=""
blocks=[]
with open("givenfile.mp4", "rb") as f:
    byte = f.read(1)
    while byte != "":
        # Do stuff with byte.
        bytestr+=byte
        if len(bytestr)==1024:
            blocks.append(bytestr)
            bytestr=""
        byte = f.read(1)
    blocks.append(bytestr)

i=0

lasthash=""
while i<len(blocks):
    hash = pycrypto.Crypto.Hash.SHA256.SHA256Hash(data=blocks[len(blocks)-1-i]+lasthash)
    lasthash=hash
    i+=1
print hash

