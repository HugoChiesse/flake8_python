from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()

print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(11))
print(fila_teste_2.chama_cliente(12))
print(fila_teste_2.chama_cliente(13))

print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))
print(fila_teste_2.estatistica('11/01/1993', 198, 'detail'))
print(fila_teste_2.estatistica('12/01/1993', 198, 'detail'))
print(fila_teste_2.estatistica('13/01/1993', 198, 'detail'))
fila_teste = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(10))
print(fila_teste.chama_cliente(11))
print(fila_teste.chama_cliente(12))
print(fila_teste.chama_cliente(13))