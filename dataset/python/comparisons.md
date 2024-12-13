
#### CONFRONTI TRA AI CHATBOT GENERAL PURPOSE

### remove_copies.py

## DOMANDA 1
Le funzioni `remove_copies()` e `remove_copies__remove()` sono semanticamente equivalenti? 
_risposta attesa_: *no*

# CHATGPT 4
Dice che sono equivalenti, ma in realtà si contraddice perché poco sotto dice che ci sono differenze dovute al comportamento diverso tra `del` e `remove()`.

# GEMINI
Dice che non sono equivalenti.

# COPILOT - GPT 4o
Dice che sono simili ma non uguali.

# COPILOT - CLAUDE 3.5 SONNET
Dice che la versione con la `remove()` potrebbe produrre risultati sbagliati rispetto alla versione con la `del`, quindi in pratica capisce che sono diverse semanticamente.

## Commento 1
I risultati qui riportati non sono esattamente riproducibili: facendo test in momenti diversi, o con account diversi, o semplicemente usando parole diverse, i vari tool danno risultati diversi. C'è una forte aleatorietà difficile da arginare. In altre parole questi esperimenti non rispettano in modo ferreo il metodo scientifico.

## Commento 2
Abbiamo provato a convincere i vari tool che si sbagliavano - talvolta correggendoli, altre volte confondendoli. Sia quando avevano ragione loro, sia quando avevano torto, dopo averli corretti ti danno sempre ragione. Questo li rende estremamente inaffidabili, perché cercano di non scontrarsi con l'utente umano.


## DOMANDA 2
Le funzioni `remove_copies()` e `remove_copies__cp()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

# CHATGPT 4
Dice che non sono equivalenti. Poi si contraddice quando dice che producono lo stesso risultato ma una è più efficiente dell'altra.

# GEMINI
Dice che non sono equivalenti. Spiega anche perché ma è sbagliato quello che dice.

# COPILOT - GPT 4o
Dice che sono uguali e spiega anche perché.

# COPILOT - CLAUDE 3.5 SONNET
Dice che sono equivalenti e mostra anche dei test di chiamata con input diversi.
Forse può runnare i programmi sottobanco?


## DOMANDA 3
Le funzioni `remove_copies()` e `remove_copies__cf()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

# CHATGPT 4
Dice che non sono equivalenti ma poi si contraddice, come al solito. Tuttavia questa volta dice una cosa interessante: sostiene che i due programmi sono uguali solo quando k = 1 mentre in generale non lo sono. Quindi dice una cosa giusta: ciò che è sbagliato è la risposta alla domanda, perché i due programmi sono *davvero* equivalenti proprio perché k = 1. Sembra che lui capisca la cosa in generale ma non nello specifico. 

# GEMINI
Dice che non sono equivalenti e quando spiega perché dice cose sbagliate. Mostra perfino dei casi di input e output, ma non sono veri.
Però è interessante una analisi che propone: sostiene che k sia una specie di "step size" e dice che se è diverso da 1 i programmi diventano differenti.
Capisce quindi il caso generale e attribuisce perfino un ruolo logico a k, però sbaglia la risposta diretta, dicendo che i programmi non sono equivalenti.

# COPILOT - GPT 4o
Dice che non sono equivalenti, poi nella conclusione si contraddice perché dice che con k = 1 sono equivalenti. Sembra capire bene sia il caso generale che il caso specifico, tuttavia si esprime male.

# COPILOT - CLAUDE 3.5 SONNET
Dice che sono equivalenti e quando spiega perché dice pure cose giuste. Capisce che nel caso generale non sono uguali, ma nel caso specifico di k = 1 l'equivalenza c'è.

## Commento 1
Più o meno tutti hanno capito che la differenza sta nella variabile k. Gemini l'ha perfino chiamato "step size", che è davvero notevole. Tuttavia non sono in grado di attribuire l'equivalenza semantica al caso specifico di k = 1 e si soffermano sulla differenza semantica con un k generico.

## Commento 2
Talvolta sembra che le risposte sbagliate siano più problemi legati alla generazione del testo che non alla mancata "comprensione" (se di comprensione di può parlare). Il fatto che molti tool si contraddicano crediamo sia dovuto al fatto che generano parola per parola usando algoritmi (complessissimi) che seguono un flusso di parole probabili da mettere in coda una dopo l'altra. Quindi capita che dicano cose in contraddizione ora che arrivano alla fine di tutto il discorso.

## Commento 3
Spesso abbiamo chiesto ai tool di darci una risposta sì o no alla domanda. A volte si contraddicevano rispetto a quando scritto sopra; altre volte confermavano.


## DOMANDA 4
Le funzioni `remove_copies()` e `remove_copies__cp__cf()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

# CHATGPT 4
Dice di no e spiega anche perché, ma dice cose sbagliate. Sostiene che la versione `__cp__cf` introduca errori logici.

# GEMINI
Dice di no. Sostiene che per alcuni input i programmi sono uguali, ma non in generale.

# COPILOT - GPT 4o
Dice che sono uguali e propone addirittura una spiegazione del perché: dice che semplificando la guardia dell'if diventano lo stesso programma quando k = 1.

# COPILOT - CLAUDE 3.5 SONNET
Dice che sono uguali e propone dei test corretti.

## Commento 1
Notiamo che Claude 3.5 Sonnet fa delle analisi step by step, azzarda anche delle sostituzioni, propone dei test e la imbrocca praticamente sempre.


## DOMANDA 5
Le funzioni `remove_copies()` e `remove_copies__cp__cf_2()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

# CHATGPT 4
Dice di no e quando spiega perché si sbaglia. Sostiene che la versione `__cp__cf_2` introduca degli errori.

# GEMINI
Dice di no con le solite motivazioni sbagliate.

# COPILOT - GPT 4o
Dice che sono diversi e dà delle motivazioni sbagliate.

# COPILOT - CLAUDE 3.5 SONNET
Dice che sono diversi: secondo lui il modulo crea delle condizioni di match differenti che precludono l'uguaglianza.
Inoltre propone dei test case sbagliati: sostiene che i suoi test case provino che le due funzioni non sono equivalenti, invece se esegui davvero i suoi test casi provi esattamente il contrario.

## Commento 1
Claude 3.5 Sonnet ci mette più tempo degli altri a rispondere. Secondo noi può lanciare un interprete python, per quello dà risposte così precise. Infatti, cambiando un particolare nella guardia dell'if della versione `__cp__cf_2` lui si accorge che sono diversi - ed ha ragione.
Non solo: mettendoci un errore sintattico, lo nota e lo dice, proprio come se avesse l'interprete a disposizione.

