""" Bu program modul olşturmak üzere 
deneme olarak yapılmıştır. """

def __dir__():
	return ['ara','ekle','sil']

def ara(sözcük):
    hata = "{} kelimesi sözlükte yok!"
    return sözlük.get(sözcük, hata.format(sözcük))
"""Ara ile ilgili aıklama"""

def ekle(sözcük, anlam):
    mesaj = "{} kelimesi sözlüğe eklendi!"
    sözlük[sözcük] = anlam
    print(mesaj.format(sözcük))
	
def sil(sözcük):
    try:
        sözlük.pop(sözcük)
    except KeyError as err:
        print(err, "kelimesi bulunamadı!")
    else:
        print("{} kelimesi sözlükten silindi!".format(sözcük))

		
		
sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming",
		  "five"       : "five"}
