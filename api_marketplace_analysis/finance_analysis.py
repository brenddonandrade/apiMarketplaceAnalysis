from api_marketplace_analysis.data.loader import Loader


class FinanceAnalysis:
    def __init__(self, sticker: str):
        self.sticker = sticker

    def operation(self):
        menu_options = """
            Digite a operaçao desejada:
            (a): Analisar os dados;
            (d): Baixar dados de um ticker;
            (q): Sair.
        """

        while (True):
            print(menu_options)
            option = input('Operation:')

            if (option == 'a'):
                print(f'Analisando os dados de {self.sticker}\n')

            elif (option == 'd'):
                print(f'Baixando os dados de {self.sticker}\n')

            elif (option == 'q'):
                print('Saindo...')
                break
            else:
                print('Operação Inválida.')
