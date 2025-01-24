# def plot_mutual_information(data, price):
#     tickers = data[price].columns

#     # Função para calcular a informação mútua
#     def mutual_information(x, y, bins=10):
#         c_xy = np.histogram2d(x, y, bins)[0]
#         mi = np.sum(c_xy * np.log(c_xy + 1e-9))  # Pequena constante para evitar log(0)
#         return mi

#     # Criar uma matriz para armazenar os valores da informação mútua
#     n = len(tickers)
#     mi_matrix = np.zeros((n, n))

#     # Calcular a informação mútua entre cada par de séries
#     for ticker_i in data[price]:
#         for ticker_j in data[price]:
#             # mi_matrix[ticker_i, ticker_j] = mutual_information(data[price][ticker_i],
#             #                                       data[price][ticker_j])
#             print(ticker_i, ticker_j)

#     # Criar um dataframe para facilitar o plot
#     mi_df = pd.DataFrame(mi_matrix, index=tickers, columns=tickers)

#     mi_df
#     # # Plotar o heatmap da informação mútua
#     # plt.figure(figsize=(8, 6))
#     # sns.heatmap(mi_df, annot=True, cmap='coolwarm', fmt='.2f', cbar_kws={'label': 'Informação Mútua'})
#     # plt.title('Informação Mútua entre Séries Temporais')
#     # plt.show()

# plot_mutual_information(data_analyzed, 'Close')
