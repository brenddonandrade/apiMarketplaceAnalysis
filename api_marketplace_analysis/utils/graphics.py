# def plot_simple(ax, data, price, ticker, ylabel):
#     # Plot on the given axis (ax) instead of creating a new figure
#     data[price][ticker].plot(ax=ax, title=f'Price [{price}][{
#                              ticker}] vs Time', ylabel=ylabel, grid=True)


# def plot_all(data, price, ylabel):
#     # Create a new figure and a grid of 2x2 subplots
#     fig, axs = plt.subplots(2, 2, figsize=(9, 6))

#     # Lists of axes to facilitate iteration
#     axes = axs.flatten()

#     # get the tickers for the specified price
#     tickers = data[price].columns

#     # Iterate over subplot positions and tickers
#     for ax, ticker in zip(axes, tickers):
#         plot_simple(ax, data, price, ticker, ylabel)

#     # Adjust the layout so titles and tags don't overlap
#     plt.tight_layout()
#     plt.show()


# plot_all(data_analyzed, 'Close', ylabel='Unit')
