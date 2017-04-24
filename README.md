Este codigo esta pensado para obtener imagenes de una ruta url automaticamente.
Este codigo sirve para descargar imagenes que estan nombradas con valores numericos, siguiendo un patron de incremento, lo que permite incrementar este valor obteniendo las imagenes.

El codigo esta preparado para modificar los valores necesarios, modificar la url de la ruta de las imagenes, y el rango del valor numerico,tras eso ya se puede usar.
Tambien contiene medidas de seguridad para evitar que detecten que se estan descargando las imagenes.
Estas medidas son:
- Paradas de 1 segundo cada vez que se alcanza un valor multiplo de 250.
- Paradas de 5 segundos cada 1000 iteraciones.
- Paradas de 7 segundos cada vez qe se alcanza un multiplo del limite de iteraciones.
De esta forma se consigue parar unos segundo para intentar que no detecten una descarga automatica y esto evitar posibles bloqueos o medidas ante las multiplesdescargas.


PARAMETROS:
Se le indica la ruta donde estan las imagenes, en la web (url), y la ruta local donde descargar las imagenes.
