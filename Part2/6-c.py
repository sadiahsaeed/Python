DListT={'2020-CS-01':[('DSA',3),('Algo',2.5),('AI',3)],
            '2020-CS-20':[('LA',3),('Algo',3.5),('PF',2.8)],
            '2020-CS-12':[('OOP',3),('DB',3.5),('PF',2.8)]}

def withForLoop(record):
    count = 0
    for x in record:
        y = record[x]
        for n in y:
            if n[0] == 'AI' and n[1] < 2.5:
                count = count + 1
    return(count)

def withoutForLoop(record):
    count = 0
    x = 0
    StudentKeyDict = list(record.keys())
    while x < len(record):
        y = 0
        while y < 3:
            if(record[StudentKeyDict[x]][y][0] == 'AI' and record[StudentKeyDict[x]][y][1] <
               2.5 ):
                count = count + 1
            y = y + 1
        x = x + 1
    return (count)

print(withForLoop(DListT))
print(withoutForLoop(DListT))
x=input()
