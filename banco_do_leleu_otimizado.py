import os
import platform

saldo = 0

def limpar_terminal():
    # Limpa o terminal de acordo com o sistema operacional
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mensagem():
    # Exibe o menu de operações bancárias
    print(""" 
    =========BANCO DO LELÉU==========
    
      QUAL OPERAÇÃO DESEJA REALIZAR?
      
      1. SALDO
      2. SAQUE
      3. DEPÓSITO
      0. SAIR

    =================================
    """)

def consultar_saldo():
    # Consulta e exibe o saldo atual
    limpar_terminal()
    print(f"SEU SALDO É: {saldo:.2f}")
    input("Pressione Enter para voltar ao menu.")

def realizar_saque():
    # Realiza a operação de saque
    global saldo
    limpar_terminal()
    while True:
        try:
            valor_saque = float(input("QUAL VALOR DESEJA SACAR? "))
            if valor_saque <= 0:
                limpar_terminal()
                print("DIGITE UM VALOR POSITIVO")
            elif valor_saque > saldo:
                limpar_terminal()
                print("SALDO INSUFICIENTE PARA O SAQUE")
                input("Pressione Enter para voltar ao menu.")
                return
            else:
                saldo -= valor_saque
                limpar_terminal()
                print(f"SAQUE REALIZADO: {valor_saque:.2f}")
                input("Pressione Enter para voltar ao menu.")
                return
        except ValueError:
            limpar_terminal()
            print("Entrada inválida. Por favor, digite um número.")

def realizar_deposito():
    # Realiza a operação de depósito
    global saldo
    limpar_terminal()
    while True:
        try:
            valor_deposito = float(input("QUAL VALOR DESEJA DEPOSITAR EM SUA LELÉU CONTA? "))
            if valor_deposito <= 0:
                limpar_terminal()
                print("DIGITE UM VALOR POSITIVO")
            else:
                saldo += valor_deposito
                limpar_terminal()
                print(f"VALOR DEPOSITADO: {valor_deposito:.2f}")
                input("Pressione Enter para voltar ao menu.")
                return
        except ValueError:
            limpar_terminal()
            print("Entrada inválida. Por favor, digite um número.")

def sair():
    # Encerra o programa
    limpar_terminal()
    print("TENHA UM LELÉU DIA! :)\n.\n.\n.\n.")

def main():
    # Função principal que gerencia o menu de operações
    while True:
        limpar_terminal()
        mensagem()
        comando = input("Digite a opção desejada: ")
        if comando == '1':
            consultar_saldo()
        elif comando == '2':
            realizar_saque()
        elif comando == '3':
            realizar_deposito()
        elif comando == '0':
            sair()
            break
        else:
            print("Opção inválida. Por favor, digite um número válido.")

# Executa o programa
if __name__ == "__main__":
    main()