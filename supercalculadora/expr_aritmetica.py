
class ExprAritmetica:
    """_summary_
    Clase ExprAritmetica
    """
    def __es_numero__(self, cadena):
        """_summary_:
            Funcion __es_numero__
            Comprueba con un bucle try except si la cadena se puede convertir a tipo int
            entonces devolvera True
            En el caso de que no se pueda convertir a int devolver Fals
            Args: 
                cadena:Any (Posiblemente string)

            Returns:
                _type_:Boolean
                return True
                or
                return False
        """
        try:
            int(cadena)
            return True
        except ValueError:
            return False

    def parse(self, exp):
        """
            _sumary_:
            Funcion parse(self,exp)
            Se crean las listas operandos y operadores como listas vacias []
            se crea variable tokens que es igual a la cadena de la variabl exp aplicada la funcion split
            Se inicia un bucle en tokens
                Si la funcion __es_numero__(token)==True entonces se añanade token como int en la lista operandos
                En los demas casos Se añadera a la lista operadores añade token sin convertir a int.
            Devuelve un diccionario con clave Operandos y valor operandos, y con clave Operadores y valo operadores.
            Args:
                exp:Any

            Returns:
                _type_:Dictionary
                {'Operandos':operandos, 'Operadores': operadores}
        """
        operandos = []
        operadores = []
        tokens = str.split(exp)
        for token in tokens:
            if self.__es_numero__(token):
                operandos.append(int(token))
            else:
                operadores.append(token)
        return {'Operandos': operandos, 'Operadores': operadores}
