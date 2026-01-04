# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Professora Sofia", color="#20a7b2")
define m = Character("Mia", color="#8a93a2")
define t = Character("Tomás", color="#403b3b")
define pm = Character("Professor Lopes", color="#403b3b")
define eu = Character("Guardião do Conhecimento", color="#b22020")
define dr = Character("Dr. Caos", color="#000000ff")
define j = Character("[player_name]")

label start:
    play music "audio/inicio.mp3"

    "Antes de comerçar o jogo, preciso de fazer-te uma pergunta"

# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

    $ player_name = renpy.input("Como é que te chamas?")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="jogador"

# And get a nostalgic sigh from Seasons of Sakura fans!
    
# Now the other characters in the game can greet the player.
  
    "É um prazer conhecer-te, %(player_name)s!"

    scene bg corredor
    with dissolve
    
    "Era uma manhã normal na Escola do Saber, até que algo estranho aconteceu."

    scene bg aula
    with dissolve
    show professora neutro

    s " Bom dia, turma! Antes de começarmos, preciso da vossa atenção."

    j "O que se passa, professora?"

    hide professora neutro
    show professora preocupada
    play music "audio/triste.mp3"
    s "O Livro do Saber desapareceu da biblioteca!"
 
    show mia preocupada at right with moveinright

    m "O livro mágico? Aquele que ajuda toda a escola?"

    show tomas preocupado at left with moveinleft

    t "Sem ele, nada vai funcionar direito…"

    menu: 
        "Vou ajudar a encontrar o livro!":
            jump one
        "Tenho um pouco de medo…":
            jump two

    label one:
        play music "audio/mingle.mp3"
        j "Conte comigo, professora. Quero ajudar."
        hide professora preocupada
        show professora happy
        hide mia preocupada
        with dissolve
        hide tomas preocupado
        with dissolve
        s "Fico muito orgulhosa de ti."
        jump chapter2
        with fade

    label two:
        play music "audio/squid.mp3"
        j "Nunca fiz isto antes… mas posso tentar."
        hide professora preocupada
        show professora neutro
        hide mia preocupada
        with dissolve
        hide tomas preocupado
        s "Ter medo é normal. O importante é tentar."
        jump chapter2
        

    label chapter2:
        hide professora neutro
        hide professora happy
        with fade
        show mia preocupada
        m "olhe professora, o quadro está a apagar-se sozinho!"
        show mia preocupada at right with move
        show professora neutro with dissolve
        s "é um enigma! vamos meninos, ainda conseguimos salvar a escola!"

        scene bg quadro
        with fade
        play music "audio/kahoot.mp3"
        t "é impressão minha ou falta alguma coisa na frase?"

        s "Tens toda a razão Tomás"
        s "Para avançarmos, precisamos de organizar as palavras."
        s "Qual é a forma correta da frase?"

    menu:
        "Nós estudámos ontem para o teste.":
            jump chapter3
        "Nós estudamos ontem para o teste.":
            jump chapter2bad

    label chapter2bad:
        s "Ambas as formas estão corretas"
        s "mas são usadas em tempos verbais diferentes"
        s "estudamos é o Presente do Indicativo (nós estudamos)"
        s "enquanto estudámos é o Pretérito Perfeito (nós estudámos)"
        scene bg aula
        with fade
        show professora preocupada with dissolve
        s "infelizmente falhamos a nossa missão..."
        stop music
        play sound "audio/perdeu.mp3"
        s "isto quer dizer que o jogo acaba aqui para ti %(player_name)s..."
        scene bg endgame
        "Sugiro que Tentes outra vez"
        return


    label chapter3:

        scene quadro_feito with dissolve
        play music "audio/certo.mp3"
        s " Muito bem!"
        s "Ambas as formas estão corretas"
        s "mas são usadas em tempos verbais diferentes"
        s "estudamos é o Presente do Indicativo (nós estudamos)"
        s "enquanto estudámos é o Pretérito Perfeito (nós estudámos)"
        s "As palavras estão novamente em ordem"
        

    scene bg corredor
    with dissolve
    stop music
    play sound "audio/grito.mp3"
    "HAAAAAAAAAA"

    scene bg aula
    with dissolve
    play music "audio/theme.mp3"
    show tomas preocupado with dissolve
    t "parecia a voz do professor Lopes"
    show tomas preocupado at left with move
    show mia preocupada with dissolve
    m "rápido! vamos ajudar o professor!"
    show tomas preocupado at offscreenleft with move
    show mia preocupada at offscreenleft with move

    scene bg corredor
    with fade
    show mia happy at center with moveinright

    m "Vamos! a sala do professor Lopes é já ali!"

    show mia happy at offscreenleft with move

    scene bg aula1
    with fade
    show macho preocupado at center with dissolve
    pm "Meninos Ajudem-me!"
    pm "Algo de estranho está a acontecer!"
    show tomas preocupado at right with moveinright
    t "já sabemos professor."
    t "roubaram o livro do Saber!"
    hide macho preocupado
    show macho pensativo
    pm "Então já sei o que podem fazer para encontrarem o livro e restabelecer a paz!"
    pm "Quem roubou o livro mexeu nos números!"
    scene conta_matematica
    with fade
    play music "audio/kahoot.mp3"
    pm "Se resolveres este problema, talvez consigas chegar mais perto de quem roubou o livro"
    pm "Quanto é 245 + 376?"

    $ secret_word = "621"

    label check_password:
        $ player_guess = renpy.input("Quanto é 245 + 376?").lower().strip()

        if player_guess == secret_word:
            play music "audio/certo.mp3"
            pm "Resposta certa"
            jump chapter4
        else:
            menu:
                "Não está certo..."
                "Queres tentar denovo?":
                    jump check_password
                "desistir":
                    stop music
                    play sound "audio/perdeu.mp3"
                    pm "falhaste a tua missão..."
                    pm "infelizmente o jogo acaba aqui para ti %(player_name)s..."
                    scene bg endgame
                    "Podias ter tentando denovo para conseguir ganhar o jogo"
                    return
    label chapter4:
        pm "muito bem"
        pm "Excelente raciocínio!"
        pm "Agora vão meninos, vejam se nas outras salas vocês conseguem encontrar outras pistas."

    scene bg corredor1 with fade
    play music "audio/mingle.mp3"
    show mia happy at center with moveinleft
    m "estou tão contente"
    m "estamos muito perto de descobrir onde está o livro"
    m "mas para onde vamos agora?"
    show tomas happy at left with moveinright
    t "ainda não fomos a duas salas."
    t "uma delas pode esconder uma pista!"
    play music "audio/kahoot.mp3"
    menu:
        "está nas tuas mãos escolher por onde seguir"
        "Sala da Esquerda":
            jump chapter_5
        "Sala da Direita":
            jump chapter_5
    label chapter_5:
    scene bg biblioteca with fade
    play music "audio/inicio.mp3"
    show eu confiante at center with dissolve
    eu "ainda bem que escolheram a sala certa"
    eu "estava mesmo à vossa espera"
    show mia happy at right with moveinright
    m "Desculpa a pergunta"
    m "mas quem és tu?"
    m "acho que nunca te vi pela escola"
    show mia happy at offscreenright with move
    hide eu confiante
    show eu cuscar at center 
    eu "eu sou o Guardião do Conhecimento"
    hide eu cuscar
    show eu falar2 at center
    eu "também sou o criador deste jogo"
    hide eu falar2
    show eu falar1 at center
    eu "mas essa parte não é importante."
    hide eu falar1
    show eu cuscar at center
    eu "Vocês para chegarem até aqui tiveram de passar por vários desafios"
    eu "Cada desafio refletiu uma matéria que vocês aprendem aqui na escola"
    eu "primeiro tiveram que responder a um enigma de Português"
    eu "depois um enigma de matemática"
    eu "mas vocês sabem que a escola não é só matéria."
    eu "Certo?"
    hide eu cuscar
    show eu confiante at center
    eu "O saber não é só estudar. É também saber sentir."
    eu "vocês os 3 chegaram até aqui em grupo."
    eu "chegaram aqui através do poder da amizade."
    play music "audio/kahoot.mp3"
    menu:
        "qual destas frases representa melhor a palavra amizade?"
        "Ajudar um amigo quando ele precisa, mesmo que dê trabalho.":
            play music "audio/certo.mp3"
            show eu confiante at center
            eu "Muito bem!"
            eu "A amizade é estar presente nos bons e maus momentos."
            jump capitulo6_correto

        "Falar apenas com quem nos dá coisas.":
            stop music
            play sound "audio/perdeu.mp3"
            hide eu confiante
            show eu zangado at center
            eu "Nem sempre, pensa melhor."
            eu "A amizade não é troca de favores."
            jump capitulo6_errado

        "Brincar sozinho sem ligar aos outros.":
            stop music
            play sound "audio/perdeu.mp3"
            hide eu confiante
            show eu zangado at center
            eu "A amizade precisa de partilha."
            eu "Vamos tentar outra vez."
            jump capitulo6_errado
    
    label capitulo6_errado:
    eu "é com muita pena minha"
    eu "mas vamos ter que trabalhar os teus valores de amizade."
    eu "infelizmente a vossa missão termina aqui..."
    eu "perdeste o jogo :("
    scene bg endgame
    "Final triste"
    return

    label capitulo6_correto:
    play music "audio/main_menu.mp3"
    show mia happy at right with moveinright
    m "Eu sabia que íamos conseguir!"

    show tomas happy at left with moveinleft
    t "Trabalhar em equipa fez toda a diferença."

    show eu confiante at center
    eu "E por isso, vocês provaram que estão prontos."

    eu "O verdadeiro saber constrói-se juntos."

    eu "Parabéns."

    hide eu confiante
    show eu cuscar at center
    eu "Cada desafio foi um teste."
    eu "Não às vossas respostas… mas às vossas escolhas."
    t "Então sempre soubeste onde estava o Livro?"
    eu "Sempre."
    eu "Mas só quem aprende em conjunto pode protegê-lo."
    eu "Agora, sigam-me."
    stop music

    scene bg cave with fade
    play music "audio/boss.mp3"
    show dr caos1 at center with dissolve
    play sound "audio/vilão.mp3"
    dr "Ahahahahaha!"
    dr "Finalmente chegaste!"
    dr "Poucos conseguem vir tão longe…"
    show mia preocupada at right with moveinright
    m "Ele é o Dr. Caos…"
    show tomas preocupado at left with moveinleft
    t "Foi ele que causou toda esta confusão na escola!"
    hide dr caos1
    show dr caos2 at center
    hide tomas preocupado with dissolve
    hide mia preocupada with dissolve
    play music "audio/triste.mp3"
    dr "Confusão?"
    dr "Eu só quis testar se vocês mereciam o Livro do Saber!"
    dr "Só o devolvo se responderes corretamente ao desafio final!"
    hide dr caos2
    show dr caos3 at center
    dr "Este desafio mistura tudo o que aprendeste."
    dr "Português, Matemática… e saber pensar."
    jump desafio1
label desafio1:
    hide dr caos1
    hide dr caos2
    show dr caos3 at center
    play music "audio/kahoot.mp3"
    dr "Primeira pergunta."
    dr "Agora atenção à pontuação."
    dr "Qual destas frases está correta?"
    menu:
        "Escolhe a resposta certa:"
        "Vamos aprender juntos, é mais divertido.":
            dr "Essa está correta."
            jump desafio2
        "Vamos aprender juntos é mais divertido.":
            dr "Falta pontuação."
            jump errado
        "Vamos, aprender juntos é mais divertido.":
            dr "A vírgula está no sítio errado."
            jump errado

label errado:
    hide dr caos3
    hide dr caos2
    stop music
    play audio "audio/perdeu.mp3"
    show dr caos1 at center
    dr "Ahahah! Ainda não é desta vez que consegues o livro!"
    dr "Tenta outra vez."
    jump desafio1

label desafio2:
    hide dr caos3
    hide dr caos1
    show dr caos2 at center
    dr "Agora Matemática!"
    dr "Quanto é 348 + 172?"
menu:
    dr "Escolhe o resultado correto: Quanto é 348 + 172?"
    "520":
        dr "Deixa eu fazer as contas para confirmar..."
        hide dr caos3
        hide dr caos2
        stop music
        show dr caos1 at center
        dr "ORA BOLAS!"
        play music "audio/certo.mp3"
        dr "tu acertaste a resposta!"
        jump desafio3
    "510":
        j "Acho que me enganei."
        jump errado
    "530":
        j "Não parece certo."
        jump errado
label desafio3:
    hide dr caos1
    hide dr caos2
    play music "audio/kahoot.mp3"
    show dr caos3 at center
    dr "Última pergunta."
    dr "O que foi mais importante nesta aventura?"
menu:
    dr "Escolhe a melhor resposta:"
    "Trabalhar em conjunto e ajudar os outros.":
        j "Sem os meus amigos não teria chegado aqui."
        jump final_bom
    "Ganhar sozinho.":
        j "Acho que isso não é o mais importante."
        jump errado
    "Ter o livro só para mim.":
        j "Isso não faz sentido."
        jump errado
label final_bom:
    hide dr caos1
    hide dr caos2
    hide dr caos3
    show dr caos2 at center
    stop music
    dr "Está bem..."
    dr "Provaste que mereces o Livro do Saber."
    play music "audio/theme.mp3"
    dr "Usaste o conhecimento e o coração."
    hide dr caos2 with dissolve
    show mia happy at center with moveinleft
    m "Aprender é melhor quando é em equipa."
    scene bg biblioteca with fade
    show professora happy at center
    s "Conseguiram!"
    s "A escola está salva graças a ti, %(player_name)s!"
    show mia happy at right with moveinright
    m "Sabia que ias conseguir!"
    show tomas happy at left with moveinright
    t "Foi incrível!"
    "O Livro do Saber voltou ao seu lugar."
    "E o conhecimento ficou com todos."
    scene final_bom with fade
    eu "Parabéns, conseguiste completar o jogo com sucesso!"
    return

# This ends the game.
return
