#!/usr/bin/env python
import sys
# lendo o input de stdin
for linha in sys.stdin:
# retirando espaços à esquerda e à direita das palavras
    linha = linha.strip()
# dividindo cada linha em palavras individuais
    palavras = linha.split()
# para cada palavra na variável palavras, uma saída com par chave-valores
for palavra in palavras:
# resultado de saída em stdout
# A API MapReduce Streaming utiliza essa saída
# e alimenta como entrada para a etapa Reduce
# delimitado por tabulação
# Contagem de palavras sempre deve retornar 1
# com o comando de saída print
print '%s\t%s' % (palavra, 1)

echo "o rato roeu a roupa do rei de roma" | /home/usuario/mapper.py | sort -k1,1 -
| /home/usuario/reducer.py

