from model import Tarefas, Gerenciador_Tarefas, linha, limpar_tela

menu = Gerenciador_Tarefas()

limpar_tela()
while True:
  
    print(f'{'GERENCIADOR DE TAREFAS':^65}')

    print("""\nOPÇÔES
1 - Adicionar Nova Tarefa
2 - Marcar Tarefa Como Concluida
3 - Remove Uma Tarefa
4 - Lista Tarefas [Pendentes / Concluidas]          
5 - Lista Tarefas Por Prioridade [baixa / media / alta]  
6 - Sair                  
\n""")
    
    while True:
        opcao = input('Opção >> ').strip()
        if opcao.isdigit() and 1 <= int(opcao) <= 6:
            break
        else:
            print('opção invalida! informe um numero de 1 a 6 referente as opçoes')
    
    if opcao == '1':
            nova_tarefa = input('Nova Tarefa: ').strip().lower()
            if not menu.existe_tarefa(nova_tarefa):
                while True:
                    add_prioridade = input('Prioridade da Tarefa [baixa - media - alta] : ').strip().lower()
                    if add_prioridade not in ['baixa','media', 'alta']:
                        print('Prioridade invalida! opçoes validas [baixa / media / alta]')
                        continue
                    break
                tarefa_adicionar = Tarefas(nova_tarefa,add_prioridade)
                menu.adicionar_tarefa(tarefa_adicionar)
                limpar_tela()
                linha()
                print(f'A tarefa {nova_tarefa} foi adicionada com sucesso!')
                linha()
            else:
                voltar = input(f'A tarefa {nova_tarefa} ja existe na lista! PRESS qualquer tecla para voltar ao menu : ')

    if opcao == '2':
        limpar_tela()
        menu.exibir_tarefas()
        if len(menu._banco_dados):
            while True:
                nome_tarefa_concluir = input('Nome Da Tarefa a Concluir: ').strip().lower()

                if menu.existe_tarefa(nome_tarefa_concluir):
                    if not menu._banco_dados[nome_tarefa_concluir].status == 'concluido':

                        tarefa_concluir = menu._banco_dados.get(nome_tarefa_concluir,'sem tarefa')
                        menu.marcar_concluida(tarefa_concluir)      
                        limpar_tela()
                        linha()
                        print(f'A tarefa {nome_tarefa_concluir} foi concluida com sucesso!')
                        linha()
                        break

                    else:
                        voltar = input(f'a tarefa {nome_tarefa_concluir} ja esta concluida! PRESS qualquer tecla para voltar ao menu : ')
                        limpar_tela()
                        break
                else:
                    print('Informe corretamente o nome da tarefa!')
        else:
            voltar = input('Lista Vazia! PRESS qualquer tecla para voltar ao menu! :  ')
            limpar_tela()

    if opcao == '3':
        limpar_tela()
        menu.exibir_tarefas()

        while True:
            if len(menu._banco_dados):
                nome_tarefa_remover = input('Nome Da Tarefa a Remover: ').strip().lower()

                if menu.existe_tarefa(nome_tarefa_remover):
                    tarefa_remover = menu._banco_dados.get(nome_tarefa_remover, 'sem tarefa')

                    menu.remover_tarefa(tarefa_remover)
                    limpar_tela()
                    linha()
                    print(f'A tarefa {nome_tarefa_remover} foi removida com sucesso!')
                    linha()
                    break
                else:
                    print('Informe corretamente o nome da tarefa!')
            else:
                voltar = input('Sem resultados! PRESS qualquer tecla para voltar ao menu! :  ')
                limpar_tela()
                break
            
    if opcao == '4':
        limpar_tela()
        menu.exibir_tarefas()
        voltar = input('Press qualquer tecla para voltar ao menu! : ')
        limpar_tela()
        
    if opcao == '5':
        limpar_tela()
        while True:
            tarefa_prioridade = input('Prioridade do Filtro [baixa , media , alta]: ').strip().lower()
            if tarefa_prioridade in ['baixa','media','alta']:
                break
            else:
                limpar_tela()
                print('digite uma prioridade valida! [baixa / media / alta]')
        menu.exibir_tarefa_prioridade(tarefa_prioridade)

        if not menu._banco_dados.get(tarefa_prioridade, 0):
            voltar = input('Sem resultados! PRESS qualquer tecla para voltar ao menu! :  ')
            limpar_tela()

    if opcao == '6':
        print('ENCERRANDO GERENCIAMENTO DE TEREFAS........')
        break
