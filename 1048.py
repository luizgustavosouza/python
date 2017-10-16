salario = float(input())

if salario>=0.00 and salario<=400.00:
    print("Novo salario: ", "%0.2f"%(salario+(salario*0.15)), "\n", "Reajuste ganho: ", "%0.2f"%(salario*0.15), "\n", "Em percentual: 15%")
elif salario>=401.00 and salario<=800.00:
    print("Novo salario: ", "%0.2f"%(salario+(salario*0.12)), "\n", "Reajuste ganho: ", "%0.2f"%(salario * 0.12), "\n", "Em percentual: 12%")
elif salario>=800.01 and salario<=1200.00:
    print("Novo salario: ", "%0.2f"%(salario+(salario*0.10)), "\n", "Reajuste ganho: ", "%0.2f"%(salario * 0.10), "\n", "Em percentual: 10%")
elif salario>=1200.01 and salario<=2000.00:
    print("Novo salario: ", "%0.2f"%(salario+(salario*0.07)), "\n", "Reajuste ganho: ", "%0.2f"%(salario * 0.07), "\n", "Em percentual: 7%")
else:
    if salario>2000.00:
        print("Novo salario: ", "%0.2f"%(salario + (salario * 0.04)), "\n", "Reajuste ganho: ", "%0.2f"%(salario * 0.04), "\n","Em percentual: 4%")

