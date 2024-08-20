from frota import *

def operar_carro(carro : Carro):

    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade em Km/H: "))
        t = float(input("Informe o tempo em Horas: "))
        carro.acelerar(v, t)

    print(carro)

if __name__ == "__main__":

    print('\nPrimeiro carro')
    nm_modelo = "X"
    nm_marca = "X"
    nm_cor = "X"
    litros = 100000
    consumo = 1

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, True, litros, consumo)

    print('Segundo carro')
    nm_modelo = "Z"
    nm_marca = "Z"
    nm_cor = "Z"
    litros = 100000
    consumo = 1

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, True, litros, consumo)

    '''
    Controlando o carro até ele atingir 300 Km
    '''
    while carro1.odometro < 300 and carro2.odometro < 300 and (carro1.tanque < 0 or carro2.tanque):
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Qual carro [1 ou 2] : "))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

            print('\nInfos atuais do carro')

        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1 and carro2)
    print('Parar para trocar óleo!!!')
