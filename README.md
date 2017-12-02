# minecraft-advent-calendar
Code improvements for the advent calendar sold by conrad.de in 2017
https://www.conrad.de/de/adventskalender-conrad-components-programmieren-mit-minecraft-experimente-ab-14-jahre-1540859.html

Since this is directed to german users, the code and all further text will be in german. Maybe i will add a translation one day.

Da ich mit der Codequalität des Minecraft-Adventskalenders nicht zufrieden war, lade ich hier meine Lösungen hoch. Das dient zum einen als Programmierübung für mich, zum anderen hoffe ich, dass ich auch anderen mit ihren Lösungen helfen kann.

Ich werde versuchen, ab dem dritten Tag immer ein paar Tage Vorsprung zu haben, damit der Code auch rechzeitig zur Verfügung steht.

Hier schon mal ein Codefix für den zweiten Tag. Leider wird die Position des Spielers falsch abgefragt. Die Abfrage muss richtigerweise lauten:

if (p.x <= 18 and p.x >= 16 and p.z <= 8 and p.z >= 6):
