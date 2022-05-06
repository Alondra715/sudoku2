#determine  si un tablero de Sudoku es  9x9 es valido 
#solo las celdas llenas deben validarse de acuerdo con las siuguientes reglas 

#paso 1 chequear quer el tablero introducido sea un tablero de 9x9 
#paso 2 cada fila debe tener datos del 1 al 9 sin repetir datos 
 # Cada caso de prueba está formado por 9 líneas, cada una con 9 números entre el 1 y el 9 separados por espacios,
 #que representan un sudoku completamente relleno.
 



tablero = [
    ["4",".","3",".",".",".","6","7","."]
    ,[".",".",".","1",".","9",".",".","."]
    ,["2",".","9",".","3","6","1",".","."]
    ,[".","9",".",".","6","2",".",".","."]
    ,["7",".","6",".",".",".","5",".","4"]
    ,[".",".",".","5","1",".",".","9","."]
    ,[".",".","1","6","9",".","3",".","7"]
    ,[".",".",".","3",".","8",".",".","."]
    ,[".","3","4",".",".",".","9",".","8"]
]

class sudoku:
     def __init__(self,tablero)->None:
      self.tablero=tablero
      

     def chequeo_general(self):
        
          "endregionc hequear quer el tablero introducido sea un tablero de 9x9"
          
        #"assert"
          assert len(self.tablero) == 9 #filas 
         
          for fila in Self.tablero:
            assert len(fila) == 9  
            "endregionel formato ingresado no respeta el tablero 9x9"
      
      
     def chequeo_filas(self):
          for fila in self.tablero:  
           for elemento in fila:
              if elemento != ".":
                assert fila.count(elemento)==1 #"tablero no valido"


#instanciar el objeto
sudoku= sudoku(tablero)
sudoku.chequeo_general()
sudoku.chequeo_filas()

#alondra_editado_parte 2 logica sudoku.

def chequeo_filas(self,lista_a_chequear)='tablero_general':
    if lista_a_chequear=='tablero_general':
        lista_a_chequear=self.tablero

    for fila in lista_a_chequear:
        for elemento in fila:
            if elemento in ".":
                assert fila.count(elemento)==1,"el tablero ingresado no es valido"

                def chequeo_columnas(self):

                    for columnas_index in range(0,9):
                        for row_index in range(0,9)
                              self.lista_invertida.append(self.tablero[row_index][colum_index])

                              self.chequeo_filas(self.lista_invertida)

                              self.lista_invertida.clear()

def chequeo_subcuadros(self):
    #funcion mayor
    #tenemos 9 subcuadros=chequear en 3 en 3
    # de mis primeras 3 filas → subcuadros del 0 al 3, 3 al 6,6 al 9
    self.chequeo_3_subcuadros(0,3)
    self.chequeo_3_subcuadros(3,6)
    self.chequeo_3_subcuadros(6,9)

def chequeo_3_subcuadros(self,rango1,rango2):
    for colum_index in range(0,9):
        if column_index==3 or column_index == 6:
            self.lista_invertida.clear()
        for [row_index] in range(rango1,rango2):
        self.lista_invertida.append(self.tablero [row_index][column_index])
        if len(self.lista_invertida)==9:
            self.chequeo_filas([self.lista_invertida])
        #chequeo filas
        

#instanciar objeto
if _name_=="_nain_":
    sudoku = validatesudoku(board)
    sudoku.chequeo_general()
    sudoku.chequeo_filas()
    sudoku.chequeo_filas()
    sudoku.chequeo_subcuadros()
    print ('el tablero de sudoku ingresado es valido')
