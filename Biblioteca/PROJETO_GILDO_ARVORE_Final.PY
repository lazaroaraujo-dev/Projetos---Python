#cria os nó
class No:
    # função que inicia o nó com nome, sinopse (se tiver) e uma lista vazia pros filhos
    def __init__(self, nome, sinopse=""):
        self.nome = nome
        self.sinopse = sinopse
        self.filhos = []
    # função pra ligar um nó dentro de outro
    def adicionar_filho(self, filho):
        self.filhos.append(filho)
    # função que mostra toda a árvore
    def mostrar_completo(self, nivel=0):
        espacos = "  " * nivel
        print(f"{espacos}{self.nome}")
        if self.sinopse:
            print(f"{espacos}  -- {self.sinopse}")
        for filho in self.filhos:
            filho.mostrar_completo(nivel + 1)

#Raiz
biblioteca = No("Biblioteca")

#Gênero Ficção
ficcao = No("Ficção")
biblioteca.adicionar_filho(ficcao)
#Gênero não_Ficção
nao_ficcao = No("Não Ficção")
biblioteca.adicionar_filho(nao_ficcao)
#Gênero Outros
outros = No("Outros Gêneros")
biblioteca.adicionar_filho(outros)

#Subgênero Ficção
romance = No("Romance")
ficcao.adicionar_filho(romance)
#Subgênero Ficção
fantasia = No("Fantasia")
ficcao.adicionar_filho(fantasia)
#Subgênero Ficção
ficcao_cientifica = No("Ficção Científica")
ficcao.adicionar_filho(ficcao_cientifica)
#Subgênero Ficção
terror = No("Terror")
ficcao.adicionar_filho(terror)
#Subgênero Ficção
misterio = No("Mistério")
ficcao.adicionar_filho(misterio)
#Subgênero Ficção
aventura = No("Aventura")
ficcao.adicionar_filho(aventura)

#Subgênero Ficção/ romance
jane_austen = No("Jane Austen")
jane_austen.adicionar_filho(No("Orgulho e Preconceito", "Sinopse: Elizabeth Bennet precisa lidar com questões de classe, orgulho e amor | Ano: 1813"))
jane_austen.adicionar_filho(No("Razão e Sensibilidade", "Sinopse: As irmãs Dashwood enfrentam as dificuldades do amor e da sociedade | Ano: 1811"))
jane_austen.adicionar_filho(No("Emma", "Sinopse: Uma jovem rica tenta bancar a casamenteira | Ano: 1815"))
romance.adicionar_filho(jane_austen)
#Subgênero Ficção/ romance
machado_assis = No("Machado de Assis")
machado_assis.adicionar_filho(No("Dom Casmurro", "Sinopse: Bentinho narra sua vida e o ciúme por Capitu | Ano: 1899"))
machado_assis.adicionar_filho(No("Memórias Póstumas de Brás Cubas", "Sinopse: Um defunto-autor narra sua vida com ironia | Ano: 1881"))
machado_assis.adicionar_filho(No("Quincas Borba", "Sinopse: Rubião herda fortuna e mergulha na loucura | Ano: 1891"))
romance.adicionar_filho(machado_assis)
#Subgênero Ficção/ romance
clarice = No("Clarice Lispector")
clarice.adicionar_filho(No("A Hora da Estrela", "Sinopse: A história de Macabéa, uma jovem nordestina | Ano: 1977"))
clarice.adicionar_filho(No("Perto do Coração Selvagem", "Sinopse: Mergulho na consciência de Joana | Ano: 1943"))
clarice.adicionar_filho(No("Laços de Família", "Sinopse: Coletânea de contos sobre relações familiares | Ano: 1960"))
romance.adicionar_filho(clarice)
#Subgênero Ficção/ romance
saramago = No("José Saramago")
saramago.adicionar_filho(No("Ensaio sobre a Cegueira", "Sinopse: Epidemia de cegueira revela fragilidade da civilização | Ano: 1995"))
saramago.adicionar_filho(No("Memorial do Convento", "Sinopse: Construção do Convento de Mafra e amor entre Baltasar e Blimunda | Ano: 1982"))
romance.adicionar_filho(saramago)
#Subgênero Ficção/ romance
marquez = No("Gabriel García Márquez")
marquez.adicionar_filho(No("Cem Anos de Solidão", "Sinopse: Saga da família Buendía em Macondo | Ano: 1967"))
marquez.adicionar_filho(No("O Amor nos Tempos do Cólera", "Sinopse: Amor que sobrevive às décadas entre Florentino e Fermina | Ano: 1985"))
romance.adicionar_filho(marquez)
#Subgênero Ficção/ fantasia
tolkien = No("J.R.R. Tolkien")
tolkien.adicionar_filho(No("O Senhor dos Anéis", "Sinopse: Jornada para destruir o Um Anel e derrotar Sauron | Ano: 1954"))
tolkien.adicionar_filho(No("O Hobbit", "Sinopse: Bilbo Bolseiro em aventura para recuperar tesouro | Ano: 1937"))
tolkien.adicionar_filho(No("O Silmarillion", "Sinopse: Mitologia da Terra-média | Ano: 1977"))
fantasia.adicionar_filho(tolkien)
#Subgênero Ficção/ fantasia
rowling = No("J.K. Rowling")
rowling.adicionar_filho(No("Harry Potter e a Pedra Filosofal", "Sinopse: Harry descobre ser bruxo e começa jornada em Hogwarts | Ano: 1997"))
rowling.adicionar_filho(No("Harry Potter e o Cálice de Fogo", "Sinopse: Harry participa de torneio perigoso entre escolas de magia | Ano: 2000"))
rowling.adicionar_filho(No("Harry Potter e as Relíquias da Morte", "Sinopse: Batalha final contra Voldemort | Ano: 2007"))
fantasia.adicionar_filho(rowling)
#Subgênero Ficção/ fantasia
martin = No("George R.R. Martin")
martin.adicionar_filho(No("A Guerra dos Tronos", "Sinopse: Nobres lutam pelo controle dos Sete Reinos | Ano: 1996"))
martin.adicionar_filho(No("A Fúria dos Reis", "Sinopse: Guerra civil brutal por poder e vingança | Ano: 1998"))
fantasia.adicionar_filho(martin)
#Subgênero Ficção/ fantasia
riordan = No("Rick Riordan")
riordan.adicionar_filho(No("Percy Jackson e o Ladrão de Raios", "Sinopse: Garoto descobre ser filho de Poseidon | Ano: 2005"))
riordan.adicionar_filho(No("O Herói Perdido", "Sinopse: Novos heróis para restaurar ordem entre semideuses | Ano: 2010"))
fantasia.adicionar_filho(riordan)
#Subgênero Ficção/ ficcao_cientifica
asimov = No("Isaac Asimov")
asimov.adicionar_filho(No("Fundação", "Sinopse: Cientistas preservam conhecimento em império galáctico decadente | Ano: 1951"))
asimov.adicionar_filho(No("Eu, Robô", "Sinopse: Dilemas éticos envolvendo robôs e Três Leis da Robótica | Ano: 1950"))
asimov.adicionar_filho(No("Fim da Eternidade", "Sinopse: Organização controla o tempo | Ano: 1955"))
ficcao_cientifica.adicionar_filho(asimov)
#Subgênero Ficção/ ficcao_cientifica
dick = No("Philip K. Dick")
dick.adicionar_filho(No("Androides Sonham com Ovelhas Elétricas?", "Sinopse: Caçador de androides enfrenta dilemas sobre humanidade | Ano: 1968"))
dick.adicionar_filho(No("O Homem do Castelo Alto", "Sinopse: Mundo onde o Eixo venceu a Segunda Guerra | Ano: 1962"))
ficcao_cientifica.adicionar_filho(dick)
#Subgênero Ficção/ ficcao_cientifica
bradbury = No("Ray Bradbury")
bradbury.adicionar_filho(No("Fahrenheit 451", "Sinopse: Sociedade onde livros são proibidos | Ano: 1953"))
bradbury.adicionar_filho(No("Crônicas Marcianas", "Sinopse: Colonização de Marte pela humanidade | Ano: 1950"))
ficcao_cientifica.adicionar_filho(bradbury)
#Subgênero Ficção/ ficcao_cientifica
verne = No("Júlio Verne")
verne.adicionar_filho(No("Vinte Mil Léguas Submarinas", "Sinopse: Capitão Nemo explora profundezas dos mares | Ano: 1870"))
verne.adicionar_filho(No("A Volta ao Mundo em 80 Dias", "Sinopse: Phileas Fogg aposta que pode dar volta ao mundo | Ano: 1873"))
ficcao_cientifica.adicionar_filho(verne)
#Subgênero Ficção/ terror
king = No("Stephen King")
king.adicionar_filho(No("It: A Coisa", "Sinopse: Grupo enfrenta entidade que se alimenta do medo | Ano: 1986"))
king.adicionar_filho(No("O Iluminado", "Sinopse: Escritor enlouquece em hotel isolado | Ano: 1977"))
king.adicionar_filho(No("Misery", "Sinopse: Escritor sequestrado por fã obsessiva | Ano: 1987"))
terror.adicionar_filho(king)
#Subgênero Ficção/ terror
poe = No("Edgar Allan Poe")
poe.adicionar_filho(No("O Corvo", "Sinopse: Poema sobre perda e desespero | Ano: 1845"))
poe.adicionar_filho(No("O Coração Delator", "Sinopse: Assassino justifica crime consumido pela culpa | Ano: 1843"))
terror.adicionar_filho(poe)
#Subgênero Ficção/ terror
shelley = No("Mary Shelley")
shelley.adicionar_filho(No("Frankenstein", "Sinopse: Cientista cria vida e enfrenta consequências | Ano: 1818"))
terror.adicionar_filho(shelley)
#Subgênero Ficção/ terror
lovecraft = No("H.P. Lovecraft")
lovecraft.adicionar_filho(No("O Chamado de Cthulhu", "Sinopse: Investigação sobre entidade cósmica ancestral | Ano: 1928"))
terror.adicionar_filho(lovecraft)
#Subgênero Ficção/ misterio
christie = No("Agatha Christie")
christie.adicionar_filho(No("Assassinato no Expresso do Oriente", "Sinopse: Poirot investiga homicídio em trem de luxo | Ano: 1934"))
christie.adicionar_filho(No("O Caso dos Dez Negrinhos", "Sinopse: Dez pessoas em ilha isolada com segredos mortais | Ano: 1939"))
misterio.adicionar_filho(christie)
#Subgênero Ficção/ misterio
conan_doyle = No("Arthur Conan Doyle")
conan_doyle.adicionar_filho(No("O Cão dos Baskervilles", "Sinopse: Sherlock Holmes investiga morte ligada a lenda | Ano: 1902"))
conan_doyle.adicionar_filho(No("Um Estudo em Vermelho", "Sinopse: Primeiro caso de Holmes com Watson | Ano: 1887"))
misterio.adicionar_filho(conan_doyle)
#Subgênero Ficção/ misterio
flynn = No("Gillian Flynn")
flynn.adicionar_filho(No("Garota Exemplar", "Sinopse: Desaparecimento de mulher e suspeitas sobre marido | Ano: 2012"))
misterio.adicionar_filho(flynn)
#Subgênero Ficção/ misterio
brown = No("Dan Brown")
brown.adicionar_filho(No("O Código Da Vinci", "Sinopse: Professor desvenda segredos históricos | Ano: 2003"))
misterio.adicionar_filho(brown)
#Subgênero Ficção/ aventura
dumas = No("Alexandre Dumas")
dumas.adicionar_filho(No("Os Três Mosqueteiros", "Sinopse: D'Artagnan e companheiros lutam por honra | Ano: 1844"))
dumas.adicionar_filho(No("O Conde de Monte Cristo", "Sinopse: Homem injustamente preso busca vingança | Ano: 1844"))
aventura.adicionar_filho(dumas)
#Subgênero Ficção/ aventura
stevenson = No("Robert Louis Stevenson")
stevenson.adicionar_filho(No("A Ilha do Tesouro", "Sinopse: Jovem em busca de tesouro pirata | Ano: 1883"))
aventura.adicionar_filho(stevenson)
#Subgênero Ficção/ aventura
london = No("Jack London")
london.adicionar_filho(No("O Chamado da Floresta", "Sinopse: Cão Buck na corrida do ouro no Alasca | Ano: 1903"))
aventura.adicionar_filho(london)

#Subgênero nâo_Ficção
biografia = No("Biografia")
nao_ficcao.adicionar_filho(biografia)
#Subgênero nâo_Ficção
ciencia = No("Ciência")
nao_ficcao.adicionar_filho(ciencia)
#Subgênero nâo_Ficção
historia = No("História")
nao_ficcao.adicionar_filho(historia)
#Subgênero nâo_Ficção
autoajuda = No("Autoajuda")
nao_ficcao.adicionar_filho(autoajuda)
#Subgênero nâo_Ficção
negocios = No("Negócios")
nao_ficcao.adicionar_filho(negocios)
#Subgênero nâo_Ficção
filosofia = No("Filosofia")
nao_ficcao.adicionar_filho(filosofia)
#Subgênero nâo_Ficção
educacao = No("Educação")
nao_ficcao.adicionar_filho(educacao)

#Subgênero nâo_Ficção/ biografia
isaacson = No("Walter Isaacson")
isaacson.adicionar_filho(No("Steve Jobs", "Sinopse: Biografia definitiva do fundador da Apple | Ano: 2011"))
isaacson.adicionar_filho(No("Einstein", "Sinopse: Vida e pensamento de Albert Einstein | Ano: 2007"))
isaacson.adicionar_filho(No("Leonardo da Vinci", "Sinopse: Analisa a vida multifacetada do artista e inventor | Ano: 2017"))
biografia.adicionar_filho(isaacson)
#Subgênero nâo_Ficção/ biografia
anne_frank = No("Anne Frank")
anne_frank.adicionar_filho(No("O Diário de Anne Frank", "Sinopse: Relato real de adolescente judia na Segunda Guerra | Ano: 1947"))
biografia.adicionar_filho(anne_frank)
#Subgênero nâo_Ficção/ biografia
mandela = No("Nelson Mandela")
mandela.adicionar_filho(No("Longa Caminhada até a Liberdade", "Sinopse: Autobiografia da luta contra o apartheid | Ano: 1994"))
mandela.adicionar_filho(No("Conversas que Tive Comigo", "Sinopse: Cartas, anotações e reflexões de Mandela | Ano: 2010"))
biografia.adicionar_filho(mandela)
#Subgênero nâo_Ficção/ biografia
michelle = No("Michelle Obama")
michelle.adicionar_filho(No("Minha História", "Sinopse: Memórias da ex-primeira-dama dos EUA | Ano: 2018"))
biografia.adicionar_filho(michelle)
#Subgênero nâo_Ficção/ ciencia
hawking = No("Stephen Hawking")
hawking.adicionar_filho(No("Uma Breve História do Tempo", "Sinopse: Explora questões da cosmologia de forma acessível | Ano: 1988"))
hawking.adicionar_filho(No("O Universo Numa Casca de Noz", "Sinopse: Busca por Teoria de Tudo unificando física | Ano: 2001"))
hawking.adicionar_filho(No("Breves Respostas para Grandes Questões", "Sinopse: Reflexões sobre temas cruciais para humanidade | Ano: 2018"))
ciencia.adicionar_filho(hawking)
#Subgênero nâo_Ficção/ ciencia
sagan = No("Carl Sagan")
sagan.adicionar_filho(No("Cosmos", "Sinopse: Jornada através de 14 bilhões de anos de evolução cósmica | Ano: 1980"))
sagan.adicionar_filho(No("O Mundo Assombrado pelos Demônios", "Sinopse: Defesa do pensamento científico | Ano: 1996"))
sagan.adicionar_filho(No("Pálido Ponto Azul", "Sinopse: Reflexão sobre o futuro da humanidade no espaço | Ano: 1994"))
ciencia.adicionar_filho(sagan)
#Subgênero nâo_Ficção/ ciencia
dawkins = No("Richard Dawkins")
dawkins.adicionar_filho(No("O Gene Egoísta", "Sinopse: Unidade fundamental da seleção natural é o gene | Ano: 1976"))
dawkins.adicionar_filho(No("O Relojeiro Cego", "Sinopse: Defesa da Teoria da Evolução | Ano: 1986"))
dawkins.adicionar_filho(No("Deus: Um Delírio", "Sinopse: Argumenta contra a crença em Deus | Ano: 2006"))
ciencia.adicionar_filho(dawkins)
#Subgênero nâo_Ficção/ ciencia
harari = No("Yuval Noah Harari")
harari.adicionar_filho(No("Sapiens", "Sinopse: História da humanidade de animal insignificante a dominador | Ano: 2011"))
harari.adicionar_filho(No("Homo Deus", "Sinopse: Explora o futuro da humanidade | Ano: 2015"))
harari.adicionar_filho(No("Lições para o Século XXI", "Sinopse: Analisa desafios do mundo contemporâneo | Ano: 2018"))
ciencia.adicionar_filho(harari)
#Subgênero nâo_Ficção/ historia
gomes = No("Laurentino Gomes")
gomes.adicionar_filho(No("1808", "Sinopse: Fuga da Família Real Portuguesa para o Brasil | Ano: 2007"))
gomes.adicionar_filho(No("1822", "Sinopse: Bastidores da Independência do Brasil | Ano: 2010"))
gomes.adicionar_filho(No("1889", "Sinopse: Proclamação da República no Brasil | Ano: 2013"))
historia.adicionar_filho(gomes)
#Subgênero nâo_Ficção/ historia
hobsbawm = No("Eric Hobsbawm")
hobsbawm.adicionar_filho(No("A Era das Revoluções", "Sinopse: Impacto da Revolução Industrial e Francesa | Ano: 1962"))
hobsbawm.adicionar_filho(No("A Era dos Impérios", "Sinopse: Examina a Belle Époque e imperialismo | Ano: 1975"))
hobsbawm.adicionar_filho(No("A Era dos Extremos", "Sinopse: Análise do breve século XX | Ano: 1994"))
historia.adicionar_filho(hobsbawm)
#Subgênero nâo_Ficção/ historia
diamond = No("Jared Diamond")
diamond.adicionar_filho(No("Armas, Germes e Aço", "Sinopse: Destinos das sociedades humanas | Ano: 1997"))
historia.adicionar_filho(diamond)
#Subgênero nâo_Ficção/ autoajuda
carnegie = No("Dale Carnegie")
carnegie.adicionar_filho(No("Como Fazer Amigos e Influenciar Pessoas", "Sinopse: Técnicas para relacionamentos e persuasão | Ano: 1936"))
carnegie.adicionar_filho(No("Como Evitar Preocupações e Começar a Viver", "Sinopse: Métodos para lidar com ansiedade | Ano: 1948"))
autoajuda.adicionar_filho(carnegie)
#Subgênero nâo_Ficção/ autoajuda
manson = No("Mark Manson")
manson.adicionar_filho(No("A Sutil Arte de Ligar o F*da-se", "Sinopse: Abordagem contra o pensamento positivo constante | Ano: 2016"))
manson.adicionar_filho(No("Tudo Está F*dido", "Sinopse: Análise das crises globais | Ano: 2019"))
manson.adicionar_filho(No("Will", "Sinopse: Autobiografia de Will Smith | Ano: 2021"))
autoajuda.adicionar_filho(manson)
#Subgênero nâo_Ficção/ autoajuda
cury = No("Augusto Cury")
cury.adicionar_filho(No("Ansiedade: O Mal do Século", "Sinopse: Abordagem sobre Síndrome do Pensamento Acelerado | Ano: 2014"))
cury.adicionar_filho(No("O Vendedor de Sonhos", "Sinopse: Romance sobre transformação pessoal | Ano: 2008"))
cury.adicionar_filho(No("O Homem Mais Inteligente da História", "Sinopse: Romance sobre investigação da mente de Jesus | Ano: 2016"))
autoajuda.adicionar_filho(cury)
#Subgênero nâo_Ficção/ autoajuda
clear = No("James Clear")
clear.adicionar_filho(No("Hábitos Atômicos", "Sinopse: Método para construir bons hábitos e eliminar maus | Ano: 2018"))
autoajuda.adicionar_filho(clear)
#Subgênero nâo_Ficção/ negocios
kiyosaki = No("Robert Kiyosaki")
kiyosaki.adicionar_filho(No("Pai Rico, Pai Pobre", "Sinopse: Educação financeira e mentalidade de investidor | Ano: 1997"))
kiyosaki.adicionar_filho(No("O Negócio do Século XXI", "Sinopse: Foco no Marketing de Rede | Ano: 2010"))
kiyosaki.adicionar_filho(No("Guia de Investimentos", "Sinopse: Guia para construção de riqueza | Ano: 2000"))
negocios.adicionar_filho(kiyosaki)
#Subgênero nâo_Ficção/ negocios
sinek = No("Simon Sinek")
sinek.adicionar_filho(No("Comece pelo Porquê", "Sinopse: Líderes inspiradores começam com propósito | Ano: 2009"))
sinek.adicionar_filho(No("Encontre seu Porquê", "Sinopse: Guia prático para descobrir propósito | Ano: 2017"))
sinek.adicionar_filho(No("Os Líderes Comem por Último", "Sinopse: Como construir equipes coesas | Ano: 2014"))
negocios.adicionar_filho(sinek)
#Subgênero nâo_Ficção/ negocios
cerbasi = No("Gustavo Cerbasi")
cerbasi.adicionar_filho(No("Casais Inteligentes Enriquecem Juntos", "Sinopse: Planejamento financeiro para casais | Ano: 2004"))
cerbasi.adicionar_filho(No("Investimentos Inteligentes", "Sinopse: Guia para iniciar jornada como investidor | Ano: 2005"))
cerbasi.adicionar_filho(No("Adeus, Aposentadoria", "Sinopse: Defende busca por Independência Financeira | Ano: 2011"))
negocios.adicionar_filho(cerbasi)
#Subgênero nâo_Ficção/ negocios
hill = No("Napoleon Hill")
hill.adicionar_filho(No("Quem Pensa Enriquece", "Sinopse: Princípios para alcançar sucesso e riqueza | Ano: 1937"))
negocios.adicionar_filho(hill)
#Subgênero nâo_Ficção/ filosofia
platao = No("Platão")
platao.adicionar_filho(No("A República", "Sinopse: Busca por definição de Justiça e cidade ideal | Ano: 380 a.C"))
platao.adicionar_filho(No("Fédon", "Sinopse: Diálogo sobre imortalidade da alma | Ano: 380 a.C"))
platao.adicionar_filho(No("Banquete", "Sinopse: Discursos sobre a natureza do Amor | Ano: 385 a.C"))
filosofia.adicionar_filho(platao)
#Subgênero nâo_Ficção/ filosofia
nietzsche = No("Friedrich Nietzsche")
nietzsche.adicionar_filho(No("Assim Falou Zaratustra", "Sinopse: Ensina sobre Super-Homem e Vontade de Poder | Ano: 1883"))
nietzsche.adicionar_filho(No("Além do Bem e do Mal", "Sinopse: Crítica à moralidade tradicional | Ano: 1886"))
nietzsche.adicionar_filho(No("O Anticristo", "Sinopse: Ataque frontal ao cristianismo | Ano: 1895"))
filosofia.adicionar_filho(nietzsche)
#Subgênero nâo_Ficção/ filosofia
dalai_lama = No("Dalai Lama")
dalai_lama.adicionar_filho(No("A Arte da Felicidade", "Sinopse: Sabedoria budista para alcançar felicidade | Ano: 1998"))
dalai_lama.adicionar_filho(No("O Livro da Alegria", "Sinopse: Conversas sobre alegria duradoura | Ano: 2016"))
dalai_lama.adicionar_filho(No("O Caminho do Meio", "Sinopse: Expõe ensinamentos do Budismo Mahayana"))
filosofia.adicionar_filho(dalai_lama)
#Subgênero nâo_Ficção/ filosofia
freire = No("Paulo Freire")
freire.adicionar_filho(No("Pedagogia do Oprimido", "Sinopse: Crítica à educação bancária e proposta libertadora | Ano: 1968"))
freire.adicionar_filho(No("Pedagogia da Autonomia", "Sinopse: Saberes essenciais para educadores | Ano: 1996"))
freire.adicionar_filho(No("Educação e Mudança", "Sinopse: Analisa papel da educação na mudança social | Ano: 1979"))
filosofia.adicionar_filho(freire)
#Subgênero nâo_Ficção/ educacao
dweck = No("Carol Dweck")
dweck.adicionar_filho(No("Mindset: A Nova Psicologia do Sucesso", "Sinopse: Mindsets Fixo e de Crescimento | Ano: 2006"))
dweck.adicionar_filho(No("Self-Theories", "Sinopse: Pesquisa fundamental sobre mindsets | Ano: 2000"))
educacao.adicionar_filho(dweck)
#Subgênero nâo_Ficção/ educacao
gardner = No("Howard Gardner")
gardner.adicionar_filho(No("Estruturas da Mente", "Sinopse: Teoria das Inteligências Múltiplas | Ano: 1983"))
gardner.adicionar_filho(No("As Inteligências Múltiplas", "Sinopse: Aplicações práticas da teoria | Ano: 1993"))
gardner.adicionar_filho(No("Mentes que Mudam", "Sinopse: Como ideias e crenças são alteradas | Ano: 2004"))
educacao.adicionar_filho(gardner)

#Subgênero Outros
poesia = No("Poesia")
outros.adicionar_filho(poesia)
#Subgênero Outros
hq = No("HQ")
outros.adicionar_filho(hq)
#Subgênero Outros
infantil = No("Infantil")
outros.adicionar_filho(infantil)

#Subgênero Outros/ poesia
drummond = No("Carlos Drummond de Andrade")
drummond.adicionar_filho(No("Alguma Poesia", "Sinopse: Estreia do poeta com olhar irônico sobre cotidiano | Ano: 1930"))
poesia.adicionar_filho(drummond)
#Subgênero Outros/ poesia
vinicius = No("Vinicius de Moraes")
vinicius.adicionar_filho(No("Soneto de Fidelidade", "Sinopse: Poema clássico sobre amor e entrega | Ano: 1946"))
poesia.adicionar_filho(vinicius)
#Subgênero Outros/ poesia
neruda = No("Pablo Neruda")
neruda.adicionar_filho(No("Vinte Poemas de Amor", "Sinopse: Obra famosa da poesia amorosa latino-americana | Ano: 1924"))
poesia.adicionar_filho(neruda)
#Subgênero Outros/ hq
lee = No("Stan Lee")
lee.adicionar_filho(No("Homem-Aranha", "Sinopse: História de Peter Parker, o herói aracnídeo | Ano: 1962"))
hq.adicionar_filho(lee)
#Subgênero Outros/ poesia
moore = No("Alan Moore")
moore.adicionar_filho(No("Watchmen", "Sinopse: Narrativa crítica sobre impacto dos heróis na sociedade | Ano: 1986"))
hq.adicionar_filho(moore)
#Subgênero Outros/ poesia
oda = No("Eiichiro Oda")
oda.adicionar_filho(No("One Piece", "Sinopse: Luffy e tripulação em busca do maior tesouro | Ano: 1997"))
hq.adicionar_filho(oda)
#Subgênero Outros/ infantil
lobato = No("Monteiro Lobato")
lobato.adicionar_filho(No("Sítio do Picapau Amarelo", "Sinopse: Universo infantil com fantasia e folclore brasileiro"))
infantil.adicionar_filho(lobato)
#Subgênero Outros/ infantil
saint_exupery = No("Antoine de Saint-Exupéry")
saint_exupery.adicionar_filho(No("O Pequeno Príncipe", "Sinopse: Garoto viajante ensina lições de amizade e vida | Ano: 1943"))
infantil.adicionar_filho(saint_exupery)

#Mostra biblioteca completa
biblioteca.mostrar_completo()

#Imprimir autores
def listar_autores(no):
    autores = []
    tem_sinopse = False
    
    for filho in no.filhos:
        if filho.sinopse:     # se esse filho tiver sinopse (não for string vazia)
            tem_sinopse = True
            break              # achou um → pode parar o loop
    if tem_sinopse:
        autores.append(no.nome)
    # Busca recursiva
    for filho in no.filhos:
        autores.extend(listar_autores(filho))
    return autores

#Funções de busca
def buscar_por_autor(no, autor_nome):
    resultados = []
    # Se o nó atual for o autor procurado
    if no.nome.lower() == autor_nome.lower():
        resultados.extend(no.filhos)  # Adiciona todos os livros do autor

    # Busca recursiva nos filhos
    for filho in no.filhos:
        resultados.extend(buscar_por_autor(filho, autor_nome))
    return resultados

def listar_livros(no):
    livros = []
    # Se o nó atual tem sinopse, ele é um livro
    if no.sinopse:
        livros.append(no.nome)

    # Busca recursiva nos filhos
    for filho in no.filhos:
        livros.extend(listar_livros(filho))
    return livros

def buscar_por_livro(no, livro_nome):
    resultados = []
    if no.nome.lower() == livro_nome.lower() and no.sinopse:
        resultados.append(no)
    for filho in no.filhos:
        resultados.extend(buscar_por_livro(filho, livro_nome))
    return resultados


#Função para navegar
def navegar():
    nivel_atual = biblioteca

    while True:
        #Aqui vai sair o nome da raiz dos nó (BIBLIOTECA)
        print(f"\n{nivel_atual.nome}:")

        for numero, opcao in enumerate(nivel_atual.filhos, 1):
            # numeração #proximos nó (Gêneros)
            print(f"{numero}. {opcao.nome}")
        print("4. Procurar por autor\n5. Procurar por livro")
        if nivel_atual == biblioteca:
            print("0. Sair")
        else:
            print("0. Voltar")

        try:
            escolha = int(input("\nEscolha: "))
            if escolha == 0:
                if nivel_atual == biblioteca:
                        print("Saindo da biblioteca...")
                        break
                nivel_atual = biblioteca

            elif escolha == 4:
                autores = listar_autores(biblioteca)
                print("\n--- Lista de Autores Disponíveis ---")
                for autor in sorted(set(autores)):
                    print("-", autor)
                autor = input("\nDigite o nome do autor desejado: ").strip()
                livros_autor = buscar_por_autor(biblioteca, autor)
                if livros_autor:
                    print(f"\nLivros de {autor}:")
                    for livro in livros_autor:
                        print(f"- {livro.nome}: {livro.sinopse}")
                else:
                    print("Autor não encontrado.")

            elif escolha == 5:
                print("\n--- Lista de Livros Disponíveis ---")
                todos_livros = sorted(set(listar_livros(biblioteca)))
                if not todos_livros:
                    print("Nenhum livro encontrado.")
                else:
                    for livro_nome in todos_livros:
                        print("-", livro_nome)

                livro = input("\nDigite o nome do livro desejado: ").strip()
                resultado = buscar_por_livro(biblioteca, livro)
                if resultado:
                    for r in resultado:
                        print(f"\nLivro encontrado: {r.nome}")
                        print(r.sinopse)
                else:
                    print("Livro não encontrado.")

            else:
                #vai descendo o nivel do nó (subgêneros)
                proximo_nivel = nivel_atual.filhos[escolha - 1]

                if proximo_nivel.sinopse:
                    print(f"\n--- {proximo_nivel.nome} ---")
                    print(f"{proximo_nivel.sinopse}")
                    print("\nOpcoes:")
                    print("1. Voltar ao menu principal")
                    print("2. Continuar navegando")
                    print("3. Sair do programa")
                    opcao_sinopse = input("\nEscolha uma opcao: ")
                    if opcao_sinopse == "1":
                        # Se escolher 1, volta para o menu
                        nivel_atual = biblioteca
                    elif opcao_sinopse == "3":
                        print("Saiu!")
                        break
                else:
                    # Se escolher 2, continua no mesmo nivel
                    nivel_atual = proximo_nivel
        except:
            print("Opcao invalida! Tente novamente.")
navegar()
