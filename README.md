# Word-Character-Exchanger

Dieses Programm wurde geschrieben, um Wörter zu finden, bei denen man die Anfangsbuchstaben miteinander vertauschen kann.
Inspiration dafür gab mir die Rubrik "Gemischtes Doppel" der Süddeutschen Zeitung.

### Disclaimer
  _Ich habe dieses Programm vor ein paar Jahren aus langeweile geschrieben und irgendwann aufgehört, ohne es zu vollenden.
  Ich bin noch etwas unerfahren was das Programmieren angeht und mir ist klar, 
  dass das Programm nicht super ordentlich und verständlich geschrieben ist. Die Benutzung ist daher auch etwas umständlich.
  Fragen versuche ich so gut es geht zu beantworten._
  
  
### Ordnerstruktur (Beispielhaft)
  
    . 
    └── Word-Changer
        ├── output                # hier werden die Resultate gespeichert
        ├── word_ids              # Ordner für Wörter (alphabetisch sortiert)
        │   ├── a.txt             # Wörter die mit "a" anfangen
        │   ├── abs.txt           # Wörter die mit "abs" anfangen
        │   ├── b.txt             # Wörter die mit "b" anfangen
        │   └── usw.txt
        └── word_ids.txt          # Alle Namen der Textdatein im Ordner "word_ids"  
        
### Funktionsweise

  Der Ordner `word_ids` besitzt Textdateien, die alphabetisch aufgeteilt sind, die alle Wörter (beginnend mit ihrer Bezeichnung) enthalten und
  die Textdatei `word_ids.txt` ist da, um diese zu finden. Dort sind die namen der Textdateien gespeichert, die die Wörter enthalten. Sie werden durch Leerzeichen getrennt.
        
  Im Code muss man nur für die Variable `change_char` den gewünschten Buchstaben einsetzten, z. B. `g`.
  Daraufhin werden die Anfangsbuchstaben aller Wörter, die in den Textdateien im Ordner `word_ids` enthalten sind, mit `g` vertauscht.
  Die neue erstellten Wörter werden mit den existierenden Wörtern, die mit `g` beginnen, abgeglichen und sozusagen verifiziert.
  Diese werden dann im `output` ordner in zwei Textdateien gespeichert.
  Eine in der die Wörter nach Entstehung und eine in der sie alphabetisch sortiert sind.
      
