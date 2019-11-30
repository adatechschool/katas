def fizzbuzz(nombre):

    if nombre % 15 == 0:
        return "fizzbuzz"

    if nombre % 3 == 0:
        return "fizz"

    if nombre % 5 == 0:
        return "buzz"

    return nombre
