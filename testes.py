# Fonte: https://pythongeeks.org/python-os-module/

import os
# print(dir(os))

# Diretorio de trabalho atual
print(os.getcwd())

# Localização deste arquivo de script
real_path = os.path.realpath(__file__)
# Localização absoluta do diretório onde está o arquivo
dir_path = os.path.dirname(real_path)

print(real_path)
print(dir_path)

# Imprime a var $HOME
print(os.getenv("HOME"))

# Lista o conteudo do diretorio atual
print(os.listdir())

# Executar comandos do sistema
os.system("python3 --version")

# Tamanho do arquivo
#print(os.path.getsize('testes.py'))
print(os.path.getsize(real_path))
