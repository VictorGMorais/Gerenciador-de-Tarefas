import os

class Tarefas:
    def __init__(self,tarefa,prioridade,categoria):
        #prioridade e status tem getter e setter para garantir que recebam apenas os dados corretos
        self.tarefa = tarefa
        self.prioridade = prioridade
        self.status = 'pendente'
        self.categoria = categoria

    @property
    def prioridade(self):
        return self._prioridade
    
    @prioridade.setter
    def prioridade(self, tarefa):
        if tarefa not in ['alta', 'media', 'baixa']:
            raise ValueError (f'Prioridade {tarefa} invalida! opçoes validas : alta - media - baixa')
        self._prioridade = tarefa
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,statu):
        if statu not in ['pendente', 'concluido']:
            raise ValueError (f'Status {statu} invalido! opçoes validas: pendente - concluido')
        self._status = statu

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self,categoria):
        if categoria not in ["financeiro", "rh", "ti", "marketing", "outro"]:
            raise ValueError (f'Categoria {categoria} invalida! opçoes validas: Financeiro - RH - TI - Marketing - Outro ')
        self._categoria = categoria


    def __str__(self):
        dados = f'Tarefa: {self.tarefa.capitalize():<15} | Prioridade: {self.prioridade:<6} | Status: {self.status:<10} | Categoria: {self.categoria:<10}'
        return dados

class Gerenciador_Tarefas:
    def __init__(self):
        self._banco_dados = {}
    
    def existe_tarefa(self,nome_tarefa):
        return nome_tarefa in self._banco_dados

    def adicionar_tarefa(self,tarefa):
        # a tarefa e adicionada ao dicionario com o nome da tarefa sendo a chave. em situaçoes reias,
        # o mais provavel seria usar um ID ou msm Email/cpf como chave para uma melhor organizaçao.
        if tarefa.tarefa in self._banco_dados:
            raise ValueError ('a tarefa ja existe!')
        self._banco_dados[tarefa.tarefa] = tarefa

    def marcar_concluida(self,tarefa):
        if tarefa.tarefa  in self._banco_dados:
           self._banco_dados[tarefa.tarefa].status = 'concluido'
        else:
            raise ValueError ('a tarefa nao existe!')       

    def exibir_tarefas(self):

        print(f'{"LISTA DE TAREFAS":^65}')
        print('-'*65)
        if len(self._banco_dados):
            for tarefa in self._banco_dados.values():
                print(tarefa) #percorre tarefa a tarefa e verifica o status.
        else:
            print(f'{"LISTA DE TAREFAS VAZIA":^65}')
        print('-'*65)

    def exibir_tarefa_prioridade(self,prioridade):
        print(f'{"TAREFAS COM PRIORIDADE " + prioridade.upper():^65}')
        print('-'*65)
        lista_vazia = False

        for tarefa in self._banco_dados.values():
            if tarefa.prioridade == prioridade:
                print(tarefa)
                lista_vazia = True

        if not lista_vazia:
            print(f'{"LISTA VAZIA":^65}')
        print('-'*65)
    
    def exibir_tarefa_categoria(self,categoria):
        print(f'Tarefas da Categoria : {categoria.upper()}')
        print('-'*65)

        lista_vazia = False

        for tarefa in self._banco_dados.values():
            if tarefa.categoria == categoria:
                print(tarefa)
                lista_vazia = True

        if not lista_vazia:
            print(f'{"LISTA VAZIA":^65}')
        print('-'*65)

    def remover_tarefa(self,tarefa):
        #verifica se a tarefa existe antes de usar o del na tarefa desejada
        if tarefa.tarefa not in self._banco_dados:
            raise ValueError ('a tarefa nao existe!')
        del self._banco_dados[tarefa.tarefa]
        return print(f'{tarefa.tarefa} foi removida com sucesso!')  

def linha():
    print('-'*65)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__': #area de teste
    t = Tarefas('bah','alta','rh')

    b = Gerenciador_Tarefas()
    b.adicionar_tarefa(t)
    b.exibir_tarefa_prioridade('alta')

    # print(len('["Financeiro", "RH", "TI", "Marketing", "Outro"]'))