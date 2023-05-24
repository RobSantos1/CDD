from datetime import datetime
agora = datetime.now()
data_formatada=agora.strftime("%d/%m/%Y %H:%M:%S")


class contaBancaria:
    def __init__(self, numConta, nomeCliente, tipoConta, saldo, statusConta):
        self.numConta = numConta
        self.saldo = saldo
        self.statusConta = statusConta
        self.nomeCliente = nomeCliente
        self.tipoConta = tipoConta
        self.saldo = 0
        self.statusConta = False
        self.limiteCredito = 0
        self.limiteDisponivel = self.limiteCredito
        self.extrato = f"""Olá {self.nomeCliente}!
----SEU EXTRATO BANCARIO----
"""

    def ativarConta(self):
        if self.statusConta == False:
            self.statusConta = True
            print("Conta Ativa!")
        else:
            print("Sua conta já está ativa")


    def depositar(self,valorDeposito):
        if self.statusConta == True:
            if self.limiteDisponivel == self.limiteCredito:
                self.saldo += valorDeposito
                print("Valor Depositado: ", valorDeposito)
                self.extrato += f"Deposito no valor de R${valorDeposito} - {data_formatada}\n"

            elif self.limiteDisponivel < self.limiteCredito:
                valor_para_limite = self.limiteCredito - self.limiteDisponivel
                valor_para_saldo = valorDeposito - valor_para_limite
                self.limiteDisponivel += valor_para_limite
                self.saldo += valor_para_saldo
                self.extrato += f"Deposito no valor de R${valorDeposito} - {data_formatada}\n"
        else:
            print("Ative sua conta!")


    def sacar(self,valorSaque):
        if self.statusConta == True:
            if valorSaque <= self.saldo:
                self.saldo -= valorSaque
                self.extrato += f"Saque no valor de R${valorSaque} - {data_formatada}\n"

            elif valorSaque <= self.saldo + self.limiteCredito:
                self.saldo -= valorSaque
                self.limiteDisponivel += self.saldo
                self.saldo = 0
                self.extrato += f"Saque no valor de R${valorSaque} - {data_formatada}\n"
            else:
                print("Saldo insuficiente")
        else:
            print("Ative sua conta!")


    def ver_extrato(self):
        print(self.extrato)

    def desativar(self):
        if self.statusConta == True:
            if self.saldo == 0:
                self.statusConta = False
                print("Conta desativada!")
            else:
                print("Primeiro saque o seu saldo antes de desativar a conta!")
        else:
            print("Conta já desativada!")


    def ativarLimite(self, limiteCredito):
        self.limiteCredito = limiteCredito
        self.limiteDisponivel = limiteCredito

        if self.limiteCredito > 0:
            print("Limite de crédito ativo!")

    def desativarLimite(self, limiteCredito):
        if limiteCredito == 0:
            self.limiteDisponivel = limiteCredito
            self.limiteCredito = limiteCredito
        else:
            print("Limite não desativado!")

conta1 = contaBancaria(1, "Robson", "Conta Corrente", 0, False)

print(vars(conta1))

conta1.ativarConta()
conta1.depositar(1000)
conta1.sacar(200)
conta1.ver_extrato()
conta1.ativarLimite(100)
conta1.sacar(900)
conta1.ver_extrato()
conta1.depositar(100)
conta1.ver_extrato()
