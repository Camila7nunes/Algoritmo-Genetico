import random

tamanho_populacao = 50
genes = '''abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890'''
objetivo = "Algoritmo codado com sucesso"


class Individual(object):

    def __init__(self, cromossomo):
        self.cromossomo = cromossomo
        self.avaliacao = self.cal_avaliacao()

    @classmethod
    # Cria genes aleatorios para funcao de mutacao
    def mutacao(self):
        global genes
        gene = random.choice(genes)
        return gene

    @classmethod
    # Cria uma sequencia de genes de acordo com o tamanho do objetivo
    def create_sGene(self):
        global objetivo
        sGene_len = len(objetivo)
        return [self.mutacao() for _ in range(sGene_len)]

    # Acasalamento e geracao de filhos
    def acasalamento(self, par2):
        cromossomo_filho = []

        for gp1, gp2 in zip(self.cromossomo, par2.cromossomo):
            prob = random.random()

            # se a probabilidade for menor que 0.45 o gene será inserido no cromossomo pai 1
            if prob < 0.45:
                cromossomo_filho.append(gp1)

            # se a probabilidade for menor que 0.90 o gene será inserido no cromossomo pai 1
            elif prob < 0.90:
                cromossomo_filho.append(gp2)

            # insere um gene aleatório
            else:
                cromossomo_filho.append(self.mutacao())

            # cria novo individuo gerado pela prole
        return Individual(cromossomo_filho)

    # Calculo da funcao de avaliacao, quantidade de caracteres diferentes da string atual em relacao a string final
    def cal_avaliacao(self):

        global objetivo
        fitness = 0
        for gs, gt in zip(self.cromossomo, objetivo):
            if gs != gt: fitness += 1
        return fitness


def main():
    global tamanho_populacao
    geracao = 1
    finalizado = False
    populacao = []

    # Cria populacao inicial
    for _ in range(tamanho_populacao):
        sGene = Individual.create_sGene()
        populacao.append(Individual(sGene))

    while not finalizado:
        # populacao classificada em ordem crescente (funcao de avaliacao)
        populacao = sorted(populacao, key=lambda x: x.avaliacao)

        # se funcao de avaliacao = 0, objetivo atingido, break
        if populacao[0].avaliacao <= 0:
            finalizado = True
            break

        # senão, gera filhos para nova populacao
        nova_geracao = []

        # Escolhe 10% da população mais apta
        s = int((10 * tamanho_populacao) / 100)
        nova_geracao.extend(populacao[:s])

        # Seleciona filhos para acasalar e gerar descendentes
        s = int((90 * tamanho_populacao) / 100)
        for _ in range(s):
            pais1 = random.choice(populacao[:30])
            pais2 = random.choice(populacao[:30])
            filho = pais1.acasalamento(pais2)
            nova_geracao.append(filho)

        populacao = nova_geracao

        print("Geracao: {}\tString: {}\tFuncao Avaliacao: {}".format(geracao, "".join(populacao[0].cromossomo),populacao[0].avaliacao))
        geracao += 1

    print("Geracao: {}\tString: {}\tFuncao Avaliacao: {}".format(geracao, "".join(populacao[0].cromossomo),populacao[0].avaliacao))


if __name__ == '__main__':
    main()