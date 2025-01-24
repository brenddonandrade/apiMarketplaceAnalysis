from finance_analysis import FinanceAnalysis


class Main:
    def __init__(self):
        print('Comecando a rodar...')

    def run(self):
        finance = FinanceAnalysis('KC=F')
        finance.operation()


if __name__ == '__main__':
    main = Main()
    main.run()
