from src.toolkit.errors import CalcErrors

supported_operations=[ "**", "*", "/", "//", "%", "+", "-"]
def str_sep(inpt_str: str) -> tuple[list, list]:
    """Tokenizer"""
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
    elif inpt_str[0] == "*":
        inpt_str= inpt_str[1:]
    elif inpt_str[0] == "/":
        inpt_str= inpt_str[1:]
    elif inpt_str[0] == "/":
        inpt_str= inpt_str[1:]
    elif inpt_str[0] == "**":
        inpt_str= inpt_str[1:]
    elif inpt_str[0] == "%":
        inpt_str= inpt_str[1:]

    while l != len(inpt_str):
        if inpt_str[l] in "0123456789,.":
            numb+=inpt_str[l]
            l+=1
        elif inpt_str[l] in supported_operations:
            numbs.append(float(numb))
            numb = ""
            if inpt_str[l] in "*/" and inpt_str[l + 1] == "-":
                operations.append(inpt_str[l])
                numb = "-"
                l += 1
            if inpt_str[l] in "*/" and inpt_str[l]==inpt_str[l+1]:
                operations.append(inpt_str[l]*2)
                l+=1
                if inpt_str[l] in "*/" and inpt_str[l+1]=="-":
                    numb="-"
                    l+=1
            else:
                operations.append(inpt_str[l])

            l+=1
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
        if operations[multiply_index]=="**":
            numbs[multiply_index] **= numbs[multiply_index + 1]
        elif operations[multiply_index]=="*":
            numbs[multiply_index] *= numbs[multiply_index + 1]
        elif operations[multiply_index]=="/":
            numbs[multiply_index] /= numbs[multiply_index + 1]
        elif operations[multiply_index]=="//":
            numbs[multiply_index] //= numbs[multiply_index + 1]
        elif operations[multiply_index]=="%":
            numbs[multiply_index] %= numbs[multiply_index + 1]
        elif operations[multiply_index]=="+":
            numbs[multiply_index] += numbs[multiply_index + 1]
        elif operations[multiply_index]=="-":
            numbs[multiply_index] -= numbs[multiply_index + 1]

        numbs.pop(multiply_index + 1)
        operations.pop(multiply_index)
    return numbs, operations

# main calculating func
def calc(inp_tstr: str, digit_round: int) -> float :
    try:
        numbs,operations = str_sep(inp_tstr)
    except:
        raise CalcErrors("Unknown input symbol")
    for operation in supported_operations:
        if operation.count(operation)!=0:
            opcalculate(numbs, operations, operation)
    if numbs[0]==int(numbs[0]):
        return int(numbs[0])
    else:
        return round(numbs[0], digit_round)

