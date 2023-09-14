import csv
import random
from faker import Faker

# Inicializa o Faker para criar dados fictícios
fake = Faker()

# Define o número de entradas no conjunto de dados
num_entries = 100

# Cria uma lista para armazenar os dados
data = []

# Cabeçalho do CSV
header = [
    "ID_Cliente", "Idade", "Genero", "Localizacao", "Estado_Civil", "Renda_Anual",
    "ID_Compra", "Data_Compra", "Valor_Total_Compra", "Numero_Produtos", "Categoria_Produtos",
    "ID_Desconto", "Tipo_Desconto", "Valor_Desconto", "Data_Validade_Desconto", "Usos_Desconto",
    "Frequencia_Compra", "Valor_Medio_Compra", "Taxa_Abandono_Carrinho", "Tempo_Gasto_Site",
    "Origem_Trafego", "Avaliacao_Produto", "Comentario_Cliente", "Data_Inscricao",
    "Data_Ultima_Compra", "Frequencia_Compra_Recorrente", "Razao_Nao_Retencao"
]

data.append(header)

# Gera dados fictícios para cada entrada
for i in range(1, num_entries + 1):
    data.append([
        i,
        random.randint(18, 70),
        random.choice(["Masculino", "Feminino"]),
        fake.city(),
        random.choice(["Solteiro", "Casado", "Divorciado", "Viuvo"]),
        random.randint(20000, 100000),
        i,
        fake.date_between(start_date='-1y', end_date='today'),
        round(random.uniform(20, 500), 2),
        random.randint(1, 5),
        random.choice(["Moda", "Eletronicos", "Beleza", "Esportes"]),
        i,
        random.choice(["Percentagem", "Valor Fixo", "Compra Minima"]),
        random.randint(5, 50),
        fake.date_between(start_date='today', end_date='+1y'),
        random.randint(1, 5),
        random.randint(1, 10),
        round(random.uniform(20, 300), 2),
        f"{random.randint(5, 90)}%",
        random.randint(5, 180),
        random.choice(["Redes Sociais", "Busca Organica", "Email Marketing", "Midia Social", "Pesquisa Paga"]),
        random.randint(1, 5),
        fake.sentence(),
        fake.date_between(start_date='-5y', end_date='-1y'),
        fake.date_between(start_date='-1y', end_date='today'),
        random.randint(1, 5),
        random.choice(["Preco alto", "Mudança de preferencia", "Entrega atrasada", "Mau atendimento", "Satisfeito", "Falta de descontos"])
    ])


with open("dados_loja_varejo.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print("Conjunto de dados gerado e salvo como 'dados_loja_varejo.csv'.")
    