from model import Tarefas, Gerenciador_Tarefas, linha, limpar_tela

menu = Gerenciador_Tarefas()

limpar_tela()
while True:
  
    print(f'{'GERENCIADOR DE TAREFAS':^65}')

    print("""\nOPÇÔES
1 - Adicionar Nova Tarefa
2 - Marcar Tarefa Como Concluida
3 - Remove Uma Tarefa
4 - Lista Tarefas [...]  
5 - Sair                  
\n""")
    
    while True:
        opcao = input('Opção >> ').strip()
        if opcao.isdigit() and 1 <= int(opcao) <= 6:
            break
        else:
            print('Opção invalida! informe um numero de 1 a 6 referente as opçoes')
    
    if opcao == '1':
            nova_tarefa = input('Nova Tarefa: ').strip().lower()
            if not menu.existe_tarefa(nova_tarefa):
                while True:
                    add_prioridade = input('Prioridade da Tarefa [baixa - media - alta] : ').strip().lower()
                    if add_prioridade not in ['baixa','media', 'alta']:
                        print('Prioridade invalida! opçoes validas [baixa / media / alta]')
                        continue
                    while True:
                        print(f'{"CATEGORIAS VALIDAS!":^48}\n["Financeiro", "RH", "TI", "Marketing", "Outro"]')
                        add_categoria = input('Categoria: ').strip().lower()
                        if add_categoria not in ["financeiro", "rh", "ti", "marketing", "outro"]:
                            print('Categoria invalida!')
                            continue
                        break
                    break
                tarefa_adicionar = Tarefas(nova_tarefa,add_prioridade,add_categoria)
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
        while True:
            
            print("""LISTAR POR!
[1] Todas
[2] Prioridade
[3] Categoria""")
            opcao = input('Opção : ').strip().lower()
            if opcao not in ['1','2','3']:
                print('Opção invalida! informe um numero de 1 a 3 referente as opçoes')
                continue

            elif opcao == '1':
                limpar_tela()
                menu.exibir_tarefas()
                voltar = input('Press qualquer tecla para voltar ao menu! : ')
                limpar_tela()
                break

            elif opcao  == '2':
                while True:
                    tarefa_prioridade = input('Prioridade do Filtro [baixa , media , alta]: ').strip().lower()
                    if tarefa_prioridade in ['baixa','media','alta']:
                        limpar_tela()
                        menu.exibir_tarefa_prioridade(tarefa_prioridade)
                        voltar = input('PRESS qualquer tecla para voltar')
                        break
                    else:
                        limpar_tela()
                        print('digite uma prioridade valida! [baixa / media / alta]\n')
                    
                    if menu._banco_dados.get(tarefa_prioridade, 0):
                        voltar = input('Sem resultados! PRESS qualquer tecla para voltar ao menu! :  ')  
                break
            
            elif opcao == '3': #daria para so usar um else. mas poderia ficar confuso no futuro para modificar
                limpar_tela()
                while True:
                    print(f'{"CATEGORIAS VALIDAS!":^48}\n["Financeiro", "RH", "TI", "Marketing", "Outro"]')
                    tarefa_categoria = input('Categoria : ').strip().lower()
                    if tarefa_categoria not in ["financeiro", "rh", "ti", "marketing", "outro"]:
                        print('Categoria invalida!')
                        continue
                    menu.exibir_tarefa_categoria(tarefa_categoria)
                    voltar = input('PRESS qualquer tecla para voltar ao menu! :  ')
                    limpar_tela()
                    break
                break 

    if opcao == '5':
        print('ENCERRANDO GERENCIAMENTO DE TEREFAS........')
        break

        
