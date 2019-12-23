#!/usr/bin/env python
from operator import itemgetter
import sys
#Inicializando variaveis
palavra_atual = None
contagem_atual = 0
palavra = None
# recebendo input stdin
for linha in sys.stdin:
# retirando espaços à esquerda e à direita das palavras
linha = linha.strip()
# dividindo a entrada de mapper.py e peguando a palavra e sua contagem
palavra, contagem = linha.split('\t', 1)
# convert count string to int
try:
contagem = int(contagem)
except ValueError:
# ignora a exceção e descarta a linha de entrada
continue
# esse IF-switch funciona apenas porque o Hadoop classifica a saída do mapa
# por chave (aqui: palavra) antes de ser passado para o redutor
if palavra_atual == palavra:
contagem_atual += contagem
else:
if palavra_atual:
# escreve o resultado em STDOUT
print '%s\t%s' % (palavra_atual, contagem_atual)
contagem_atual = contagem
palavra_atual = palavra
# não podemos esquecer de imprimir a última palavra, se necessário!
if palavra_atual == palavra:
print '%s\t%s' % (palavra_atual, contagem_atual)



echo "o rato roeu a roupa do rei de roma" | /home/usuario/mapper.py