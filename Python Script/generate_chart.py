import pandas as pd
import matplotlib.pyplot as plt



def generate_chart(file_path,png_path):
    # Lendo o arquivo Excel
    df = pd.read_excel(file_path, sheet_name='Simple Fields - Formatted')

    df['Tax Percentage'] = (df['Tax'] / df['Total']) * 100
    # Criando o gráfico de Tax Percentage
    df.plot(x='Vendor', y='Tax Percentage', kind='bar')
    plt.title('Tax Percentage by Vendor')
    plt.ylabel('Tax Percentage (%)')

    # Salvando o gráfico
   # plt.savefig('E:/RPA/Uipath/UiPath Projects/Python Uipath Test/Python Script/tax_percentage_chart.png')
    plt.savefig(png_path)
    return 'Chart generated successfully!'


#file_path = 'E:/RPA/Uipath/UiPath Projects/Uipath Technical Demo/Uipath Technical Demo/Data/Output/Invoice 1-105683.xlsx'

##result = generate_chart(file_path)
##print(result)