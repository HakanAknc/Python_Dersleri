#dosya işlemleri
#3 tür komut vardır
#w = write = yazma modu her açılışta dosya sıfırlanır
#a = append = yazı ekleme modu dosyanın içindeki yazıların üstüe ekler
#r = read = sadece okuma yapar yazmaya izin vermez
#utf-8 ise türkçe karekter desteği

dosya = open("deneme.txt",mode="w",encoding="utf-8")
dosya.write("birinci satır\n")
dosya.write("ikinci satır\n")

#\n -> new line demektir
#ikinci satırın aşağa yazılmasını sağlar

dosya.close()

#okuma işlemi

dosya = open("deneme.txt",mode="r",encoding="utf-8")
print(dosya.read())
dosya.close()
