import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

def frame(df, name):
	#print(df.columns.values.tolist())
	print(df['PRODUCT_CODE'])
	#plot_to_pdf(df, name)

#example
#def plot_to_pdf(df, name):
	# with PdfPages(name) as pdf:
	#     plt.figure(figsize=(3, 3))
	#     plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
	#     plt.title('Page One')
	#     pdf.savefig()  # saves the current figure into a pdf page
	#     plt.close()