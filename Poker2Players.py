import random
from os import system, name
from time import sleep

def Cartesiano(listA, listB):
    return [(elemA, elemB) for elemA in listA for elemB in listB]

def NovaCarta():
    cont = 0
    while cont != 1:
        try: 
            num = random.randint(0,51)
            carta = baralho[num]
            mesa.append(carta)
            cont += 1
            del baralho[num]
        except:
            continue
    return mesa

def DarCartas(jogador):
    cont = 0
    while cont !=2:
        try:
            num = random.randint(0,51)
            carta = baralho[num]
            jogador.append(carta)
            cont += 1
            del baralho[num]
        except:
            continue
    return jogador

def CartasMesa(jogador):
    cont = 0
    while cont !=3:
        try:
            num = random.randint(0,51)
            carta = baralho[num]
            jogador.append(carta)
            cont += 1
            del baralho[num]
        except:
            continue
    return jogador

def LimparConsole():
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)
    
def Espaço():
    a = print('''          
              
          

          ''')
    return a

def Espaco4():
    print('\n\n\n')

def Ok():
    input('Aperte ENTER para continuar')

def calculo(mesa, cartas_jogador):
    jogo1 = mesa + cartas_jogador
    lista_jogo1 = []
    ordem_jogo1 = []
    lista_jogo2 = []
    ordem_jogo2 = []
    lista_final = []
    ordem_final = []
    a, b, c, d, e, f, g, h, n, j, k, l, m, n = [], [], [], [], [], [], [], [], [], [], [], [], [], []
    paus, copas, espadas, ouros = [], [], [], []
    pontos = []
    combinações = 0
    jogos = {0.02:'2',
             0.03:'3',
             0.04:'4',
             0.05:'5',
             0.06:'6',
             0.07:'7',
             0.08:'8',
             0.09:'9',
             0.1:'10',
             0.11:'J',
             0.12:'Q',
             0.13:'K',
             0.14:'A'}
    par, trinca, quadra = 0, 0, 0
    flush = 0
    lista_sequencia = []
    sequencia = ''
    valor_sequencia = 0
    resultado = 0
    mao = ''
    
    for carta in jogo1:
        for carta1 in jogo1:
            if carta == carta1:
                for valor in carta:
                    if carta.index(valor) == 0:
                        lista_jogo1.append(valor)
                    if carta.index(valor) == 1:
                        lista_jogo2.append(valor)
                        
    for sla in cartas_jogador:
        for sla1 in cartas_jogador:
            if sla == sla1:
                for valor_sla in sla:
                    if sla.index(valor_sla) == 0:
                        lista_final.append(valor_sla)
                                                
    lista_jogo1.sort()
    lista_jogo2.sort()
    lista_final.sort()
    
    for meu in lista_final:
        ordem_final.append(valores[meu])
    ordem_final.sort()
    for item in lista_jogo1:
        ordem_jogo1.append(valores[item])
    ordem_jogo1.sort()
    for cada in ordem_jogo1:
        if cada not in lista_sequencia:
            lista_sequencia.append(cada)
    lista_sequencia.sort()
    for coisa in lista_sequencia:
        cada_sequencia = str(coisa)
        sequencia += cada_sequencia + ','
    for itemo in lista_jogo2:
        ordem_jogo2.append(naipes[itemo])
    ordem_jogo2.sort()
    
    if '10,11,12,13,14' in sequencia:
            valor_sequencia += 10
            nome_sequencia = ' de 10 à Ás'
    elif '9,10,11,12,13' in sequencia:
        valor_sequencia += 9
        nome_sequencia = ' de 9 à Rei'
    elif '8,9,10,11,12' in sequencia:
        valor_sequencia += 8
        nome_sequencia = ' de 8 à Dama'        
    elif '7,8,9,10,11' in sequencia:
        nome_sequencia = ' de 7 à Valete'
        valor_sequencia += 7
    elif '6,7,8,9,10' in sequencia:
        nome_sequencia = ' de 6 à 10'
        valor_sequencia += 6
    elif '5,6,7,8,9' in sequencia:
        valor_sequencia += 5
        nome_sequencia = ' de 5 à 9'
    elif '4,5,6,7,8' in sequencia:
        valor_sequencia += 4
        nome_sequencia = ' de 4 à 8'
    elif '3,4,5,6,7' in sequencia:
        valor_sequencia += 3
        nome_sequencia = ' de 3 à 7'
    elif '2,3,4,5' in sequencia:
        if '6' in sequencia:
            valor_sequencia += 2
            nome_sequencia = ' de 2 à 6'
        elif '14' in sequencia:
            valor_sequencia += 1
            nome_sequencia = ' de Ás à 5'
 
    for q in lista_jogo2:
        if naipes[q] == 1:
            paus.append(q)
        if naipes[q] == 2:
            copas.append(q)
        if naipes[q] == 3:
            espadas.append(q)
        if naipes[q] == 4:
            ouros.append(q)       
    
    for i in lista_jogo1:
        if valores[i] == 2:
            a.append(valores[i])
        if valores[i] == 3:
            b.append(valores[i])
        if valores[i] == 4:
            c.append(valores[i])
        if valores[i] == 5:
            d.append(valores[i])
        if valores[i] == 6:
            e.append(valores[i])
        if valores[i] == 7:
            f.append(valores[i])
        if valores[i] == 8:
            g.append(valores[i])
        if valores[i] == 9:
            h.append(valores[i])
        if valores[i] == 10:
            n.append(valores[i])
        if valores[i] == 11:
            j.append(valores[i])
        if valores[i] == 12:
            k.append(valores[i])
        if valores[i] == 13:
            l.append(valores[i])
        if valores[i] == 14:
            m.append(valores[i])
    if len(a) == 2:
        par += 1
        combinações += 1
        pontos.append(10.02)
    elif len(a) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.02)
    elif len(a) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.02)
    if len(b) == 2:
        par += 1
        combinações += 1
        pontos.append(10.03)
    elif len(b) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.03)
    elif len(b) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.03)
    if len(c) == 2:
        par += 1
        combinações += 1
        pontos.append(10.04)
    elif len(c) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.04)
    elif len(c) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.04)
    if len(d) == 2:
        par += 1
        combinações += 1
        pontos.append(10.05)
    elif len(d) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.05)
    elif len(d) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.05)
    if len(e) == 2:
        par += 1
        combinações += 1
        pontos.append(10.06)
    elif len(e) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.06)
    elif len(e) == 4:
        quadra += 1
        combinações += 1    
        pontos.append(30.06)
    if len(f) == 2:
        par += 1
        combinações += 1
        pontos.append(10.07)
    elif len(f) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.07)
    elif len(f) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.07)
    if len(g) == 2:
        par += 1
        combinações += 1
        pontos.append(10.08)
    elif len(g) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.08)
    elif len(g) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.08)
    if len(h) == 2:
        par += 1
        combinações += 1
        pontos.append(10.09)
    elif len(h) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.09)
    elif len(h) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.09)
    if len(n) == 2:
        par += 1
        combinações += 1
        pontos.append(10.1)
    elif len(n) == 3:
        trinca += 1
        combinações += 1
        pontos.append(10.1)
    elif len(n) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.1)
    if len(j) == 2:
        par += 1
        combinações += 1
        pontos.append(10.11)
    elif len(j) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.11)
    elif len(j) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.11)
    if len(k) == 2:
        par += 1
        combinações += 1
        pontos.append(10.12)
    elif len(k) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.12)
    elif len(k) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.12)
    if len(l) == 2:
        par += 1
        combinações += 1
        pontos.append(10.13)
    elif len(l) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.13)
    elif len(l) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.13)
    if len(m) == 2:
        par += 1
        combinações += 1
        pontos.append(10.14)
    elif len(m) == 3:
        trinca += 1
        combinações += 1
        pontos.append(20.14)
    elif len(m) == 4:
        quadra += 1
        combinações += 1
        pontos.append(30.14)
        
    for chave,numero in valores.items():
        if numero == ordem_jogo1[len(cartas_jogador + mesa)-1]:
            carta_alta = chave
        
    pontos.sort(reverse=True)
    if trinca == 2:
        pontos[1] -= 10
        trinca -= 1
        par += 1
        pontos.sort(reverse=True)
        
    if quadra == 1:
        if len(pontos) > 1:
            if pontos[1] > 20:
                trinca -= 1 
            else:
                par -= 1
            pontos.pop(1)
            combinações -= 1
        
    if len(pontos) > 2:
        par -= 1
        combinações -= 1 
        pontos.pop(2)
    
    if len(paus) == 5:
        flush += 1
        nome_flush = 'Flush de Paus'
    elif len(copas) == 5:
        flush += 2
        nome_flush = 'Flush de Copas'
    elif len(espadas) == 5:
        flush += 3
        nome_flush = 'Flush de Espadas'
    elif len(ouros) == 5:
        flush += 4
        nome_flush = 'Flush de Ouros'
    
    if valor_sequencia != 0:
        if flush != 0:
            if valor_sequencia == 10:
                resultado = 10
                mao = 'Royal Straight Flush'
            else:
                resultado = 9 + round(valor_sequencia/10,1)
                mao = 'Straight' + nome_flush + nome_sequencia
    if combinações == 1 and quadra == 1:
        resultado =  8 + round(valores[jogos[round(pontos[0]%1, 2)]]/100,2)
        mao = f'Quadra de {valores2[jogos[round(pontos[0]%1, 2)]]}'
    elif combinações == 2 and trinca == 1:
        resultado = 7 + round(valores[jogos[round(pontos[0]%1, 2)]]/100,2) + round(valores[jogos[round(pontos[1]%1, 2)]]/10000,4)
        mao = f'Full House de {valores2[jogos[round(pontos[0]%1, 2)]]} e {valores2[jogos[round(pontos[1]%1, 2)]]}'
    else:
        if flush != 0:
            resultado = 6
            mao = nome_flush
        else:
            if valor_sequencia != 0:
                resultado = 5 + round(valor_sequencia/100,2)
                mao = 'Sequencia' + nome_sequencia
            else:
                if combinações == 1 and trinca == 1:
                    resultado = 4  + round(valores[jogos[round(pontos[0]%1, 2)]]/100,2)
                    mao = f'Trinca de {valores2[jogos[round(pontos[0]%1, 2)]]}'
                elif combinações == 2 and par == 2:
                    resultado = 3 + round(valores[jogos[round(pontos[0]%1, 2)]]/100,2) + round(valores[jogos[round(pontos[1]%1, 2)]]/10000,4)
                    mao = f'Dois Pares: {valores2[jogos[round(pontos[0]%1, 2)]]} e {valores2[jogos[round(pontos[1]%1, 2)]]}'
                elif combinações == 1 and par == 1:
                    resultado = 2 + round(valores[jogos[round(pontos[0]%1, 2)]]/100,2)
                    mao = f'Par de {valores2[jogos[round(pontos[0]%1, 2)]]}'
                elif combinações == 0:
                    resultado = 1 + round(valores[carta_alta] / 100, 2)
                    mao = f'Carta Alta {valores2[carta_alta]}'
    kicker = [round(ordem_final[1] / 1000000, 6), round(ordem_final[0] / 1000000, 6)]
    return mao, resultado, kicker

def PrintPadrão(jogador):
    if jogador == jogadores[1]:
        pdj = cartas_jogador1
        aposta = aposta_jogador[1]
        outro_jogador = jogadores[0]
        aposta_outro = aposta_jogador[0]
    else:
        pdj = cartas_jogador2
        aposta = aposta_jogador[0]
        outro_jogador = jogadores[1]
        aposta_outro = aposta_jogador[1]
    print(f'''Suas Cartas: {pdj[0][0]}{pdj[0][1]}, {pdj[1][0]}{pdj[1][1]}
Cartas do {outro_jogador}: ░,  ░''')
    Printmesa()
    print(f'''Seu Dinheiro: {banca_total[jogadores.index(jogador)]:.0f}
Dinheiro do {outro_jogador}: {banca_total[jogadores.index(outro_jogador)]:.0f}
Sua Aposta: {aposta:.0f}
Aposta do {outro_jogador}: {aposta_outro:.0f}
Pote: {pote[0]:.0f}
''')

def PadrãoJogador(jogador):
    LimparConsole()
    verificador = False
    verificador2 = False
    ultimo_jogador[0] = jogador
    if jogador == jogadores[1]:
        pdj = cartas_jogador1
        aposta = aposta_jogador[1]
        outro_jogador = jogadores[0]
        aposta_outro = aposta_jogador[0]
        banca_jogador = banca_total[1]
        banca_outro = banca_total[0]
    else:
        pdj = cartas_jogador2
        aposta = aposta_jogador[0]
        outro_jogador = jogadores[1]
        aposta_outro = aposta_jogador[1]
        banca_jogador = banca_total[0]
        banca_outro = banca_total[1]
    if jogador != 'Bot':
        Espaço()
        if modo_de_jogo == 1:
            print(f'Turno do {jogador}')
        else: 
            print('Seu turno')
        Espaço()
        input('Aperte ENTER para ver suas cartas')
        LimparConsole()
        PrintPadrão(jogador)
    else:
        Devagarin('Bot está jogando')
        LimparConsole()      
        resultado = calculo(mesa, pdj)[1]

    if banca_total[jogadores.index(jogador)] == 0:
        if jogador != 'Bot':
            escolha = input('Aperte ENTER para passar: ')
    else:
        if aposta < aposta_outro and banca_total[jogadores.index(outro_jogador)] > 0 and aposta + banca_jogador > aposta_outro:
            while verificador == False:
                if jogador != 'Bot':
                    escolha = input('Deseja Aumentar, Pagar ou Desistir? (A/P/D): ')
                    escolha = escolha.upper()
                else:
                    if resultado < 2:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 25:
                            escolha = 'D'
                        elif chance > 25 and chance <= 75:
                            escolha = 'P'
                        else:
                            escolha = 'A'
                    elif resultado > 2 and resultado < 3:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 15:
                            escolha = 'D'
                        elif chance > 15 and chance <= 75:
                            escolha = 'P'
                        else:
                            escolha = 'A'
                    elif resultado > 3 and resultado < 4:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 10:
                            escolha = 'D'
                        elif chance > 10 and chance <= 60:
                            escolha = 'P'
                        else:
                            escolha = 'A'
                    elif resultado > 4 and resultado < 5:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 40:
                            escolha = 'P'
                        else:
                            escolha = 'A'
                    elif resultado >= 5:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 10:
                            escolha = 'P'
                        else:
                            escolha = 'A'                  
                if escolha == 'A':
                    while verificador2 == False:
                        try:                           
                            if jogador != 'Bot':
                                novo_valor = int(input('Digite o valor da aposta: '))
                            else:
                                aposta_blefe = random.randint(1,100)
                                if banca_jogador < banca_outro:
                                    if aposta_blefe > 0 and aposta_blefe <= 20:
                                        novo_valor = random.randint(aposta_outro - aposta + 1, aposta_outro - aposta + round(banca_jogador*15/100,0))
                                    elif aposta_blefe > 20 and aposta_blefe <= 40:
                                        novo_valor = random.randint(aposta_outro - aposta + round(banca_jogador*45/100,0), aposta_outro - aposta + round(banca_jogador*85/100,0))
                                    else:
                                        if resultado < 2:
                                            novo_valor = random.randint(aposta_outro - aposta + 1, aposta_outro - aposta + round(banca_jogador*10/100,0))
                                        elif resultado > 2 and resultado < 3:
                                            novo_valor = random.randint(aposta_outro - aposta + round(banca_jogador*5/100,0), aposta_outro - aposta + round(banca_jogador*15/100,0))
                                        elif resultado > 3 and resultado < 4:
                                            novo_valor = random.randint(aposta_outro - aposta + round(banca_jogador*10/100,0), aposta_outro - aposta + round(banca_jogador*25/100,0))
                                        elif resultado > 4 and resultado < 5:
                                            novo_valor = random.randint(aposta_outro - aposta + round(banca_jogador*25/100,0), aposta_outro - aposta + round(banca_jogador*80/100,0))
                                        elif resultado >= 5:
                                            novo_valor = random.randint(aposta_outro - aposta + round(banca_jogador*50/100,0), banca_jogador)
                                else:
                                    if aposta_blefe > 0 and aposta_blefe <= 20:
                                        novo_valor = random.randint(aposta_outro - aposta + 1, aposta_outro - aposta + round(banca_outro*15/100,0))
                                    elif aposta_blefe > 20 and aposta_blefe <= 40:
                                        novo_valor = random.randint(aposta_outro - aposta + round(banca_outro*45/100,0), aposta_outro - aposta + round(banca_outro*85/100,0))
                                    else:
                                        if resultado < 2:
                                            novo_valor = random.randint(aposta_outro - aposta + 1, aposta_outro - aposta + round(banca_outro*10/100,0))
                                        elif resultado > 2 and resultado < 3:
                                            novo_valor = random.randint(aposta_outro - aposta + round(banca_outro*5/100,0), aposta_outro - aposta + round(banca_outro*15/100,0))
                                        elif resultado > 3 and resultado < 4:
                                            novo_valor = random.randint(aposta_outro - aposta + round(banca_outro*10/100,0), aposta_outro - aposta + round(banca_outro*25/100,0))
                                        elif resultado > 4 and resultado < 5:
                                            novo_valor = random.randint(aposta_outro - aposta + round(banca_outro*25/100,0), aposta_outro - aposta + round(banca_outro*80/100,0))
                                        elif resultado >= 5:
                                            novo_valor = random.randint(aposta_outro + round(banca_outro*50/100,0), banca_outro)
                                if novo_valor == 0:
                                    novo_valor = 1 + aposta_outro - aposta
                            if novo_valor <= banca_jogador and novo_valor <= banca_outro + aposta_outro - aposta:
                                if novo_valor > (aposta_outro - aposta):
                                    banca_total[jogadores.index(jogador)] -= novo_valor
                                    pote[0] += novo_valor
                                    aposta_jogador[aposta_jogador.index(aposta)] += novo_valor
                                    PadrãoJogador(outro_jogador)
                                    verificador2 = True
                                    verificador = True 
                                else:
                                    LimparConsole()
                                    PrintPadrão(jogador) 
                                    print('Valor da aposta não deve ser menor que a aposta de seu oponente')
                            else:
                                LimparConsole()
                                PrintPadrão(jogador) 
                                print('Valor da aposta não deve exceder sua banca ou a de seu oponente')
                        except:
                            if jogador != 'Bot':
                                LimparConsole()
                                PrintPadrão(jogador)                    
                                print('ERRO: Escolha um valor válido')
                elif escolha == 'D':
                    LimparConsole()
                    Espaço()
                    print(f'♥  ♦  ♣  ♠  {outro_jogador} ganha o pote com {pote[0]} fichas   ♠  ♣  ♦  ♥\n')
                    banca_total[jogadores.index(outro_jogador)] += pote[0]
                    desistir[0] = 1
                    verificador = True
                elif escolha == 'P':
                    novo_valor = aposta_outro - aposta
                    banca_total[jogadores.index(jogador)] -= novo_valor
                    pote[0] += novo_valor
                    aposta_jogador[aposta_jogador.index(aposta)] += novo_valor
                    verificador = True
                else:
                    LimparConsole()
                    PrintPadrão(jogador)                    
                    print('ERRO: Escolha uma opção válida')
        elif aposta < aposta_outro and banca_total[jogadores.index(outro_jogador)] <= 0 or aposta + banca_jogador == aposta_outro:
            while verificador == False:             
                if jogador != 'Bot':
                    escolha = input('Deseja Pagar ou Desistir? (P/D): ')
                    escolha = escolha.upper()
                else:
                    if resultado < 2:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 80:
                            escolha = 'D'
                        else:
                            escolha = 'P'
                    elif resultado > 2 and resultado < 3:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 80:
                            escolha = 'D'
                        else:
                            escolha = 'P'
                    elif resultado > 3 and resultado < 4:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 60:
                            escolha = 'D'
                        else:
                            escolha = 'P'
                    elif resultado > 4 and resultado < 5:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 10:
                            escolha = 'D'
                        else:
                            escolha = 'P'
                    elif resultado >= 5:                       
                        escolha = 'P'                            
                if escolha == 'D':
                    LimparConsole()
                    Espaço()
                    print(f'♥  ♦  ♣  ♠  {outro_jogador} ganha o pote com {pote[0]} fichas   ♠  ♣  ♦  ♥\n')
                    banca_total[jogadores.index(outro_jogador)] += pote[0]
                    desistir[0] = 1
                    verificador = True
                elif escolha == 'P':
                    novo_valor = aposta_outro - aposta
                    banca_total[jogadores.index(jogador)] -= novo_valor
                    pote[0] += novo_valor
                    aposta_jogador[aposta_jogador.index(aposta)] += novo_valor
                    verificador = True
                else:
                    LimparConsole()
                    PrintPadrão(jogador)                    
                    print('ERRO: Escolha uma opção válida')
        elif aposta == aposta_outro and banca_total[jogadores.index(outro_jogador)] <= 0:
            if jogador != 'Bot':
                escolha = input('Aperte ENTER para passar: ')
        else:
            while verificador == False:                
                if jogador != 'Bot':
                    escolha = input('Deseja Aumentar ou Passar? (A/P): ')
                    escolha = escolha.upper()
                else: 
                    if resultado < 2:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 30:
                            escolha = 'A'
                        else:
                            escolha = 'P'
                    elif resultado > 2 and resultado < 3:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 35:
                            escolha = 'A'
                        else:
                            escolha = 'P'
                    elif resultado > 3 and resultado < 4:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 50:
                            escolha = 'A'
                        else:
                            escolha = 'P'
                    elif resultado > 4 and resultado < 5:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 70:
                            escolha = 'A'
                        else:
                            escolha = 'P'
                    elif resultado >= 5:
                        chance = random.randint(1,100)
                        if chance > 0 and chance <= 90:
                            escolha = 'A'
                        else:                            
                            escolha = 'P'  
                if escolha == 'A':
                    while verificador2 == False:
                        try:
                            if jogador != 'Bot':
                                novo_valor = int(input('Digite o valor da aposta: '))
                            else:
                                aposta_blefe = random.randint(1,100)
                                if banca_jogador < banca_outro:
                                    if aposta_blefe > 0 and aposta_blefe <= 20:
                                        novo_valor = random.randint(1, round(banca_jogador*15/100,0))
                                    elif aposta_blefe > 20 and aposta_blefe <= 40:
                                        novo_valor = random.randint(round(banca_jogador*45/100,0), round(banca_jogador*85/100,0))
                                    else:
                                        if resultado < 2:
                                            novo_valor = random.randint(1, round(banca_jogador*10/100,0))
                                        elif resultado > 2 and resultado < 3:
                                            novo_valor = random.randint(round(banca_jogador*5/100,0), round(banca_jogador*15/100,0))
                                        elif resultado > 3 and resultado < 4:
                                            novo_valor = random.randint(round(banca_jogador*10/100,0), round(banca_jogador*25/100,0))
                                        elif resultado > 4 and resultado < 5:
                                            novo_valor = random.randint(round(banca_jogador*25/100,0), round(banca_jogador*80/100,0))
                                        elif resultado >= 5:
                                            novo_valor = random.randint(round(banca_jogador*50/100,0), banca_jogador)
                                else:
                                    if aposta_blefe > 0 and aposta_blefe <= 20:
                                        novo_valor = random.randint(1, round(banca_outro*15/100,0))
                                    elif aposta_blefe > 20 and aposta_blefe <= 40:
                                        novo_valor = random.randint(round(banca_outro*45/100,0), round(banca_outro*85/100,0))
                                    else:
                                        if resultado < 2:
                                            novo_valor = random.randint(1, round(banca_outro*10//100,0))
                                        elif resultado > 2 and resultado < 3:
                                            novo_valor = random.randint(round(banca_outro*5/100,0), round(banca_outro*15/100,0))
                                        elif resultado > 3 and resultado < 4:
                                            novo_valor = random.randint(round(banca_outro*10/100,0), round(banca_outro*25/100,0))
                                        elif resultado > 4 and resultado < 5:
                                            novo_valor = random.randint(round(banca_outro*25/100,0), round(banca_outro*80/100,0))
                                        elif resultado >= 5:
                                            novo_valor = random.randint(round(banca_outro*50/100,0), banca_outro)
                                if novo_valor == 0:
                                    novo_valor = 1
                            if novo_valor <= banca_total[0] and novo_valor <= banca_total[1]:
                                if novo_valor > 0:
                                    banca_total[jogadores.index(jogador)] -= novo_valor
                                    pote[0] += novo_valor
                                    aposta_jogador[jogadores.index(jogador)] += novo_valor
                                    PadrãoJogador(outro_jogador)
                                    verificador2 = True
                                    verificador = True 
                                else:
                                    LimparConsole()
                                    PrintPadrão(jogador)  
                                    print('Valor da aposta não deve ser menor que a aposta de seu oponente')
                            else:
                                LimparConsole()
                                PrintPadrão(jogador) 
                                print('Valor da aposta não deve exceder sua banca ou a de seu oponente')                            
                        except:
                            if jogador != 'Bot':
                                LimparConsole()
                                PrintPadrão(jogador)                    
                                print('ERRO: Escolha um valor válido')
                elif escolha == 'P':
                    verificador = True 
                else:
                    LimparConsole()
                    PrintPadrão(jogador)                    
                    print('ERRO: Escolha uma opção válida')

def Printmesa():
    if len(mesa) == 0:
        print('Cartas na mesa: ░, ░, ░, ░, ░')
    elif len(mesa) == 3:
        print(f'Cartas na mesa: {mesa[0][0]}{mesa[0][1]}, {mesa[1][0]}{mesa[1][1]}, {mesa[2][0]}{mesa[2][1]}, ░, ░')
    elif len(mesa) == 4:
        print(f'Cartas na mesa: {mesa[0][0]}{mesa[0][1]}, {mesa[1][0]}{mesa[1][1]}, {mesa[2][0]}{mesa[2][1]}, {mesa[3][0]}{mesa[3][1]}, ░')
    elif len(mesa) >= 5:
        print(f'Cartas na mesa: {mesa[0][0]}{mesa[0][1]}, {mesa[1][0]}{mesa[1][1]}, {mesa[2][0]}{mesa[2][1]}, {mesa[3][0]}{mesa[3][1]}, {mesa[4][0]}{mesa[4][1]}')

def Frufru(nome,num):
    print(' ♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠')
    sleep(0.2)
    for _ in range(3):
        print('')
        sleep(0.2)
    print(f"♥  ♦  ♣  ♠   {nome}    ♠   ♣  ♦  ♥")
    sleep(0.2)
    if num == 1:
        print('     Um jogo em Python por Eduardo Cunha Santiago')
        sleep(0.2)
        for _ in range(2):
            print('')
            sleep(0.2)
    else:
         for _ in range(3):
            print('')
            sleep(0.2)
    print('♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠  ♥  ♦  ♣  ♠')
    sleep(0.5)
    Ok()
    LimparConsole()

def Devagarin(nome):
    LimparConsole()
    Espaco4()
    print(f'{nome}.')
    sleep(0.7)
    LimparConsole()
    Espaco4()
    print(f'{nome}..')
    sleep(0.7)
    LimparConsole()
    Espaco4()
    print(f'{nome}...')
    sleep(0.7)
    LimparConsole()
    sleep(0.7)

def Inicio():
    LimparConsole()
    Espaço()
    print(f'{jogadores[0]} começa')
    Espaço()
    Ok()

def ApostaMaxima():
    if banca_total[0] == 0:
        aposta_jogador[1] = aposta_jogador[0]
        banca_total[1] -= aposta_jogador[1]

    if banca_total[1] == 0:
        aposta_jogador[0] = aposta_jogador[1]
        banca_total[0] -= aposta_jogador[0]

def Calculo_banca():
    if banca_total[1] < blind[1]:
        if banca_total[0] < blind[0]:
            if banca_total[1] < banca_total[0]:
                pote[0] += banca_total[1]*2
                aposta_jogador[1] = banca_total[1]
                aposta_jogador[0] = aposta_jogador[1]
                banca_total[0] -= aposta_jogador[0]
                banca_total[1] = 0
            else:
                pote[0] += banca_total[0]*2
                aposta_jogador[0] = banca_total[0]
                aposta_jogador[1] = aposta_jogador[0]
                banca_total[1] -= aposta_jogador[1]
                banca_total[0] = 0
        else:
            pote[0] += banca_total[1]*2
            aposta_jogador[1] = banca_total[1]
            aposta_jogador[0] = aposta_jogador[1]
            banca_total[0] -= aposta_jogador[0]
            banca_total[1] = 0
    else:        
        if banca_total[0] < blind[0]:
             pote[0] += banca_total[0]*2
             aposta_jogador[0] = banca_total[0]
             aposta_jogador[1] = aposta_jogador[0]
             banca_total[1] -= aposta_jogador[1]
             banca_total[0] = 0
        if banca_total[0] >= blind[0]: 
            aposta_jogador[1] = blind[1]
            banca_total[1] -= aposta_jogador[1]
            ApostaMaxima()
            pote[0] += aposta_jogador[1]   
            aposta_jogador[0] = blind[0]
            banca_total[0] -= aposta_jogador[0]
            ApostaMaxima()
            pote[0] += aposta_jogador[0]
    if banca_total[0] + aposta_jogador[0] < aposta_jogador[1]:
        pote[0] -= aposta_jogador[1]
        aposta_jogador[1] = banca_total[0] + aposta_jogador[0]
        pote[0] += aposta_jogador[1]
    elif banca_total[1] + aposta_jogador[1] < aposta_jogador[0]:
        pote[0] -= aposta_jogador[0]
        aposta_jogador[0] = banca_total[1] + aposta_jogador[1]
        pote[0] += aposta_jogador[0]

jogar = 'S'
while jogar == 'S':
    LimparConsole()
    valores = {"2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14}
    valores2 = {"2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":'Valete',
    "Q":'Dama',
    "K":'Rei',
    "A":'Ás'}
    valores3 = {2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    'Valete':11,
    'Dama':12,
    'Rei':13,
    'Ás':14}
    naipes = {'♣':1,
            '♥':2,
            '♠':3,
            '♦':4}

    nova_lista_chave = list(valores3.keys())
    novo_valores = list(valores3.values())
    jogadores = []
    cartas_jogador1, cartas_jogador2, mesa, nova_carta, nova_carta2 = [], [], [], [], []
    banca_total = [500, 500]
    jogadores_fora = []
    jogadores_ordem = []
    outro_jogador, aposta_outro = [], 0
    blind, blind1, blind2, blind3, blind4, blind5 = [], [15, 30], [25, 50], [50, 75], [75, 100], [100, 200]
    cont_blind = 0
    pote = [0]
    aposta_jogador = [0, 0]
    desistir = [0]
    ultimo_jogador = ['']

    Frufru("Bem Vindo ao Poker Texas Hold'em", 1)

    verificador_mdj = False
    while verificador_mdj == False:
        try:
            modo_de_jogo = int(input('''
        \n
                        ╔═════════════════════════╗
                        ║ 1. Jogador X Jogador    ║
                        ║ 2. Jogador X Computador ║
                        ╚═════════════════════════╝
        \n\n
Escolha seu modo de jogo: '''))
            if modo_de_jogo == 1 or modo_de_jogo == 2:
                verificador_mdj = True
            LimparConsole()
        except:
            LimparConsole()
            continue
    if modo_de_jogo == 1:
        print("\n\n\n\n")
        verificador_nome1 = False
        while verificador_nome1 == False:
            try:
                jogador1 = input('Digite o Primeiro Nome: ')
                if jogador1 != '' and jogador1 != 'Bot':
                    verificador_nome1 = True
                else:
                    LimparConsole()          
                    print('\n\n\n\nNome inválido')
            except:
                continue
        LimparConsole()
        print(f'\n\n\n\nDigite o Primeiro Nome: {jogador1}')
        verificador_nome2 = False
        print('\n')
        while verificador_nome2 == False:
            try:
                jogador2 = input('Digite o Segundo Nome: ')
                if jogador2 != '' and jogador2 != jogador1 and jogador2 != 'Bot':
                    verificador_nome2 = True
                else:
                    LimparConsole()
                    print(f'\n\n\n\nDigite o Primeiro Nome: {jogador1}\n')
                    print('Nome inválido')
            except:
                continue
    else:
        print("\n\n\n\n")
        verificador_nome1 = False
        while verificador_nome1 == False:
            try:
                jogador1 = input('Digite o Seu Nome: ')
                if jogador1 != '' and jogador1 != 'Bot':
                    verificador_nome1 = True
                else:
                    LimparConsole()          
                    print('\n\n\n\nNome inválido')
            except:
                continue
        jogador2 = 'Bot'
        LimparConsole()

    Devagarin('Sorteando')

    aleatorio = random.randint(0, 1)
    if aleatorio == 0:
        jogadores.append(jogador1)
        jogadores.append(jogador2)
    else:
        jogadores.append(jogador2)
        jogadores.append(jogador1)

    while banca_total[0] > 0 and banca_total[1] > 0:
        LimparConsole()
        baralho = Cartesiano(valores, naipes)
        cartas_jogador1 = DarCartas(cartas_jogador1)
        cartas_jogador2 = DarCartas(cartas_jogador2)
        jogadores.reverse()
        banca_total.reverse()
        tem_kicker = False
        kicker_final1 = 0
        kicker_final2 = 0
        Espaço()
        if cont_blind < 1:
            blind = blind1
            print(f'As Blinds começam com {blind1}')
        elif cont_blind < 2 and cont_blind >= 1:
            blind = blind2
            print(f'As Blinds sobem para {blind2}')
        elif cont_blind < 3 and cont_blind >= 2:
            blind = blind3
            print(f'As Blinds sobem para {blind3}')
        elif cont_blind < 4 and cont_blind >= 3:
            blind = blind4
            print(f'As Blinds sobem para {blind4}')
        elif cont_blind >= 4 and cont_blind < 5:
            blind = blind5
            print(f'As Blinds sobem para {blind5}')
        elif cont_blind >= 5:
            blind = blind5
        Espaço()
        Ok()
        LimparConsole()
        Calculo_banca()
        Inicio()

        if ultimo_jogador[0] != jogadores[0]:
            PadrãoJogador(jogadores[0])
            turno_pulado = 1
        if ultimo_jogador[0] != jogadores[1] and desistir[0] != 1:
            PadrãoJogador(jogadores[1])
        if turno_pulado == 0 and desistir[0] != 1:
            PadrãoJogador(jogadores[0])

        mesa = CartasMesa(mesa)
        turno_pulado = 0
        if desistir[0] != 1:
            for _ in range(3):
                if ultimo_jogador[0] != jogadores[0]:
                    PadrãoJogador(jogadores[0])
                    turno_pulado = 1
                if desistir[0] == 1:
                    break
                if ultimo_jogador[0] != jogadores[1]:
                    PadrãoJogador(jogadores[1])
                if desistir[0] == 1:
                    break
                if turno_pulado == 0:
                    PadrãoJogador(jogadores[0])
                if len(mesa) < 5:
                    NovaCarta()
                turno_pulado = 0
        if desistir[0] == 0:
            LimparConsole()
            Devagarin('Calculando Resultado')
            LimparConsole()
            func_jogador1 = calculo(mesa, cartas_jogador1)
            func_jogador2 = calculo(mesa, cartas_jogador2)
            resultado1 = func_jogador1[1]
            resultado2 = func_jogador2[1]
            kicker1 = func_jogador1[2]
            kicker2 = func_jogador2[2]
            Printmesa()
            print(f'Cartas do {jogadores[1]}: {cartas_jogador1[0][0]}{cartas_jogador1[0][1]}, {cartas_jogador1[1][0]}{cartas_jogador1[1][1]}')
            print(f'Cartas do {jogadores[0]}: {cartas_jogador2[0][0]}{cartas_jogador2[0][1]}, {cartas_jogador2[1][0]}{cartas_jogador2[1][1]}')
            if resultado1 == resultado2:
                if kicker1[0] == kicker2[0]:
                    kicker_final1 = kicker1[1]
                    kicker_final2 = kicker2[1]
                else:     
                    kicker_final1 = kicker1[0]
                    kicker_final2 = kicker2[0]
                resultado1 += kicker_final1
                resultado2 += kicker_final2
                tem_kicker = True
                nova_posicao1 = novo_valores.index(kicker_final1*1000000)
                nova_posicao2 = novo_valores.index(kicker_final2*1000000)
            if resultado1 > resultado2:
                if tem_kicker == True:
                    print(f'\n{jogadores[1]} vence pote de {pote[0]} com {func_jogador1[0]} + {nova_lista_chave[nova_posicao1]} Kicker')
                else:
                    print(f'\n{jogadores[1]} vence pote de {pote[0]} com {func_jogador1[0]}')
                print(f'{jogadores[0]} tem {func_jogador2[0]}')
                banca_total[1] += pote[0]
            elif resultado2 > resultado1:
                if tem_kicker == True:
                    print(f'\n{jogadores[0]} vence pote de {pote[0]} com {func_jogador2[0]} + {nova_lista_chave[nova_posicao2]} Kicker')
                else:
                    print(f'\n{jogadores[0]} vence pote de {pote[0]} com {func_jogador2[0]}')
                print(f'{jogadores[1]} tem {func_jogador1[0]}')
                banca_total[0] += pote[0]
            else:
                print('\nEmpate, os jogadores dividem o pote')
                print(f'{jogadores[0]} tem {func_jogador1[0]}')
                print(f'{jogadores[1]} tem {func_jogador2[0]}')
                banca_total[0] += pote[0]/2
                banca_total[1] += pote[0]/2
        print('\n\n')
        Ok()
        desistir[0] = 0
        cartas_jogador1.clear()
        cartas_jogador2.clear()
        mesa.clear()
        pote[0] = 0
        cont_blind += 1
        ultimo_jogador[0] = ' '
        LimparConsole()

    if banca_total[0] == 0:
        Frufru(f'♥  ♦  ♣  ♠  {jogadores[1]} vence o jogo  ♠  ♣  ♦  ♥', 2)
    elif banca_total[1] == 0:
        Frufru(f'♥  ♦  ♣  ♠  {jogadores[0]} vence o jogo  ♠  ♣  ♦  ♥', 2)

    LimparConsole()
    verificador_jogar = False
    while verificador_jogar == False:
        try:
            Espaço()
            jogar = input('Deseja jogar novamente? (S/N): ')
            jogar = jogar.upper()
            if jogar == 'S' or jogar == 'N':
                verificador_jogar = True
        except:
            continue
        LimparConsole()
    LimparConsole()

for _ in range(6):
    LimparConsole()
    print('''

    ♦      ♠      ♦      ♠      ♦      ♠      ♦      ♠       
♥      ♣      ♥      ♣      ♥      ♣      ♥      ♣      
    
                  OBRIGADO POR JOGAR
                        
    ♦      ♠      ♦      ♠      ♦      ♠      ♦      ♠       
♥      ♣      ♥      ♣      ♥      ♣      ♥      ♣        ''')
    sleep(0.2)
    LimparConsole()
    print('''

♥      ♣      ♥      ♣      ♥      ♣      ♥      ♣      
    ♦      ♠      ♦      ♠      ♦      ♠      ♦      ♠      
        
                  OBRIGADO POR JOGAR
                        
♥      ♣      ♥      ♣      ♥      ♣      ♥      ♣      
    ♦      ♠      ♦      ♠      ♦      ♠      ♦      ♠     ''')
    sleep(0.2)
