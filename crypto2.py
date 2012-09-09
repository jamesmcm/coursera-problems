#Implement AES CBC and counter encryption and decryption using random IVs
#Use PyCrypto for AES implementation
#block size 16 bytes AES, also IV?

from Crypto.Cipher import AES
import binascii

def CBCencrypt(m, k):
    mlist=[]
    for i in range(len(m)/16):
        mlist.append(m[16*i:(16*(i+1))])
    mlist.append(m[-(len(m)%16):])
    
    for i in range(16-len(mlist[len(mlist)-1])):
        mlist[len(mlist)-1]+=str(16-len(mlist[len(mlist)-1]))
    print mlist

#CBCencrypt("averylongtestmessageofover16characters", 1)

def CBCdecrypt(c, k):

    clist=[]
    for i in range(len(c)/16):
        clist.append(c[16*i:(16*(i+1))])
    #clist.append(c[-(len(c)%16):])
    print clist
    pmlist=[]
    for i in range(len(clist)-1):
        cipher = AES.new(k, AES.MODE_ECB)    
        i+=1
        
        pm=cipher.decrypt(clist[i])
        pm=binascii.hexlify(pm)
        print pm
        pm=str(hex(int(pm, 16)^int(binascii.hexlify(clist[i-1]), 16)))[2:]
        print pm
        pm=pm.strip("L")
        print pm
        pmlist.append(str(pm))
    print pmlist
    print "".join(pmlist)
    return "".join(pmlist)
    
#print str(binascii.unhexlify(CBCdecrypt(binascii.unhexlify(b'4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'), binascii.unhexlify(b'140b41b22a29beb4061bda66b6747e14'))))

#print str(binascii.unhexlify(CBCdecrypt(binascii.unhexlify(b'5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'), binascii.unhexlify(b'140b41b22a29beb4061bda66b6747e14'))))


def CTRdecrypt(c, k):

    clist=[]
    for i in range(len(c)/16):
        clist.append(c[16*i:(16*(i+1))])
    clist.append(c[-(len(c)%16):])
    #print len(clist[2])
    #for j in clist:
        #print binascii.hexlify(j), len(j)
    pmlist=[]
    for i in range(len(clist)-1):
        cipher = AES.new(k, AES.MODE_ECB)    
        i+=1
        
        #pm=cipher.decrypt(clist[i])
        pm=str(hex(int(binascii.hexlify(cipher.encrypt(binascii.unhexlify(str(hex(int(binascii.hexlify(clist[0]), 16)+(i-1)))[2:].strip("L"))))[0:2*len(clist[i])], 16) ^int(binascii.hexlify(clist[i]), 16)))[2:]
        #pm=binascii.hexlify(pm)
        #pm=str(hex(int(pm, 16)^int(binascii.hexlify(clist[i-1]), 16)))[2:]
        pm=pm.strip("L")
        print pm
        pmlist.append(str(pm))
    print pmlist
    print "".join(pmlist)
    return "".join(pmlist)

print str(binascii.unhexlify(CTRdecrypt(binascii.unhexlify(b'69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'), binascii.unhexlify(b'36f18357be4dbd77f050515c73fcf9f2'))))

#print str(binascii.unhexlify(CTRdecrypt(binascii.unhexlify(b'770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'), binascii.unhexlify(b'36f18357be4dbd77f050515c73fcf9f2'))))
