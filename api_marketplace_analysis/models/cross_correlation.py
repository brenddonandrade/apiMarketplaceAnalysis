# def cross_correlation_analysis(data, price, lags):

#     tickers = list(data[price].columns)
#     for ticker1 in tickers:

#         # create a new figure and a grid with 2x2 subplots
#         fig, axs = plt.subplots(2, 2, figsize=(12, 9))

#         # Flatten the 2x2 array of axes for easy iteration
#         axes = axs.flatten()

#         for ax, ticker2 in zip(axes, tickers):
#             # if ticker1 == ticker2:
#             #     continue
#             # else:
#             plot_ccf(data[price][ticker1], data[price][ticker2], ax = ax, adjusted=False, lags=lags, title=f'Cross-Correlation entre {ticker1} e {ticker2}')

#         # Adjust the layout so titles and labels don't overlap
#         plt.tight_layout()
#         plt.show()

# cross_correlation_analysis(data_analyzed, 'Close', 200)
