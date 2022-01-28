# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/tools.svg" card_color="#22A7F0" width="50" height="50" style="vertical-align:bottom"/> My Sqlite Database Assistant
Mycroft Skill for adding records to a database using sqlite

## About
My-sqlite-database-assistant-skill (MSDAS) was born out of the need not to constantly search for a tool in my small and hopelessly overcrowded workshop. This resulted in the table name and the data field labels t_name, t_synonym, etc. In my workshop is a Raspberry Pi 3A with Respeaker 4-mic array.

Meanwhile, I use MSDAS as a general tool for retrieving things.

How should MSDAS be used?
Let's start at the end. I'm looking for the hammer again:
Hey Mycroft, where is the tool hammer? The answer is then: Hammer is on shelf 1, bottom shelf, right.


## Further examples
* Hey Mycroft, search tool {tool}
* Hey Mycroft, where is tool {tool}
* Hey Mycroft, record tool
* Hey Mycroft, change tool {tool}
* Hey Mcroft, create database tool

## More...
The trigger word "tool" is important ({tool} is only a substitute for a real tool name). This word generally activates the MSDAS skill (required). The phrase Where is tool ... calls the intent to search for an entry in the database. First, the data field t_name is searched (exact search: WHERE tool = ... ). In t_name are the main names of the tool (or the names by which a tool is known). If the word "hammer" is found there, the record (or records) will be retrieved. The data fields t_storage and t_place contain the information about the storage location, where t_storage represents the storage furniture (cabinet, shelf) and t_place a more precise information, e.g. "bottom board" or "left drawer", where the object is exactly located in the storage furniture.

If "hammer" is not found in the t_name column, the t_synonym column is then searched (similarity search: WHERE tool LIKE %word%). If it is found there, Mycroft reports the location using the main name (t_name). If "hammer" cannot be found as a synonym either, there is a corresponding statement.

### The beginning
How are tools (books, keys, ties, shoes) transported to the data table:
"Hey Mycroft, recording tool!". Now a dialog with the user is started, which asks for name, synonym, storage location and then enters it.

Thereby the table doesn't care at all whether tools are really entered there. So this dialog is possible: 
*User:* Hey Mycroft, recording tool
*Mycroft:* What is the name of the tool?
*User:* Gone with the wind
*Mycroft:* What other names are there for the tool?
*User:* Rhett Butler
*Mycroft:* What cabinet or shelf is it on?
*User:* Black bookshelf
*Mycroft:* Where exactly there?
*User:* Third shelf from the top.

Mycroft confirms the storage if it was successful.

To find out where the *book* Gone With The Wind is I must of course ask the question Hey Mycroft, where is the *tool* Gone With The Wind (or change the code ;-)).

### Configuration on home.mycroft.ai
Path to database: relative or absolute path with '/' at the end
Default: ../databases/
File name: name of the database file
Default: tools.db

**Note:** The directory where the database file is located should be created beforehand to avoid errors. There are built-in functions that check if the tools.db database exists (hard coded) and there is a function that creates the folder ../databases/ and the file tools.db in the specified path.

Example for Picroft: If a default installation of Picroft is used, the working directory for the skills is /home/pi/mycroft-core. If I specify "../databases/" as the path in the skills configuration, then there must be the directory /home/pi/databases.

### Intents
**Create the database in ~./databases (The directory should already exist)**

create.database.intent

create tool database!


**Recording of a new entry**

insert.tool.intent

(addition | record | register) tool

new tool (record | create | register)


**search for a tool (entry)**

find.tool.intent

search tool {tool}

where is tool {tool}

where is the tool {tool}


**change storage location**

change.storage.intent

change tool {tool}!

put tool {tool} somewhere else!


## Credits
JoergZ2

## Category
**Information**
Productivity

## Tags
#Database management
#Picroft

## Deutsche Version
My-sqlite-database-assistant-skill (MSDAS) wurde aus dem Bedürfnis heraus programmiert, in meiner kleinen und hoffnungslos überfüllten Werkstatt nicht ständig nach einem Werkzeug suchen zu müssen. Daraus resultierten der Tabellenname und die Datenfeldbezeichnungen t_name, t_synonym, etc. In meiner Werkstatt steht ein Raspberry Pi 3A mit Respeaker 4-Mikrofon-Array.

Inzwischen benutze ich MSDAS als allgemeines Werkzeug zum Abrufen von Dingen.

Wie sollte MSDAS verwendet werden?
Fangen wir am Ende an. Ich suche wieder den Hammer:
Hey Mycroft, wo ist der Werkzeughammer? Die Antwort lautet dann: Der Hammer ist auf Regal 1, unterstes Regal, rechts.


## Weitere Beispiele
* Hey Mycroft, suche **Werkzeug** {Werkzeug}
* Hey Mycroft, wo ist **Werkzeug** {Werkzeug}
* Hey Mycroft, erfasse **Werkzeug**
* Hey Mycroft, ändere **Werkzeug** {Werkzeug}
* Hey Mccroft, Datenbank **Werkzeug** erstellen

## Mehr...
Das Triggerwort "Werkzeug" ist wichtig ({tool} ist nur ein Ersatz für einen echten Toolnamen). Dieses Wort aktiviert im Allgemeinen die MSDAS-Fähigkeit (erforderlich). Die Phrase Where is tool ... ruft die Absicht auf, nach einem Eintrag in der Datenbank zu suchen. Zunächst wird das Datenfeld t_name durchsucht (genaue Suche: WHERE tool = ... ). In t_name stehen die Hauptnamen des Werkzeugs (oder die Namen, unter denen ein Werkzeug bekannt ist). Wenn das Wort "Hammer" dort gefunden wird, wird der Datensatz (oder die Datensätze) abgerufen. Die Datenfelder t_storage und t_place enthalten die Information über den Lagerort, wobei t_storage das Lagermöbel (Schrank, Regal) darstellt und t_place eine genauere Information, z.B. "Bodenbrett" oder "linke Schublade", wo sich das Objekt im Lagermöbel genau befindet.

Wird "Hammer" in der Spalte t_name nicht gefunden, wird anschließend die Spalte t_synonym durchsucht (Ähnlichkeitssuche: WHERE tool LIKE %word%). Wird er dort gefunden, meldet Mycroft den Ort anhand des Hauptnamens (t_name). Wird "hammer" auch nicht als Synonym gefunden, gibt es eine entsprechende Aussage.

### Der Anfang
Wie werden Werkzeuge (Bücher, Schlüssel, Krawatten, Schuhe) in die Datentabelle transportiert:
"Hey Mycroft, erfasse Werkzeug!". Nun wird ein Dialog mit dem Benutzer gestartet, der nach Name, Synonym, Speicherort fragt und diesen dann eingibt.

Dabei ist es der Tabelle völlig egal, ob dort wirklich Werkzeuge eingetragen sind. So ist dieser Dialog möglich: 
*Benutzer:* Hey Mycroft, erfasse Werkzeug
*Mycroft:* Wie heißt das Werkzeug?
*Benutzer:* Gone with the wind
*Mycroft:* Welche anderen Namen gibt es für das Werkzeug?
*Benutzer:* Rhett Butler
*Mycroft:* In welchem Schrank oder Regal steht es?
*Benutzer:* Schwarzes Bücherregal
*Mycroft:* Wo genau dort?
*Benutzer:* Drittes Regal von oben.

Mycroft bestätigt die Speicherung, wenn sie erfolgreich war.

Um herauszufinden, wo das *Buch* Vom Winde verweht ist, muss ich natürlich die Frage stellen Hey Mycroft, wo ist das *Werkzeug* Vom Winde verweht (oder den Code ändern ;-)).

### Konfiguration auf home.mycroft.ai
Pfad zur Datenbank: relativer oder absoluter Pfad mit '/' am Ende
Standard: ../databases/
Dateiname: Name der Datenbankdatei
Voreinstellung: tools.db

**Hinweis:** Das Verzeichnis, in dem sich die Datenbankdatei befindet, sollte vorher erstellt werden, um Fehler zu vermeiden. Es gibt eingebaute Funktionen, die prüfen, ob die Datenbank tools.db existiert (hart kodiert) und es gibt eine Funktion, die den Ordner ../databases/ und die Datei tools.db im angegebenen Pfad erstellt.

Beispiel für Picroft: Wenn eine Standardinstallation von Picroft verwendet wird, ist das Arbeitsverzeichnis für die Skills /home/pi/mycroft-core. Wenn ich in der Skill-Konfiguration als Pfad "../databases/" angebe, dann muss das Verzeichnis /home/pi/databases vorhanden sein.

### Intents
**Erstellen Sie die Datenbank in ~./databases (Das Verzeichnis muss bereits existieren)**

create.database.intent

erzeuge werkzeug datenbank


**Eintragung eines neuen Eintrags**

insert.tool.intent

(ergänzung | erfassung | erfasse) werkzeug

neues werkzeug (erfassen | anlegen | registrieren)


**Suchen nach einem Werkzeug (Eintrag)**

find.tool.intent

suche werkzeug {tool}

wo (liegt | ist) das werkzeug {tool}


**Speicherort ändern**

change.storage.intent

verändere werkzeug {tool}!

lege werkzeug {tool} woanders hin!