def check(x, y, oper):
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7
    if (x == 0 or y == 0) and oper in "*+-":
        msg += msg_8
    if msg:
        print(msg_9 + msg)


def is_one_digit(v):
    if v.is_integer() and (-10 < v < 10):
        return True
    else:
        return False


def data_collection(memory=0):
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n):"
    msg_5 = "Do you want to continue calculations? (y / n):"
    msg_10 = "Are you sure? It is only one digit! (y / n)"
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
    result = 0
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        return data_collection(memory)
    if oper not in "+-*/":
        print(msg_2)
        return data_collection(memory)
    check(x, y, oper)
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0:
        result = x / y
    else:
        print(msg_3)
        return data_collection(memory)
    print(result)
    loop = True
    while loop:
        print(msg_4)
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                message_index = 10
                while True:
                    print(locals()["msg_" + str(message_index)])
                    answer = input()
                    if answer == "y" and message_index < 12:
                        message_index += 1
                        continue
                    elif answer == "y":
                        memory = result
                        loop = False
                        break
                    elif answer == "n":
                        loop = False
                        break
                    else:
                        continue
            else:
                memory = result
                loop = False
                break
        elif answer == "n":
            loop = False
            break
        else:
            continue
    while True:
        print(msg_5)
        answer = input()
        if answer == "y":
            return data_collection(memory)
        elif answer == "n":
            break
        else:
            continue
data_collection()