DListT={'2020-CS-01':[('DSA',3),('Algo',2.5),('AI',3)],
            '2020-CS-20':[('LA',3),('Algo',3.5),('PF',2.8)],
            '2020-CS-12':[('OOP',3),('DB',3.5),('PF',2.8)]}

def withForLoop(RecordsList):
    GPAList = []
    
    for Student in RecordsList.values():
        GPA = 0
        for subj in Student:
            GPA  = GPA + subj[1] * 3 
        GPA = GPA / (len(Student) * 3)
        GPAList.append(GPA)
    return GPAList

def withoutForLoop(RecordsList):
    GPAList = []
    GPA = 0
    a = 0
    StudentKeyDict = list(RecordsList.keys())
    while a < len(RecordsList):
        b = 0
        while b < len(RecordsList[StudentKeyDict[a]]):
            GPA = GPA + RecordsList[StudentKeyDict[a]][b][1] * 3
            b = b + 1
        GPA = GPA / (len(RecordsList[StudentKeyDict[a]]) * 3)
        GPAList.append(GPA)
        GPA = 0
        a = a + 1
    return GPAList

print(withForLoop(DListT))
print(withoutForLoop(DListT))
x=input()
