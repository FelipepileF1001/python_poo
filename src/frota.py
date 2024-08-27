class Carro:
    modelo: str
    marca: str
    cor: str
    __odometro: 0.0
    __motor_on: False
    __tanque: float
    __consumo: float

    def __init__(self, modelo: str, marca: str, cor: str,
                       odometro: float, motor: bool, tanque: float, consumo: float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor
        self.__tanque = tanque
        self.__consumo = consumo

    def ligar(self):
        if not self.__motor_on and self.__tanque > 0:
            self.__motor_on = True
        else:
            raise Exception("Erro: Motor já ligado, ou o tanque tá vazio")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on and self.__tanque > 0:
            km = velocidade * tempo
            litros = km/self.__consumo
            if self.__tanque >= litros:
                self.__odometro += km
                self.__tanque -= litros
            else:
                km = self.__tanque*self.__consumo
                self.__odometro += km
                self.__tanque = 0
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")
    def get_odometro(self):
        return self.__odometro
    def get_tanque(self):
        return self.__tanque

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'consumo medio {self.__consumo} Km/L, '
                f'tanque {self.__tanque} L')
        return info
    def __repr__(self):
        return f'Carro (Modelo = {self.modelo}, Marca = {self.marca}, ' \
                f'Cor = {self.cor}\n{self.__odometro} Km, ' \
                f'Consumo = {self.__consumo} Km/L, ' \
                f'tanque {self.__tanque})'
