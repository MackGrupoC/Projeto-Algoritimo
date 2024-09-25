preco_base_1 = 20
preco_base_2 = 15
preco_base_3 = 10


media_f1 = 0
it_f1 = 0
media_f2 = 0
it_f2 = 0
media_f3 = 0
it_f3 = 0

f1_s1 = 0  
f1_s2 = 0 
f2_s1 = 0 
f2_s2 = 0
f3_s1 = 0
f3_s2 = 0 

capacidade_f1 = 50
capacidade_f2 = 40 
capacidade_f3 = 30


relatorio = ""

while (True):

    print("Filmes disponíveis: Filme 1, Filme 2 e Filme 3")

    t_filme=input("Qual filme deseja assistir? ")

    print("Escolha entre sessão 1 e 2")

    sessao=int(input("Qual a sessão:"))
    while (sessao >= 3) or (sessao < 1):
        sessao = int(input("Digite uma sessão válida:" ))

    print("Os tipos de ingresso são: Inteira, Meia e VIP ")

    inteira_1=int(input("Quantas entradas inteiras:" ))
    meia_1=int(input("Quantas entradas meia:" ))
    vip_1=int(input("Quantas entradas vip:" ))

    soma_inteira=0
    soma_meia=0
    soma_vip=0
    soma_filme=""
    
    inteira=inteira_1
    meia=meia_1
    vip=vip_1

    if t_filme.lower() == "filme 1":
        if sessao == 1:
            f1_s1 += (inteira_1 + meia_1 + vip_1)
        elif sessao == 2:
            f1_s2 += (inteira_1 + meia_1 + vip_1)

        if f1_s1 > capacidade_f1 or f1_s2 > capacidade_f1:
            print("Capacidade acima do limite, Descartando os Ingressos ")
            continue

    if t_filme.lower() == "filme 2":
        if sessao == 1:
            f2_s1 += (inteira_1 + meia_1 + vip_1)
        elif sessao == 2:
            f2_s2 += (inteira_1 + meia_1 + vip_1)

        if f2_s2 > capacidade_f1 or f2_s2 > capacidade_f1:
            print("Capacidade acima do limite, Descartando os Ingressos ")
            continue

    if t_filme.lower() == "filme 3":
        if sessao == 1:
            f3_s1 += (inteira_1 + meia_1 + vip_1)
        elif sessao == 2:
            f3_s2 += (inteira_1 + meia_1 + vip_1)

        if f3_s1 > capacidade_f1 or f3_s2 > capacidade_f1:
            print("Capacidade acima do limite, Descartando os Ingressos ")
            continue

    print("Avalie o filme de 1 a 5 estrelas")
    
    avaliacao = int(input("Qual a avaliação desse filme:" ))

    inte1 = 0
    mei1 = 0
    vp1 = 0
    
    inte2 = 0
    mei2 = 0
    vp2 = 0
    
    inte3 = 0
    mei3 = 0
    vp3 = 0
    
    if t_filme.lower() == "filme 1":
        media_f1 += avaliacao
        it_f1 += 1

    elif t_filme.lower() == "filme 2":
        media_f2 += avaliacao
        it_f2 += 1

    elif t_filme.lower() == "filme 3":
        media_f3 += avaliacao
        it_f3 += 1

    if (t_filme.lower() == "filme 1" ):

        inteira = preco_base_1 * inteira 
        meia = (meia * preco_base_1) / 2
        vip = (vip * preco_base_1) * 1.5 
        
    elif (t_filme.lower() == "filme 2" ):
        
        inteira *= preco_base_2 
        meia = (meia * preco_base_2) / 2 
        vip = (vip * preco_base_2) * 1.5
            
    elif (t_filme.lower() == "filme 3" ):

        inteira *= preco_base_3
        meia = (meia * preco_base_3) / 2 
        vip = (vip * preco_base_3) * 1.5
        
    endloop = input ("Deseja encerrar o atendimento:" )

    inte1 = inteira 
    mei1 = meia 
    vp1 = vip 
    
    inte2 = (inteira + inte1)
    mei2 = (meia + mei1)
    vp2 = (vip + vp1)
    
    inte3 = (inteira+inte2)
    mei3 = (meia+mei2)
    vp3 = (vip+vp2)
   

    
    relatorio += f"""
{t_filme} - Sessão {sessao}: 
Quantidade de ingressos vendidos
-Inteira: {inteira_1}
-Meia:{meia_1}
-VIP:{vip_1}
Receita por tipo (Sessão {sessao})
- Inteira: R$ {inteira:.2f}
- Meia: R$ {meia:.2f}
- VIP: R$ {vip:.2f}\n
    """
    
    if (endloop.lower() == "sim"):
        print(relatorio)
        print ("Média de avaliações:\n")

        if it_f1 > 0:
            print (f"Filme 1: {round(media_f1 / it_f1 )}" )
            relatorio += f"Filme 1: {round(media_f1 / it_f1 )}"
        if it_f2 > 0:
            print (f"Filme 2: {round(media_f2 / it_f2)}" )
            relatorio += f"Filme 2: {round(media_f2 / it_f2)}"
        if it_f3 > 0: 
            print (f"Filme 3: {round(media_f3 / it_f3 )}\n" )
            relatorio += f"Filme 3: {round(media_f3 / it_f3 )}"
        print (f"Total de ingresso vendidos: {f1_s1 + f1_s2 + f2_s1 + f2_s2 + f3_s1 + f3_s2}")
        print (f"Receita total do dia: R$ { inte3 + mei3 + vp3 }\n")
        print (inte1)
        print (mei1)
        print (vp1)
        
        print (inte2)
        print (mei2)
        print (vp2)
        
        print (inte3)
        print (mei3)
        print (vp3)
    
        break
                
   
   


