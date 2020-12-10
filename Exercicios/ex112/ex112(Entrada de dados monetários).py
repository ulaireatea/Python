from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço R$ ')
moeda.resumo(p, 20, 12) # 20% de aumento e 12% de redução
