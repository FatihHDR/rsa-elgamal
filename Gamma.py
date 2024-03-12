def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus

    print(f"{base} ^ {exponent} mod {modulus} =")
    print(f"[ {base} ^ {exponent//2} mod {modulus} ] = [", end="")

    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
            print(f"{base} * ", end="")
        exponent = exponent >> 1
        base = (base * base) % modulus
        print(f"{base} ] = [ ", end="")

    print(f"{result} ]")
    print(f"{result} mod {modulus} = ", end="")
    return result % modulus

base = int(input("Masukkan nilai dasar: "))
exponent = int(input("Masukkan nilai eksponen: "))
modulus = int(input("Masukkan nilai modulo: "))

hasil = modular_pow(base, exponent, modulus)
print(f"{hasil}")