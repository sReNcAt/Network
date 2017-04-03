'''

do not perfect....

'''

import os
import sys

filePath = os.getcwd()+'/subnet.txt'

class txt:
    def prints(self,p_filePath):
        f = open(p_filePath)
        #print('Read File\n')
        print(f.read())
        f.close()
        return 0

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
        print(tempip)
        print(tempip2)
        for i in range(0,len(tempip)):
            if(tempip[i]==tempip2[i]):
                temp+='1'
            else:
                for j in range(0,len(tempip)-i):
                    temp+='0'
                break;
        
        print('\nSubnet Mask Bit')
        print(temp+'\n')
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
        print('same = '+str(same))
        if(same==100):
            temp+='default network'
        elif (same>0):
            temp+='\nSubNet Mask\n'+self.subnetreturn(same,int(sames),int(samee))
        txt.write(filePath,temp)
            
network = network()

if __name__ == '__main__':
    if(len(sys.argv)<3):
        pass
    else:
        ip = []
        ip2 = []
        temp = 0
        count = 0
        for i in range(0,len(sys.argv[1])):
            if(sys.argv[1][i]=='.'):
                ip.append(sys.argv[1][temp:i])
                if(count==2):
                    ip.append(sys.argv[1][i+1:])
                temp=i+1
                count+=1
        if(count<3):
            pass
        else:
            temp = 0
            count = 0
            for i in range(0,len(sys.argv[2])):
                if(sys.argv[2][i]=='.'):
                    ip2.append(sys.argv[2][temp:i])
                    if(count==2):
                        ip2.append(sys.argv[2][i+1:])
                    temp=i+1
                    count+=1
            if(count<3):
                pass
            else:
                network.subnet(ip,ip2)
                txt.prints(filePath)
