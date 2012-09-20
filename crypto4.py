import urllib2
import sys
import binascii

TARGET = 'http://crypto-class.appspot.com/po?er='
#cipher="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd"

cipher="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
listc=[]
cipherstr=binascii.unhexlify(cipher)
for i in range(9):
    listc.append(9)
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

if __name__ == "__main__":
    po = PaddingOracle()

    found=False
    for i in range(9,16):
        g=0
        found=False
        while found==False:
            newcipher=cipherstr
            #newcipher[len(newcipher)-1-i]=chr(g^(i+1))
            nlist=list(newcipher)
            #nlist[len(newcipher)-1-i]=chr((g^(i+1))^ord(cipherstr[len(newcipher)-1-i]))
            nlist[(48)-1-i]=chr((g^(i+1))^ord(cipherstr[(48)-1-i]))
            #nlist[(len(newcipher)/2)-1-i]=chr((g^(i+1)))
            for j in range(i):
                #newcipher[len(newcipher)-1-j]=chr((i+1))
                nlist[(48)-1-j]=chr(((i+1)^listc[j])^ord(cipherstr[(48)-1-j])) #cross with correct byte
                
                
            newcipher="".join(nlist)
            #print binascii.hexlify(newcipher)
            if(po.query(binascii.hexlify(newcipher))==True):
                found=True #Padding okay
                print "Found byte " + str(i+1) + " of " + str(16) +". Byte was: "+ chr(g) + "value: " + str(g) +"\n"
                listc.append(g)
                break
            else:
                g+=1 #Should never exceed 255
                if g>=256:
                    print "MAJOR ERROR\n"
                    
listc.reverse()
s=""

print listc
for item in listc:
    s+=chr(item)

print s
print binascii.hexlify(s)


    
                    #po.query(cipher)       # Issue HTTP query with the given argument




