from src.toolkit.errors import CalcErrors

supported_operations=[ "**", "*", "/", "//", "%", "+", "-"]
def str_sep(inpt_str: str, digit_round:int) -> tuple[list, list]:
    """Tokenizer"""
    while inpt_str.count(" ")>0:
        inpt_str=inpt_str.replace(" ", "")
    while inpt_str.count("-(")>0:
        inpt_str=inpt_str.replace("-(", "-1*(")
    numb = ""
    numbs=[]
    operations=[]
    l=0

    if ")" in inpt_str:
        inpt_str=brackets_calculation(inpt_str, digit_round)

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

    flag = 0
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
                flag=1
            if inpt_str[l] in "*/" and inpt_str[l]==inpt_str[l+1]:
                operations.append(inpt_str[l]*2)
                l+=1
                if inpt_str[l] in "*/" and inpt_str[l+1]=="-":
                    numb="-"
                    l+=1

            elif flag==0:
                operations.append(inpt_str[l])
            l+=1
        else:
            raise CalcErrors("Unknown digit/operation")
    numbs.append(float(numb))
    return numbs,operations

# calculating brackets
def brackets_calculation(inpt_str:str, digit_round:int) -> str:
    back_index=inpt_str.index(")")
    front_index=back_index-1
    while inpt_str[front_index]!= "(":
        front_index-=1

    return inpt_str[:front_index] + str(calc(inpt_str[front_index+1:back_index], digit_round)) + inpt_str[back_index+1::]

# calculating each operation
def opcalculate(numbs: list, operations: list, operation: str) -> tuple[list, list]:
    while operations.count(operation)!=0:
        solving_index = operations.index(operation)
        if operations[solving_index]=="**":
            numbs[solving_index] **= numbs[solving_index + 1]
        elif operations[solving_index]=="*":
            numbs[solving_index] *= numbs[solving_index + 1]
        elif operations[solving_index]=="/":
            if numbs[solving_index + 1] !=0:
                numbs[solving_index] /= numbs[solving_index + 1]
            else:
                raise CalcErrors("Zero division")
        elif operations[solving_index]=="//":
            if numbs[solving_index + 1] != 0:
                numbs[solving_index] //= numbs[solving_index + 1]
            else:
                raise CalcErrors("Zero division")
        elif operations[solving_index]=="%":
            if numbs[solving_index + 1] != 0:
                numbs[solving_index] %= numbs[solving_index + 1]
            else:
                raise CalcErrors("Zero division")
        elif operations[solving_index]=="+":
            numbs[solving_index] += numbs[solving_index + 1]
        elif operations[solving_index]=="-":
            numbs[solving_index] -= numbs[solving_index + 1]

        numbs.pop(solving_index + 1)
        operations.pop(solving_index)
    return numbs, operations

# main calculating func
def calc(inp_tstr: str, digit_round: int) -> float :
    try:
        numbs,operations = str_sep(inp_tstr, digit_round)
    except:
        raise CalcErrors("Unknown input symbol")
    for operation in supported_operations:
        if operation.count(operation)!=0:
            opcalculate(numbs, operations, operation)
    if numbs[0]==int(numbs[0]):
        return int(numbs[0])
    else:
        return round(numbs[0], digit_round)
