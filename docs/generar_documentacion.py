from pathlib import Path
import shutil
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit

ROOT=Path(__file__).resolve().parent
TEMP=Path('C:/Users/jomac/AppData/Local/Temp')
CAP=ROOT/'capturas'
CAP.mkdir(exist_ok=True)
items=[
('01-listado','90b5985f-48ee-4819-a471-251346ee088a','Prueba 1. Listado de productos','GET 200; página inicial, tamaño 10 y orden por nombre ascendente. Cada fila muestra su categoría.'),
('02-precio-asc-peticion','cd17f268-1c38-4a1f-a70d-5e16c4ac5ef1','Prueba 2. Petición de orden ascendente','Red muestra ordenarPor=precio y direccion=asc. La tabla visible ya corresponde al orden descendente; esta captura acredita la petición, no el resultado ascendente.'),
('03-precio-desc','f1710fb1-b5ba-4075-abe8-384fdc4f56f2','Prueba 2. Orden descendente por precio','GET 200 con direccion=desc; la tabla presenta precios de mayor a menor.'),
('04-pagina-inicial','0f422a28-71c4-4ad8-af81-edad717e4c91','Prueba 3. Tamaño de página','Tamaño 5, primera página de dos y seis productos en total. La petición incluye tamanio=5.'),
('05-pagina-siguiente','e07db6c4-e7a4-4bcb-be17-b450f83f8d90','Prueba 3. Página siguiente','Página 2 de 2 y petición pagina=1 con tamanio=5; Siguiente queda deshabilitado.'),
('06-filtro-local','573c7309-e871-4103-b546-b80438b83312','Prueba 4. Filtro local por categoría','Se muestran los productos de Analgesicos. Red permanece vacía después de aplicar el filtro sobre la página actual.'),
('07-categorias-activas','d70b701e-75f5-4cd5-bf10-53abc8d3c6a9','Prueba 5. Selector de categorías','El formulario ofrece Analgesicos y Antibioticos. Se observa el selector; no se muestra una categoría inactiva de control para contrastar su exclusión.'),
('08-validaciones','ac85f351-0bc4-4351-9393-3b0019659a54','Prueba 6. Registro vacío','Aparecen validaciones de categoría, nombre y precio. No se observa un POST de registro.'),
('09-alta-payload','5303dced-8f43-471c-b2c3-1b42a704a0c3','Prueba 7. Registro válido: cuerpo','El cuerpo de Ibuprofenado contiene categoriaId: 1 como número, precio: 1, stock: 122 y estado: true.'),
('10-alta-201','9503a3a8-3359-4934-a59e-d6b86de28adc','Prueba 7. Registro válido: respuesta','POST /api/v1/productos responde 201 Created. Ibuprofenado aparece en el listado.'),
('11-duplicado','3a0581fc-1282-4a89-aa5a-986c8a0e63c4','Prueba 8. Nombre duplicado','POST 409 Conflict y mensaje: Ya existe un producto con el nombre flunomarizina. La captura no contrasta por separado variantes de mayúsculas.'),
('12-edicion-inactivo','a4cad64a-236a-4167-8182-187f4c9ebb87','Prueba 9. Aclaración sobre el estado','Se puede editar un producto inactivo: flunomarizin conserva estado false y cambia su precio a 122. Esto no acredita el bloqueo por categoría inactiva; ese caso queda pendiente de evidencia visual.'),
('13-cambio-categoria','b819b227-7cef-47a5-9ce8-c2ff0bed8d2b','Prueba 10. Cambiar categoría','PUT /api/v1/productos/3 responde 200. Amoxicilina pasa de Antibioticos a Analgesicos, como se compara con el listado inicial.'),
('14-confirmacion-baja','c74ee6c7-4a19-4e48-9226-47382b92f6ba','Prueba 11. Confirmación de baja','La interfaz solicita confirmar la baja de Ibuprofeno 400mg antes de enviarla.'),
('15-baja-logica','e89f3442-049f-4e87-bffc-bdbdaf7d2873','Prueba 11. Baja lógica','Red muestra DELETE /productos/42 con 204 No Content. Las filas inactivas permanecen visibles y sus botones Dar de baja están deshabilitados.'),
('16-categoria-conflicto','8a08d583-da02-4932-8be8-e6814f627c81','Prueba 12. Categoría con productos','Mensaje de bloqueo y consola con DELETE /categorias/1 409 Conflict. El panel Headers seleccionado corresponde a otra petición anterior de Productos.')
]
W,H=landscape(A4)
out=ROOT/'Condori_LP2_S8_Practica.pdf'
c=canvas.Canvas(str(out),pagesize=(W,H))
c.setTitle('Condori - LP2 - Práctica 08 - Productos')
c.setAuthor('Condori')
page=0
def frame(title):
 global page
 page+=1
 c.setFillColor(HexColor('#12315c')); c.rect(0,H-65,W,65,fill=1,stroke=0)
 c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',18);c.drawString(30,H-40,title)
 c.setFillColor(HexColor('#617086'));c.setFont('Helvetica',9)
 c.drawString(30,19,'LP II | Práctica 08 | PharmaSoft | 11/10/2026')
 c.drawRightString(W-30,19,str(page))
def lines(text,y,size=12):
 c.setFillColor(HexColor('#173251'));c.setFont('Helvetica',size)
 for line in simpleSplit(text,'Helvetica',size,W-70):
  c.drawString(35,y,line);y-=size+6
 return y-10
frame('Informe de práctica 08')
y=H-103
for t in ['Condori | Lenguaje de Programación II','Módulo Productos dependiente de Categorías','Objetivo: integrar listado paginado, ordenamiento, filtro local, registro, edición y baja lógica de productos en PharmaSoft.',
'Implementación: Angular con rutas diferidas, HttpParams, PaginaResponse<T>, signals y formularios reactivos; Spring Boot con DTO categoriaId, validaciones y paginación. La edición carga producto y categorías con forkJoin.',
'Repositorio: https://github.com/Irxui666/tarea08','Rama: feature/productos-condori | Destino: develop','Pull request: https://github.com/Irxui666/tarea08/pull/1']:
 y=lines(t,y)
c.linkURL('https://github.com/Irxui666/tarea08/pull/1',(30,y,650,y+40),relative=0)
c.showPage()
frame('Alcance, verificación y límites de la evidencia')
y=H-100
for t in ['Validación técnica registrada: compilación Angular correcta; 18 pruebas frontend aprobadas en 13 archivos; empaquetado Java correcto y 10 pruebas backend aprobadas sin errores.',
'Reglas: nombre de 3 a 150 caracteres, precio mínimo 0.01 con hasta dos decimales, stock entero no negativo y categoría numérica obligatoria. Se muestran mensajes del backend y se impide repetir la baja de una fila inactiva.',
'Producto inactivo y categoría inactiva son estados distintos. Editar un producto inactivo está permitido. Para guardar, su categoría debe estar activa. La implementación contempla la categoría original inactiva y el aviso para cambiarla.',
'Las capturas aportadas cubren las operaciones principales. La prueba 9 de categoría inactiva queda pendiente de evidencia visual. En la prueba 2 se acredita la petición ascendente, pero falta una imagen del resultado ascendente. En las pruebas 5 y 8 no se acredita el contraste con una categoría inactiva ni una variante del nombre en mayúsculas.',
'Entorno: frontend localhost:4200, API mediante proxy /api/v1 y Oracle local. La base usa ddl-auto=update; no incluye las migraciones Flyway del backend docente.',
'Fuente de requisitos: s8_lp2_guia_practica_okrbb6xr6o.pdf, paso 9 y lista de cotejo. Las páginas siguientes conservan las capturas originales, con sus observaciones; no se declara que todos los casos estén visualmente comprobados.']:
 y=lines(t,y,11)
c.showPage()
for name,uid,title,caption in items:
 src=TEMP/f'codex-clipboard-{uid}.png'; dst=CAP/f'{name}.png'
 if src.exists(): shutil.copy2(src,dst)
 frame(title)
 y=lines(caption,H-85,10)
 ir=ImageReader(str(dst));iw,ih=ir.getSize()
 avail=y-42;scale=min((W-50)/iw,avail/ih)
 dw,dh=iw*scale,ih*scale
 c.drawImage(ir,(W-dw)/2,42+(avail-dh)/2,width=dw,height=dh)
 c.showPage()
c.save()
print(out)
