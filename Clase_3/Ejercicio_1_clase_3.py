
rut= "30686957"
rut_invertido= (lambda x: x[::-1])(rut)
serie = [2,3,4,5,6,7,2,3]
suma = 0
for i in range(len(rut)):
    valor = serie[i] * int(rut_invertido[i])
    suma = suma + valor

resto = suma % 11
digito_verificador = 11 - resto

if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = "K"
else:
    digito_verificador = digito_verificador
print(digito_verificador)



    # lambda rut: "0" if (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)==11) \
    # else ("K" if (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)==10) \
    #             else (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)))("10000000")

print((
    lambda rut: "0" if (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)==11) \
    else ("K" if (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)==10) \
                else (11-((int(rut[-1])*2+int(rut[-2])*3+int(rut[-3])*4+int(rut[-4])*5+int(rut[-5])*6+int(rut[-6])*7+int(rut[-7])*2+int(rut[-8])*3)%11)))
)("10000000")
)