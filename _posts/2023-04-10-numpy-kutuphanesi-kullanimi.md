---
title: 'Numpy kütüphanesi kullanımı (Jupyter Notebook ile)'
date: 2023-04-10
permalink: 
tags:
  - blog
  - veri bilimi
  - veri madenciliği
---

Numpy dizileri, tüm elemanları aynı değişken tipine sahip olan bir matrisler kümesidir. Numpy, Python `list` gömülü kütüphanesine göre matematiksel hesaplamalar için bir çok önemli fonksiyona sahiptir.

Numpy dizileri tanımlamak için `np.array()` fonksiyonunun içerisine köşeli parantez ile değerler girilir.

##  Numpy Hakkında


```python
import numpy as np
dizi1 = np.array([2,4,6], dtype=np.int32) # dtype eleman tipini belirtir
print(type(dizi1)) # <class 'numpy.ndarray'>
```

Numpy paketinin farklı versiyonlarında çalışılması durumunda bazen paket sürümlerinden kaynaklı problemler ile karşılaşılabilmektedir. Bu nedenle çalışılan paketin sürümünü bilmekte fayda vardır.

Eğer Numpy yüklü değilse `!conda install numpy` komutu ile yükleme gerçekleştirilir.

En kapsamlı Numpy dokümantasyonuna [bu linkten](https://numpy.org/doc/stable/reference/) ulaşılabilir.


```python
print(np.__version__) # 1.20.3 --> Numpy paketinin versiyonununu gösterir.

help(np) # Numpy yardım dosyasına ulaşmak için kullanılır.

np? # benzer şekilde yardım dosyasını açar.
```

## Çok Boyutlu Diziler

`shape` komutu ile dizinin eleman sayıları veya kaç boyutlu olduğu gösterilebilir. 


```python
print(dizi1.shape) # (3, )
```

Dizinin elemanlarına ulaşmak için köşeli parantez kullanılır.


```python
print(dizi1[0], dizi1[1], dizi1[2]) # 2 4 6
```


```python
dizi2 = np.array([[1, 3, 5], [2, 4, 6]]) # 2 boyutlu bir dizi
print(dizi2.shape) # (2, 3) --> 2 satır 3 sütundan oluşan bir matris
print(dizi2[0, 0], dizi2[0, 1], dizi2[1, 2]) # 1 3 6
```


```python
dizi3 = np.array([[[2, 4, 6], [4, 8, 10]], [[1, 3, 5], [6, 7, 8]]]) # 3 boyutlu bir dizi
```


```python
dizi3.shape # (2, 2, 3) 2 satır 3 sütundan oluşan 2 dizi
```

3 boyutlu bir dizinin son boyuttaki elemanına ulaşmak için 3 adet köşeli parantez kullanılır. 4 ve üzeri boyuttaki diziler de tanımlanabilir ancak bu dizilerin gösterilmesi veya görselleştirilmesi çok zordur.


```python
print(dizi3[0][0][0], dizi3[1][0][0]) # 2 1
```

Dizilerin diğer önemli özellikleri şunlardır:

- shape: tuple olarak dizinin şekli hakkında bilgi verir.
- size: dizinin büyüklüğü hakkında bilgi verir. Kaç adet eleman var bilgisi.
- Ndim: Dizinin kaç boyutlu olduğu hakkında bilgi verir.
- nbytes: Verilerin ne kadar yer tuttuğunu söyler.
- dtype: Tutulan elemanların hangi tipte veri olduğunu söyler.


```python
print(dizi3.shape) # (2, 2, 3)
print(dizi3.size) # 12
print(dizi3.ndim) # 3
print(dizi3.nbytes) # 48
print(dizi3.dtype) # int32
```

## Dizi Oluşturma

Dizilerin oluşturulması için `zeros()`, `ones()`, `full()`, `eye()`, `random()` fonksiyonlarından yararlanılabilir.


```python
a = np.zeros((3,3))   # Tüm elemanları 0 olan 3 satır 3 sütun dizi
print(a)              

b = np.ones((2,2))    # Tüm elemanları 1 olan 2 satır 2 sütun dizi
print(b)              

c = np.full((2,2), 3.14)  # Sabit sayılı dizi
print(c)               

d = np.eye(2)         # 2x2 birim matris
print(d)              

e = np.random.random((2,2))  # Rassal sayılardan oluşan bir dizi
print(e)                     #[0.17586812 0.14706117]
                             #[0.13253182 0.25126119]]
```

`arange()`, `linspace()` fonksiyonları sıralı diziler oluşturmak için kullanılır.


```python
print(np.linspace(0,9,3)) # [0,9) arasındaki tam sayılardan eşit aralıkta 3 sayı getirme
# [0.  4.5 9. ]

print(np.arange(5)) # [0,5) arasındaki tam sayılar

print(np.arange(0,10,3)) # [0, 10) arasındaki tam sayıları 3'er artması
```

`random` modülü ile farklı rassal sayı işlemleri gerçekleştirilebilir. `seed` özelliği ile rassal sayıların aynı gelmesi sağlanabilir.


```python
np.random.seed(0) # her zaman aynı rassal sayı üretebilmek için
print(np.random.randint(10, size=(3,5))) # 3 satır 5 sütundan oluşan sayılar
print(np.random.normal(10,2,size=(10,))) # ortalaması 10 standart sapması 2 olan normal dağılıma uyan sayılar

print(np.random.randint(10, size=6)) # Tek boyutlu dizi
print(np.random.randint(10, size=(3, 4))) # iki boyutlu dizi
print(np.random.randint(10, size=(3, 4, 5))) # üç boyutlu dizi

```

## Dizi Dizinleme

Dizi dizinlemek için 3 seçenek bulunmaktadır. Bunlar:
1. Dilimleme ile Dizinleme (Slicing): 
2. Sayılar ile Dizinleme (Integer array indexing)
3. Mantıksal Sınama ile Dizinleme (Boolean array indexing)

### Dilimleme ile Dizinleme


```python
x = np.arange(10)  # 0-10 arasındaki sayılar
print(x[:5])  # ilk 5 eleman
print(x[5:])  # 5 elemandan sonrası
print(x[4:7])  # 4. ve 7 elemanlar arası
print(x[::2])  # tüm elemanlar iki iki artır
print(x[::-1])  # elemanları ters çevir
print(x[5::-2])  # 5 ten sonrasını bir sonraki olacak şekilde ters çevir
```


```python
a = np.array([[1,2,3], [4,5,6], [7,8,9]])

b = a[:2, 1:3] # satırlardaki 2. elemana kadar(0 ve 1), sütunlarda 1 ve 2. eleman

print(a[0, 1])   # 2
b[0, 0] = 99     # b[0, 0] elemanını 99 ile değiştir
print(a[0, 1])   # 77
```


```python
# iç içe diziler(nested) için dilimleme işlemleri
ic_ice = np.array([1,2,[3,4,5, [6,7,8]]])
print(ic_ice[0]) # 1
print(ic_ice[2]) # [3, 4, 5, [6, 7, 8]]
```

### Sayılar ile Dizinleme (Integer array indexing)


```python
b = np.array([0, 2]) # dizinlenecek elemanların sırası

print(a[0, b])  # [1 3] ilk satırdaki ilk ve üçüncü elemanı getir.
```

### Mantıksal Sınama ile Dizinleme (Boolean array indexing)


```python
mantiksal_idler = (a>3) # 3 ten büyük olan verilerin indeks değerleri
print(mantiksal_idler) # Mantıksal sınamaya göre doğru ya da yanlış dönderir

print(a[mantiksal_idler]) # [99  4  5  6  7  8  9]

print(a[a>3]) # aynı çıktıyı verecektir.
```


```python
print(a % 3 == 0) # 3 ile bölünebilen yerlere doğru yazdırır
print(a[a % 3 == 0]) # [99  3  6  9]
```

## Dizilerde Aritmetik İşlemler


```python
x = np.arange(4)
print("x =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # kaç sefer var
print("-x = ", -x)
print("x ** 2 = ", x**2)  # karesi
print("x % 2 = ", x % 2)  # mod bölümünden kalan
```


```python
print(-(0.5 * x + 1)**2) # dizideki elemanları 0.5 ile çarp 1 ekle, karesini al - ile çarp
print(abs(-(0.5 * x + 1)**2))  # mutlak değer
print(np.sum(x))  # dizideki elemanların toplamı
print(np.sum(x, axis=0)) # sütunlardaki elemanların toplamı
print(np.min(x)) # minimun
print(np.max(x)) # maximum
print(np.std(x))  # standart sapma
print(np.var(x))  # varyans
print(np.argmin(x))  # minimum değerin indeksi
print(np.argmax(x)) # maximum değerin indeksi
print(np.median(x)) # medyan
print(np.percentile(x, q=25)) # Q1 yani birinci çeyreklik
```


```python
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(np.add(x, y)) # Eleman eleman toplama

print(np.subtract(x, y)) # Eleman eleman çıkarma

print(np.multiply(x, y)) # Eleman eleman çarpma

print(np.divide(x, y)) # Eleman eleman bölme

print(np.sqrt(x)) # Eleman eleman kök alma
```

`*` veya `multiply()` fonksiyonları eleman eleman çarpım işlemi gerçekleştirir. Vektörel çarpım için `dot` fonksiyonu kullanılmalıdır.


```python
A = np.array([1,2,3])
B = np.array([[4],[5],[6]])
print(A*B) #[[ 4  8 12]
            # [ 5 10 15]
            # [ 6 12 18]]
```


```python
print(np.dot(A,B)) # Vektör çarpım 32
print(A.dot(B)) # benzer kullanım
```

## Boyutsal Dönüşümler

Dizilerin şekillerinden değişiklik yapmak için `reshape` fonksiyonu kullanılabilir.


```python
print(A.reshape(3,1)) # array([[1],
                        # [2],
                        # [3]])
        
print(B.transpose()) # sütunları satır satırları sütuna çevirir.
```


```python
C = np.zeros((2, 2))
D = np.ones((2, 2))
print(np.vstack((C, D))) # D dizisini C dizisinin altına koyar
print(np.hstack((C,D))) # D dizisini C dizisinin sağ tarafına koyar

E = np.eye(2)
print(np.column_stack((C, D, E))) # sütunlarda birleştirir
print(np.row_stack((C, D, E))) # satırlarda birleştirir
```

## Eksenler (Axes)

Yalnızca dizilerin hangi şekilde olduğunu anlamak yeterli olmayabilir bununla birlikte hangi elemanların dizinin hangi ekseninde olduğunu bilmek de önemlidir. NumPy dizilerinde, 0 ve 1 olmak üzere 2 eksen vardır. Örneğin, iki boyutlu bir dizinin dikey ekseni (eksen 0) ve yatay ekseni (eksen 1) vardır. NumPy'deki birçok işlev ve komut, hangi ekseni işlemelerini söylediğinize bağlı olarak değişir.

- `axis=0`: sütunlardaki değerler ile ilgili
- `axis=1`: satırdaki değerler ile ilgilidir.


```python
table = np.array([
    [5, 3, 7, 1],
    [2, 6, 7, 9],
    [1, 1, 1, 1],
    [4, 3, 2, 0],
])
print(table.max()) # 9 
print(table.max(axis=0)) # sutündaki maxlar [5 6 7 9] 
print(table.max(axis=1)) # satırdaki maxlar[7 9 1 4]
```

## Dizilerin Kopyalanması ve Kaydedilmesi

Dizilerin kopyalanması için `copy()` kayıt için ise `save()` fonksiyonları kullanılabilir. Kayıt esnasında `fmt` parametresi ile kaydın formatı değiştirilebilir.


```python
a1 = np.array([1, 2, 3])
b1 = a1
print(b1) # [1 2 3]

a1[0] = 99 # a1'deki değişiklik b1'i etkileyecektir.
print(b1) # [99  2  3]
```


```python
a1 = np.array([1, 2, 3])
b1 = a1.copy() # copy işlemi
a1[0] = 99
print(a1) # [99  2  3]
print(b1) # [1 2 3] a1'deki değişiklik b1'i etkilemeyecektir.

```


```python
np.save("a1_data", a1) # .npy dosyası kaydı gerçekleştirilir.
okunan_a1 = np.load("a1_data.npy")
print(okunan_a1) # [99  2  3]
```


```python
np.savetxt("a1_txt.txt", a1) # txt dosyasına kayıt
a1_txt_okunan = np.loadtxt("a1_txt.txt")
print(a1_txt_okunan) # [99.  2.  3.]
```

fmt nin yapısı şu şekildedir: 

(%[flag]width[.precision]specifier)

flags:
* (-) : left justify
* (+) : Forces to precede result with + or -.
* (0) : Left pad the number with zeros instead of space (see width).

width:
Yazdırılacak minimum karakter sayısı.

precision:
Tam sayı belirteçleri (d,i,o,x), minimum dijit sayısı

- e, E ve f, ondalık noktadan sonra yazdırılacak basamak sayısı.
- g ve G için, anlamlı basamakların maksimum sayısı.
- s için maksimum karakter sayısı.

specifiers:
- c : character
- d or i : signed decimal integer
- e or E : scientific notation with e or E.
- f : decimal floating point
- g,G : use the shorter of e,E or f
- o : signed octal
- s : string of characters
- u : unsigned decimal integer
- x,X : unsigned hexadecimal integer

Daha fazla bilgi için [link](https://docs.python.org/3/library/string.html#format-specification-mini-language).


```python
np.savetxt("a1_txt.txt", a1, fmt='%.2i') # iki basamaklı tam sayı formatında kayıt
np.savetxt('a1_txt.txt', x, fmt='%1.4e')   # üstel gösterimi kullan
```

