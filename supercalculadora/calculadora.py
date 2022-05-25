
class Calculadora:
    """
Clase Calculadora
"""
    def sumar(self, a, b):
        """_summary_:
            Funcion sumar
            Suma numero a + numero b
        Args:
            a(int):numero a
            b(int):numero b
        
        Returns:
            _type_: a+b
        
        """ 
        return a + b
    
   

    def restar(self, a, b):
        """ _summary_:
            Funcion restar
            Resta numero a - numero b

        Args:
            a (int): numero a
            b (int): numero b

        Returns:
            _type_: a-b
        """
        return a - b
    

    def dividir(self, a, b):
        """_sumary_:
        Funcion dividir
            Funcion que divide a entre b, si b es igual a 0 devuelve un error por division entre cero
            si el resto de a entre b es distinto a cer devulve error de valor
            Devuelve el cociente de a entre b     
        Args:
            a (int): numero a
            b (int): numero b
        
        Returns:
            _type_:a/b(Int)
        """
        if b == 0:
            return ZeroDivisionError
        if a % b != 0:
            return ValueError
        else:
            return a // b  # En Python 2.x esto funciona sin problemas, pero en Python 3, no. ¿Sabes arreglarlo?
        
