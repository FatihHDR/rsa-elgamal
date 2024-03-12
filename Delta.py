def modular_pow(base, exponent, modulus, multiplication_factor=1):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus

    print(f"[{base}^{exponent} mod {modulus}] . [{multiplication_factor}] mod {modulus} = ", end="")
    print(f"[", end="")

    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
            print(f"{base} * ", end="")
        exponent = exponent >> 1
        base = (base * base) % modulus
        print(f"{base} ] = [ ", end="")

    result = (result * multiplication_factor) % modulus
    print(f"{result} ]")
    print(f"{result} mod {modulus} = ", end="")
    return result % modulus

base = int(input("Masukkan nilai dasar: "))
exponent = int(input("Masukkan nilai eksponen: "))
multiplication_factor = int(input("Masukkan faktor perkalian: "))
modulus = int(input("Masukkan nilai modulo: "))

hasil = modular_pow(base, exponent, modulus, multiplication_factor)
print(f"{hasil} mod {modulus} = {hasil % modulus}")