@echo off

echo Pobieranie najnowszych zmian z GitHuba...
git pull

echo Dodawanie wszystkich zmian do indeksu...
git add .

echo Zatwierdzanie zmian...
git commit -m "Automatyczna aktualizacja"

echo Wysyłanie zmian na GitHub...
git push origin master

echo Zakończono aktualizację!
pause
