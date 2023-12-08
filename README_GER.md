# WBGym-Webseite
Die neue Webseite des WBGym in Kleinmachnow

## Informationen für Entwickler

### Ordnerstruktur

Der gesamte Server liegt in dem Order `wbgym/`.
Darin befinden sich die sogenannten Apps, die verschiedene Bereiche der Webseite darstellen:
* Die App namens `wbgym` ist der Kern des Servers und enthält allgemeine Einstellungen für den gesamten Server. Sie wird von Django automatisch erstellt.
* Die App namens `content` ist für die eigentlichen Inhalte der Webseite gedacht, also das, was die Benutzer der Webseite am Ende sehen. Die Benennung ist nicht zwingend und kann geändert werden, falls ein besserer Name gefunden wird.
* Außerdem können weitere Apps hinzugefügt werden, die z.B. für die Verwaltung der Benutzer (ams) oder für die Verwaltung der Datenbank(cms) zuständig sind.

Neben den Apps, sind außerdem zwei weitere Ordner enthalten:
* Der Ordner `static` enthält alle statischen Dateien, die von der Webseite ausgeliefert werden. Das sind z.B. Bilder, CSS-Dateien, JavaScript-Dateien, etc.
* Der Ordner `templates` enthält alle HTML-Dateien, die von der Webseite ausgeliefert werden. Diese Dateien werden von Django als Vorlage genutzt, die dann mit Inhalt befüllt wird, bevor sie dem Nutzer gesendet wird.
