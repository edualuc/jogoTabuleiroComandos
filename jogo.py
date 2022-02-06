#
# Jogo de tabuleiro inspirado em Comandos
# Autor Edualuc
#

#tabuleiro
#	terrenos
#		tipo
#			obstrui
#			piso
#jogadores
#	pecas
#		tipo
#			movimento
#			forca

class Status:
	def __init__(self, Tipo = 0, Descr = 'ok'):
		# Status == 0 - sem erro
		# Status != 0 - com erro
		#
		# Tipo == 0 - sem erro
		
		self.descricao = Descr
		self.tipo = Tipo
		
		if Tipo == 0: 
			self.status = 0
		else: 
			self.status = 1
	
	def hasError(self):
		if status == 0: 
			return False
		else: 
			return True

class Terreno:
	def __init__(self):
		self.setTipo(0)
		self.setObstrui(False)
		self.pecas = []
		self.setExclusivo(False)
	
	def getTipo(self):
		return self.tipo
	def getObstrui(self):
		return self.obstrui
	def getExclusivo(self):
		return self.exclusivo
	def setTipo(self, Tipo):
		self.tipo = Tipo
	def setObstrui(self, Obstrui):
		self.obstrui = Obstrui
	def setExclusivo(self, Exclusivo):
		self.exclusivo = Exclusivo
	def addPeca(self, Peca):
		self.pecas.append(Peca)
	def removePeca(self, Peca):
		self.pecas.remove(Peca)
	
	def countPecas(self):
		return len(self.pecas)
	
	def incluirPeca(self, peca):
		if self.getObstrui(self):
			return Status(1, 'Terreno obstrui pecas. Nao pode posicionar pecas nele.')
		elif self.getExclusivo(self) & self.countPecas():
			return Status(2, 'Terreno exclusivo. Ja existe peca nele.')
		self.addPeca(peca)
		return Status()
	
	def imprimir(self, tipo = 'terrenos'):
		if tipo == 'terrenos':
			print(self.getTipo()),
		elif tipo == 'pecas':
			print(self.countPecas()),

class TerrenoPasto(Terreno):
	def __init__(self):
		Terreno.__init__(self)
		self.setTipo('pasto')

class TerrenoAgua(Terreno):
	def __init__(self):
		Terreno.__init__(self)
		self.setTipo(' agua')
		self.setObstrui(True)

class Peca:
	prox = 1
	
	def __init__(self, Tipo):
		self.id = Peca.prox
		self.setViva(True)
		self.setTipo(Tipo)
		self.setAnda(True)
		# terreno
		Peca.prox += 1
	
	def getTipo(self):
		return self.tipo
	def getViva(self):
		return self.viva
	def getAnda(self):
		return self.anda
	def getId(self):
		return self.id
	def getTerreno(self):
		return self.terreno
	def setTipo(self, Tipo):
		self.tipo = Tipo
	def setViva(self, Viva):
		self.viva = Viva
	def setAnda(self, Anda):
		self.anda = Anda
	def setTerreno(self, Terreno):
		self.terreno = Terreno
		
	def moverParaTerreno(self, Terreno):
		# terreno pertence ao Jogador
		# verificar: se pode mover,
		#            se atacou
		#            se ganhou
		#            tomar acoes
		self.setTerreno(Terreno)
		Terreno.addPeca(self)
		
	def imprimir(self, tipo = 'tipo'):
		if tipo == 'tipo':
			print(self.getTipo()),
		elif tipo == 'id':
			print(self.getId()),

class PecaBandeira(Peca):
	def __init__(self):
		Peca.__init__(self, 'bandeira')
		self.setAnda(False)

class PecaSoldado(Peca):
	def __init__(self):
		Peca.__init__(self, 'soldado')

class PecaCabo(Peca):
	def __init__(self):
		Peca.__init__(self, 'cabo')

class PecaSargento(Peca):
	def __init__(self):
		Peca.__init__(self, 'sargento')

class Jogador:
	def __init__(self, Nome):
		self.setNome(Nome)
		self.setPecas({})
		# cria pecas para inicio do jogo
		self.criaPecasIniciais()
		
	def getNome(self):
		return self.nome
	def getPecas(self):
		return self.pecas
	def setNome(self, Nome):
		self.nome = Nome
	def setPecas(self, Pecas):
		self.pecas = Pecas
		
	def criaPecasIniciais(self):
		tempPecas = ('bandeira',
					 'soldado',
					 'soldado', 
					 'soldado',
					 'cabo', 
					 'cabo', 
					 'sargento')
		for tipoPeca in tempPecas:
			proxPeca = Peca.prox # feito pois o lado direito eh executado antes do lado esquerdo da atribuicao
			if tipoPeca == 'bandeira' :
				self.pecas[proxPeca] = PecaBandeira()#self.pecas[peca])
			elif tipoPeca == 'soldado' :
				self.pecas[proxPeca] = PecaSoldado()
			elif tipoPeca == 'cabo' :
				self.pecas[proxPeca] = PecaCabo()#self.getPeca(peca))
			elif tipoPeca == 'sargento' :
				self.pecas[proxPeca] = PecaSargento()#self.getPeca(peca))
	
	def getPeca(self, indice):
		return self.pecas[indice]
	
	def incluirPecaTabuleiro(self, idPeca, Terreno):
		if self.pecas.has_key(idPeca):
			self.pecas[idPeca].moverParaTerreno(Terreno)
			#print('N:' + str(self.getNome()) + ' Id:' + str(idPeca))
	
	def imprimir(self):
		print(self.nome)
		print("  Pecas"),
		print("("),
		for idPeca in self.pecas.keys():
			self.pecas[idPeca].imprimir('id')
		print(")")

class Tabuleiro:
	def __init__(self):
		self.terrenos = []
		self.montarTabuleiroInicial()
	
	def montarTabuleiroInicial(self):
		tabuleiroTemp = ((1, 1, 1, 1, 1),
		                 (1, 1, 1, 1, 1),
						 (1, 2, 1, 2, 1),
						 (1, 1, 1, 1, 1),
		                 (1, 1, 1, 1, 1))
		for terrenoLinhaTemp in tabuleiroTemp:
			tabuleiroLinha = []
			for terrenoTemp in terrenoLinhaTemp:
				if terrenoTemp == 1 :
					tabuleiroLinha.append(TerrenoPasto())
				elif terrenoTemp == 2 :
					tabuleiroLinha.append(TerrenoAgua())
			self.terrenos.append(tabuleiroLinha)
	
	#def posionarPeca(self, peca, terrenoX, terrenoY):
		# peca - obj peca do jogador. - NAO ALTERAR
		# terrenoX - posicao X - comeca do ZERO
		# terrenoY - posicao Y - comeca do ZERO
	#	self.terrenos[terrenoX][terrenoY] = 0
	
	def imprimir(self, tipo):
		for terrenoLinha in self.terrenos:
			print(" ("),
			for terreno in terrenoLinha:
				terreno.imprimir(tipo)
			print(")")
		print
	
	def getTerreno(self, coordenadas):
		return self.terrenos[ coordenadas[0]][ coordenadas[1] ]

class Jogo:
	def __init__(self):
		self.jogadores = ()
		self.tabuleiro = Tabuleiro()
	
	def incluirJogadores(self, quantJogadores):
		for indice in range(quantJogadores):
			self.jogadores = tuple( list(self.jogadores) + [Jogador(indice)] )
	
	def incluirJogador(self):
		self.jogadores = tuple( list(self.jogadores) + [Jogador(len(self.jogadores))] )
	
	def iniciar(self): 
		self.posionarPecasIniciais()
	
	def posionarPecasIniciais(self):
		#                  J Id    Y,X
		tempPosicionar = {(0, 1): (0,2),
						  (0, 2): (0,0),
						  (0, 3): (0,1),
						  (0, 4): (0,4),
						  (0, 5): (0,3),
						  (0, 6): (1,1),
						  (0, 7): (1,3),
						  
						  (1, 8): (4,2),
						  (1, 9): (4,0),
						  (1,10): (4,1),
						  (1,11): (4,4),
						  (1,12): (4,3),
						  (1,13): (3,3),
						  (1,14): (3,1)}
		
		for peca in tempPosicionar.keys():
			jogador = peca[0]
			idPeca = peca[1]
			terreno = self.tabuleiro.getTerreno(tempPosicionar[peca])
			
			self.jogadores[jogador].incluirPecaTabuleiro(idPeca, terreno) #.posionarPecas(jogador)
	
	def printTab(self):
		print("Tabuleiro:")
		print("( ")
		self.tabuleiro.imprimir('terrenos')
		print(")")
		print("")
		print("Jogador:")
		print("(")
		for jogador in self.jogadores:
			jogador.imprimir()
		print(")")
		print("Pecas no Tabuleiro")
		self.tabuleiro.imprimir('pecas')

def main():
	jogo = Jogo()
	jogo.incluirJogadores(2)
	jogo.iniciar()
	jogo.printTab()

main()
