di = input("")
digito = len(str(di))
exponente = 0
dr = 0
w= 0
f_d = 0
q = 0
d = 0
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
print (dr)


