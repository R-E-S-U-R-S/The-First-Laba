from src.toolkit.errors import calc_error_unknown_input_simbol

# tokenizer
def str_sep(inpt_str: str) -> tuple[list, list]:
    while inpt_str.count(" ")>0:
        inpt_str=inpt_str.replace(" ", "")
    numb = ""
    numbs=[]
    operations=[]
    l=0

    if ")" in inpt_str:
        inpt_str=brackets_calculation(inpt_str)

    if inpt_str[0] == "-":
        numb+=inpt_str[0]
        inpt_str= inpt_str[1:]
    elif inpt_str[0] == "+":
        inpt_str= inpt_str[1:]

    while l != len(inpt_str):
        if inpt_str[l] in "0123456789,.":
            numb+=inpt_str[l]
            l+=1
        elif inpt_str[l] in "+-*/":
            numbs.append(float(numb))
            numb = ""
            operations.append(inpt_str[l])
            l+=1
        else:
            return None
    numbs.append(float(numb))
    return numbs,operations

# calculating brackets
def brackets_calculation(inpt_str:str) -> str:
    back_index=inpt_str.index(")")
    front_index=back_index-1
    while inpt_str[front_index]!= "(":
        front_index-=1


    return inpt_str[:front_index] + str(calc(inpt_str[front_index+1:back_index])) + inpt_str[back_index+1::]

# calculating each operation
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

# main calculating func
def calc(inptstr: str) -> float :
    try:
        numbs,operations = str_sep(inptstr)
    except:
        return calc_error_unknown_input_simbol()
    for operation in "*/+-":
        if operation.count(operation)!=0:
            opcalculate(numbs, operations, operation)
    if numbs[0]==int(numbs[0]):
        return int(numbs[0])
    else:
        return numbs[0]