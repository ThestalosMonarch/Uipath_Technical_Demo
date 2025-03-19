import pandas as pd
import os

def process_invoices():
    folder_path = 'E:/RPA/UiPath/UiPath Projects/UiPath Technical Demo/UiPath Technical Demo/Data/Output'  # Caminho da pasta de invoices
    output_excel_path = 'E:/RPA/UiPath/UiPath Projects/UiPath Technical Demo/UiPath Technical Demo/Data/Output/comparativo.xlsx'  # Caminho do arquivo de saída


    if os.path.exists(output_excel_path):
        os.remove(output_excel_path)
        print(f"O arquivo {output_excel_path} já existia e foi removido.")

    # Criando uma lista para armazenar os dados dos comparativos
    comparison_data = []

    # Percorrendo todos os arquivos Excel na pasta
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)

            # Lendo o arquivo Excel
            df = pd.read_excel(file_path, sheet_name='Simple Fields - Formatted')

            # Calculando a porcentagem de taxa
            df['Tax Percentage'] = (df['Tax'] / df['Total']) * 100

            # Pegando o nome do arquivo sem a extensão
            invoice_name = os.path.splitext(filename)[0]

            # Calculando a média da Tax Percentage
            avg_tax_percentage = df['Tax Percentage'].mean()

            # Adicionando os dados ao comparativo
            comparison_data.append([invoice_name, avg_tax_percentage])

    # Criando um DataFrame com os dados de comparação
    comparison_df = pd.DataFrame(comparison_data, columns=['Invoice File', 'Tax Percentage'])

    # Salvando o DataFrame em um novo arquivo Excel
    comparison_df.to_excel(output_excel_path, index=False)

    return 'Comparative Excel file generated successfully!'
