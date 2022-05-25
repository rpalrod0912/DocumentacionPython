import expr_aritmetica
import calculadora



class Supercalculadora:
    """_summary_
        Clase Supercalculadora
    """
    def __init__(self, parser):
        self.calc = calculadora.Calculadora()
        self.parser = parser
    """_summary_:
    Metodo constructor init, inicializa parser
    inicializa calc con valor del metodo Calculadora de la clase calculadora
    inicializa la propiedad parse con valor de parser
        Args:
            parser
    Returns:
        _type_: None
    """
    
    def __operar__(self, expr_descompuesta):
        
        """_summary_:
        Metodo operar con parametro expr_descompuesta
        i-> None, valor nulo
        res_intermedio->0
        Si la cadena '/' esta en expr_descompuesta en los valores de la clave operadores entonces
        Si no se cumple la primera condicion entonces comprobaremos si '-'esta en expr_descompuesta
        clave Operadores, creamos variable i que sera el indice donde se encuentra / en operadores
        Si no se cumple tampoco,comprobaremos si '+' esta en expr_descompuesta clave operadores
        lo mismo pero esta vez sumamos res_intermedito con funciion sumar
        Si no se cumple lo mismo pero comprobando si '-' esta en operadores, se usa funcion restar
        En el caso de no cumplirse nada es un error, assertFalse

        Return(i,res_intermedio)
        
        Args:
            expr_descompuesta:Any
            i:int Indice donde se encuentra el elemento

        Returns :
            _type_:None
            return (i,res_intermedio)
    """
        
        i = None
        res_intermedio = 0
        if '/' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('/')
            res_intermedio = self.calc.dividir(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        elif '-' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('-')
            res_intermedio = self.calc.restar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        elif '+' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('+')
            res_intermedio = self.calc.sumar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        else:
            # Es un error, tenemos que decidir que hacer en los test
            # siguientes
            # Forzamos el error para que no haya problemas luego
            assert False
        return (i, res_intermedio)
    
    def __simplificar__(self, expr_descompuesta):

        """_summary_
            Function:__simplificar__
            
            Si el diccionario expr_descompuesta con clave Operadores tiene de valor lista vacia
                return expr_descompuesta
            En otro caso la tupla i,res_intermedio sera igual a llamar a la funcion operar con expr_descompuesta como parametro
            expresion_simplificado con valo de la expr_descompuesta
            expr_simplificada con clave operadores, le quitamos el elemento(i)
            realizamos lo mismo pero con clave Operandos, 2 veces
            Luego en expr_simplifica con clave Operandos insertamos(i,res_intermedio)
                return funcion simplificar con parametro expr_simplificada
            Args:
                expr_descompuesta: Any

        Returns:
            _type_: None(Any)
                return expr_descompuesta
                or
                return self.__simplificar__(expr_simplificada)
        """

        if expr_descompuesta['Operadores'] == []:
            return expr_descompuesta

        (i, res_intermedio) = self.__operar__(expr_descompuesta)
        expr_simplificada = expr_descompuesta
        expr_simplificada['Operadores'].pop(i)
        expr_simplificada['Operandos'].pop(i)
        expr_simplificada['Operandos'].pop(i)
        expr_simplificada['Operandos'].insert(i, res_intermedio)

        return self.__simplificar__(expr_simplificada)

    def calcular(self, expresion):
        """_summary_
            Function calcular(self,expresion)
            Calcular la expresion y la convierte en str, devuelve en string el resultado de la funcion simplicada con parametro expresion en la clave Operandos con valor 0
        Args:
            expresion (Any): parametro expresion

        Returns:
            _type_: str
            str(self.__simplificar__(self.parser.parse(expresion))['Operandos'][0])
        """
        return str(self.__simplificar__(
            self.parser.parse(expresion))['Operandos'][0])
