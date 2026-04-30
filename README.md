# SWIFT Middleware Simulation

## Opis projektu

Projekt symuluje działanie sieci SWIFT – pośrednika w komunikacji między bankami. System odbiera komunikaty płatnicze w formacie XML (zgodnym z ISO 20022), analizuje je i przekazuje do odpowiedniego banku na podstawie identyfikatora (BIC).

## Jak to działa

1. Bank wysyła komunikat XML do endpointu `/swift/message`
2. System parsuje dane (nadawca, odbiorca, kwota)
3. Na podstawie odbiorcy (BIC) wybierany jest docelowy bank
4. Wiadomość zostaje przekazana dalej (HTTP POST)
5. Operacja jest zapisywana w logach

## Struktura

- `app/` – logika aplikacji (API, serwisy, modele)
- `mocks/` – testowe banki
- `config.py` – mapa banków (BIC → URL)
- `logs.txt` – zapis operacji

## Uruchomienie

### 1. Instalacja zależności

```
pip install -r requirements.txt
```

### 2. Start serwera SWIFT

```
python -m app.main
```

### 3. Start mock banków

```
python mocks/mock_bank.py 3001
...
python mocks/mock_bank.py 3006
```

## Test

### PowerShell:

```
Invoke-WebRequest -Uri http://localhost:3000/swift/message `
  -Method POST `
  -ContentType "application/xml" `
  -InFile payment.xml
```

## Przykładowy komunikat

System używa uproszczonego XML inspirowanego ISO 20022.

## Funkcjonalności

- odbiór komunikatów XML
- parsowanie danych płatności
- routing między bankami
- forward wiadomości
- logowanie operacji

## Autorzy

- Kacper Kowalski
- Jakub Kwaśniak
