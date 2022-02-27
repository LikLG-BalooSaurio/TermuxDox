from os import system

import socket
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED

import nmap

from time import sleep

import platform
sistema = platform.system()

from colorama import Style, init, Fore
init()






print(Fore.GREEN + """
            ████████████████████████████████████████████████████████████████████
            █─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▀█▀─▄█▄─██─▄█▄─▀─▄███▀▀▀▀▀████▄─▄▄▀█─▄▄─█▄─▀─▄█
            ███─████─▄█▀██─▄─▄██─█▄█─███─██─███▀─▀██████████████─██─█─██─██▀─▀██
            ▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄█▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▀▀▄▄▄▄▀▄▄█▄▄▀
""")



print(Fore.RED + """
                                                                        ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                                                                        ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                                                                        ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█
""")

opcion = 0

print(Fore.GREEN + """
                1) Consguir los puertos de una IP
                2) Localización Numero de telefono
                3) Paginas de Doxing
""")

opcion = int(input(Fore.RED + "    Elige una opción: "))

if opcion == 1:
    system("clear")
    host = input(Fore.GREEN + "    Coloca la IP del objetivo: ")
    print(Fore.GREEN + "Espera un momento!...")
    nm = nmap.PortScanner()
    results = nm.scan(host)


    print(Fore.RED + "Host : %s" % host)
    print(Fore.RED + "State : %s" % nm[host].state())
    for proto in nm[host].all_protocols():
        print(Fore.RED + 'Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        sorted(lport)
        for port in lport:
            print (Fore.RED + 'port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


elif opcion == 2:
    system("clear")
    import phonenumbers
    from phonenumbers import carrier, geocoder

    def numChecker(phoneNumber):
        info = []
        phone = phonenumbers.parse(phoneNumber)
        info.append(geocoder.description_for_number(phone,"es"))
        info.append(carrier.name_for_number(phone,"es"))
        return info
    
    print("""Recuerda que el numero debe llevar el pais!
Ejemplo: +522221927451
""")
    phoneNumber = input("Digite un numero de telefono: ")
    print(Fore.GREEN + "Este numero proviene de: ", numChecker(phoneNumber))
    exit()



elif opcion == 3:
    system("clear")
    d = 0
    print (Fore.RED + """
                ███████████████████████████████
                █▄─▄███▄─▄█▄─▀█▄─▄█▄─█─▄█─▄▄▄▄█
                ██─██▀██─███─█▄▀─███─▄▀██▄▄▄▄─█
                ▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
""")

    print("""
1) pipl             11) ExifData         21) Runt
2) DNI              12) Acreditacion     22) Libreta
3) EstCiv           13) censo            23) StalkScan
4) Operdora         14) EstadoDoc        24) Colegiados
5) Ruc              15) BuscarDatos      25) Direccion
6) Tinfoleak        16) Certificados     26) SkypeIP
7) Sis              17) Licencia         27) Multas
8) FecNac           18) Curp             28) Username
9) Credito          19) Sanciones        29) About
10) Sentinel        20) Sat              30) Salir
""")




int(input(Fore.GREEN + "Selecciona el numero: "))

if d == "1":
        webbrowser.open('https://pipl.com/')

elif d == "2":
        webbrowser.open('http://www.consultadni.info/')

elif d == "3":
        webbrowser.open('https://cel.reniec.gob.pe/valreg/valreg.do')

elif d == "4":
        webbrowser.open('http://www.deperu.com/celulares/')

elif d == "5":
        webbrowser.open('http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias')

elif d == "6":
        webbrowser.open('https://tinfoleak.com/')

elif d == "7":
        webbrowser.open('http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx')

elif d == "8":
        webbrowser.open('https://www.reniec.gob.pe/concer/concer.do')

elif d == "9":
        webbrowser.open('https://www.icetex.gov.co/portalacces/tradicional/solicitar/cptConsultarEstado.asp?origen=portal')

elif d == "10":
        webbrowser.open('https://misentinel.sentinelperu.com/misentinel/misentinel.aspx')

elif d == "11":
        webbrowser.open('http://exifdata.com')

elif d == "12":
        webbrowser.open('http://ww4.essalud.gob.pe:7777/acredita/index.jsp')

elif d == "13":
        webbrowser.open('https://wsp.registraduria.gov.co/censo/_censoResultado.php')

elif d == "14":
        webbrowser.open('https://wsp.registraduria.gov.co/estadodocs/')

elif d == "15":
        webbrowser.open('http://buscardatos.com/')

elif d == "16":
        webbrowser.open('http://certificados.sena.edu.co/')

elif d == "17":
        webbrowser.open('http://web.mintransporte.gov.co/Consultas/transito/Consulta23122010.htm')

elif d == "18":
        webbrowser.open('https://consultas.curp.gob.mx/')

elif d == "19":
        webbrowser.open('https://consulta.simit.org.co/Simit/index.html')

elif d == "20":
        webbrowser.open('https://www.sat.gob.pe/Websitev9')

elif d == "21":
        webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')

elif d == "22":
        webbrowser.open('https://www.libretamilitar.mil.co/Modules/Consult/MilitarySituation')

elif d == "23":
        webbrowser.open('https://stalkscan.com/')

elif d == "24":
        webbrowser.open('http://www.cipica.com/buscolegiado/buscolegiado.php')

elif d == "25":
        webbrowser.open('http://www.midis.gob.pe/padron/')

elif d == "26":
        webbrowser.open('http://mostwantedhf.info/')

elif d == "27":
        webbrowser.open('http://aplicaciones007.jne.gob.pe/multas/')

elif d == "28":
        webbrowser.open('https://namechk.com/')

elif d == "29":
        webbrowser.open('https://www.facebook.com/HackingEnVivo/')

elif d == "30":
        exit()