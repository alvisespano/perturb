
# CONFRONTI TRA CHATBOT


## remove_copies.py

### DOMANDA 1
Le funzioni `remove_copies()` e `remove_copies__remove()` sono semanticamente equivalenti? 
_risposta attesa_: *no*

#### AMAZON Q
Dice che sono uguali e si sbaglia.

#### CHATGPT 4o (free)
Dice che sono equivalenti, ma in realtà si contraddice perché poco sotto dice che ci sono differenze dovute al comportamento diverso tra `del` e `remove()`.

#### GEMINI (free)
Dice che non sono equivalenti.

#### COPILOT - GPT 4o
Dice che sono simili ma non uguali.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che la versione con la `remove()` potrebbe produrre risultati sbagliati rispetto alla versione con la `del`, quindi in pratica capisce che sono diverse semanticamente.

##### Commento 1
I risultati qui riportati non sono esattamente riproducibili: facendo test in momenti diversi, o con account diversi, o semplicemente usando parole diverse, i vari tool danno risultati diversi. C'è una forte aleatorietà difficile da arginare. In altre parole questi esperimenti non rispettano in modo ferreo il metodo scientifico.

##### Commento 2
Abbiamo provato a convincere i vari tool che si sbagliavano - talvolta correggendoli, altre volte confondendoli. Sia quando avevano ragione loro, sia quando avevano torto, dopo averli corretti ti danno sempre ragione. Questo li rende estremamente inaffidabili, perché cercano di non scontrarsi con l'utente umano.


### DOMANDA 2
Le funzioni `remove_copies()` e `remove_copies__cp()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

#### AMAZON Q
Dice che sono uguali ed ha ragione.

#### CHATGPT 4
Dice che non sono equivalenti. Poi si contraddice quando dice che producono lo stesso risultato ma una è più efficiente dell'altra.

#### GEMINI
Dice che non sono equivalenti. Spiega anche perché ma è sbagliato quello che dice.

#### COPILOT - GPT 4o
Dice che sono uguali e spiega anche perché.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che sono equivalenti e mostra anche dei test di chiamata con input diversi.
Forse può runnare i programmi sottobanco?


### DOMANDA 3
Le funzioni `remove_copies()` e `remove_copies__cf()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

#### AMAZON Q
Dice che sono uguali ed ha ragione.

#### CHATGPT 4
Dice che non sono equivalenti ma poi si contraddice, come al solito. Tuttavia questa volta dice una cosa interessante: sostiene che i due programmi sono uguali solo quando k = 1 mentre in generale non lo sono. Quindi dice una cosa giusta: ciò che è sbagliato è la risposta alla domanda, perché i due programmi sono *davvero* equivalenti proprio perché k = 1. Sembra che lui capisca la cosa in generale ma non nello specifico. 

#### GEMINI
Dice che non sono equivalenti e quando spiega perché dice cose sbagliate. Mostra perfino dei casi di input e output, ma non sono veri.
Però è interessante una analisi che propone: sostiene che k sia una specie di "step size" e dice che se è diverso da 1 i programmi diventano differenti.
Capisce quindi il caso generale e attribuisce perfino un ruolo logico a k, però sbaglia la risposta diretta, dicendo che i programmi non sono equivalenti.

#### COPILOT - GPT 4o
Dice che non sono equivalenti, poi nella conclusione si contraddice perché dice che con k = 1 sono equivalenti. Sembra capire bene sia il caso generale che il caso specifico, tuttavia si esprime male.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che sono equivalenti e quando spiega perché dice pure cose giuste. Capisce che nel caso generale non sono uguali, ma nel caso specifico di k = 1 l'equivalenza c'è.

##### Commento 1
Più o meno tutti hanno capito che la differenza sta nella variabile k. Gemini l'ha perfino chiamato "step size", che è davvero notevole. Tuttavia non sono in grado di attribuire l'equivalenza semantica al caso specifico di k = 1 e si soffermano sulla differenza semantica con un k generico.

##### Commento 2
Talvolta sembra che le risposte sbagliate siano più problemi legati alla generazione del testo che non alla mancata "comprensione" (se di comprensione di può parlare). Il fatto che molti tool si contraddicano crediamo sia dovuto al fatto che generano parola per parola usando algoritmi (complessissimi) che seguono un flusso di parole probabili da mettere in coda una dopo l'altra. Quindi capita che dicano cose in contraddizione ora che arrivano alla fine di tutto il discorso.

##### Commento 3
Spesso abbiamo chiesto ai tool di darci una risposta sì o no alla domanda. A volte si contraddicevano rispetto a quando scritto sopra; altre volte confermavano.


### DOMANDA 4
Le funzioni `remove_copies()` e `remove_copies__cp__cf()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

#### AMAZON Q
Dice che sono uguali ed ha ragione.

#### CHATGPT 4
Dice di no e spiega anche perché, ma dice cose sbagliate. Sostiene che la versione `__cp__cf` introduca errori logici.

#### GEMINI
Dice di no. Sostiene che per alcuni input i programmi sono uguali, ma non in generale.

#### COPILOT - GPT 4o
Dice che sono uguali e propone addirittura una spiegazione del perché: dice che semplificando la guardia dell'if diventano lo stesso programma quando k = 1.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che sono uguali e propone dei test corretti.

##### Commento 1
Notiamo che Claude 3.5 Sonnet fa delle analisi step by step, azzarda anche delle sostituzioni, propone dei test e la imbrocca praticamente sempre.



### DOMANDA 5
Le funzioni `remove_copies()` e `remove_copies__cp__cf_2()` sono semanticamente equivalenti?
_risposta attesa_: *sì*

#### AMAZON Q
Dice che sono diversi ed ha torto.

#### CHATGPT 4
Dice di no e quando spiega perché si sbaglia. Sostiene che la versione `__cp__cf_2` introduca degli errori.

#### GEMINI
Dice di no con le solite motivazioni sbagliate.

#### COPILOT - GPT 4o
Dice che sono diversi e dà delle motivazioni sbagliate.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che sono diversi: secondo lui il modulo crea delle condizioni di match differenti che precludono l'uguaglianza.
Inoltre propone dei test case sbagliati: sostiene che i suoi test case provino che le due funzioni non sono equivalenti, invece se esegui davvero i suoi test casi provi esattamente il contrario.

##### Commento 1
Claude 3.5 Sonnet ci mette più tempo degli altri a rispondere. Secondo noi può lanciare un interprete python, per quello dà risposte così precise. Infatti, cambiando un particolare nella guardia dell'if della versione `__cp__cf_2` lui si accorge che sono diversi - ed ha ragione.
Non solo: mettendoci un errore sintattico, lo nota e lo dice, proprio come se avesse l'interprete a disposizione.




## bubblesort.py

### DOMANDA 1
Le 3 funzioni `bubblesort()`, `bubblesort__cp()` e `bubblesort__cf()` sono semanticamente equivalenti? 
_risposta attesa_: *sì*

#### AMAZON Q
Dice di sì ed ha ragione.

#### CHATGPT 4o (free)
Dice di dì ed ha ragione. Incredibile.

#### GEMINI
Dice che `__cf` è uguale ma `__cp` no perché fa una copia dell'input. Si sbaglia: il binding U = A non è una copia.

#### COPILOT - GPT 4o
Dice che sono tutte semanticamnte equivalenti.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che sono tutte equivalenti.




## crivello.py

### DOMANDA 1
Le 3 funzioni `crivello_eratostene()`, `crivello_eratostene__cp()`, `crivello_eratostene__cf()` e `crivello_eratostene__cp__cf/()` sono semanticamente equivalenti? 
_risposta attesa_: *sì*

#### AMAZON Q
Dice di no ed ha torto. Ad esempio, sostiene che la guardia del while nella versione `__cf` sia differente da quella originale.

#### CHATGPT 4o (free)
Dice di sì ed ha ragione.

#### GEMINI
Dice di sì ed ha ragione. Addirittura è in grado di capire che la guardia del while della versione `__cf` è equivalente a quella originale. 
E dice pure che la versione `__cp__cf` è la combinazione delle due precedenti.

#### COPILOT - GPT 4o
Dice che la versione cp  dovrebbe essere equivalente, mentre le ultime due potrebbero avere un comportamento differente per valori di n piccoli,
#### COPILOT - CLAUDE 3.5 SONNET
Dice che le prime due sono emanticamente equivalenti, mentre le ultime due NON lo sono perchè le condizioni nel loop portano a terminare la computazione prima.




## iterative_fibonacci.py

### DOMANDA 1
Le 3 funzioni `ifib()`, `ifib__cp()` e `ifib__cf()` sono semanticamente equivalenti? 
_risposta attesa_: *sì*

#### AMAZON Q
Dice di no ed ha torto. Più precisamente, dice che la `__cf` sia diversa, mentre capisce che le altre due sono uguali.

#### CHATGPT 4o (free)
Dice di sì ed ha ragione.

#### GEMINI
Qui sbaglia e dice che solo `__cp` è equivalente all'originale, mentre `__cf` no.

#### COPILOT - GPT 4o
Dice che le prime due sono equivalenti mentre `__cf` non lo è per colpa del numero diverso di iterazioni.

#### COPILOT - CLAUDE 3.5 SONNET
Come 4o, dice che le prime due sono equivalenti mentre `__cf` non lo è per colpa del numero diverso di iterazioni.





## find_duplicate.py

### DOMANDA 1
Le 3 funzioni `find_duplicate()`, `find_duplicate__cp()` e `find_duplicate__cf()` sono semanticamente equivalenti? 
_risposta attesa_: *sì*

#### AMAZON Q
Dice che sono tutte semanticamente equivalenti.

#### CHATGPT 4o (free)
Sbaglia e dice che solo `__cp` è equivalente all'originale, mentre `__cf` no.

#### GEMINI
Sbaglia e dice che solo `__cp` è equivalente all'originale, mentre `__cf` no. Stavolta come ChatGPT 4o. Mah.

#### COPILOT - GPT 4o
Uguale, sbaglia e dice che solo `__cp` è equivalente all'originale, mentre `__cf` no.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che SONO TUTTE semanticamente equivalenti.



## find_max_count.py

### DOMANDA 1
Le 3 funzioni `find_max_count()`, `find_max_count__cp()` e `find_max_count__cf()` sono semanticamente equivalenti? 
_risposta attesa_: *sì*

#### AMAZON Q
Dice che sono equivalenti.

#### CHATGPT 4o (free)
Dice che sono equivalenti.

#### GEMINI
Dice che sono uguali. Sostiene ci siano solo piccole variazioni che inficiano solo la performance e non la semantica.

#### COPILOT - GPT 4o
Dice che sono equivalenti.

#### COPILOT - CLAUDE 3.5 SONNET
Dice che SONO TUTTE semanticamente equivalenti.

## is_prime.py

### DOMANDA 1
Le 3 funzioni `is_prime()`, `is_prime__cp()`, `is_prime__cf()` e `is_prime__cp_cf()` sono semanticamente equivalenti? 
_risposta attesa_: *sì*

#### AMAZON Q
Dice che la versione `__cf` è equivalente all'originale, mentre la `__cp` e la `__cp_cf` sono diverse. Sembra sia confuso dalla CP.

#### CHATGPT 4o (free)
Anche lui dice che la versione `__cf` è equivalente all'originale, mentre la `__cp` e la `__cp_cf` sono diverse.

#### GEMINI
Dice che sono tutte equivalenti.

#### COPILOT - GPT 4o
Dice che sono tutte semanticamente equivalenti tranne l'ultima.

#### COPILOT - CLAUDE 3.5 SONNET

Dice che SONO TUTTE semanticamente equivalenti.