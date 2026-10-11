# PharmaSoft - Práctica 08

Angular está en la raíz. Spring Boot está en `backend/`. El desarrollo local también se conserva en SEMANA7/tarea07-frontend y SEMANA7/tarea07-backend. Repositorio de esta práctica: https://github.com/Irxui666/tarea08.

## Ejecución
- Frontend: `npm ci` y `npm start -- --port 4200`.
- Backend: Java 21, Oracle en localhost:1522/freepdb1; definir DB_USERNAME y DB_PASSWORD. Desde backend: `mvnw.cmd spring-boot:run`.
- Abrir http://localhost:4200/productos y Swagger http://localhost:8080/swagger-ui.html.
- Reiniciar ambos procesos si estaban ejecutando la versión de sesión 7.

## Funcionalidad
Listado paginado y ordenable por nombre, precio y stock. Filtro de categoría sobre la página actual. Registro y edición con categoría numérica (categoriaId), categorías activas y categoría original inactiva visible con aviso. Guardado bloqueado para categoría inactiva; aviso cuando no existen activas. Baja lógica con botón deshabilitado al quedar inactivo. Errores del servidor mostrados al usuario.

Backend adaptado a categoriaId, paginación, orden permitido, rechazo de categorías inexistentes/inactivas y baja repetida. Categorías conserva el bloqueo de eliminación si existen productos asociados, incluidos inactivos. Esta base usa Oracle y ddl-auto=update; no incluye las migraciones Flyway del backend docente. No se dispone del repositorio docente para actualizarlo desde master.

## Validación
`npm run build`: correcto, chunks diferidos de Productos.
`npm test -- --watch=false`: 18 pruebas aprobadas en 13 archivos.
`mvnw.cmd -DskipTests package`: correcto.
Pruebas Java: ejecutar `mvnw.cmd "-Dtest=CategoriaServiceRulesTest,ClienteServiceRulesTest,ProductoServiceRulesTest" test`.

## Entrega
Rama feature/productos-condori basada en develop. La base de sesión 7 se importó al repositorio inicialmente vacío; no se fusionó ni modificó autonoma07. Ver docs/capturas-practica08.md para las doce evidencias que exige la guía. El PDF Condori_LP2_S8_Practica.pdf debe generarse con capturas reales de Productos; las capturas de sesión 7 no sirven para esta práctica.
