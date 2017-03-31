from PIL import Image
from urllib import urlopen
from StringIO import StringIO
import time

def descargar_imagen(nombre):
	###########################################################
	### Descarga las imagenes desde la web que se le indica ###
	### se le pasa el nombre de la imagen por parametros    ###
	###########################################################
	try:
		# Se la ruta donde esta la imagen a descargar
		URL='http://www.web.con/ruta/de/la/imagen/' + nombre
		data = urlopen(URL).read() # Trata la imagen como una cadena
		# Maneja la cadena como un fichero
		file = StringIO(data) 
		imagen = Image.open(file) 
		
		# Muestra la informacion de la imagen a descargar
		print ":: Tamanho ::"
		print imagen.size # informa del tamanho
		print ":: Formato ::"
		print imagen.format # formato
		print ":: Metadatos::"
		print imagen.info # meta informacion
		
		# Ruta donde deseamos guardar la imagen en local
		imagen.save('/ruta/donde/guardar/la/imagen/descargada' + nombre)
		print "Imagen %s guardada", nombre
	except:
		print "Imagen %s no encontrada", nombre

####################################################
### Obtiene valores, que los convertira a nombre ###
####################################################
maximo = 15000
aux = 0 
cntEspera = 0

while aux <= maximo:
	# Convierte el numero en String
	valor = str(aux)
	
	# El nombre de lo que deseamos descargar ha de ser de 6 carcateres
	while len(valor) < 6:
		valor = '0'+ valor	# Anhade un 0 delante
	
	# El nombre de la imagen a descargar
	imagen = str(valor) + '.jpg' # puede ser del tipo que sea
	print imagen
	descargar_imagen(imagen)
	aux +=1
	cntEspera += 1
	# Espera un tiempo cada x descargar, por seguridad
	if cntEspera == 250:
		print "Espera 1\" "
		time.sleep(1);
	
	if cntEspera == 1000:
		print "Espera 5\" "
		time.sleep(5);
		cntEspera = 0
