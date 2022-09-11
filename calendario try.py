
import calendar
def dia_nacimiento(dia,mes,año):
    año = int(mes)
    mes = int(mes)
    dia = int(dia)
    cod_año= 0

    cod_mes = 0

    dia_semana = 0
    if año in range(1900,1999):
        cod_año = 0
    elif año in range(2000,2099):
        cod_año = 6
    else:
        print("sapo")
    if mes==1:
        cod_mes = 0
        mes = "enero "
    elif mes==2:
        cod_mes = 3
        mes ="febrero"
    elif mes==3:
        cod_mes = 3
        mes = "marzo"
    elif mes==4:
        cod_mes = 6
        mes = "abril"
    elif mes==5:
        cod_mes = 1
        mes= "mayo"
    elif mes==6:
        cod_mes = 4
        mes = "junio"
    elif mes==7:
        cod_mes = 6
        mes = "julio"
    elif mes==8:
        cod_mes = 2
        mes = "agosto"
    elif mes==9:
        cod_mes = 5
        mes = "septiembre"
    elif mes==10:
        cod_mes =0
        mes = "octubre"
    elif mes==11:
        cod_mes = 3
        mes = "noviembre"
    elif mes==12:
        cod_mes = 5
        mes = "diciembre"
    den_1 = año / 4
    numerador = dia+cod_mes+año+den_1+cod_año
    sapo= int(numerador%7)
    if sapo == 0:
        dia_semana= "domingo"
    elif sapo == 1:
        dia_semana="lunes"
    elif sapo == 2:
        dia_semana = "martes"
    elif sapo ==3:
        dia_semana= "miercoles"
    elif sapo == 4:
        dia_semana = "jueves"
    elif sapo == 5:
            dia_semana = "viernes"
    elif sapo == 6:
        dia_semana = "sabado"

    return "nacio el dia",dia_semana,"de",mes,"del año",año
def calendario(mes,año):
    return calendar.month(año,mes)
def main():
    dia = input("ingrese el dia en el qeu nacio")
    mes = input("Ingrese el mes en el que nacio")
    año = input("ingrese el año en el que nacio")
    resultado = input("1,2")
    if resultado == 1:
        resultado = dia_nacimiento(dia,mes,año)
    else:
        resultado = calendario(mes,año)
    print(resultado)
main()
