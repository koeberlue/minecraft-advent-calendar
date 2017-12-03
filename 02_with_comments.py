#!/usr/bin/python
# Die erste Zeile sagt dem Computer, wie er unser Programm verstehen soll. Sie
# darf nicht gelöscht werden!

# Wenn eine Zeile mit einer Raute (#) anfängt, wird sie vom Programm ignoriert.
# Solche Zeilen nennt man auch "Kommentar". Kommentare werden benutzt, um Code
# zu erklären. Wir können alle Kommentare löschen und unser Programm würde
# trotzdem genauso funktionieren.

# Wir importieren zunächst "Bibliotheken". Mit der Hilfe von Bibliotheken können
# wir einfach auf andere Programme zugreifen und nützliche Befehle ausführen.

# Die erste Bibliothek (mcpi.minecraft) erlaubt es uns mit unserem Programm auf
# Minecraft zuzugreifen.
import mcpi.minecraft

# Mit der zweiten Bibliothek (RPi.GPIO) können wir dir Anschlüsse des Raspberry
# Pi ein- und ausschalten.
import RPi.GPIO


# Als nächstes definieren wir "Variablen". Variablen sind Platzhalter für unsere
# Daten. Statt also zum Beispiel im Code immer die Zahl 18 zu benutzen, können
# wir sie in der Variable "red" ablegen und können dann immer "red" schreiben,
# wenn wir die Zahl 18 brauchen.

# In der Aufbauanleitung kannst du sehen, dass wir die rote LED am Anschluss
# mit der Nummer 18 angesteckt haben. Einen Anschluss am Computer
# nennt man auch "Port". Damit wir nicht immer in der Anleitung
# nachgucken müssen, an welchem Port die rote LED angeschlossen ist,
# speichern wir die Zahl 18 in der Variable "red".
red = 18

# Die grüne LED ist am Anschluss mit der Nummer 23 angeschlossen.
green = 23

# Die minecraft Variable benutzen wir später, um auf Minecraft zugreifen zu
# können. Dafür benutzen wir die mcpi.minecraft Bibliothek
minecraft = mcpi.minecraft.Minecraft.create()

# Hier sagen wir dem Raspberry Pi, wie wir seine Ports benutzen wollen.
# Zuerst bestimmen wir, welche Nummerierung wir benutzen wollen.
# ( Wenn du diese Zeile jetzt noch nicht verstehst, ist das gar nicht schlimm.
#   Du musst dir nur merken, dass du sie immer hinschreiben musst, bevor
#   du die Ports benutzt ) 
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Jetzt sagen wir dem Raspberry Pi, dass wir die Ports, an denen die
# rote und grüne LED angeschlossen sind, als "Ausgabe"-Port benutzen
# wollen. Das bedeutet, dass wir an diesen Ports mit dem richtigen
# Kommando Strom fliessen lassen können.
# ( Wie man "Eingabe"-Anschlüsse benutzt, sehen wir vielleicht an einem anderen
#   Tag )
RPi.GPIO.setup(red, RPi.GPIO.OUT)
RPi.GPIO.setup(green, RPi.GPIO.OUT)

# Wir haben jetzt alles eingerichtet und können mit dem eigentlichen Programm
# loslegen. Dafür definieren wir erst mal ein paar "Methoden". Methoden sind
# kleine Programme, die wir später in unserem Hauptprogramm benutzen können.

# Mit dieser Methode können wir die LED auf einem Port einschalten.
def ledOn(port):
    # Damit sagen wir der Bibliothek, dass sie den Strom anschalten soll.
    RPi.GPIO.output(port, True)

# Mit dieser Methoden können wir die LED auf einem Port ausschalten.
def ledOff(port):
    # Damit sagen wir der Bibliothek, dass sie den Strom ausschalten soll.
    RPi.GPIO.output(port, False)

# Jetzt kommt unser Hauptprogramm. Unser Programm soll solange laufen, bis es
# über die Tastenkombination Strg+C vom Benutzer beendet wird. Wir wollen
# dauerhaft kontrollieren, wo sich Steve gerade befindet. Wenn er auf der
# grünen Fläche ist, soll die grüne LED angehen. Ansonsten soll die rote LED
# angehen.

# Das 'try' ist wichtig, damit wir später noch "aufräumen" können, wenn
# wir das Programm wieder beenden. Du musst diese Zeile aber noch nicht
# verstehen.
try:

    # 'while' bedeutet, dass das Programm so lange laufen soll, wie die
    # Bedingung erfüllt ist, die hinter dem while steht. Die Bedingung "True"
    # ist immer erfüllt. Damit haben wir also eine "Endlosschleife" gebaut.
    # Unser Programm läuft also eigentlich unendlich lange.
    # ( Die Tastenkombination Strg+C ist in der Computerwelt ein Sonderfall.
    #   Wenn jemand diese Tastenkombination drückt, wird das Programm
    #   beendet, auch wenn es eigentlich unendlich lange laufen sollte).
    while True:

        # Mit diesem Befehl holen wir uns die aktuelle Position von Steve und
        # legen sie in einer Variablen ab.
        position = minecraft.player.getTilePos()

        # ( Wenn du sehen willst, auf welcher Position Steve sich gerade
        #   befindet, kannst du dieses Kommando benutzen)
        # print(position)

        # Jetzt überprüfen wir, ob die Position von Steve mit der Position
        # des grünen Felds übereinstimmt. Das grüne Feld ist in der
        # "x-Richtung" auf Position 17 und in der "z-Richtung" auf
        # Position 7
        if (position.x<=18 and position.x>=16 and position.z<=8 and position.z >=6):
            ledOn(green)
            ledOff(red)
        else:
            ledOn(red)
            ledOff(green)
except KeyboardInterrupt:
    Rpi.GPIO.cleanup()
            
