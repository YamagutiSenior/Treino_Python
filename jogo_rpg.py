import random

# Classe para o personagem principal
class Personagem:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp # Pontos de vida
        self.ataque = ataque

    def atacar(self, inimigo):
        dano = random.randint(1, self.ataque) # Causa dano aleatorio baseado no ataque
        inimigo.hp -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano !")
        if inimigo.hp <= 0:
            print(f"{inimigo.nome} foi derrotado!")
    
    def esta_vivo(self):
        return self.hp > 0

# Classe para os monstros
class Monstro:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
    
    def atacar (self, personagem):
        dano = random.randint(1, self.ataque)
        personagem.hp -= dano
        print (f"{self.nome} atacou {personagem.nome} e causou {dano} de dano!")
        if personagem.hp <= 0:
            print(F"{personagem.nome} foi derrotado!")

    def esta_vivo(self):
        return self.hp > 0
    

# Função principal do jogo
def jogo():
    print("Bem-vindo ao War of Bitches !")
    nome = input("Digite o nome do seu personagem: ").title()
    
    # Criar o jogador
    jogador = Personagem(nome=nome, hp=50, ataque=10)
    
    # Lista de monstros
    monstros = [
        Monstro(nome="Goblin", hp=20, ataque=5),
        Monstro(nome="Esqueleto", hp=25, ataque=7),
        Monstro(nome="Dragão", hp=40, ataque=15)
    ]
    
    print(f"\nBoa sorte, {jogador.nome}! Você tem {jogador.hp} de HP e {jogador.ataque} de ataque.\n")


    # Loop para enfrentar monstros
    for monstro in monstros:
        print(f"\nVocê encontrou um {monstro.nome}! Prepare-se para a batalha!")
        while monstro.esta_vivo() and jogador.esta_vivo():
            print(f"\n{jogador.nome}: {jogador.hp} HP | {monstro.nome}: {monstro.hp} HP")
            acao = input("O que você quer fazer? (1: Atacar, 2: Fugir): ")
            
            if acao == "1":
                jogador.atacar(monstro)
                if monstro.esta_vivo():
                    monstro.atacar(jogador)
            elif acao == "2":
                print("Você fugiu da batalha!")
                return
            else:
                print("Ação inválida!")

        if not jogador.esta_vivo():
            print("Game Over! Você foi derrotado!")
            return

    print("\nParabéns! Você derrotou todos os monstros e venceu o jogo!")

# Iniciar o jogo
jogo()



#print("Ola Mundo")