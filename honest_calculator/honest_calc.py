# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

end = False
memory = 0


def check_value(number):
    try:
        float(number)
        result = True
    except ValueError:
        result = False
    return result


def is_one_digit(n):
    try:
        if -10 < float(n) < 10 and float(n).is_integer():
            return True
    except ValueError:
        return False

    return False


def check(num1, num2, oper):
    msg = ""
    if is_one_digit(num1) and is_one_digit(num2):
        msg += msg_6

    if (float(num1) == 1 or float(num2) == 1) and oper == '*':
        msg += msg_7

    if (float(num1) == 0 or float(num2) == 0) and (oper == '*' or oper == '+' or oper == '-'):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg

    print(msg)


def get_result(num1, oper, num2):
    n1 = float(num1)
    n2 = float(num2)
    if oper == '+':
        r = n1 + n2
    elif oper == '-':
        r = n1 - n2
    elif oper == '*':
        r = n1 * n2
    elif oper == '/':
        r = n1 / n2

    return r


def get_message(index):
    if index == 10:
        return msg_10
    elif index == 11:
        return msg_11
    elif index == 12:
        return msg_12


def additiona_verification():
    global memory
    msg_index = 0
    finish = False
    if is_one_digit(result):
        msg_index = 10
        while not finish:
            print(get_message(msg_index))
            answer = input()
            if answer == 'y':
                if msg_index < 12:
                    msg_index += 1
                else:
                    finish = True
                    memory = result
            else:
                finish = True
    else:
        memory = result


while not end:
    print(msg_0)
    calc = input().split(' ')

    if calc[0] == 'M':
        calc[0] = str(memory)

    if calc[2] == 'M':
        calc[2] = str(memory)

    if not check_value(calc[0]) or not check_value(calc[2]):
        print(msg_1)
    elif calc[1] in ('+', '-', '*', '/'):
        check(calc[0], calc[2], calc[1])
        if calc[1] == '/' and calc[2] == '0':
            print(msg_3)
        else:
            result = get_result(calc[0], calc[1], calc[2])
            print(result)
            print(msg_4)
            answer = input()
            if answer == 'y':
                additiona_verification()
                print(msg_5)
                answer = input()
                if answer == 'y':
                    continue
                else:
                    end = True
            else:
                print(msg_5)
                answer = input()
                if answer == 'y':
                    continue
                else:
                    end = True

    else:
        print(msg_2)
