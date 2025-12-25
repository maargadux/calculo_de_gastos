#gerenciador financeiro/controlefinanceiro.py

salario = input('Informe o seu salario mensal(liquido): ')
adcgasto = input('Informe o quanto voce gasta com alimentacao: ')
transp = input('Informe o quanto voce gasta com transporte: ')
moradia = input('Informe o quanto voce gasta com moradia: ')
fatura_cartao = input('Informe o valor da sua fatura do cartao de credito: ')

total = float(adcgasto) + float(transp) + float(moradia) + float(fatura_cartao)
#de acordo com as informacoes adicionadas, o programa calcula o total de gastos planejados
print(f'O total de gastos em: R$ {total:.2f}')
if total > float(salario):
    print('Atenção: Seus gastos excedem o valor do seu salario. \nConsidere revisar seu orçamento para evitar problemas financeiros.')
    #dica para o usuario caso os gastos ultrapassem o limite recomendado
else:
    print(f'Sobrou {salario} - {total:.2f} = R$ {float(salario) - total:.2f} no seu orçamento mensal. Pode usar como quiser! \nRecomendamos poupar uma parte desse valor para emergências ou investimentos futuros.')
#mensagem positiva caso os gastos estejam dentro do limite do salario