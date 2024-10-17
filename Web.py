from nicegui import ui, app 
from bicicleta import Bici
from bicipuerto import BiciPuerto

nombre_BiciPuerto = "CUCEI"
biciPuerto =  BiciPuerto(nombre=nombre_BiciPuerto)
app.add_static_files('/csv', 'csv')

bici = Bici()

with ui.header():
    ui.label('|BiciPuerto| ' + nombre_BiciPuerto)

with ui.row().classes("w-full pb-2").style('aling-items:center; justify-content:center; border: 1px solid black; border-radius: 8px'):#pb: para bajar el margen inferior tantos pixeles
    ui.label("Agregar Una Bici")
    ui.separator()#crea o dibuja una franja o renglon en blanco

    style = 'aling-items:center;justify-content:center;border:1px solid gray;border-radius:8px'
    tail = 'w-full ml-5 mr-5'#w-full: window full pantalla completa

with ui.row().classes(tail).style(style):
    ui.label('ID:')
    id_input = ui.input().props('type=number')
    
with ui.row().classes(tail).style(style):
    ui.label('Tiempo de Uso en Horas:')
    uso_input = ui.input().props('type=number')
    
with ui.row().classes(tail).style(style):
    ui.label('Distancia Recorrida:')
    distancia_input = ui.input().props('type=number')

with ui.row().classes(tail).style(style):
    ui.label('Usuario:')
    usuario_input = ui.input()

ui.separator()
with ui.row().classes(tail).style(style):
    ui.button('guardar', on_click = lambda: biciPuerto.insertar_final(Bici(id = id_input.value,
    uso = uso_input.value,
    distancia = distancia_input.value,
    usuario = usuario_input.value)))#lambda es una forma corta de declarar funciones pequeñas y anónimas, osea que no se puedan utilizar en el resto del codigo 

    def mostrar_tabla():
        biciPuerto.mostrar_tabla()
        # bicis = [bici.to_dict() for bici in biciPuerto.bicicletas]
        # print(bicis)
        tabla.add_rows([bici.to_dict() for bici in biciPuerto.bicicletas])
    
    ui.button('mostrar', on_click=mostrar_tabla)

    def guardar():
            biciPuerto.guardar()
            ui.download('/csv/bicis.csv')
            
    def recuperar(e):
            from tempfile import SpooledTemporaryFile
            ui.notification('se subió el archivo ' + e.name)
            content: SpooledTemporaryFile = e.content  # SpooledTemporaryFile es para decirle que es de tipo temporal = 'e.name' en este caso
            with open('./temp/' + e.name, 'wb') as temp:
                temp.write(content.read())
            biciPuerto.recuperar(nombre='./temp/'+e.name)

    ui.button('Respaldar', on_click=guardar)
    ui.upload(label='Recuperar', on_upload=lambda e: recuperar(e))
tabla = ui.table(columns=[{"name": 'id', "label": "ID", "field": "id"},
                  {"name": 'uso', "label": "Uso en Horas", "field": "uso"},
                  {"name": 'distancia', "label": "Metros Recorridos", "field": "distancia"},
                  {"name": 'usuario', "label": "Usuario", "field": "usuario"}],
         rows=[])

 
ui.run()