# File Mover con Programmazione Temporale

Questo script Python, `mover.py`, legge le informazioni da un file CSV per copiare, rinominare e spostare file da una cartella all'altra in momenti programmati.

## Funzionalità

- **Programmazione temporale:** Copia e rinomina file a una data e ora specificate.
- **Configurazione tramite CSV:** Definisci le operazioni in un file CSV con campi per cartella di origine, cartella di destinazione, nuovo nome del file, data e ora.

## Formato del file CSV

Il file CSV deve contenere le seguenti colonne:

- `source_dir`: Il percorso della cartella di origine.
- `destination_dir`: Il percorso della cartella di destinazione.
- `new_name`: Il nuovo nome del file dopo la copia.
- `date`: La data in formato `YYYY-MM-DD` in cui effettuare l'operazione.
- `time`: L'orario in formato `HH:MM` in cui effettuare l'operazione.

### Esempio

```csv
source_dir,destination_dir,new_name,date,time
/path/to/source1,/path/to/destination1,new_file1.txt,2024-09-01,14:00
/path/to/source2,/path/to/destination2,new_file2.txt,2024-09-02,10:30
/path/to/source3,/path/to/destination3,new_file3.txt,2024-09-03,16:45
```
## Utilizzo
1. Prepara un file CSV con le operazioni desiderate.
2. Esegui lo script:
```bash
python mover.py
```
3. Inserisci il percorso del file CSV quando richiesto.


## Requisiti
- Python 3.x
- Un file CSV con le informazioni delle operazioni

## Note
- Lo script controlla se l'ora attuale corrisponde a quella programmata nel file CSV, con una tolleranza di 1 minuto.
- Le operazioni non verranno eseguite in anticipo rispetto all'orario programmato.

## Licenza
Questo progetto è rilasciato sotto la licenza MIT. Vedi il file LICENSE per maggiori dettagli.