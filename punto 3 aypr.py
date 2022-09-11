def f(di):
    digito = len(str(di))
    acum = 0
    exponente = 0
    dr = 0
    d = 0
    f_d = 0
    w = 0
    q = 0
    while digito != 0:
        if digito % 2 == 1 and exponente > 0:
            exponente = digito - 1
            denominador = 10 ** exponente
            d = di // denominador
            f_d = 2 * d
            w = f_d // 10
            q = f_d % 10
            dr = w + q
            resta = digito * denominador
            di = di - resta
        elif digito % 2 == 0 and exponente > 0:
            exponente = digito - 1
            denominador = 10 ** exponente
            dr = di // denominador
            resta = digito * denominador
            di = di - resta
        digito = digito - 1
        acum = acum + dr
    if acum / 10 == acum // 10:
        return "el numero es valido", acum
    else:
        return "el numero no es valido", acum
def main():
    x=int(input("escriba su numero de cuenta"))
    resultado = f(x)
    print(resultado)
main()











