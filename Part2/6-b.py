DListT={'2020-CS-20':[('DSA',2),('Algo',2.5),('AI',3)],'2020-CS-12':
            [('DSA',3),('Algo',3.5),('PF',2.8)],'2018-CS-36':
            [('OOP',3),('DB',3.5),('PF',2.8)]}
def withoutForLoop(RecordsList):
    highNumber = 0
    index = 0
    DKeys = list(RecordsList.keys())
    while index < len(RecordsList):
        if(RecordsList[DKeys[index]][0][1] > highNumber):
            highNumber = RecordsList[DKeys[index]][0][1]
        index = index + 1
    return highNumber

print(withoutForLoop(DListT))
input()
