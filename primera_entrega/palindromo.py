class Palindromo():
    
    def __init__(self, palabra):
        self.palabra = palabra  
    
    # Método para obtener la palabra almacenada
    def get_palabra(self):
        return self.palabra
    
    # Método para verificar si la palabra es un palíndromo
    def es_palindromo(self):
        palabra = self.palabra.replace(' ', '').lower()  # Elimina espacios y convierte a minúsculas
        return palabra == palabra[::-1]  # Compara la palabra con su inversa para verificar si es palíndromo
    
    # Método para obtener el resultado de si la palabra es un palíndromo o no
    def resultado(self):
        if self.es_palindromo():
            return f'La palabra {self.palabra} es un palíndromo'
        else: 
            return f'La palabra {self.palabra} no es un palíndromo'
    
    # Método para realizar una prueba y obtener el resultado como una tupla
    def test(self):
        return (self.es_palindromo(), self.palabra)
    
    # Método para representar la clase como una cadena de texto
    def __str__(self):
        return self.resultado()


# Función principal para probar la clase Palindromo
def main():
    palabra = input('Escribe una palabra: ')  
    palindromo = Palindromo(palabra)  # Crea una instancia de Palindromo con la palabra proporcionada
    print(palindromo)  # Imprime el resultado si la palabra es un palíndromo o no


if __name__ == "__main__":
    main()

            