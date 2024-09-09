felipe = 36
fabiana = 37
idade_felipe = felipe
idade_fabiana = fabiana
nota = 65

if idade_felipe > idade_fabiana:
    print("Felipe é mais velho que Fabiana, ele tem", felipe, "anos. E Fabiana tem",fabiana, "de idade.")

else:
    print("Fabiana é mais velha que Felipe, ela tem", fabiana, "anos. E Felipe tem", felipe, "de idade.")

if nota >= 90:
    print("Você tirou uma nota excelente")
elif nota >= 80:
    print("Você tirou uma nota muito boa.")
elif nota >=70:
    print("Você tirou uma nota boa.")
else:
    print("Você precisa se dedicar um pouco mais aos estudos.")