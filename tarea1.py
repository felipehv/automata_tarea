
def q0(i, s):
    # print(s[i], "q0")
    # Verificar mayuscula al principio
    if s[i].isupper():
        return "q1", i+1
    else:
        return "qe",i

def q1(i,s):
    # print(s[i], "q1")
    # Verificar primera minuscula del apellido
    if s[i].islower():
        return "q2",i+1
    else:
        return "qe",i


def q2(i,s):
    # print(s[i], "q2")
    # Verificar el resto de las minusculas o pasar a segundo apellido o pasar a fecha
    if s[i].islower():
        return "q2",i+1

    elif s[i].isupper():
        return "q3",i+1

    elif s[i].isdigit():
        return "q4",i+1

    else:
        return "qe",i

def q3(i,s):
    # print(s[i], "q3")
    # Verificar mas mayusculas
    if s[i].isupper():
        return "q3",i+1

    elif s[i].isdigit():
        return "q4", i+1

    return

def q4(i,s):
    # print(s[i], "q4")
    # Verificar el año de nacimiento
    count = 0
    while count < 3:
        if s[i].isdigit():
            i += 1
            count += 1
        else:
            return "qe",i
    if s[i] == "@":
        return "q5",i+1
    return "qe",i

def q5(i,s):
    # print(s[i], "q5")
    mail = "iingen.unam.mx"
    for j in range(len(mail)):
        if i+j>len(s):
            return "qe",i
        if s[i+j] != mail[j]:
            return "qe",i

    return "qp",i

def test(string):
    state = "q0"
    i = 0
    state,i = states[state](i,string)

    while state != "qe" and state != "qp":
        state,i = states[state](i,string)

    if state == "qe":
        print("Failed on char #", str(i))
        return

    print("Passed")



states = {"q0": q0, "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5}


if __name__ == '__main__':
    with open("hola.txt", 'r') as reader:
        for string in reader:
            string.strip()
            print("------ Testing {}".format(string))
            test(string)










