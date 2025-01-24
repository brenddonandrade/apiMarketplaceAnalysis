# def test_nullity(data, price):

#     # Calcular os retornos diários
#     returns = data[price].pct_change().dropna()

#     results = {}
#     tickers = list(data[price].columns)

#     #  Studant's t-test (Comparando as médias dos retornos dos tickers)
#     for ticker_i in data[price].columns:
#         for ticker_j in data[price].columns:
#             t_stat, p_value_ttest = stats.ttest_ind(returns[ticker_i], returns[ticker_j])
#             results["Studant's t-test", f'{ticker_i}, {ticker_j}'] = {'Statistic t': t_stat, 'p-value': p_value_ttest}

#     # # Interpretação do valor p (nível de significância 0,05)
#     # if p_value_ttest < 0.05:
#     #     print("Há uma diferença significativa entre os retornos de AAPL e MSFT.")
#     # else:
#     #     print("Não há uma diferença significativa entre os retornos de AAPL e MSFT.")


#     #  Teste Qui-quadrado (Criando categorias com base nos retornos)
#     # Criar categorias de retornos: 1 para positivo e 0 para negativo
#     returns_categorized = returns.apply(lambda x: np.where(x > 0, 1, 0))

#     for ticker_i in data[price].columns:
#         for ticker_j in data[price].columns:
#             # Criar tabela de contingência
#             contingency_table = pd.crosstab(returns_categorized[ticker_i], returns_categorized[ticker_j])

#             # Teste qui-quadrado
#             chi2_stat, p_value_chi2, dof, expected = stats.chi2_contingency(contingency_table)
#             results['Qui-square Test', f'{ticker_i}, {ticker_j}'] = {"Statistic Qui-square": chi2_stat, 'p-value': p_value_chi2}

#     # # Interpretação do valor p (nível de significância 0,05)
#     # if p_value_chi2 < 0.05:
#     #     print("Há uma associação significativa entre os retornos categorizados de AAPL e MSFT.")
#     # else:
#     #     print("Não há uma associação significativa entre os retornos categorizados de AAPL e MSFT.")


#     # Teste ANOVA (Comparando as médias dos retornos de várias ações)
#     anova_stat, p_value_anova = stats.f_oneway(*[returns[ticker] for ticker in tickers])
#     results["ANOVA Test"] = {'Statistic F': anova_stat, 'p-value': p_value_anova}

#     # # Interpretação do valor p (nível de significância 0,05)
#     # if p_value_anova < 0.05:
#     #     print("Há uma diferença significativa entre os retornos das ações.")
#     # else:
#     #     print("Não há uma diferença significativa entre os retornos das ações.")


#     # Teste F (Comparando a variância dos retornos de AAPL e MSFT)
#     for ticker_i in data[price].columns:
#         for ticker_j in data[price].columns:
#             var_i = np.var(returns[ticker_i], ddof=1)
#             var_j = np.var(returns[ticker_j], ddof=1)
#             f_stat = var_i / var_j
#             df1 = len(returns[ticker_i]) - 1  # graus de liberdade do numerador
#             df2 = len(returns[ticker_j]) - 1  # graus de liberdade do denominador
#             p_value_f = stats.f.cdf(f_stat, df1, df2)
#             results['F-test', f'{ticker_i}, {ticker_j}'] = {'Statistic F': f_stat, 'p-value': p_value_f}

#     # Interpretação do valor p (nível de significância 0,05)
#     # if p_value_f < 0.05:
#     #     print("Há uma diferença significativa nas variâncias dos retornos de AAPL e MSFT.")
#     # else:
#     #     print("Não há uma diferença significativa nas variâncias dos retornos de AAPL e MSFT.")


#     # Teste de Shapiro-Wilk (Verificando a normalidade dos retornos de AAPL)
#     for ticker in data[price].columns:
#         shapiro_stat, p_value_shapiro = stats.shapiro(returns[ticker])
#         results['Shapiro-Wilk tests', ticker] = {'Statistics W': shapiro_stat, 'p-value': p_value_shapiro}

#     # # Interpretação do valor p (nível de significância 0,05)
#     # if p_value_shapiro < 0.05:
#     #     print("Os retornos de AAPL não seguem uma distribuição normal.")
#     # else:
#     #     print("Os retornos de AAPL seguem uma distribuição normal.")

#     return results

# results_test_nullity = test_nullity(data_analyzed, 'Close')


# # Função para aplicar os testes de nulidade
# def test_normality(data, price):
#     results = {}

#     let_data = data[price]

#     # Teste de Shapiro-Wilk
#     for ticker in let_data.columns:
#         shapiro_test = stats.shapiro(let_data[ticker])
#         results['Shapiro-Wilk', ticker] = {
#             'statistic': shapiro_test.statistic, 'p-value': shapiro_test.pvalue}

#     # Teste de Kolmogorov-Smirnov (comparando com distribuição normal)
#     for ticker in let_data.columns:
#         ks_test = stats.kstest(let_data[ticker], 'norm', args=(
#             let_data[ticker].mean(), let_data[ticker].std()))
#         results['Kolmogorov-Smirnov',
#                 ticker] = {'statistic': ks_test.statistic, 'p-value': ks_test.pvalue}

#     # Teste de Lilliefors
#     for ticker in data[price].columns:
#         # calcular os retornos logarítmicos
#         returns = np.log(data[price][ticker] / data[price][ticker].shift(1))
#         retruns = returns.dropna()

#         # realizar o teste de Lilliefors (usando a aproximação de Kolmogorov-Smirnov)
#         statistic, p_value = diag.lilliefors(returns)
#         results['Lilliefors', ticker] = {
#             'Statistic': statistic, 'p-value': p_value}

#     # Teste de Anderson-Darling
#     for ticker in let_data.columns:
#         ad_test = stats.anderson(let_data[ticker], dist='norm')
#         results['Anderson-Darling', ticker] = {
#             'statistic': ad_test.statistic, 'critical_values': ad_test.critical_values}

#     # Teste de Jarque-Bera
#     for ticker in let_data.columns:
#         jb_test = stats.jarque_bera(let_data[ticker])
#         results['Jarque-Bera',
#                 ticker] = {'statistic': jb_test.statistic, 'p-value': jb_test.pvalue}

#     # Teste de D'Agostino-Pearson
#     for ticker in let_data.columns:
#         dp_test = stats.normaltest(let_data[ticker])
#         results['D\'Agostino-Pearson',
#                 ticker] = {'statistic': dp_test.statistic, 'p-value': dp_test.pvalue}

#     return results

# results_test_normality = test_normality(data_analyzed, 'Close')

# results_test_normality
