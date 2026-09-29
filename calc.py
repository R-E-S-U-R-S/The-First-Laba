from errors import calc_error_unknown_input_simbol

# функция для разделения и преобразования начальной строки
def str_sep(inptstr: str):
    while inptstr.count(" ")>0:
        inptstr=inptstr.replace(" ", "")
    numb = ""
    numbs=[]
    operations=[]
    l=0
    if inptstr[0] == "-":
        numb+=inptstr[0]
        inptstr=inptstr[1:]
    elif inptstr[0] == "+":
        inptstr=inptstr[1:]

    while l != len(inptstr):
        if inptstr[l] in "0123456789":
            numb+=inptstr[l]
            l+=1
        elif inptstr[l] in "()":
            operations.append(inptstr[l])
            l+=1
        elif inptstr[l] in "+-*/":
            numbs.append(int(numb))
            numb = ""
            operations.append(inptstr[l])
            l+=1
        else:
            calc_error_unknown_input_simbol()
            break
    numbs.append(int(numb))
    return numbs,operations

# провожу вычисления для каждой функции
def opcalculate(numbs: list, operations: list, operation: str) -> tuple[list, list]:
    while operations.count(operation)!=0:
        multiply_index = operations.index(operation)
        if operations[multiply_index]=="*":
            numbs[multiply_index] *= numbs[multiply_index + 1]
        elif operations[multiply_index]=="/":
            numbs[multiply_index] /= numbs[multiply_index + 1]
        elif operations[multiply_index]=="+":
            numbs[multiply_index] += numbs[multiply_index + 1]
        elif operations[multiply_index]=="-":
            numbs[multiply_index] -= numbs[multiply_index + 1]
        numbs.pop(multiply_index + 1)
        operations.pop(multiply_index)
    return numbs, operations

# вызываю функции для вычисления
def calc(inptstr: str) :
    numbs,operations = str_sep(inptstr)
    for operation in "*/+-":
        if operation.count(operation)!=0:
            opcalculate(numbs, operations, operation)
    return numbs[0]

print(calc(input("Input str: ")))