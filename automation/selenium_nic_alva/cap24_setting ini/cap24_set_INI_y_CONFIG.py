import configparser

configuracion = configparser.ConfigParser()
configuracion["General"] = {"chrome": "C:\dchrome\chromedriver.exe"}
configuracion["Paginas"] = {"pages": "https://www.outlook.com"}

with open("configuracion.ini", "w") as archivoconfig:
	configuracion.write(archivoconfig) 