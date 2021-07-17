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
        #para cada cpf/carteira não classificado é necessário descobrir os 3 mais proximos e classificar o perfil
        x = (item_data[2][0]-item_no_class[0]) **2 +  (item_data[2][1]-item_no_class[1]) **2 +  (item_data[2][2]-item_no_class[2]) **2 + (item_data[2][3]-item_no_class[3]) **2
        x = pow(x,1/2)
        saida.append(round(x, 2))
        saida.append(item_data[1])
        saida.append(item_data[2])        

        lista.append(saida)
                  
    lista.sort()
    return determinaPerfil(lista[0:k])  #determinar a frequencia das classes

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
