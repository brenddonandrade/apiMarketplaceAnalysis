# def plot(data, price, lags, type_analysis):
#     # Create a new figure and a grid of 2x2 subplots
#     fig, axs = plt.subplots(2, 2, figsize=(9, 6))

#     # Flatten the 2x2 array of axes for easy iteration
#     axes = axs.flatten()

#     # Getting tickers
#     tickers = data[price].columns

#     if type_analysis == 'acf':
#         for ax, ticker in zip(axes, tickers):
#             plot_acf(data[price][ticker], ax=ax, lags=lags,
#                      title=f'Autocorrelation Function (ACF) - {ticker}')

#     elif type_analysis == 'pacf':
#         for ax, ticker in zip(axes, tickers):
#             plot_pacf(data[price][ticker], ax=ax, lags=lags,
#                       title=f'Partial Autocorrelation Function (PACF) - {ticker}')

#     elif type_analysis == 'hist':
#         for ax, ticker in zip(axes, tickers):
#             ax.hist(data[price][ticker], bins=30, edgecolor='black')
#             ax.set_title(f'Series Histogram - {ticker}')
#             ax.set_xlabel(price)
#             ax.set_ylabel('Frequency')

#     # Adjust the layout so titles and labels don't overlap
#     plt.tight_layout()
#     plt.show()

# data_analyzed['Close']['KC=F']

# plot(data_analyzed, 'Close', 40, 'acf')
