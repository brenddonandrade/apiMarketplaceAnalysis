# def verify_nan(df):
#     # Encontrar valores NaN
#     nan_locations = df.isna()

#     cont_nan = 0
#     lost_days = []
#     for row_idx, row in nan_locations.iterrows():
#         for col_idx, is_nan in row.items():
#             if is_nan:
#                 # Exibindo o índice do DataFrame e a localização do NaN
#                 print(f'Index: {row_idx}\tColumn: {col_idx}')
#                 if 'Adj Close' in col_idx:
#                     lost_days.append((row_idx.strftime('%Y-%m-%d'),  col_idx.__getitem__(1)))

#                 cont_nan += 1

#     result = int(cont_nan/6)
#     approx = result/len(df)*100
#     print(f'\nQuantity: {int(cont_nan/6)}')
#     print(f'Approx {approx:.2f}% of the data is NaN' )
#     return result, lost_days

# quantity_nan, lost_days = verify_nan(data_analyzed)


# # removing NaNs
# data = data_analyzed.dropna()
# # lost days:
# print(lost_days)
