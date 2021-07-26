#atributos: Nome, Fome, Saúde e Idade
#Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Existe mais uma informação que devemos levar em consideração, o Humor do nosso 
# tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja,
# um campo calculado, então não devemos criar um atributo para armazenar
# esta informação por que ela pode ser calculada a qualquer momento.

import os

class Bichinho: 
    def __init__(self,nome,fome,saude,idade,humor) :
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        self.__humor = humor

    def status(self):
        print("Nome: {}\nFome: {}%\nSaúde: {}%\nidade: {}\nHumor: {}%".format(self.__nome,self.__fome,self.__saude,self.__idade,self.__humor))

    def alterar_nome(self):
        self.__nome = input("Digite o novo nome do seu tamagushi: ")

    def fome(self):
        self.__fome -= 5

    def saude(self):
        self.__saude -= 5

    def idade(self):
        self.__idade += 1

    def humor(self):
        self.__humor -= 5
    
    def falta_de_humor(self):
        if(self.__saude or self.__fome <70):
            self.__humor -=10

    #cuidados
    def morte(self):
        condição = self.__fome + self.__saude
        return condição

    def alimentar(self):
        self.__fome+=5
    def medicar(self):
        self.__saude+=5
    def brincar(self):
        self.__humor+=10

    #menssagens

    def menssagem_humor(self):

        if(self.__humor>50):
            print("hoje o seu bichinho está muito feliz")
            print("escolha o que fazer com ele")
        
        elif(self.__humor<50):
            print("hoje o seu bichinho meio bravo")
            print("escolha o que fazer com ele")

        elif(self.__humor<20):
            print("hoje o seu bichinho muito triste")
            print("escolha o que fazer com ele")
        


#inicio da programação
#tamagushi

print("Bem vindo ao tamagushi\nSeu bichinho virtual")

#tamagushi inicio
nome = input("Escolha o nome do seu bichinho: ")
fome = 100
saude = 100
idade = 0
humor = 100

tamagushi = Bichinho(nome,fome,saude,idade,humor)

while (tamagushi.morte() > 140):

    tamagushi.status()
    tamagushi.humor()
    tamagushi.saude()
    tamagushi.fome()
    tamagushi.menssagem_humor()
    tamagushi.morte()
    tamagushi.idade()

    print("\n1 - Alimentar")
    print("2 - Medicar")
    print("3 - Brincar")
    print("4 - Alterar nome:")

    opcao = int(input("Escolha a opção: "))

    if(opcao == 1):
        tamagushi.alimentar()
    elif(opcao == 2 ):
        tamagushi.medicar()
    elif (opcao == 3):
        tamagushi.brincar()
    elif (opcao == 4):
        tamagushi.alterar_nome()

    os.system("cls")


print("Seu bixinho faleceu!!!!!")
