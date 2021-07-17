
dict_cadastro = {}
  
def cadastroUsuario():

    cpf = input('Informe seu cpf: ')
    nome = input('Informe seu nome: ')
    idade = input('Informe seu idade: ')
    email = input('Informe seu email: ')

    dict_cadastro[cpf] = {(nome,idade,email)}


def pergunta():
    resposta = int(input('Digite 1, 2 ou 3: '))
    
    if resposta == 1:
        cadastroUsuario()       
    elif resposta == 2:
        print(dict_cadastro)
    elif resposta == 3:
        return
    
    pergunta()
        
pergunta()      
        
