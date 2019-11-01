def Chek_simvol(number):
    Number = str(number)
    if len(Number) == 5:
        for i in range(2):
            if Number[i] != Number[-(i + 1)]:
                return False
        return True
    else:
        for i in range(3):
            if Number[i] != Number[-(i + 1)]:
                return False
        return True


def Pol():
    Pol_numbers = []
    for i in range(100,1000):
        for j in range(100,1000):
            if Chek_simvol(i*j):
                Pol_numbers.append(i*j)
    return max(Pol_numbers)


print(Pol())
