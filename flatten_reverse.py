'''Soru 1:
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
------'''
#ÇÖZÜM: 

#liste tanımlama
a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

#listeyi düzleştiren fonksiyon
def flat(x):
    #fonksiyona verilen değişken üzerinde for döngüsü ile dönüyoruz.
    for i in x:
        
	  #i değişkeninin veri tipi list,tuple veya set mi diye sorguladığımız kısım.
        if isinstance (i,(list,tuple,set)):
            #eğer i değişkeninin veri tepi list,tuple veya set tiplerinden birisi ise bu i'yi tekrardan fonksiyona gönderiyoruz ta ki bunlardan biri olmayana kadar.
            flat(i)
        else:
            #i nin değeri belirttiğimiz veri tiplerinden birisi değil ise artık bunu artık ekrana yazdırıyoruz.
            print(i)

#fonksiyonu başlattığımız kısım.
flat(a)

#----------------------------------------------------------

'''Soru 2:
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine 
döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
---------'''

#ÇÖZÜM

#liste tanımlıyoruz
a=[[1, 2], [3, 4], [5, 6, 7]]


#listeyi tersine çeviren fonksiyon
def reverse(my_list):
  #ilk başta listenin içerisindeki listelerin sırasını tersine alıyoruz.
  my_list=my_list[::-1]
  
  #listenin eleman sayısı kadar dönen döngü
  for index in range(0,len(my_list)):
    #listenin içerisindeki her bir listenin tersine çevrildiği kısım
    my_list[index]=my_list[index][::-1]
    
  #sonucu return ediyoruz
  return my_list
    
#fonksiyonun çalıştırılıp çıktıların ekrana yazdırıldığı kısım.
print(reverse(a))