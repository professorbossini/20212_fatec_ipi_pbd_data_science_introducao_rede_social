from collections import Counter
from collections import defaultdict
usuarios = [
    {"id": 0, "nome": "João", "sexo": "M", "idade": 17, "interessado_em": "feminino"},
    {"id": 1, "nome": "Pedro"},
    {"id": 2, "nome": "Jaqueline"},
    {"id": 3, "nome": "Maria"},
    {"id": 4, "nome": "Cristina"},
    {"id": 5, "nome": "Sônia"},
    {"id": 6, "nome": "Carla"},
    {"id": 7, "nome": "Erik"},
    {"id": 8, "nome": "Kátia"},
    {"id": 9, "nome": "Cléber"},
]
# print (usuarios)
#{0: (5, 8), 1: (2, 1)}

amizades = [(0,1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for usuario in usuarios:
    usuario["amigos"] = []

for i, j in amizades:
    usuarios[i]["amigos"].append(usuarios[j])
    usuarios[j]["amigos"].append(usuarios[i])

# print (usuarios)

def numero_de_amigos (usuario):
    return len(usuario["amigos"])

# teste = (numero_de_amigos(usuario) for usuario in usuarios)
# for t in teste:
#     print (t)

total_de_conexoes = sum(numero_de_amigos(usuario) for usuario in usuarios)

# print (total_de_conexoes)

numero_de_usuarios = len(usuarios)
media_de_conexoes = total_de_conexoes / numero_de_usuarios

# print (media_de_conexoes)

numero_de_amigos_por_id = [(usuario["id"], numero_de_amigos(usuario)) for usuario in usuarios]

# print (numero_de_amigos_por_id)

lista_ordenada = sorted(numero_de_amigos_por_id, key = lambda numero_de_amigos: numero_de_amigos[1], reverse=True)

#print (lista_ordenada)

def ids_dos_amigos_dos_amigos_ruim (usuario):
    return [
        amigo_de_um_amigo["id"]
        for amigo in usuario["amigos"]
        for amigo_de_um_amigo in amigo["amigos"]
    ]

def sao_diferentes (usuario, outro_usuario):
    return usuario["id"] != outro_usuario["id"]


#print (all([2 == 2, 1 == 1, 3 == 3]))

def nao_sao_amigos (usuario, outro_usuario):
    return all(sao_diferentes(amigo, outro_usuario) for amigo in usuario["amigos"])

def ids_dos_amigos_dos_amigos (usuario):
    return set([
        amigo_de_um_amigo["id"]
        for amigo in usuario["amigos"]
        for amigo_de_um_amigo in amigo["amigos"]
        if (sao_diferentes(usuario, amigo_de_um_amigo))
        and nao_sao_amigos(usuario, amigo_de_um_amigo)
    ])

# print (ids_dos_amigos_dos_amigos(usuarios[0]))

def frequencias_dos_ids_dos_amigos_dos_amigos(usuario):
    return Counter([
        amigo_de_um_amigo["id"]
        for amigo in usuario["amigos"]
        for amigo_de_um_amigo in amigo["amigos"]
        if sao_diferentes(usuario, amigo_de_um_amigo)
        and nao_sao_amigos(usuario, amigo_de_um_amigo)
    ])

# print (frequencias_dos_ids_dos_amigos_dos_amigos(usuarios[0]))

interesses = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]

def usuarios_que_gostam_de (interesse_alvo):
    return [id_usuario for id_usuario, interesse in interesses if interesse == interesse_alvo]

# print (usuarios_que_gostam_de("Java"))

def gera_lista_vazia ():
    return []

interesses_por_id_de_usuario = defaultdict(gera_lista_vazia)
for id_usuario, interesse in interesses:
    interesses_por_id_de_usuario[id_usuario].append(interesse)

ids_de_usuario_por_interesse = defaultdict(list)
for id_usuario, interesse in interesses:
    ids_de_usuario_por_interesse[interesse].append(id_usuario)

def usuarios_que_tem_interesses_em_comum_com (usuario):
   return set([
        id_usuario_interessado
        for interesse in interesses_por_id_de_usuario[usuario["id"]]
        for id_usuario_interessado in ids_de_usuario_por_interesse[interesse]
       if id_usuario_interessado != usuario["id"]
   ])

# print (usuarios_que_tem_interesses_em_comum_com(usuarios[0]))


def ids_de_quem_tem_mais_interesses_em_comum_com (usuario):
    return Counter(
        id_usuario_interessado
        for interesse in interesses_por_id_de_usuario[usuario["id"]]
        for id_usuario_interessado in ids_de_usuario_por_interesse[interesse]
        if id_usuario_interessado != usuario["id"]
    )

# print (ids_de_quem_tem_mais_interesses_em_comum_com(usuarios[0]))

salarios_anuais_e_anos_de_experiencia = [
    (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)
]

salario_por_tempo_de_experiencia = defaultdict(list)
for salario, tempo_de_experiencia in salarios_anuais_e_anos_de_experiencia:
    salario_por_tempo_de_experiencia[tempo_de_experiencia].append(salario)

# print (salario_por_tempo_de_experiencia)

media_salarial_por_tempo_de_experiencia = {
    tempo_de_experiencia: sum (salarios) / len(salarios)
    for tempo_de_experiencia, salarios in salario_por_tempo_de_experiencia.items()
}

# print (media_salarial_por_tempo_de_experiencia)

def grupo_por_tempo_de_experiencia (tempo_de_experiencia):
    if tempo_de_experiencia < 2:
        return "<2"
    if tempo_de_experiencia < 5:
        return "2 <= t < 5"
    return ">=5"

salario_por_grupo_de_tempo_de_experiencia = defaultdict(list)

for salario, tempo_de_experiencia in salarios_anuais_e_anos_de_experiencia:
    grupo = grupo_por_tempo_de_experiencia(tempo_de_experiencia)
    salario_por_grupo_de_tempo_de_experiencia[grupo].append(salario)

#print (salario_por_grupo_de_tempo_de_experiencia)


media_salarial_por_grupo_de_tempo_de_experiencia = {
    grupo_por_tempo_de_experiencia: sum(salarios) / len(salarios)
    for grupo_por_tempo_de_experiencia, salarios in salario_por_grupo_de_tempo_de_experiencia.items()
}

# print (media_salarial_por_grupo_de_tempo_de_experiencia)

tempo_de_experiencia_e_tipo_de_conta = [
    (0.7, 'paga'),
    (1.9, 'gratis'),
    (2.5, 'paga'),
    (4.2, 'gratis'),
    (6, 'gratis'),
    (6.5, 'gratis'),
    (7.5, 'gratis'),
    (8.1, 'gratis'),
    (8.7, 'paga'),
    (10, 'paga')
]

def predizer_tipo_de_conta (anos_de_experiencia):
    if anos_de_experiencia < 3:
        return 'paga'
    if anos_de_experiencia < 8.5:
        return 'gratis'
    return 'paga'
