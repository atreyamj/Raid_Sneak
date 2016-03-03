import sys,getopt

class ReadFromInputFile:
    #input_file_handle = open('foo.txt','r')
    AlgoName=0
    PlayerName = 0
    CutOff = 0
    GameBoard = dict()
    CurrentBoard= dict()

    def read_game(self,file_handle):
        self.AlgoName = int(file_handle.readline().rstrip('\r\n'))
        self.PlayerName = str(file_handle.readline().rstrip('\r\n'))
        self.CutOff=int(file_handle.readline().rstrip('\r\n'))
        myList1=file_handle.readline().rstrip('\r\n').split(' ')
        for x in range(0,5):
            self.GameBoard[x]=myList1[x]

        myList2=file_handle.readline().rstrip('\r\n').split(' ')
        for x in range(0,5):
            self.GameBoard[x+5]=myList2[x]

        myList3=file_handle.readline().rstrip('\r\n').split(' ')
        for x in range(0,5):
            self.GameBoard[x+10]=myList3[x]

        myList4=file_handle.readline().rstrip('\r\n').split(' ')
        for x in range(0,5):
            self.GameBoard[x+15]=myList4[x]

        myList5=file_handle.readline().rstrip('\r\n').split(' ')
        for x in range(0,5):
            self.GameBoard[x+20]=myList5[x]

        mylist6=file_handle.readline().rstrip('\r\n').split(' ')
        stringtest= str(mylist6)
        for x in range(2,7):
            self.CurrentBoard[x-2]=stringtest[x]

        mylist7=file_handle.readline().rstrip('\r\n').split(' ')
        stringtest= str(mylist7)
        for x in range(2,7):
            self.CurrentBoard[x+3]=stringtest[x]

        mylist8=file_handle.readline().rstrip('\r\n').split(' ')
        stringtest= str(mylist8)
        for x in range(2,7):
            self.CurrentBoard[x+8]=stringtest[x]

        mylist9=file_handle.readline().rstrip('\r\n').split(' ')
        stringtest= str(mylist9)
        for x in range(2,7):
            self.CurrentBoard[x+13]=stringtest[x]

        mylist10=file_handle.readline().rstrip('\r\n').split(' ')
        stringtest= str(mylist10)
        for x in range(2,7):
            self.CurrentBoard[x+18]=stringtest[x]

class BestFirstSearch:
    def getNextMoveSum(self,prev,index,GridObj,depth,player):
        if GridObj.getOccupantAt(index)!="*" and depth==0:
            return 0
        if GridObj.getOccupantAt(index) ==player and depth ==1:
            return 0
        if index < 1  or index > 25 or ((prev)%5==0 and (index)%5!=0  and prev<index) or ((prev)%5!=0 and (index)%5==0 and prev > index):
            return 0
        if depth==1:
            if self.getNextMoveSum(index,index,GridObj,depth+1,player)!=0:
                return int(self.getNextMoveSum(index,index,GridObj,depth+1,player))+int(self.getNextMoveSum(index,index-1,GridObj,depth+1,player))+int(self.getNextMoveSum(index,index+1,GridObj,depth+1,player))+int(self.getNextMoveSum(index,index+5,GridObj,depth+1,player))+int(self.getNextMoveSum(index,index-5,GridObj,depth+1,player))
                #return self.getNextMoveSum(index,index,GridObj,depth+1,player)
            else:
                return 0
        if (GridObj.getOccupantAt(index) == "*" or GridObj.getOccupantAt(index) == GridObj.getOtherPlayer(player) )and prev == index and depth==2:
            return GridObj.getValueAt(index)
        elif GridObj.getOccupantAt(index) != "*" and prev == index and depth==2:
            return 0

        elif GridObj.getOccupantAt(index) == GridObj.getOtherPlayer(player) and prev != index and depth==2:
            return GridObj.getValueAt(index)
        elif GridObj.getOccupantAt(index) == player and prev != index and depth==2:
            return 0
        elif GridObj.getOccupantAt(index) =="*" and prev!=index and depth==2:
            return 0
        return max((self.getNextMoveSum(index,index+1,GridObj,depth+1,player),self.getNextMoveSum(index,index-5,GridObj,depth+1,player),self.getNextMoveSum(index,index-1,GridObj,depth+1,player),self.getNextMoveSum(index,index+5,GridObj,depth+1,player)))

class Grid:
    MAX_SIZE=25;
    GridValueDict=dict()
    GridOccupantDict=dict()
    GridOccupantDictCopy=dict()
    GridOccupantDictShadow=dict()
    GridOccupantDictSneakRaidShadow=dict()
    GridIndexDict=dict()
    GBFS=BestFirstSearch()
    GridMaxValues=dict()
    GridMinMaxMaxValues=dict()
    NextXPos=0;
    NextOPos=0;
    GridCount=0;
    maxDepth=2;
    FileHandleObject=ReadFromInputFile()

    ReadFileHandle = open(str(sys.argv[2]),'r')
    FileHandleObject.read_game(ReadFileHandle)
    #GridValueDict=FileHandleObject.GameBoard
    GridValueTemp=FileHandleObject.GameBoard
    GridOccupantTemp=FileHandleObject.CurrentBoard
    ii=0
    jj=1
    while ii < 25:
        GridOccupantDict[jj]=GridOccupantTemp[ii]
        ii=ii+1
        jj=jj+1

    ii=0
    jj=1
    while ii < 25:
        GridValueDict[jj]=GridValueTemp[ii]
        ii=ii+1
        jj=jj+1

    ##print GridValueDict
    ##print GridOccupantDict



    #GridOccupantDict=FileHandleObject.CurrentBoard

    ''' GridValueDict[1] = 8
    GridValueDict[2] = 16
    GridValueDict[3] = 1
    GridValueDict[4] = 32
    GridValueDict[5] = 20

    GridValueDict[6] = 20
    GridValueDict[7] = 12
    GridValueDict[8] = 2
    GridValueDict[9] = 23
    GridValueDict[10] = 8

    GridValueDict[11] = 28
    GridValueDict[12] = 48
    GridValueDict[13] = 4
    GridValueDict[14] = 1
    GridValueDict[15] = 21

    GridValueDict[16] = 1
    GridValueDict[17] = 1
    GridValueDict[18] = 1
    GridValueDict[19] = 60
    GridValueDict[20] = 2

    GridValueDict[21] = 25
    GridValueDict[22] = 30
    GridValueDict[23] = 23
    GridValueDict[24] = 21
    GridValueDict[25] = 30

    GridOccupantDict[1] = "*"
    GridOccupantDict[2] = "X"
    GridOccupantDict[3] = "*"
    GridOccupantDict[4] = "X"
    GridOccupantDict[5] = "*"

    GridOccupantDict[6] = "*"
    GridOccupantDict[7] = "*"
    GridOccupantDict[8] = "*"
    GridOccupantDict[9] = "*"
    GridOccupantDict[10] = "*"

    GridOccupantDict[11] = "O"
    GridOccupantDict[12] = "*"
    GridOccupantDict[13] = "O"
    GridOccupantDict[14] = "*"
    GridOccupantDict[15] = "*"

    GridOccupantDict[16] = "*"
    GridOccupantDict[17] = "X"
    GridOccupantDict[18] = "*"
    GridOccupantDict[19] = "X"
    GridOccupantDict[20] = "*"

    GridOccupantDict[21] = "O"
    GridOccupantDict[22] = "X"
    GridOccupantDict[23] = "*"
    GridOccupantDict[24] = "O"
    GridOccupantDict[25] = "O"'''



    GridIndexDict=dict()
    GridIndexDict[1]= 'A1'
    GridIndexDict[2]= 'B1'
    GridIndexDict[3]= 'C1'
    GridIndexDict[4]= 'D1'
    GridIndexDict[5]= 'E1'
    GridIndexDict[6]= 'A2'
    GridIndexDict[7]= 'B2'
    GridIndexDict[8]= 'C2'
    GridIndexDict[9]= 'D2'
    GridIndexDict[10]= 'E2'
    GridIndexDict[11]= 'A3'
    GridIndexDict[12]= 'B3'
    GridIndexDict[13]= 'C3'
    GridIndexDict[14]= 'D3'
    GridIndexDict[15]= 'E3'
    GridIndexDict[16]= 'A4'
    GridIndexDict[17]= 'B4'
    GridIndexDict[18]= 'C4'
    GridIndexDict[19]= 'D4'
    GridIndexDict[20]= 'E4'
    GridIndexDict[21]= 'A5'
    GridIndexDict[22]= 'B5'
    GridIndexDict[23]= 'C5'
    GridIndexDict[24]= 'D5'
    GridIndexDict[25]= 'E5'
    #def InitGrids(self,**ValueDict,**OccupantDict,**IndexDict):
     #   self.GridValueDict=ValueDict.copy()
      #  self.GridOccupantDict=OccupantDict.copy()
       # self.GridIndexDict=IndexDict.copy()

    def CopyOccupantDict(self):
        i=1
        while(i<=25):
            self.GridOccupantDictCopy[i]=self.GridOccupantDict[i]
            i=i+1

    def ResetOccupantDict(self):
        i=1
        while(i<=25):
            self.GridOccupantDict[i]=self.GridOccupantDictCopy[i]
            i=i+1

    def RestoreOccupantDict(self):
        i=1
        while(i<=25):
            self.GridOccupantDict[i]=self.GridOccupantDictShadow[i]
            i=i+1

    def CopyShadowOccupantDict(self):
        i=1
        while(i<=25):
            self.GridOccupantDictShadow[i]=self.GridOccupantDict[i]
            i=i+1
    def RestoreSneakOccupantDict(self):
        i=1
        while(i<=25):
            self.GridOccupantDict[i]=self.GridOccupantDictSneakRaidShadow[i]
            i=i+1

    def CopySneakShadowOccupantDict(self):
        i=1
        while(i<=25):
            self.GridOccupantDictSneakRaidShadow[i]=self.GridOccupantDict[i]
            i=i+1

    def getValueAt(self,index):
        if self.GridValueDict.has_key(index) == True:
            return self.GridValueDict.get(index)
        else:
            return 0

    def getOccupantAt(self,index):
          if self.GridOccupantDict.has_key(index) == True:
            return self.GridOccupantDict.get(index)
          else:
            return 0

    def getIndexAt(self,index):
        if self.GridValueDict.has_key(index) == True:
            return self.GridIndexDict.get(index)
        else:
             return 0
    def getGridCount(self):
        return self.GridCount

    def setValueAt(self,index,value):
         self.GridValueDict[index]=value

    def setOccupantAt(self,index,value):
         self.GridOccupantDict[index]=value

    def setIndexAt(self,index,value):
         self.GridIndexDict[index]=value

    def setGridCount(self):
        i=1
        self.GridCount=0
        while i<=25:
            if self.getOccupantAt(i)=="*":
                self.GridCount+=1
            i+=1

    def getOtherPlayer(self,player):
        if player=="X":
            return "O"
        else:
            return "X"


        #Entry Point
    def doMaxMove(self,AlgoVal,index,player):
        nextIndex=index
        self.NextOPos=self.NextXPos=nextIndex
        if player== "X":
            self.NextOPos=nextIndex
            nextIndex=self.getNextMove(AlgoVal, self.NextXPos,player)
        else:
            self.NextXPos=nextIndex
            nextIndex=self.getNextMove(AlgoVal, self.NextOPos,player)
        return nextIndex

    def isSneakable(self,index):
        Sneakable=False
        val1=val2=val3=val4=True
        if index!=1 and index!=6 and index!=11 and index!=16 and index!=21:
            if self.getOccupantAt(index-1)!="X":
                val1=True
            else:
                val1=False
        if index>5:
            if self.getOccupantAt(index-5)!="X":
                val2=True
            else:
                val2=False
        if index!=5 and index!=10 and index!=15 and index!=20 and index!=25:
            if self.getOccupantAt(index+1)!="X":
                val3=True
            else:
                val3=False
        if index<21:
            if self.getOccupantAt(index+5)!="X":
                val4=True
            else:
                val4=False
        return (val1 & val2 & val3 & val4)

    def getSneak_Raid_Value(self,player,RaidMax,RaidIndex):
        i=1
        maxm=0
        maxIndex=0
        while(i<=25):
            if maxm < int(self.getValueAt(i)) and self.getOccupantAt(i)=="*" and self.isSneakable(i)==True:
                maxm= int(self.getValueAt(i))
                maxIndex=i
            i=i+1
        if RaidMax<=maxm:
            self.GridMaxValues[maxIndex]=maxm
            return maxIndex
        else:
            self.GridMaxValues[RaidIndex]=RaidMax
            return RaidIndex


    def getNextMove(self,AlgoVal,index,player):
        if AlgoVal==1:
            val1=val2=val3=val4=0
            if self.getOccupantAt(index+1)=="*":
                val1=self.GBFS.getNextMoveSum(index,index+1,self,1,player)
            if self.getOccupantAt(index-5)=="*":
                val2=self.GBFS.getNextMoveSum(index,index-5,self,1,player)
            if self.getOccupantAt(index-1)=="*":
                val3=self.GBFS.getNextMoveSum(index,index-1,self,1,player)
            if self.getOccupantAt(index+5)=="*":
                val4=self.GBFS.getNextMoveSum(index,index+5,self,1,player)
            #val =  self.GBFS.getNextMoveSum(-1,index,self,0,player)
            val =  max(val1,val2,val3,val4)
            if val==0:
                return  self.getSneak_Raid_Value(player,val,0)
            if val1 == val :
                return self.getSneak_Raid_Value(player,val,index+1)
            elif val2 == val:
                return self.getSneak_Raid_Value(player,val,index-5)
            elif val3 ==val:
                return self.getSneak_Raid_Value(player,val,index-1)
            elif val4 == val:
                return self.getSneak_Raid_Value(player,val,index+5)
            return 0

    def StartGBFS(self,AlgoVal,player):
        i=1
        self.GridMaxValues.clear()
        if 'key' in self.GridMaxValues:
            del self.GridMaxValues['key']
        max=self.getSneak_Raid_Value(player,0,0)
        maxIndex=0
        val=0
        while i<=25:

            if self.getOccupantAt(i)==player:
                val=self.doMaxMove(AlgoVal,i,player)
            i=i+1

        i=1
        for key, value in self.GridMaxValues.iteritems():
            if i==1:
                max=self.getSneak_Raid_Value(player,0,0)
                i=i+1
            if max < value:
                max=value
                maxIndex=key

        if maxIndex==0:
            print "No solutions"
            return 0
       # print str(maxIndex) + " --- > " + str(max)

        self.setOccupantAt(maxIndex,player)
        if maxIndex!=1 and maxIndex!=6 and maxIndex!=11 and maxIndex!=16 and maxIndex!=21:
            if self.getOccupantAt(maxIndex-1)==self.getOtherPlayer(player):
                #print str(maxIndex-1) +"----->"+ self.getOccupantAt(maxIndex-1)
                self.setOccupantAt(maxIndex-1,player)
               # print str(maxIndex-1) +"----->" +self.getOccupantAt(maxIndex-1)
        if maxIndex>5:
            if self.getOccupantAt(maxIndex-5)==self.getOtherPlayer(player):
               # print str(maxIndex-5) +"----->"+ self.getOccupantAt(maxIndex-5)
                self.setOccupantAt(maxIndex-5,player)
               # print str(maxIndex-5) +"----->"+ self.getOccupantAt(maxIndex-5)
        if maxIndex!=5 and maxIndex!=10 and maxIndex!=15 and maxIndex!=20 and maxIndex!=25:
            if self.getOccupantAt(maxIndex+1)==self.getOtherPlayer(player):
               # print str(maxIndex+1) +"----->"+ self.getOccupantAt(maxIndex+1)
                self.setOccupantAt(maxIndex+1,player)
                #print str(maxIndex+1) +"----->" +self.getOccupantAt(maxIndex+1)
        if maxIndex<21:
            if self.getOccupantAt(maxIndex+5)==self.getOtherPlayer(player):
               # print str(maxIndex+5) +"----->"+ self.getOccupantAt(maxIndex+5)
                self.setOccupantAt(maxIndex+5,player)
              #  print str(maxIndex+5) +"----->" +self.getOccupantAt(maxIndex+5)

        return maxIndex

    def EvalFunction(self,Player):
        PlayerVal=0
        OPlayerVal=0
        i=0
        while i<=25:
            if self.getOccupantAt(i)==Player:
                PlayerVal=PlayerVal+int(float(self.getValueAt(i)))
            elif self.getOccupantAt(i)==self.getOtherPlayer(Player):
                OPlayerVal=OPlayerVal+int(float(self.getValueAt(i)))
            i=i+1
        return PlayerVal-OPlayerVal


    def RaidAtIndex(self,index,Player,depth):
        val=0;
        if index!=1 and index!=6 and index!=11 and index!=16 and index!=21:
            if self.getOccupantAt(index-1)==self.getOtherPlayer(Player):
                val+=self.getValueAt(index-1)
                self.setOccupantAt(index-1,Player)

        if index>5:
          if self.getOccupantAt(index-5)==self.getOtherPlayer(Player):
                val+=self.getValueAt(index-5)
                self.setOccupantAt(index-5,Player)

        if index!=5 and index!=10 and index!=15 and index!=20 and index!=25:
           if self.getOccupantAt(index+1)==self.getOtherPlayer(Player):
                val+=self.getValueAt(index+1)
                self.setOccupantAt(index+1,Player)

        if index<21:
          if self.getOccupantAt(index+5)==self.getOtherPlayer(Player):
                val+=self.getValueAt(index+5)
                self.setOccupantAt(index+5,Player)
        return val

    def SneakAtIndex(self,index,Player,depth):
        self.setOccupantAt(index,Player)
        return self.getValueAt(index)

    def getRaidSneakPositions(self,index,Player,depth):
        val1=0
        val2=0
        val3=0
        val4=0

        if index!=1 and index!=6 and index!=11 and index!=16 and index!=21:
            if self.isSneakable(index-1)==True:
                self.SneakAtIndex(index-1,Player,depth)
            else:
                self.RaidAtIndex(index-1,Player,depth)
            depth=depth+1
            self.CopyShadowOccupantDict()
            val1=self.getPositions(self.getOtherPlayer(Player),depth)
            self.RestoreOccupantDict()
            depth=depth-1

        if index>5:
            if self.isSneakable(index-5)==True:
                self.SneakAtIndex(index-5,Player,depth)

            else:
                self.RaidAtIndex(index-5,Player,depth)
            depth=depth+1
            self.CopyShadowOccupantDict()
            val2=self.getPositions(self.getOtherPlayer(Player),depth)
            self.RestoreOccupantDict()
            depth=depth-1

        if index!=5 and index!=10 and index!=15 and index!=20 and index!=25:
            if self.isSneakable(index+1)==True:
                self.SneakAtIndex(index+1,Player,depth)
            else:
                self.RaidAtIndex(index+1,Player,depth)
            depth=depth+1
            self.CopyShadowOccupantDict()
            val3=self.getPositions(self.getOtherPlayer(Player),depth)
            self.RestoreOccupantDict()
            depth=depth-1

        if index<21:
            if self.isSneakable(index+5)==True:
                self.SneakAtIndex(index+5,Player,depth)
            else:
                self.RaidAtIndex(index+5,Player,depth)
            depth=depth+1
            self.CopyShadowOccupantDict()
            val4=self.getPositions(self.getOtherPlayer(Player),depth)
            self.RestoreOccupantDict()
            if depth%2==0:
                return max(val1,val2,val3,val4)
            else:
                return min(val1,val2,val3,val4)

    def getPositions(self,Player,depth):
        if depth>=self.maxDepth:
            return self.EvalFunction(Player)
        maxs=0
        mins=0
        val=0
        i=0
        while i<=25:
            if self.getOccupantAt(i)==Player:
               self.CopyShadowOccupantDict()
               val=self.getRaidSneakPositions(i,Player,depth)
               self.RestoreOccupantDict()
               if val>maxs:
                maxs=val
               if val<mins:
                mins=val
            i=i+1
        if depth==0:
            return maxs
        elif depth==1:
            return mins


    def MinMaxInit(self,index,Player,StartPlayer,RaidFlag,depth):
        if depth==0:
            return self.EvalFunction(Player)
        val=lval=rval=upval=downval=0
        depth=depth-1
        self.setOccupantAt(index,Player)
        if index!=1 and index!=6 and index!=11 and index!=16 and index!=21:

            if self.getOccupantAt(index-1)== "*":
                if depth==self.getGridCount()-1:
                    lval= self.getValueAt(index)+self.MinMaxInit(index-1,Player,StartPlayer,1,depth)
                else:
                    lval= self.getValueAt(index)+self.MinMaxInit(index-1,self.getOtherPlayer(Player),StartPlayer,1,depth)
        if index>5:
            if self.getOccupantAt(index-5)== "*":
                if depth==self.getGridCount()-1:
                    rval=self.getValueAt(index)+self.MinMaxInit(index-5,(Player),StartPlayer,1,depth)
                else:
                    rval=self.getValueAt(index)+self.MinMaxInit(index-5,self.getOtherPlayer(Player),StartPlayer,1,depth)


        if index!=5 and index!=10 and index!=15 and index!=20 and index!=25:
            if self.getOccupantAt(index+1)== "*":
                  if depth==self.getGridCount()-1:
                      upval=self.getValueAt(index)+self.MinMaxInit(index+1,(Player),StartPlayer,1,depth)
                  else:
                      upval=self.getValueAt(index)+self.MinMaxInit(index+1,self.getOtherPlayer(Player),StartPlayer,1,depth)

        if index<21:
            if self.getOccupantAt(index+5)== "*":
                if depth==self.getGridCount()-1:
                    downval=self.getValueAt(index)+self.MinMaxInit(index+5,(Player),StartPlayer,1,depth)
                else:
                    downval=self.getValueAt(index)+self.MinMaxInit(index+5,self.getOtherPlayer(Player),StartPlayer,1,depth)

        if lval == 0 and rval == 0 and upval == 0 and downval==0:
            print " "
        else:
            if Player==self.getOtherPlayer(StartPlayer):
                val=min(lval,rval,upval,downval)
            else:
                val=max(lval,rval,upval,downval)
        return val

        #print "called"

    def ParseGrid(self,Algo,Player):
        TestGrid.setGridCount()
        if Algo==2:
            self.GridMinMaxMaxValues.clear()

            if 'key' in self.GridMinMaxMaxValues:
                del self.GridMinMaxMaxValues['key']
           # max=self.getSneak_Raid_Value(Player,0,0)
            maxIndex=0
            val=0
            self.CopyOccupantDict()
            i=0
            while i<=25:
                if self.getOccupantAt(i)==Player:
                    print self.MinMaxInit(i,Player,Player,1,self.getGridCount())
                i=i+1
            i=1


'''TestGrid=Grid()
TestGrid.setGridCount()
print TestGrid.getPositions("O",0)
#TestGrid.ParseGrid(2,"X")'''



TestGrid=Grid()
TestGrid.setGridCount()
#print str(TestGrid.FileHandleObject.AlgoName)+" ------------- Player"
if TestGrid.FileHandleObject.AlgoName==1:
    TestGrid.StartGBFS(1,TestGrid.FileHandleObject.PlayerName)

f = open('next_state.txt','w')
f.write ("")
f.close()
f = open('next_state.txt','w')
i=1
while i<=25:
    f.write( TestGrid.getOccupantAt(i) + TestGrid.getOccupantAt(i+1)+TestGrid.getOccupantAt(i+2)+TestGrid.getOccupantAt(i+3)+TestGrid.getOccupantAt(i+4))
    f.write("\n")
    i=i+5
f.close() # you can omit in most cases as the destructor will call it










