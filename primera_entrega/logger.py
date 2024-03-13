class Logger:
    def __init__(self):
        self.log_file = open("log.txt", "w")  
        # Abre el archivo de registro en modo escritura
        self.log_count = 0 
        # Inicializa el contador de registros

        self.log_file.write("--Start log--\n")
        # Escribe la línea "--Start log--" al inicio del archivo y /n para hacer el salto de linea

    def log(self, message):
        self.log_file.write(message + "\n") 
        # Escribe el mensaje en una nueva línea en el archivo
        self.log_count += 1 

    def __del__(self):
        # Escribe la línea "--End log: x log(s)--" al final del archivo, donde x es el número de registros
        self.log_file.write("--End log: {} log(s)--\n".format(self.log_count))

        self.log_file.close()  
        # Cierra el archivo al destruir la instancia


class Test:
    def __init__(self):
        self.logger = Logger()  
        # Inicializa una instancia de Logger

    def llamada(self, message):
        self.logger.log(message)  
        # Llama al método log de la instancia de Logger


test = Test()  
# Crea una instancia de Test
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada("{}ª llamada".format(i))
