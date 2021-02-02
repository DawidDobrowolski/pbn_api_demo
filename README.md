# PBN API DEMO
Prosta aplikacja demonstrująca sposób integracji z API PBN.

## Technologie
- Python 3.8
- Anaconda 3

## Uruchomienie
W celu skorzystania z aplikacji należy:
- dostosować do własnych potrzeb dane w pliku variables.py;
- uruchomić aplikację za pomocą polecenia:
```console
python main.py
```

Możliwe jest także uruchomienie aplikacji z wykorzystaniem środowiska programistycznego.

Po uruchomieniu aplikcja będzie dostępna pod adresem [http://localhost:5000/](http://localhost:5000/),


## Jak zacząć

1. Dostosowujemy plik variables.py, między innymi ustawiamy wartość pól:
- base.auth.uri - adres autoryzacji w systemie PBN np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/auth
- base.api.uri - adres API w systemie PBN np. dla środowiska alpha należy podać https://pbn-micro-alpha.opi.org.pl/api
- application.id - identyfikator aplikacji użytkownika
- application.token - token aplikacji użytkownika, uzyskany przy rejestracji roli Menadżer aplikacji w PBN
2. Wchodzimy na adres, pod którym dostępna jest aplikacja (domyślnie  [http://localhost:5000/](http://localhost:5000/))
3. Logujemy się w tej samej przeglądarce do systemu PBN, z któym chcemy się integrować
4. Przechodzimy pod link na stronie oznaczony "Pobierz token użytkownika".
5. Zostajemy przeniesieni na adres zwrotny aplikacji instytucji, w ramach której wystawienia tokenu żądano. Do adresu doklejony zostanie jednorazowy kod, który służy do pozyskania właściwego tokenu uwierzytelniającego (tokenu użytkownika)
6. Przechodzimy pod adres końcówki, która jest odpowiedzialna za pozyskanie tokenu użytkownika. Do adresu doklejamy pozyskany jednorazowy kod. Przykładowe zapytanie dla domyślnych ustawień: [http://localhost:5000/one-time-token?ott=c69df69c-f1da-4404-b3ea-4031b7399c45](http://localhost:5000/one-time-token?ott=) <br />UWAGA ta operacja wygeneruje nowy token użytkownika, stary token przestanie być aktywny
7. Zostajemy przeniesieni na stronę, na której możemy przetestować końcówki API PBN

## Informacje o aplikacji
Wszystkie niezbędne informacje podano w komentarzach do poszczególnych klas i metod.
Struktura projektu:
```
.
|-- api_demo
|   |-- authorprofile               - pliki obsługi author-profile-controller 
|   |-- conference                  - pliki obsługi conferences-controller
|   |-- data
|   |   |-- multiple-book-and-chapter.json   - przykładowy argument dla /v1/publications
|   |   |-- single-article.json              - przykładowy argument dla /v1/publications/import|   |-- dictionary                  - pliki obsługi dictionary-controller
|   |-- get_token                   - pliki obsługi pozyskania tokenu
|   |-- home                        - pliki obsługi strony głównej
|   |-- institution                 - pliki obsługi institution-controller
|   |-- institution_profile         - pliki obsługi institution-profile-controller
|   |-- journal                     - pliki obsługi journals-controller
|   |-- person                      - pliki obsługi person-controller
|   |-- publication                 - pliki obsługi publications-controller
|   |-- publisher                   - pliki obsługi publishers-controller
|-- templates
|   |-- home.html
|-- main.py
`-- variables.py
```

## Dokumentacja API PBN
- [Centrum pomocy](https://pbn.nauka.gov.pl/centrum-pomocy/baza-wiedzy-kategoria/masowe-interfejsy-wymiany-danych/)
- [Opis końcówek (środowisko testowe)](https://pbn-micro-alpha.opi.org.pl/api/)
- [Opis końcówek (środowisko produkcyjne)](https://pbn.nauka.gov.pl/api/)
