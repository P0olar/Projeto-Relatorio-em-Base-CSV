import pandas as pd
import os
import sys

def inicial(escolha):
    if escolha == "1":
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
        output_file = "Relatorio/report-fs.html"

        # Abrir o arquivo para escrita
        with open(output_file, "w", encoding='utf-8') as file:
            # Redirecionar stdout para o arquivo
            original_stdout = sys.stdout
            sys.stdout = file

            print(f"<html><head><title>Relatório FS Ribeiro</title></head><body>")
            print(f"<h1>Relatório da FS Ribeiro do Período {data_inicio} a {data_fim}</h1>")

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
            print("<h2>Curva A dos produtos mais vendidos:</h2>")
            print(curva_a_total.to_frame().to_html(index=True, header=True))
            print("<br>")

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

            print("<h2>Resumo Financeiro</h2>")
            print(f"<p>Valor Bruto Recebido: <b>{total_formatado}</b></p>")
            print(f"<p>Valor Total das Taxas Pagas à Shopee: <b>{sum_total_formatada}</b></p>")
            print(f"<p>Valor Líquido Recebido: <b>{sum_liquido_formt}</b></p>")

            print("<br>")
            
            print("<h2>Status dos Pedidos</h2>")
            print(fs_total["Status do pedido"].value_counts(normalize=True).map("{:.2%}".format).to_frame().to_html(index=True, header=True))
            print("<br>")
            print(fs_total["Status do pedido"].value_counts().to_frame().to_html(index=True, header=True))

            motivos_canc = fs_total["Cancelar Motivo"].value_counts().head(5)
            print(f"<h2>Principais Motivos de Cancelamento</h2>")
            print(motivos_canc.to_frame().to_html(index=True, header=True))
            print("<br>")

            print(f"</body></html>")

            # Restaurar stdout
            sys.stdout = original_stdout

        print(f"Relatório salvo em {output_file}")

    elif escolha == "2":
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
        print("Bem Vindo ao Relatorio da Farma Florida")

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

    elif escolha == "3":
        def limpar_terminal():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        limpar_terminal()

        # Função para carregar e filtrar os dados por período
        def carregar_e_filtrar_dados(caminho, coluna_data, data_inicio, data_fim, encoding='latin1'):
            df = pd.read_csv(caminho, encoding=encoding)
            df[coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce')
            filtro = (df[coluna_data] >= data_inicio) & (df[coluna_data] <= data_fim)
            df_filtrado = df.loc[filtro]
            return df_filtrado

        print("")
        print("Bem Vindo ao Relatorio da RE Transportes")

        # Especificar o período desejado
        data_inicio = input("Digite uma data Inicial neste formato 'YYYY-MM-DD HH:MM':\n")
        data_fim = input("Digite uma data Final neste formato 'YYYY-MM-DD HH:MM':\n")
        print("\n")

        # Caminho do arquivo de saída
        output_file = "Relatorio/report-re.html"

        # Abrir o arquivo para escrita
        with open(output_file, "w", encoding='utf-8') as file:
            # Redirecionar stdout para o arquivo
            original_stdout = sys.stdout
            sys.stdout = file

            print(f"<html><head><title>Relatório RE Transportes</title></head><body>")
            print(f"<h1>Relatório da RE Transportes {data_inicio} a {data_fim}</h1>")

            # Carregar e filtrar os dados
            re_jan = carregar_e_filtrar_dados("re/01-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_fev = carregar_e_filtrar_dados("re/02-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_mar = carregar_e_filtrar_dados("re/03-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_abr = carregar_e_filtrar_dados("re/04-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_mai = carregar_e_filtrar_dados("re/05-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_jun = carregar_e_filtrar_dados("re/06-2024.csv", "Data de criação do pedido", data_inicio, data_fim)

            # Combinar os DataFrames filtrados em um único DataFrame
            re_total = pd.concat([re_jan, re_fev, re_mar, re_abr, re_mai, re_jun])

            # Analisar e gerar o relatório - por exemplo, Curva A dos produtos mais vendidos
            curva_a_total = re_total["Nome do Produto"].value_counts().head(15)
            print("<h2>Curva A dos produtos mais vendidos:</h2>")
            print(curva_a_total.to_frame().to_html(index=True, header=True))
            print("<br>")

            # Calcular as taxas de comissão e de serviço
            taxa_de_venda = 'Taxa de comissão'
            taxa_de_servico = 'Taxa de serviço'

            re_total[taxa_de_venda] = pd.to_numeric(re_total[taxa_de_venda], errors='coerce').fillna(0)
            re_total[taxa_de_servico] = pd.to_numeric(re_total[taxa_de_servico], errors='coerce').fillna(0)

            sum_tx_venda = re_total[taxa_de_venda].sum()
            sum_tx_servico = re_total[taxa_de_servico].sum()
            total_de_venda = re_total['Valor Total'].sum()

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
            print(re_total["Status do pedido"].value_counts(normalize=True).map("{:.2%}".format).to_frame().to_html(index=True, header=True))
            print("<br>")
            print(re_total["Status do pedido"].value_counts().to_frame().to_html(index=True, header=True))

            motivos_canc = re_total["Cancelar Motivo"].value_counts().head(5)
            print(f"<h2>Principais Motivos de Cancelamento</h2>")
            print(motivos_canc.to_frame().to_html(index=True, header=True))
            print("<br>")

            print(f"</body></html>")

            # Restaurar stdout
            sys.stdout = original_stdout

        print(f"Relatório salvo em {output_file}")
    elif escolha == "4":
        def limpar_terminal():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        limpar_terminal()

        # Função para carregar e filtrar os dados por período
        def carregar_e_filtrar_dados(caminho, coluna_data, data_inicio, data_fim, encoding='utf-8'):
            df = pd.read_csv(caminho, encoding=encoding)
            df[coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce')
            filtro = (df[coluna_data] >= data_inicio) & (df[coluna_data] <= data_fim)
            df_filtrado = df.loc[filtro]
            return df_filtrado

        print("")
        print("Bem Vindo ao Relatorio Total das Lojas")

        # Especificar o período desejado
        data_inicio = input("Digite uma data Inicial neste formato 'YYYY-MM-DD HH:MM':\n")
        data_fim = input("Digite uma data Final neste formato 'YYYY-MM-DD HH:MM':\n")
        print("\n")

        # Caminho do arquivo de saída
        output_file = "Relatorio/report-total.html"

        # Abrir o arquivo para escrita
        with open(output_file, "w", encoding='utf-8') as file:
            # Redirecionar stdout para o arquivo
            original_stdout = sys.stdout
            sys.stdout = file

            print(f"<html><head><title>Relatório Total das Lojas</title></head><body>")
            print(f"<h1>Relatório das Lojas {data_inicio} a {data_fim}</h1>")

            # Carregar e filtrar os dados
            fs_jan = carregar_e_filtrar_dados("fs/01-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            fs_fev = carregar_e_filtrar_dados("fs/02-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            fs_mar = carregar_e_filtrar_dados("fs/03-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            fs_abr = carregar_e_filtrar_dados("fs/04-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            fs_mai = carregar_e_filtrar_dados("fs/05-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            fs_jun = carregar_e_filtrar_dados("fs/06-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            ff_jan = carregar_e_filtrar_dados("ff/01-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            ff_fev = carregar_e_filtrar_dados("ff/02-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            ff_mar = carregar_e_filtrar_dados("ff/03-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            ff_abr = carregar_e_filtrar_dados("ff/04-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            ff_mai = carregar_e_filtrar_dados("ff/05-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            ff_jun = carregar_e_filtrar_dados("ff/06-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_jan = carregar_e_filtrar_dados("re/01-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_fev = carregar_e_filtrar_dados("re/02-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_mar = carregar_e_filtrar_dados("re/03-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_abr = carregar_e_filtrar_dados("re/04-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_mai = carregar_e_filtrar_dados("re/05-2024.csv", "Data de criação do pedido", data_inicio, data_fim)
            re_jun = carregar_e_filtrar_dados("re/06-2024.csv", "Data de criação do pedido", data_inicio, data_fim)

            # Combinar os DataFrames filtrados em um único DataFrame
            lojas_total = pd.concat([fs_jan,fs_fev,fs_mar,fs_abr,fs_mai,fs_jun, ff_jan,ff_fev,ff_mar,ff_abr,ff_mai,ff_jun, re_jan, re_fev, re_mar, re_abr, re_mai, re_jun])

            # Analisar e gerar o relatório - por exemplo, Curva A dos produtos mais vendidos
            curva_a_total = lojas_total["Nome do Produto"].value_counts().head(30)
            print("<h2>Curva A dos produtos mais vendidos:</h2>")
            print(curva_a_total.to_frame().to_html(index=True, header=True))
            print("<br>")

            # Calcular as taxas de comissão e de serviço
            taxa_de_venda = 'Taxa de comissão'
            taxa_de_servico = 'Taxa de serviço'
            
            lojas_total[taxa_de_venda] = pd.to_numeric(lojas_total[taxa_de_venda], errors='coerce').fillna(0)
            lojas_total[taxa_de_servico] = pd.to_numeric(lojas_total[taxa_de_servico], errors='coerce').fillna(0)

            sum_tx_venda = lojas_total[taxa_de_venda].sum()
            sum_tx_servico = lojas_total[taxa_de_servico].sum()
            total_de_venda = lojas_total['Valor Total'].sum()

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
            print(lojas_total["Status do pedido"].value_counts(normalize=True).map("{:.2%}".format).to_frame().to_html(index=True, header=True))
            print("<br>")
            print(lojas_total["Status do pedido"].value_counts().to_frame().to_html(index=True, header=True))

            motivos_canc = lojas_total["Cancelar Motivo"].value_counts().head(5)
            print(f"<h2>Principais Motivos de Cancelamento</h2>")
            print(motivos_canc.to_frame().to_html(index=True, header=True))
            print("<br>")

            print(f"</body></html>")

            # Restaurar stdout
            sys.stdout = original_stdout

        print(f"Relatório salvo em {output_file}")
    else:
        print("Opção inválida, tente novamente.")
        return False
    return True

def limpar_terminal():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

limpar_terminal()

def main():
    while True:
        print("Opções:")
        print("1. FS Ribeiro")
        print("2. Farma Florida")
        print("3. RE Transportes")
        print("4. Todas as Lojas")
        escolha = input("Digite uma das opções: \n")
        if inicial(escolha):
            break

# Executar o sistema de escolha de opção
main()