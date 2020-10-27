# Called Function
def convertToLowerCase(StringsList):
    TempList=[string.lower() for string in StringsList if len(string)>5]
    return TempList

# calling function
arr_list = ["KHAnsa","FARIA","MANAHIL","EISHA","KhadiJa"]
print(convertToLowerCase(arr_list))
x = input()

