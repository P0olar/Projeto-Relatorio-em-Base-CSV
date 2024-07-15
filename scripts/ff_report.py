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

print("")
print("Bem Vindo ao Relatorio da FS Ribeiro Conveniencia")

# Especificar o período desejado
data_inicio = input("Digite uma data Inicial neste formato 'YYYY-MM-DD HH:MM':\n")
data_fim = input("Digite uma data Final neste formato 'YYYY-MM-DD HH:MM':\n")
print("\n")

# Caminho do arquivo de saída
output_file = "Relatorio/report-ff.html"

# Abrir o arquivo para escrita
with open(output_file, "w", encoding='utf-8') as file:
    # Redirecionar stdout para o arquivo
    original_stdout = sys.stdout
    sys.stdout = file

    print(f"<html><head><title>Relatório Farma Florida</title></head><body>")
    print(f"<h1>Relatório da Farma Florida do Período {data_inicio} a {data_fim}</h1>")

    # Carregar e filtrar os dados
    ff_jan = carregar_e_filtrar_dados("ff/01-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    ff_fev = carregar_e_filtrar_dados("ff/02-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    ff_mar = carregar_e_filtrar_dados("ff/03-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    ff_abr = carregar_e_filtrar_dados("ff/04-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    ff_mai = carregar_e_filtrar_dados("ff/05-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
    ff_jun = carregar_e_filtrar_dados("ff/06-2024.csv", "Data de criação do pedido", data_inicio, data_fim)

    # Combinar os DataFrames filtrados em um único DataFrame
    ff_total = pd.concat([ff_jan, ff_fev, ff_mar, ff_abr, ff_mai, ff_jun])

    # Analisar e gerar o relatório - por exemplo, Curva A dos produtos mais vendidos
    curva_a_total = ff_total["Nome do Produto"].value_counts().head(15)
    print("<h2>Curva A dos produtos mais vendidos:</h2>")
    print(curva_a_total.to_frame().to_html(index=True, header=True))
    print("<br>")

    # Calcular as taxas de comissão e de serviço
    taxa_de_venda = 'Taxa de comissão'
    taxa_de_servico = 'Taxa de serviço'

    ff_total[taxa_de_venda] = pd.to_numeric(ff_total[taxa_de_venda], errors='coerce').fillna(0)
    ff_total[taxa_de_servico] = pd.to_numeric(ff_total[taxa_de_servico], errors='coerce').fillna(0)

    sum_tx_venda = ff_total[taxa_de_venda].sum()
    sum_tx_servico = ff_total[taxa_de_servico].sum()
    total_de_venda = ff_total['Valor Total'].sum()

    sum_total = sum_tx_venda + sum_tx_servico
    sum_liquido = total_de_venda - sum_total

    sum_total_formatada = f"R$ {sum_total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    total_formatado = f"R$ {total_de_venda:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    sum_liquido_formt = f"R$ {sum_liquido:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    print("<h2>Resumo Financeiro</h2>")
    print(f"<p>Valor Bruto Recebido: {total_formatado}</p>")
    print(f"<p>Valor Total das Taxas Pagas à Shopee: {sum_total_formatada}</p>")
    print(f"<p>Valor Líquido Recebido: {sum_liquido_formt}</p>")

    print("<br>")
    
    print("<h2>Status dos Pedidos</h2>")
    print(ff_total["Status do pedido"].value_counts(normalize=True).map("{:.2%}".format).to_frame().to_html(index=True, header=True))
    print("<br>")
    print(ff_total["Status do pedido"].value_counts().to_frame().to_html(index=True, header=True))

    motivos_canc = ff_total["Cancelar Motivo"].value_counts().head(5)
    print(f"<h2>Principais Motivos de Cancelamento</h2>")
    print(motivos_canc.to_frame().to_html(index=True, header=True))
    print("<br>")

    print(f"</body></html>")

    # Restaurar stdout
    sys.stdout = original_stdout

print(f"Relatório salvo em {output_file}")
