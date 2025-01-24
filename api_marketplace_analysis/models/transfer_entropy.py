
# def transfer_entropy(data, price, lags):

#     # Transformar os dados em um array numpy (IDTxl trabalha com arrays numpy)
#     time_series = data[price].values.T  # Transposta para colocar em formato [n_variables, n_timepoints]

#     # Preparar os dados para IDTxl
#     data_idtxl = Data(time_series, dim_order='ps')

#     # Configurações da análise de Transfer Entropy
#     settings = {
#         "verbose": True,
#         "fdr_correction": True,
#         "cmi_estimator": 'JidtGaussianCMI',  # Estimador comum para TE
#         "max_lag_sources": lags,  # Define o lag máximo para o embedding das séries temporais
#         "min_lag_sources": 1  # Define o lag mínimo
#     }

#     # Configuração da análise de Transfer Entropy
#     network_analysis = MultivariateTE()
#     results = network_analysis.analyse_network(settings=settings, data=data_idtxl)

#     # Visualizar os resultados
#     plot_network(results, threshold=0.0)

# transfer_entropy(data_analyzed, 'Close', 10)
