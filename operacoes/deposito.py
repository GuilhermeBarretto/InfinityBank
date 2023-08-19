from banco import obterConta

def depositar(conta: int, valor: float) -> bool:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('Deposito Realizado com sucesso!')
    else:
        print("Cliente não encontrado!")