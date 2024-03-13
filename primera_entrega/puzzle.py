#Adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible.
'''para el ejercicio he cogido el codigo dado y lo he tratado de hacer mas 
legible y comprensible'''
# Definición de la clase ClaseA
class Clase_A: 

    def obtener_instancia (self): #metodo 1 de la clase A , devuelve self
        return self 
 
    def calcular_longitud(self, t): #metodo 2 de la clase A, toma un parámetro 't' y devuelve su longitud
        return len(t) 


instancia_a = Clase_A 
#Asigna la clase A a la variable instancia_a
metodo_y = instancia_a.obtener_instancia 
#asigna el método obtener_instancia a la variable metodo_y
print(metodo_y(instancia_a))

instancia_2a = instancia_a()
#instancia de la clase ClaseA asignada a la variable instancia_2a
print(instancia_2a is instancia_a())
#Comprobación de si instancia_2a es la misma instancia que instancia_a , debuelve un booleano

metodo_z= instancia_2a.calcular_longitud
# Asigna el método calcular_longitud de la instancia instancia_2a a la variable
print(metodo_z(()))  # Llama al método calcular_longitud de instancia_2a con una tupla vacía como argumento
# al estar vacia, el metodo devuelve que la longitud de la tupla es 0
print(instancia_a().calcular_longitud((instancia_a)))  
# Crea una nueva instancia de A y llama al método obtener_longitud con una tupla que contiene la clase A
