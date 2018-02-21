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
		
def calcular_sal_liq():


