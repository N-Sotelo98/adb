# Nicolas Sotelo 201623026

import subprocess
import time


# TODO - instalar la aplicacion aqui. Comando = "adb install /path/to/apk"

# el PACKAGE_NAME_AQUI se puede buscar usando el comando "adb shell pm list packages" y buscando el nombre de la aplicacion instalada: com.APLICACION.algo

# TODO - abrir la aplicacion instalada aqui. Comando = "adb shell monkey -p PACKAGE_NAME_AQUI -c android.intent.category.LAUNCHER 1"

# TODOD - Tomar pantallazo y guardar pantallazo (el codigo está abajo con su comentario)

# TODO - LOOP

n = input("Ingeresar numero positivo:\n")
n = int(n) if int(n) > 0 else 1

codigo = (201623026 % 4) + 7

while ( n >= 0 ) {
    
    # EMPIEZA LOOP ========================================
    
    
    # EVENTO 1. Ir a Home Menu
    subprocess.Popen(["adb shell input keyevent 3"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)

    # Tomar pantallazo : guarda la imagen dentro del celular en /sdcard/NOMBRE.png
    subprocess.Popen(["adb shell screencap /sdcard/Inicio.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    # Guardar pantallazo : extrae la imagen del celular y la guarda en el computador, la guarda en la misma carpeta en donde se encuentra este archivo por defecto
    subprocess.Popen(["adb pull /sdcard/Inicio.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open("index.html", 'a') as archivo:
        archivo.write("<img src=\"Inicio.png\" />")
    time.sleep(2)
   
    # Abre el Launcher, sigue siendo evento 1
    subprocess.Popen(["adb shell input swipe 400 880 400 50 800"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)

    # abrir primera aplicacion, se usan coordenadas X, Y. En este caso se utiliza un Nexus 5. En el menu de desarrollador se pueden activar las COORDS para el dispositivo fisico conectado al pc
    subprocess.Popen(["adb shell input tap 120 355"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)

    #tomar pantallazo
    subprocess.Popen(["adb shell screencap /sdcard/App1.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    #guardar pantallazo
    subprocess.Popen(["adb pull /sdcard/App1.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open("index.html", 'a') as archivo:
        archivo.write("<img src=\"App1.png\" />")
    time.sleep(2)
    
    
    
    
    # AQUI SE ACABA EL EVENTO 1, ENTONCES SE DISMINUYE N SEGUN LO QUE DIJO SERGIO HOY
    n -= 1
    if n % codigo == 0: # oprime el boton BACK (home es con '3')
        subprocess.Popen(["adb shell input keyevent 4"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if n == 0:
        break;
    
    
    


    # EVENTO 2. volver a inicio y abrir launcher (el launcher se abre haciendo un SWIPE desde la parte inferior de la pantalla hasta una parte superio: coordenadas X1 Y2 X2 Y2 DURACION_MILIS)
    subprocess.Popen(["adb shell input keyevent 3"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    #Arbir launcher
    subprocess.Popen(["adb shell input swipe 400 880 400 50 800"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)

    #sigue en evento 2 - long tap en 3 apps, esta es la primera app
    subprocess.Popen(["adb shell input swipe 120 355 120 355 1500"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    #tomar pantallazo
    subprocess.Popen(["adb shell screencap /sdcard/Long1.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    #guardar pantallazo
    subprocess.Popen(["adb pull /sdcard/Long1.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open("index.html", 'a') as archivo:
        archivo.write("<img src=\"Long1.png\" />")
    time.sleep(2)

    # segunda app long atp
    subprocess.Popen(["adb shell input swipe 340 355 340 355 1500"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #tomar pantallazo
    subprocess.Popen(["adb shell screencap /sdcard/Long2.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    #guardar pantallazo
    subprocess.Popen(["adb pull /sdcard/Long2.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open("index.html", 'a') as archivo:
        archivo.write("<img src=\"Long2.png\" />")
    time.sleep(2)

    # tercera app long tap
    subprocess.Popen(["adb shell input swipe 460 355 460 355 1500"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #tomar pantallazo
    subprocess.Popen(["adb shell screencap /sdcard/Long3.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    #guardar pantallazo
    subprocess.Popen(["adb pull /sdcard/Long3.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open("index.html", 'a') as archivo:
        archivo.write("<img src=\"Long3.png\" />")
    time.sleep(2)


     # AQUI SE ACABA EL EVENTO 2, ENTONCES SE DISMINUYE N SEGUN LO QUE DIJO SERGIO HOY
    n -= 1
    if n % codigo == 0: # oprime el boton BACK (home es con '3')
        subprocess.Popen(["adb shell input keyevent 4"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if n == 0:
        break;


    #EVENTO 3 - estado wifi
    script = subprocess.Popen(["adb shell dumpsys wifi | grep 'Wi-Fi is'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = script.communicate()
    with open("index.html", 'a') as archivo:
        archivo.write("<p>Estado de wifi = " + str(out.decode('utf-8')) +  "</p>")
    time.sleep(2)

    
    
    # AQUI SE ACABA EL EVENTO 3, ENTONCES SE DISMINUYE N SEGUN LO QUE DIJO SERGIO HOY
    n -= 1
    if n % codigo == 0: # oprime el boton BACK (home es con '3')
        subprocess.Popen(["adb shell input keyevent 4"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
    
    

    #EVENTO 4 - estado modo avion
    script = subprocess.Popen(["adb shell dumpsys wifi | grep 'mAirplaneModeOn'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = script.communicate()
    with open("index.html", 'a') as archivo:
        archivo.write("<p>Estado de modo avion = " + str(out.decode('utf-8')) +  "</p>")
    time.sleep(2)

    
    
    # AQUI SE ACABA EL EVENTO 4, ENTONCES SE DISMINUYE N SEGUN LO QUE DIJO SERGIO HOY
    n -= 1
    if n % codigo == 0: # oprime el boton BACK (home es con '3')
        subprocess.Popen(["adb shell input keyevent 4"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if n == 0:
        break;
    
    
    
    
    

    # EVENTO 5 - abrir contactos, ABRE LA APLICACION USANDO SU NOMBRE PACKAGE (ESTE ES EL MISMO COMANDO CON EL QUE SE ABRE LA APLICACION EXTERNA AL PRINCIPIO DE TODO)
    try:
        subprocess.Popen(["adb shell monkey -p com.android.contacts -c android.intent.category.LAUNCHER 1"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    time.sleep(2)

    #oprimir en BOTON nuevo PARA AGREGAR (SE USAN COORDENADAS SEGUN UN NEXUS 5)
    subprocess.Popen(["adb shell input tap 950 1684"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)

    # agregar contacto - input keyevent 66 LO QUE HACE ES OPRIMIR 'ENTER' PARA CAMBIAR DE LINEA (esto se hace para nombre, apellido y numero)
    subprocess.Popen(["adb shell \"input keyboard text 'Oscar'\""], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    subprocess.Popen(["adb shell input keyevent 66"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.Popen(["adb shell \"input keyboard text 'Posada'\""], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    subprocess.Popen(["adb shell input keyevent 66"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.Popen(["adb shell \"input keyboard text '1234567890'\""], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)

    #guardar contacto - POR COORDENADAS SE OPRIME SAVE
    subprocess.Popen(["adb shell input tap 990 130"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)

    #tomar pantallazo
    subprocess.Popen(["adb shell screencap /sdcard/contacto.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    #guardar pantallazo
    subprocess.Popen(["adb pull /sdcard/contacto.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open("index.html", 'a') as archivo:
        archivo.write("<img src=\"contacto.png\" />")
        archivo.write("</body></html>")
    time.sleep(2)
    
    
    
     # AQUI SE ACABA EL EVENTO 5, ENTONCES SE DISMINUYE N SEGUN LO QUE DIJO SERGIO HOY
    n -= 1
    if n % codigo == 0: # oprime el boton BACK (home es con '3')
        subprocess.Popen(["adb shell input keyevent 4"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if n == 0:
        break;
    
    
    
    
    
    
    # TERMINA LOOP ========================
    
}



print("end")












