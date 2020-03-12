# Nicolas Sotelo 201623026

import subprocess
import time


#ir a inicio
subprocess.Popen(["adb shell input keyevent 3"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)

#tomar pantallazo
subprocess.Popen(["adb shell screencap /sdcard/Inicio.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
#guardar pantallazo
subprocess.Popen(["adb pull /sdcard/Inicio.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
with open("index.html", 'a') as archivo:
    archivo.write("<img src=\"Inicio.png\" />")
time.sleep(2)

#Arbir launcher
subprocess.Popen(["adb shell input swipe 400 880 400 50 800"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)


# abrir primera aplicacion
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


# volver a inicio y abrir launcher
subprocess.Popen(["adb shell input keyevent 3"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
#Arbir launcher
subprocess.Popen(["adb shell input swipe 400 880 400 50 800"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)


#long tap en 3 apps
subprocess.Popen(["adb shell input swipe 120 355 120 355 1500"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#tomar pantallazo
subprocess.Popen(["adb shell screencap /sdcard/Long1.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
#guardar pantallazo
subprocess.Popen(["adb pull /sdcard/Long1.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
with open("index.html", 'a') as archivo:
    archivo.write("<img src=\"Long1.png\" />")
time.sleep(2)


subprocess.Popen(["adb shell input swipe 340 355 340 355 1500"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#tomar pantallazo
subprocess.Popen(["adb shell screencap /sdcard/Long2.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
#guardar pantallazo
subprocess.Popen(["adb pull /sdcard/Long2.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
with open("index.html", 'a') as archivo:
    archivo.write("<img src=\"Long2.png\" />")
time.sleep(2)


subprocess.Popen(["adb shell input swipe 460 355 460 355 1500"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#tomar pantallazo
subprocess.Popen(["adb shell screencap /sdcard/Long3.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
#guardar pantallazo
subprocess.Popen(["adb pull /sdcard/Long3.png"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
with open("index.html", 'a') as archivo:
    archivo.write("<img src=\"Long3.png\" />")
time.sleep(2)


#ir a inicio
subprocess.Popen(["adb shell input keyevent 3"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)


#estado wifi
script = subprocess.Popen(["adb shell dumpsys wifi | grep 'Wi-Fi is'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = script.communicate()
with open("index.html", 'a') as archivo:
    archivo.write("<p>Estado de wifi = " + str(out.decode('utf-8')) +  "</p>")
time.sleep(2)


#estado modo avion
script = subprocess.Popen(["adb shell dumpsys wifi | grep 'mAirplaneModeOn'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = script.communicate()
with open("index.html", 'a') as archivo:
    archivo.write("<p>Estado de modo avion = " + str(out.decode('utf-8')) +  "</p>")
time.sleep(2)



# abrir contactos
try:
    subprocess.Popen(["adb shell monkey -p com.android.contacts -c android.intent.category.LAUNCHER 1"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
    pass
time.sleep(2)


#oprimir en nuevo
subprocess.Popen(["adb shell input tap 950 1684"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)

# agregar contacto
subprocess.Popen(["adb shell \"input keyboard text 'Oscar'\""], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
subprocess.Popen(["adb shell input keyevent 66"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.Popen(["adb shell \"input keyboard text 'Posada'\""], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
subprocess.Popen(["adb shell input keyevent 66"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.Popen(["adb shell \"input keyboard text '1234567890'\""], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)

#guardar contacto
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


print("end")












