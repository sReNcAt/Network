'''

do not perfect....

'''

import os
import sys

filePath = os.getcwd()+'/subnet.txt'
innertxt = ""

class txt:
    def write(self,p_filePath,string):
        file = open(p_filePath, 'w+')
        file.write(string)
        file.close()
        return 0

txt = txt()

class network:
    def subnetreturn(self,length,ip,ip2):
        mask = ''
        temp=''
        if(length==50):
            length=0
        for i in range(1,length+2):
            mask+='255.'
        tempip=str(bin(ip)[2:])
        tempip2=str(bin(ip2)[2:])
        
        if(len(tempip)<8):
            for i in range (0,8-len(tempip)):
                tempip='0'+tempip
        if(len(tempip2)<8):
            for i in range (0,8-len(tempip2)):
                tempip2='0'+tempip2
        for i in range(0,len(tempip)):
            if(tempip[i]==tempip2[i]):
                temp+='1'
            else:
                for j in range(0,len(tempip)-i):
                    temp+='0'
                break;
        maskt=0
        for i in range(0,8):
            if(i==0):
                if(temp[0]=='1'):
                    maskt+=128
            if(i==1):
                if(temp[1]=='1'):
                    maskt+=64
            if(i==2):
                if(temp[2]=='1'):
                    maskt+=32
            if(i==3):
                if(temp[3]=='1'):
                    maskt+=16
            if(i==4):
                if(temp[4]=='1'):
                    maskt+=8
            if(i==5):
                if(temp[5]=='1'):
                    maskt+=4
            if(i==6):
                if(temp[6]=='1'):
                    maskt+=2
            if(i==7):
                if(temp[7]=='1'):
                    maskt+=1
        
        mask+=str(maskt)
        count = 0
        for i in range(0,len(mask)):
            if(mask[i]=='.'):
                count+=1
        if(count<3):
            for i in range(0,3-count):
                mask+='.0'
        return mask
    
    def subnet(self,start,end):
        global innertxt
        stemp=''
        etemp=''
        temp='Host Range\n'
        same = 100
        sames = ''
        samee = ''
        for i in range(0,4):
            if(i<3):
                stemp+=str(start[i])+'.'
                etemp+=str(end[i])+'.'
            else:
                stemp+=str(start[i])
                etemp+=str(end[i])
            if(start[i]==end[i]):
                if(i==0):
                    same=50
                else:
                    same = i
                sames = str(start[i+1])
                samee = str(end[i+1])
        temp+=stemp+' ~ '+etemp+'\n'
        if(same==100):
            temp+='default network'
        elif (same>0):
            temp+='SubNet Mask\n'+self.subnetreturn(same,int(sames),int(samee))
        innertxt+="\n\n"+temp
            
network = network()
def sort(array):
    left=[]
    center=[]
    right=[]
    if len(array) in [0,1]:
        return array
    pivot = array[0]
    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            center.append(i)
    return (sort(left)+center+sort(right))
netw = "2.2.2"
vsl=[10,25,50,50,2,2,50]

vsl = sort(vsl)
vsl.reverse()

def bitarray(a):
    bit=0
    if(a<2):
        bit=2
    elif(a<4):
        bit=4
    elif(a<8):
        bit=8
    elif(a<16):
        bit=16
    elif(a<32):
        bit=32
    elif(a<64):
        bit=64
    elif(a<128):
        bit=128
    return bit
def to8bit(a):
    b=str(bin(a)[2:])
    if(len(b)<8):
        for i in range (0,8-len(b)):
            b='0'+b
    return '0b'+b
full=0


def tobin(arr):
    global full
    for i in range(0,len(arr)):
        x=arr[i]
        t=to8bit(x)
        y=bitarray(x)
        z=to8bit(y)
        one = int(to8bit(full),2)+1
        two = int(to8bit(full),2)+y-2
        address = str(netw)+'.'+str(one)
        address2 = str(netw)+'.'+str(two)
        ip = []
        ip2 = []
        temp = 0
        count = 0
        for i in range(0,len(address)):
            if(address[i]=='.'):
                ip.append(address[temp:i])
                if(count==2):
                    ip.append(address[i+1:])
                temp=i+1
                count+=1
        if(count<3):
            pass
        else:
            temp = 0
            count = 0
            for i in range(0,len(address2)):
                if(address2[i]=='.'):
                    ip2.append(address2[temp:i])
                    if(count==2):
                        ip2.append(address2[i+1:])
                    temp=i+1
                    count+=1
            if(count<3):
                pass
            else:
                network.subnet(ip,ip2)
                pass
        full+=y
        if(full>255):
            break
    print(innertxt)
    #txt.write(filePath,innertxt)
tobin(vsl)
