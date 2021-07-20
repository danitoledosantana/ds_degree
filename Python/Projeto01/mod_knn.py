def classifica_perfil_knn(k ,item_no_class, data):
    ''' Calcula knn (distancia entre dois pontos)
        Entrada:k (numero de vizinhos que será considerado),
                item_no_class (item não classificado)
                data (base classificada usada como referência)                 
        Retorna: lista classificada
    '''    

    lista = []
    x=0
    for item_data in data:
        
        saida = []
        saida.append(calcularDistancia(item_data[2],item_no_class))
        saida.append(item_data[1])
        saida.append(item_data[2]) 
        lista.append(saida)
                  
    lista.sort()
    return determinaPerfil(lista[0:k])  #determinar a frequencia das classes

def calcularDistancia(cartAtual, cartVizinho):
    x = []
    for i in range(len(cartAtual)):
        x.append((cartAtual[i] - cartVizinho[i])**2)
    distancia = sum(x)
    distancia = distancia**.5
    
    return distancia
        

def determinaPerfil(lista):
    moderado = 0
    agressivo = 0
    conservador = 0
    retornaPerfil = ''
    for perfil in lista:
        if perfil[1] == 'Moderado':
            moderado += 1
        elif perfil[1] == 'Agressivo':
            agressivo += 1
        elif perfil[1] == 'Conservador':
            conservador += 1

    if agressivo > moderado:
        if agressivo > conservador:
            retornaPerfil = 'Agressivo'
    elif moderado > conservador:
        retornaPerfil = 'Moderado'
    else:
        retornaPerfil = 'Conservador'

    return retornaPerfil
