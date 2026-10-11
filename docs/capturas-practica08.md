# Pruebas de aceptación: sesión 8

Preparar al menos tres categorías (una inactiva), más de cinco productos y un producto asociado a la categoría que se inactivará. No insertar datos en la base del usuario automáticamente. Abrir F12 > Red y conservar las peticiones al navegar.

1. Productos: GET 200 con pagina=0&tamanio=10&ordenarPor=nombre&direccion=asc; categoría en cada fila.
2. Precio: capturar asc y desc con ordenarPor=precio.
3. Tamaño 5 y Siguiente: pagina=1, Página 2.
4. Categoría: limpiar Red, elegir categoría y capturar filtro local sin nuevas peticiones.
5. Nuevo producto: desplegar select, solo categorías activas.
6. Registrar vacío: validaciones de categoría, nombre y precio; sin POST.
7. Registro válido: POST 201, categoriaId numérico y producto en listado.
8. Nombre repetido en minúsculas: POST 409 con mensaje.
9. Editar producto cuya categoría se inactivó después del alta: categoría original visible como inactiva, aviso y guardado bloqueado. Seleccionar otra activa para continuar.
10. Cambiar categoría: PUT 200 y nueva categoría en listado.
11. Baja: DELETE 204, fila Inactivo y botón deshabilitado.
12. Categorías: eliminar una con productos, DELETE 409 y mensaje.

Las pruebas unitarias no reemplazan las capturas. Aún no se adjuntan imágenes ni se afirma que las doce pruebas integradas hayan sido ejecutadas. El PDF se completará a partir de estas evidencias reales.
