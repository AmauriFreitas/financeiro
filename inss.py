def calcula_inss(salario):
	if salario <= 1000.0:
		return 0.0
	if salario <= 2000.0:
		return salario * 0.1
	else:
		return salario * 0.2
		

def calcular_ir(salario_liq):
	if salario_liq <= 1400.0:
		return 0.0
	elif salario_liq <= 2500.0:
		return salario_liq * 0.12
	elif salario_liq <= 5000.0:
		return salario_liq * 0.2
	else:
		return salario_liq * 0.27
		
def calcular_sal_liq(salario, num_dep):
	
	desconto_dependente = num_dep * 100
	salario_base_ir = salario - calcula_inss(salario) - desconto_dependente
	salario_liq = salario_base_ir - calcular_ir(salario_base_ir)

	return salario_liq 

salario_bruto = 3000.0
num_dependentes = 2

print("salario bruto de:", salario_bruto) 
print("salario liquido de: ", calcular_sal_liq(salario_bruto, num_dependentes))


