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
                return self.getNextMoveSum(index,index,GridObj,depth+1,player)+self.getNextMoveSum(index,index-1,GridObj,depth+1,player)+self.getNextMoveSum(index,index+1,GridObj,depth+1,player)+self.getNextMoveSum(index,index+5,GridObj,depth+1,player)+self.getNextMoveSum(index,index-5,GridObj,depth+1,player)
                #return self.getNextMoveSum(index,index,GridObj,depth+1,player)
            else
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
    GridIndexDict=dict()
    GBFS=BestFirstSearch()
    GridMaxValues=dict()
    NextXPos=0;
    NextOPos=0;
    GridCount=0;
    GridValueDict[1] = 8
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
    GridOccupantDict[25] = "X"

    #def InitGrids(self,**ValueDict,**OccupantDict,**IndexDict):
     #   self.GridValueDict=ValueDict.copy()
      #  self.GridOccupantDict=OccupantDict.copy()
       # self.GridIndexDict=IndexDict.copy()

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
            if self.getOccupantAt(index-1)=="*":
                val1=True
            else:
                val1=False
        if index>5:
            if self.getOccupantAt(index-5)=="*":
                val2=True
            else:
                val2=False
        if index!=5 and index!=10 and index!=15 and index!=20 and index!=25:
            if self.getOccupantAt(index+1)=="*":
                val3=True
            else:
                val3=False
        if index<21:
            if self.getOccupantAt(index+5)=="*":
                val4=True
            else:
                val4=False
        return (val1 & val2 & val3 & val4)

    def getSneak_Raid_Value(self,player,RaidMax,RaidIndex):
        i=1
        maxm=0
        maxIndex=0
        while(i<=25):
            if maxm < self.getValueAt(i) and self.getOccupantAt(i)=="*" and self.isSneakable(i)==True:
                maxm= self.getValueAt(i)
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
        print str(maxIndex) + " --- > " + str(max)

        self.setOccupantAt(maxIndex,player)
        if maxIndex!=1 and maxIndex!=6 and maxIndex!=11 and maxIndex!=16 and maxIndex!=21:
            if self.getOccupantAt(maxIndex-1)==self.getOtherPlayer(player):
                print str(maxIndex-1) +"----->"+ self.getOccupantAt(maxIndex-1)
                self.setOccupantAt(maxIndex-1,player)
                print str(maxIndex-1) +"----->" +self.getOccupantAt(maxIndex-1)
        if maxIndex>5:
            if self.getOccupantAt(maxIndex-5)==self.getOtherPlayer(player):
                print str(maxIndex-5) +"----->"+ self.getOccupantAt(maxIndex-5)
                self.setOccupantAt(maxIndex-5,player)
                print str(maxIndex-5) +"----->"+ self.getOccupantAt(maxIndex-5)
        if maxIndex!=5 and maxIndex!=10 and maxIndex!=15 and maxIndex!=20 and maxIndex!=25:
            if self.getOccupantAt(maxIndex+1)==self.getOtherPlayer(player):
                print str(maxIndex+1) +"----->"+ self.getOccupantAt(maxIndex+1)
                self.setOccupantAt(maxIndex+1,player)
                print str(maxIndex+1) +"----->" +self.getOccupantAt(maxIndex+1)
        if maxIndex<21:
            if self.getOccupantAt(maxIndex+5)==self.getOtherPlayer(player):
                print str(maxIndex+5) +"----->"+ self.getOccupantAt(maxIndex+5)
                self.setOccupantAt(maxIndex+5,player)
                print str(maxIndex+5) +"----->" +self.getOccupantAt(maxIndex+5)

        return maxIndex





TestGrid=Grid()
TestGrid.setGridCount()
print TestGrid.StartGBFS(1,"O")
print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")
print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")
print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")
print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")
print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")
print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")
print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")

print TestGrid.StartGBFS(1,"X")
print TestGrid.StartGBFS(1,"O")











