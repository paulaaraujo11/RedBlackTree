class No:
 	def __init__(self, chave, dados = None, pai = None, left = None, right = None):
 		self.chave = chave
 		self.dados = dados
 		self.left = left
 		self.right =  right
 		self.cor = preto
 		self.pai = pai

 	def __str__(self):
 		return str(self.chave)

class ArvoreRB:
	def __init__(self):
		self.null = No(float('inf'))
		self.raiz = self.null.right = self.null.left = self.null.pai = self.null 

	def busca_MinimoArvore(x):
		while x.left != None:
			x = x.left
		return x
	
	def rotacionaraEsquerda(self,x):
		y = x.right
		x.right = y.left
		if y.left != self.null:
			y.left.pai = x
		y.pai = x.pai
		if x.pai == self.null:
			self.raiz = y
		elif x == x.pai.left:
			x.pai.left = y
		else:
			x.pai.right = y
		y.left = x
		x.pai = y

	def rotacionaraDireita(self,y):
		y = x.left
		x.left = y.right
		if y.right != self.null:
			y.right.pai = x
		y.pai = x.pai
		if x.pai == self.null:
			self.raiz = y
		elif x == x.pai.right:
			x.pai.right = y 
		else:
			x.pai.left = y
		y.right = x
		x.pai = y

  def corrigir_InserirRBTree(self,z):
		while z.pai.cor == vermelho:
			if z.pai == z.pai.pai.left:
				y = z.pai.pai.right
				if  y.cor == vermelho:
					z.pai.cor = preto
					y.cor = preto
					z.pai.pai.cor = vermelho
					z = z.pai.pai
				elif z == z.pai.right:
					z = z.pai
					rotacionaraEsquerda(self,z)
				z.pai.cor = preto
				z.pai.pai.cor = vermelho
				rotacionaraDireita(self,z.pai.pai)
			else:
				y = z.pai.pai.left
				if  y.cor == vermelho:
					z.pai.cor = preto
					y.cor = preto
					z.pai.pai.cor = vermelho
					z = z.pai.pai
				elif z == z.pai.left:
					z = z.pai
					rotacionaraDireita(self,z)
				z.pai.cor = preto
				z.pai.pai.cor = vermelho
				rotacionaraEsquerda(self,z.pai.pai)

	def inserirRBTree(self,z):
		z = No(key,pai =  self.null, left = self.null, right = self.null)
		y = self.null
		x = self.raiz
		while x != self.null:
			y = x 
			if z.chave < x.chave:
				x = x.left
			else:
				x = x.right
		z.pai = y
		if y == self.null:
			self.raiz = z
		elif z.chave < y.chave:
			y.left = z
		else:
			y.right = z
		z.left = self.null
		z.right = self.null
		z.cor = vermelho
		inserirRBTree(z)

	

	def transplatar_ArvoreRB(self,u,v):
		if u.pai == self.null:
			self.raiz = v
		elif u == u.pai.left:
			u.pai.left = v
		else:
			u.p.direita = v
		v.pai = u.pai


	def excluir_RBTree(self,chave):
		z = Node(chave, pai = self.null, left = self.null, right = self.null)
	  z.left = self.null
	  z.right = self.null
		y = z
		y_cor_original = y.cor
		if z.left == self.null:
			x = z.right
			transplatar_ArvoreRB(z,z.right)
		elif z.right == self.null:
			x = z.left
			transplatar_ArvoreRB(z,z.left)
		else:
			y = busca_MinimoArvore(z.right)
			y_cor_original = y.cor
			x = y.right
			if y.pai == z:
				x.pai = y
			else:
				transplatar_ArvoreRB(y,y.right)
				y.right = z.right
			transplatar_ArvoreRB(z,y)
			y.left = z.left
			y.left.pai = y
			y.cor = z.cor
		if y_cor_original == preto:
			corrigir_ExcluirRBTree(x)

	def corrigir_ExcluirRBTree(self,x):
		while x != self.raiz and x.cor == preto:
			if x == x.pai.left:
				w = x.pai.right
				if w.cor == vermelho:
					w.cor = preto
					x.pai.cor = vermelho
					rotacionaraEsquerda(self.x.pai)
					w = x.pai.right
				if w.left.corr == preto and w.right.cor == preto:
					w.left.cor = preto
					w.cor = vermelho
					x = x.pai
				elif w.right.cor == preto:
					w.left.cor = preto
					w.cor = vermelho
					rotacionaraDireita(self,w)
					w = x.pai.right
				w.cor = x.pai.cor
				w.right.cor = preto
				rotacionaraEsquerda(self,x.pai)
				x = self.raiz
			else:
				w = x.pai.left
				if w.cor == vermelho:
					w.cor = preto
					x.pai.cor = vermelho
					rotacionaraEsquerda(self.x.pai)
					w = x.pai.left
				if w.right.cor == preto and w.left.cor == preto:
					w.right.cor = preto
					w.cor = vermelho
					x = x.pai
				elif w.left.cor == preto:
					w.right.cor = preto
					w.cor = vermelho
					rotacionaraDireita(self,w)
					w = x.pai.left
				w.cor = x.pai.cor
				w.left.cor = preto
				rotacionaraEsquerda(self,x.pai)
				x = self.raiz

	def buscar_Dados(self, chave):
    if self.raiz == self.null:
      return False

    x = self.raiz
    
    while chave != x.chave:
      if chave < x.chave:
        x = x.left
      else:
        x = x.right
      return True


  def percorre_ArvoreRB(self, no):
    if no != self.null:
      self.percorre_ArvoreRB(no.left)
      print(no)
      self.percorre_ArvoreRB(no.right)

  def imprimir_ArvoreRB(self):
    print("Arvore: ", end=" ")
    self.percorre_ArvoreRB(self.raiz)

rbA= ArvoreRB()

while True:
	print('='*30)
	print('-'*10,'RED BLACK TREE','-'*10)
	print()
	print('|| 1 - Inserir um dado  ||')
	print('|| 2 - Mostrar a arvore ||')
	print('|| 2 - Excluir um dado  ||')
	print('|| 0 - SAIR             ||')
	print('='*30)
	n = int(input('Escolha uma opção para testar a arvore RB: '))
	if n == 0:
		break
	if n == 1:
		dado = int(input("Insira um valor: "))
		rbA.inserirRBTree(dado)
		print('Inserido com sucesso!')
	if n == 2:
		rbA.imprimir_ArvoreRB()
	if n == 3:
	  dado = int(input("Insira um valor: "))
      if rbA.buscar_Dados(dado) == True:
        print("Valor nao encontrado!")
      else:
        rbA.excluir_RBTree(dado)
		print("Excluído com sucesso")
	
				