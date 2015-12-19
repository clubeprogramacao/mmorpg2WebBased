(!) O documento está sujeito às mudanças e aberto a discussões,
	este ReadMe é apenas um modo de termos um plano devidamente
	evidente e para não andarmos em círculos.				 (!)

Back end => mySQL e PHP;
Front end => HTML CSS javascript/python;
	Para python ainda nao sabemos qual webframework usar. 
	Mais detalhes na pagina: https://wiki.python.org/moin/WebFrameworks


Quanto a ideias, seguem elas aqui.
Se quiseres adicionar uma nova ideia preceda ela de (@seuNome)
para todos sabermos quem fez a sugestão e manter a lista 
minimamente possível de se fazer x)
		
Mecanicas de jogo:
	Stamina:
		Delimita quantas acoes voce pode fazer em cadencia;
		Quantos mais LVLs mais stamina;
	Ações:
		Baseadas em tempo;
		Pode-se fazer ate X acoes e cada uma dessas demora um tempo Y;

HEROI:
	Escolha de Origem:
		Raça (altera os atributos iniciais):
			Humano;
			Elfo;
			Anao;
			
		Classe (cada classe da uma afinidade a um tipo de arma):
			Guerreiro;
			Mago;
			Arqueiro;
		Profissao:
			Esta em aberto mas essa categoria diz respeito às
			possibilidades de craft que poderas ter no jogo como
			ferreiro, alquimista(pocoes), etc;
	
	Hitpoints(vida):
		Perde vida até 0 e morre com respawn;
		Morte  a principio possui penalidades como perca de xp;

	Gold:
		Associado a conta;
		Recebido de missões;

	Craft:
		Baseado em recursos:
			Obtidos por quests e monstros;
		Pode-se ter upgrades dos equipamentos: +1, +2, +3...;
		Tipos:
			Cada equipamento associada a um recurso diferente:
				Armaduras de couro usam couro (duh), de metais usam minerais e assim por diante;

	Inventario:
		Equipamento para o heroi:
			Botas;
			Luvas;
			Armas;
			Peitoral;
			Calça;
			Amuletos;
			Aneis;
			Trinkets;
			
	Atributos:
	Cada atributo possui um nivel:
	(IDEIA) Nivel = valor do atributos/100 e quando == 1 => lvl up
		Destreza (DEX);
		Força (FOR);
		Inteligência (INT);
		Agilidade (AGI):
			Possui um sub-atributo;
		Vitalidade (VIT):
			Aumenta HP;
		Sorte (LCK):
			Aumenta chance de crítico;
			Aumenta change de ganhar recompensas e/ou raridades;

MAPA:
	Zonas:
		Separado em sub-zonas e estas separadas por níveis:
			Sub-zonas sao cidades, dungeons, objetivos em geral;
			
	Quests:
		Delimitadas por zonas mas teras de ir à uma sub-zona para fazer as quests;
		
	Pontos de interesse:
		Cidades:
			Interação com outros players* (guild hall* e action house*);
			NPCs;
			Centro onde ha todas as lojas:
				Centro de missoes(taverna);
				Igreja (respawn) -> talvez com penalidades de gold;
				Workshop (craft e melhorar as os equipamentos e/ou itens em geral);
				Craft para material;
			Dungenons;
			Minas e Jardins;
				Recursos p/ coleta;
				
	Dungeons, Quests, Grind:
		São ações, portanto, usam stamina e são limitadas pela mesma.
		Tempo da ação:
			Depende de todos os atributos;
		Recompensas:
			Recompensas com 100% de chance de obter; (?)
			As aleatorias dependem da LCK

Objetivo do primeiro passo:
Como vocês devem ter lido o design inicial do jogo já é um tanto
extenso e é por isso que vamos começar devagar na implementação inicial.

A ideia inicial:
	Começar com nº limitado de classes e raças e ter apenas um local
	de interesse inicial com algumas poucas atividades, sem craft e
	ainda com poucas implementações do resto do sistema. Depois de termos
	este protótipo inicial iremos adicionar o novos blocos de funcionalidade
	em cima dos protótipos anteriores.
	
INDICE:
* -> Nao é o objetivo inicial introduzir o multiplayer de início.
(?) -> Ideia adicional que ainda não foi discutida pelo time de desenvolvimento.