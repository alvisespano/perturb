
#### RISULTATI DEI CONFRONTI 

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
