import pandas as pd
import os
import sys

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpar_terminal()

# Função para carregar e filtrar os dados por período
def carregar_e_filtrar_dados(caminho, coluna_data, data_inicio, data_fim):
    df = pd.read_csv(caminho)
    df[coluna_data] = pd.to_datetime(df[coluna_data])  # Converter coluna de data para datetime
    df_filtrado = df[(df[coluna_data] >= data_inicio) & (df[coluna_data] <= data_fim)]
    return df_filtrado

# Especificar o período desejado
data_inicio = input("Digite uma data Inicial neste formato 'YYYY-MM-DD HH:MM':\n")
data_fim = input("Digite uma data Final neste formato 'YYYY-MM-DD HH:MM':\n")
print("\n")

# Caminho do arquivo de saída
output_file = "Relatorio/report-fs.pdf"

# Abrir o arquivo para escrita
with open(output_file, "w", encoding='utf-8') as file:
    # Redirecionar stdout para o arquivo
    original_stdout = sys.stdout
    sys.stdout = file

    print(f"Relatorio da FS Ribeiro do Periodo {data_inicio} a {data_fim}")
    print("")

    # Carregar e filtrar os dados
    fs_jan = carregar_e_filtrar_dados("fs/01-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    fs_fev = carregar_e_filtrar_dados("fs/02-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    fs_mar = carregar_e_filtrar_dados("fs/03-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    fs_abr = carregar_e_filtrar_dados("fs/04-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    fs_mai = carregar_e_filtrar_dados("fs/05-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    fs_jun = carregar_e_filtrar_dados("fs/06-2024.csv", "Data de criação do pedido", data_inicio, data_fim)

    # Combinar os DataFrames filtrados em um único DataFrame
    fs_total = pd.concat([fs_jan, fs_fev, fs_mar, fs_abr, fs_mai, fs_jun])

    # Analisar e gerar o relatório - por exemplo, Curva A dos produtos mais vendidos
    curva_a_total = fs_total["Nome do Produto"].value_counts().head(15)
    print("Curva A dos produtos mais vendidos:")
    print(curva_a_total)
    print("\n")

    # Calcular as taxas de comissão e de serviço
    taxa_de_venda = 'Taxa de comissão'
    taxa_de_servico = 'Taxa de serviço'

    fs_total[taxa_de_venda] = pd.to_numeric(fs_total[taxa_de_venda], errors='coerce').fillna(0)
    fs_total[taxa_de_servico] = pd.to_numeric(fs_total[taxa_de_servico], errors='coerce').fillna(0)

    sum_tx_venda = fs_total[taxa_de_venda].sum()
    sum_tx_servico = fs_total[taxa_de_servico].sum()
    total_de_venda = fs_total['Valor Total'].sum()

    sum_total = sum_tx_venda + sum_tx_servico
    sum_liquido = total_de_venda - sum_total

    sum_total_formatada = f"R$ {sum_total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    total_formatado = f"R$ {total_de_venda:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    sum_liquido_formt = f"R$ {sum_liquido:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    print("Valor Bruto Recebido:")
    print(total_formatado)
    print("Valor Total das Taxas Pagas à Shopee:")
    print(sum_total_formatada)
    print("====================================")
    print("Valor Liquido Recebido:")
    print(sum_liquido_formt)

    print("")

    print(fs_total["Status do pedido"].value_counts(normalize=True).map("{:.2%}".format))
    print("")
    print(fs_total["Status do pedido"].value_counts())
    motivos_canc = fs_total["Cancelar Motivo"].value_counts().head(5)
    print(f"\nOs Principais {motivos_canc}")
    print("")

    # Restaurar stdout
    sys.stdout = original_stdout

print(f"Relatório salvo em {output_file}")