# Comando de execução da tarefa Map
echo "o rato roeu a roupa do rei de roma" | /home/usuario/map.py

# Comando de execução da tarefa Reduce
echo "o rato roeu a roupa do rei de roma" | /home/usuario/map.py | sort -k1,1 -
| /home/usuario/reducer.py

# Comando de input de um arquivo .txt
hadoop fs -put input.txt input.txt