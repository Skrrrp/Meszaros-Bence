Mészáros Bence(GCWJHV) beadandó feladat

Projekt: GUI-s felületen elkészített akasztófa játék

A felület létrehozásához tkinter modult használtam, az ábrák megrajzolásához pedig canvast

definicióim:

hibakezeles(szo): Ha a felhasználó hibásan ad meg adatokak akkor ez kezeli az egyes hibákat

ujrakezdes(): A játék ujrakezdéséért felelős

vege(): Ez akkor fut le ha a felhasználó vesztett

rajzol(hibaSzam): Felelős azért, hogy a megfelelő vonalakat és alakokat kirajzolja a canvasra

nyertes(): Ha a játékos nyert akkor lefut

talaltBetu(tippeltbetu): Ha a felhasználó eltalált egy betűt helyesen akkor fut le és kezeli a guis felületen a betűk megjelenését

probaGomb(betu,szo): Ha a próba gombot nyomja le a felhasználó ez fut le és kezeli a lehetséges kimeneteleket

kuldesGomb(): A küldés gombért felelős

A játék 2 emberre van szabva, egy átlagos akasztófa játék ami azt jelenti, hogy valaki kitalál egy szót a másiknak pedig ki kell találni azt

Amikor elindítjuk a programot látható egy entrybox ahová az első felhasználónak be kell irnia azt a szót amit ki kell majd találni

Ezután ha helyesen adta meg a szót a felhasználó akkor átváltozik a felület és elkezdődhet a próbálkozás a másik felhasználó számára
