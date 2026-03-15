import math
import random
import datetime
import statistics as st
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# ENTRADAS
capital   = float(input('Capital inicial: '))
aporte    = float(input('Aporte mensal: '))
meses     = float(input('Prazo (meses): '))
cdi_anual = float((input('CDI anual (%): ')))/100
perc_cdb  = float(input('Percentual do CDI - CDB (%): '))/100
perc_lci  = float(input('Percentual do CDI - LCI (&): '))/100
taxa_fii  = float(input('Rentabilidade do FII(%): '))/100
meta      = float(input('Meta financeira (R$): '))

# Conversão do CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) - 1

# total investido
total_investido = capital + (aporte * meses)

# -------------------------
# CDB
# -------------------------

taxa_cdb = cdi_mensal * perc_cdb

montante_cdb = (capital * math.pow((1+taxa_cdb), meses)) + (aporte * meses)

lucro_cdb = montante_cdb - total_investido

montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

# -------------------------
# LCI/LCA
# -------------------------

taxa_lci = cdi_mensal * perc_lci

montante_lci = (capital * math.pow((1+taxa_lci), meses))+(aporte * meses)

# -------------------------
# POUPANÇA
# -------------------------

taxa_poupanca = 0.005

montante_poupanca = (capital * math.pow((1+taxa_poupanca), meses))+(aporte * meses)

# -------------------------
# FII
# -------------------------

base_fii = (capital * math.pow((1+taxa_fii), meses)) + (aporte * meses)

sim1 = base_fii * (1 + random.uniform(-0.03,0.03))
sim2 = base_fii * (1 + random.uniform(-0.03,0.03))
sim3 = base_fii * (1 + random.uniform(-0.03,0.03))
sim4 = base_fii * (1 + random.uniform(-0.03,0.03))
sim5 = base_fii * (1 + random.uniform(-0.03,0.03))

lista_fii = [sim1,sim2,sim3,sim4,sim5]

media_fii = st.mean(lista_fii)
mediana_fii = st.median(lista_fii)
desvio_fii = st.stdev(lista_fii)

montante_fii = media_fii

# -------------------------
# DATAS
# -------------------------

data_simulacao = datetime.date.today()

data_resgate = data_simulacao + datetime.timedelta(days=meses*30)

# -------------------------
# META FINANCEIRA
# -------------------------

meta_cdb = montante_cdb_liquido >= meta
meta_lci = montante_lci >= meta
meta_poup = montante_poupanca >= meta
meta_fii = montante_fii >= meta

# -------------------------
# GRÁFICOS ASCII
# -------------------------

graf_cdb = "█" * int(montante_cdb_liquido/1000)
graf_lci = "█" * int(montante_lci/1000)
graf_poup = "█" * int(montante_poupanca/1000)
graf_fii = "█" * int(montante_fii/1000)

# -------------------------
# RELATÓRIO FINAL
# -------------------------

print("\n========== RELATÓRIO PYINVEST ==========\n")

print("Data da simulação :", data_simulacao)
print("Data de resgate   :", data_resgate)

print("\nTotal investido :", locale.currency(total_investido, grouping=True))

print("\n------------- RESULTADOS -------------\n")

print("CDB:", locale.currency(montante_cdb_liquido, grouping=True))
print(graf_cdb)
print("Meta atingida:", meta_cdb)

print("\nLCI/LCA:", locale.currency(montante_lci, grouping=True))
print(graf_lci)
print("Meta atingida:", meta_lci)

print("\nPoupança:", locale.currency(montante_poupanca, grouping=True))
print(graf_poup)
print("Meta atingida:", meta_poup)

print("\nFII:", locale.currency(montante_fii, grouping=True))
print(graf_fii)
print("Meta atingida:", meta_fii)

print("\n------ ESTATÍSTICAS FII ------\n")

print("Média:", locale.currency(media_fii, grouping=True))
print("Mediana:", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(desvio_fii, grouping=True))
