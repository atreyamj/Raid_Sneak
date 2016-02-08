'''
Common workspace for us to collab
'''
////Reading from File


import collections

input_file_handle = open('foo.txt','r')
AlgoName=0
PlayerName = 0
CutOff = 0
GameBoard = dict()
CurrentBoard= dict()



def read_game(file_handle):
    global AlgoName,PlayerName,CutOff,GameBoard,CurrentBoard

    AlgoName = int(file_handle.readline().rstrip('\n'))
    PlayerName = str(file_handle.readline().rstrip('\n'))
    CutOff=int(file_handle.readline().rstrip('\n'))
    myList1=file_handle.readline().rstrip('\n').split(' ')
    for x in range(0,5):
        GameBoard[x]=myList1[x]

    myList2=file_handle.readline().rstrip('\n').split(' ')
    for x in range(0,5):
        GameBoard[x+5]=myList2[x]

    myList3=file_handle.readline().rstrip('\n').split(' ')
    for x in range(0,5):
        GameBoard[x+10]=myList3[x]

    myList4=file_handle.readline().rstrip('\n').split(' ')
    for x in range(0,5):
        GameBoard[x+15]=myList4[x]

    myList5=file_handle.readline().rstrip('\n').split(' ')
    for x in range(0,5):
        GameBoard[x+20]=myList5[x]

    mylist6=file_handle.readline().rstrip('\n').split(' ')
    stringtest= str(mylist6)
    for x in range(2,7):
        CurrentBoard[x-2]=stringtest[x]

    mylist7=file_handle.readline().rstrip('\n').split(' ')
    stringtest= str(mylist7)
    for x in range(2,7):
        CurrentBoard[x+3]=stringtest[x]

    mylist8=file_handle.readline().rstrip('\n').split(' ')
    stringtest= str(mylist8)
    for x in range(2,7):
        CurrentBoard[x+8]=stringtest[x]

    mylist9=file_handle.readline().rstrip('\n').split(' ')
    stringtest= str(mylist9)
    for x in range(2,7):
        CurrentBoard[x+13]=stringtest[x]

    mylist10=file_handle.readline().rstrip('\n').split(' ')
    stringtest= str(mylist10)
    for x in range(2,7):
        CurrentBoard[x+18]=stringtest[x]






    print AlgoName
    print PlayerName
    print CutOff





    GridValueDict=dict()
    GridValueDict=GameBoard

    print GridValueDict

    GridOccupantDict=dict()
    GridOccupantDict=CurrentBoard
    print GridOccupantDict

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

    print GridIndexDict






def main():

    input_file_handle = open('foo.txt','r')
    read_game(input_file_handle)




if __name__ == '__main__':
	main()
