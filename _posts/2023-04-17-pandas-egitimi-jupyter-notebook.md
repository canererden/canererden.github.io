---
layout: post
title: Pandas Kütüphanesine Giriş Eğitimi Jupyter Notebook ile
date: 2023-04-17
permalink: 
tags:
  - blog
  - veri bilimi
  - veri madenciliği
---

**Bölüm Hakkında**

Bu bölümde, temel pandas veri yapılarını oluşturmadan verileri pandas ile analiz etmeye kadar, pandas'ın veri işleme ve analizi alanındaki yeteneklerini uygulama örnekleri ve pratik egzersizlerle göstererek size yardımcı olacak bir kısa bir kurs olarak verilmiştir. Bu bölümün sonunda, veri okuma ve yazma, veri çerçeveleri birleştirme, veri ön işleme, veri görselleştirme vb. temel deneyimleri kazanmış olacaksınız. Daha sonraki bölümlerinde daha ayrıntılı bir şekilde ele alacağımız kütüphanenin çoğu temel özelliklerini bu bölümde belirteceğiz.

# pandas Kütüphanesine Giriş
Python Pandas kütüphanesi, veri analizi ve işleme için kullanılan açık kaynaklı bir kütüphanedir. Bu kütüphane, veri manipülasyonu, filtreleme, görselleştirme ve veri analizi gibi birçok işlemi kolaylaştırır. Python programlama dilinde Pandas kütüphanesi kullanarak veri analizi yapmak oldukça kolaydır.

Bu yazıda, Python Pandas kütüphanesi hakkında genel bir bilgi edineceğiz ve kütüphane ile nasıl veri analizi yapabileceğimizi öğreneceğiz. 

## pandas Kütüphanesi

Pandas, Python programlama dilinde veri analizi için kullanılan bir kütüphanedir. Veri manipülasyonu, veri filtreleme, veri birleştirme, veri işleme, veri analizi ve veri görselleştirme gibi birçok işlemi yapmamıza yardımcı olur. Pandas, verileri düzenlemek, analiz etmek ve modellemek için yaygın olarak kullanılan bir araçtır.

Pandas kütüphanesi, iki temel veri yapıları olan DataFrame ve Series sınıflarına dayanmaktadır. DataFrame, iki boyutlu bir veri yapısıdır ve sütunlar ve satırlar şeklinde organize edilir. Series, bir boyutlu bir veri yapısıdır ve sadece bir sütun içerir.

## Nasıl Yüklenir?

Pandas kütüphanesi, Python programlama dilinin bir varsayılan kütüphanesi değildir ve sonradan yüklenmesi gerekmektedir. Pandas kütüphanesini yüklemek için aşağıdaki komutu kullanabilirsiniz:

`pip install pandas`


```python
import pandas as pd
import numpy as np
```


```python
pd.__version__ # pandas versiyonu: '1.3.4'
```

## pandas Kullanım Alanları

Pandas, Python programlama dilinde yüksek performanslı ve kullanımı kolay veri analizi ve manipülasyonu kütüphanesidir. Pandas, özellikle tablo benzeri yapıdaki veriler üzerinde çalışmak için tasarlanmıştır ve sütun ve satırların adlandırılmasına ve indekslenmesine izin verir. Pandas ayrıca, veri okuma ve yazma işlemleri için de birçok araç sağlar.

Pandas kütüphanesi ile yapılabilecek işlemler şu şekilde özetlenebilir:
- Veri Okuma ve Yazma
- Veri Seçme ve Sıralama
- Veri Dönüştürme ve Temizleme
- Veri Gruplama ve Birleştirm
- Zaman Serisi Analizi
- Veri Görselleştirme
- Veri Modelleme ve Karşılaştırma


## Veri Yapıları

Pandas kütüphanesi, üç temel veri yapısı olan DataFrame, İndeks ve Series sınıflarına dayanmaktadır: Seriler (Series), Indeksler (Indexes) ve Veri Çerçeveleri (DataFrames).


### Seriler (Series)

Seriler, tek boyutlu bir veri yapısıdır ve birbirinden farklı veri tiplerini içerebilirler. Seriler, indeks ve değerlerden oluşur. Indeksler varsayılan olarak 0'dan başlayan tam sayılar olarak atanabilir veya belirtilen etiketleri kullanarak özelleştirilebilirler.

Seriler, bir boyutlu bir veri yapısıdır ve sadece bir sütun içerir. Seriler, bir liste, dizi veya sözlük gibi bir veri yapısından oluşturulabilir. Seriler aslında veri çerçevesinin sütununu temsil eder.

Aşağıdaki örnekte, bir Seriler nesnesi oluşturulup nesne üzerinde işlemler gösterilmiştir. Örnekler Jupyter Notebook üzerinde gerçekleştirilmiştir.


```python
import pandas as pd

veriler = [1, 2, 5, 8]
seri_ornegi = pd.Series(veriler)

print(seri_ornegi)
```

Bu kod parçacığı aşağıdaki gibi bir görüntü oluşturacaktır.

|       ![](https://bit.ly/3KL6j74)       |
| :-------------------------------------: |
| Şekil 1 - Serilerin ekrana yazdırılması |

Aşağıdaki kod parçacıklarında Seriler hakkında çeşitli metotlara örnekler verilmiştir. 


```python
print(seri_ornegi.dtype) # int64
print(seri_ornegi.values) # [1 2 5 8]
print(seri_ornegi.name) # seri_ornegi
print(seri_ornegi.shape) # (4,)

seri_ornegi2 = pd.Series([2,3,4], index= ['a','b','c'], name='seri_ornegi') # indeks değerlerinin değiştirilmesi 
print(seri_ornegi2.index) # Index(['a', 'b', 'c'], dtype='object')


print(seri_ornegi[seri_ornegi>2]) # 2den büyük veriler

sayilar = np.linspace(0, 10, num=5)
print(sayilar) # [ 0.   2.5  5.   7.5 10. ]

x = pd.Series(sayilar) # indeksler [0, 1, 2, 3, 4]
y = pd.Series(sayilar, index=pd.Index([1, 2, 3, 4, 5]))

print(x + y) # indekslere göre toplama yapılır.

# numpy da iki diziyi toplayınca
print(np.array([1, 1, 1]) + np.array([-1, 0, 1]))
```


```python
print(2 in seri_ornegi) # seri örneğinde 2 değeri var mı?
print(10 in seri_ornegi) # False
```

Görüldüğü gibi Seriler tek boyutlu veri yapılarını temsil etmektedir. İki veya daha fazla boyuttaki veri tipleri ile ilgili ise Veri Çerçeveleri kullanılmaktadır.

### Veri Çerçeveleri (DataFrames)

Veri Çerçeveleri, iki boyutlu bir veri yapısıdır ve birden çok Seriden oluşur. Veri Çerçeveleri, sütunlara ve satırlara göre indekslenir ve her sütun bir Seri nesnesi temsil eder. Her sütun farklı bir veri türüne sahip olabilir. Veri Çerçeveleri, birçok veri kaynağından okunabilir ve birçok farklı şekilde dönüştürülebilir.


DataFrame, iki boyutlu bir veri yapısıdır ve sütunlar ve satırlar şeklinde organize edilir. DataFrame, tablo benzeri bir yapıya sahiptir ve her sütun bir Series nesnesidir. DataFrame'in her bir satırı, bir gözlem veya bir veri noktasını temsil eder. DataFrame, verileri işlemek ve manipüle etmek için birçok yöntem sağlar.

Aşağıdaki örnekte, "isim", "yas" ve "sehir" sütunları olan bir DataFrame nesnesi oluşturur.


```python
data = {'isim': ['Ahmet', 'Mehmet', 'Ali', 'Ayşe'],
        'yas': [28, 22, 30, 25],
        'sehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa']}

df = pd.DataFrame(data)

df
```


|    ![](https://bit.ly/3ooucda)    |
| :-------------------------------: |
| Şekil 2 - Veri Çerçevesi Yazdırma |

Veri Çerçevelerini oluşturmak için yukarıdaki örnekte olduğu gibi tüm veriler listeler içerisine yazılabilir. Bununla birlikte birkaç yöntemden daha bahsetmemiz gerekirse aşağıdaki yöntemleri söyleyebiliriz.


```python
# Veri Çerçevesi oluşturma 1. yöntem
veri_cercevesi = pd.DataFrame(np.random.rand(3, 2),
                              columns=['Sütun 1', 'Sütun 2'],
                              index=['a', 'b', 'c'])
veri_cercevesi
```

Veri çerçevesi oluşturmada 2. yöntem olarak Python veri tiplerinden `sözlükler (dictionary)` kullanılabilir. Sözlükler key:value tiplerinden oluşur.


```python
plakalar = {'istanbul':'34','sakarya':'54','kmaraş':'46'}
nufus_sayilari = {'istanbul':20000000,'sakarya':1000000,'kmaraş':900000}
sehirler = pd.DataFrame({'plaka kodları':plakalar,'nufuslar':nufus_sayilari})
print(sehirler)
```

Eğer index ve sütun değerleri eşleşirse toplama gerçekleşir. Bu durumda `sehirler + sehirler` komutu aşağıdaki çıktıyı verir.


```python
sehirler + sehirler
```

|    ![](https://bit.ly/3L8HLGh)    |
| :-------------------------------: |
| Şekil 3 - İndekslere göre toplama |

sehirler iki boyutlu bir veri yapısına sahiptir. Bu veri yapısı Numpy nesnesine dönüştürülebilir. Bunun için kullanılması gereken komut `to_numpy` komutudur.


```python
print(sehirler.columns) # Index(['plaka kodları', 'nufuslar'], dtype='object')
print(sehirler.values)
print(sehirler.values)
sehirler_numpy = sehirler.to_numpy()
```

Veri Çerçevesi oluşturmanın üçüncü yöntemi de liste fonksiyonları kullanmaktır. Bu duruma örnek aşağıdaki kod parçacıklarında verilmiştir.


```python
veri_listesi = [(n, n**2, n**3) for n in range(5)] # list comprehensions
pd.DataFrame(veri_listesi, columns=['n', 'karesi', 'kubu'])
```

|      ![](https://bit.ly/3MSc0CN)      |
| :-----------------------------------: |
| Şekil 4 - Listeler ile Veri Çerçevesi |

Son olarak Veri Çerçeveleri `random` modülü ile oluşturulabilir.


```python
np.random.seed(12345)
pd.Series(np.random.rand(5), name='rassal')
```


```python
np.random.seed(12345)
disari_cikma = pd.DataFrame(
    {
        'rassal': np.random.rand(5),
        'hava durumu': ['sicak', 'ilik', 'soguk', 'yagmurlu', 'karli'],
        'karar': [np.random.choice(['Dışarı Çık', 'Dışarı Çıkma']) for _ in range(5)]
    },
    index=pd.date_range(start='1/1/2018',
                        freq='1D',
                        periods=5,
                        name='tarih'))

disari_cikma
```

Bu kod parçacığının çıktısı aşağıdaki ekran görüntüsünde verilmiştir.

|         ![](https://bit.ly/3KJqr9K)         |
| :-----------------------------------------: |
| Şekil 5 - random oluşturulan Veri Çerçevesi |

Veri Çerçevesindeki herhangi bir sütuna ulaşmak için iki yöntem kullanılabilir. Birincisinde köşeli parantez içerisinde sütun ismi verilir. Bu durumda sütun isminde boşluk gibi durumların olması çağırmayı etkilemez. İkinci yöntem olan nokta kullanımında ise boşluk gibi özel karakterlerin kullanılması mümkün değildir. Bu kullanımlara örnekler aşağıda verilmiştir.


```python
print(disari_cikma["karar"]) # dışarı çıkma kararı series oldu
print(disari_cikma.karar)# yukarıdaki ile aynı kullanıma sahiptir.
```

### Indeksler (Index)

Pandas Serilerini numpy tek boyutlu dizilerden ayıran nokta indeks değerleridir. Indeks veri tipi sayesinde satır kayıtlarına etiketler ile ulaşılabilir.


```python
indexler = seri_ornegi.index
print(indexler) # Index(['a', 'b', 'c'], dtype='object')
print(type(indexler)) # <class 'pandas.core.indexes.base.Index'>
print(indexler.is_unique) # indeksler tekil verilerden mi oluşuyor mu? True

# indeksler: Değiştirilemez listelerdir.

indeks_1 = pd.Index([1,2,3,4])
indeks_2 = pd.Index([3,4,5])

print(indeks_1.intersection(indeks_2)) # Kesişim: Int64Index([3, 4], dtype='int64')
print(indeks_1.union(indeks_2)) # Birleşim Int64Index([1, 2, 3, 4, 5], dtype='int64')
print(indeks_2.difference(indeks_1)) # Fark Int64Index([5], dtype='int64')
```

## Veri Giriş / Çıkış İşlemleri

Pandas ile işlem yaparken çoğu kez farklı kaynak dosyalarından veri alma ve çıktıları farklı formatlarda yazmak gerekecektir. Bu işlemler, veri ile çalışırken vazgeçilmez işlemlerdir. Aşağıdaki komutlar ile, farklı dosya tipleri ile işlemler gerçekleştirilebilir.
- text dosyası `genfromtxt`
- csv dosyası `read_csv`
- Excel dosyası `read_excel`
- json dosyası `read_json()`
- Veritabanından `read_sql()`

### Verilerin Okunması

Burada bir uygulama üzerinde veri giriş çıkış ve kayıt işlemleri gerçekleştirilecektir. Uygulama için [bu adreste](https://bit.ly/43JubQW) yer alan veri seti kullanılacaktır.


```python
# CSV dosyasının okunması
calisan_verileri = pd.read_csv("employees.csv",
                               skiprows=0,
                               sep=',',
                               header=0,
                               index_col=0)
```

Pandas içerisindeki önemli fonksiyonlardan birisi `read_csv`fonksiyonudur. Bu fonksiyon CSV dosyalarını pandas DataFrame veri yapısına dönüştürmek için kullanılır. Bu yöntem aşağıdaki parametrelerle çağrılabilir:

- `filepath_or_buffer`: Okunacak CSV dosyasının yolu ya da URL'si.
- `sep`: Dosya içerisindeki sütunları ayırmak için kullanılacak ayırıcı karakteri belirtir. Varsayılan ayırıcı virgüldür.
- `delimiter`: Dosya içerisindeki sütunları ayırmak için kullanılacak ayırıcı karakteri belirtir. sep parametresiyle aynı işlevi görür.
- `header`: Başlık satırının (sütun adları) var olup olmadığını belirtir. Varsayılan değer infer ile, ilk satırdaki değerlere göre otomatik olarak belirlenir.
- `index_col`: Veri setinde hangi sütunun index olarak kullanılacağını belirtir.
- `usecols`: Hangi sütunların alınacağını belirtir. Varsayılan olarak tüm sütunlar alınır.
- `dtype`: Sütunların veri tiplerini belirtir.
- `skiprows`: Dosyadaki belirtilen satır sayısı kadar okunmadan atlanır.
- `skipfooter`: Dosyanın sonundan belirtilen satır sayısı kadar okunmadan atlanır.
- `nrows`: Okunacak maksimum satır sayısını belirtir.
- `na_values`: Boş veya eksik verilerin nasıl işleneceğini belirtir. Varsayılan olarak, herhangi bir boş veya eksik veri NAN olarak belirlenir.
- `encoding`: Dosyanın karakter kodlamasını belirtir.

### Verilerin Kaydedilmesi

pandas kütüphanesi, farklı dosya biçimleri için çeşitli yazdırma metotları sunar. Bazı örnekler aşağıdaki gibidir:

to_csv: Bu metot, verileri bir CSV dosyasına yazdırmak için kullanılır. 



```python
# DataFrame'i bir CSV dosyasına yazdır
calisan_verileri.to_csv('calisan_verileri.csv', index=False)
```

Bu örnekte, `to_csv()` metodu kullanılarak bu veriler calisan_verileri.csv dosyasına yazdırılır. index=False parametresi, verilerin index sütununu dahil etmemeyi sağlar.

to_csv() yöntemi, verileri CSV dosyasına yazarken belirli bir klasöre kaydetmek için `path_or_buf` parametresini kullanır. Bu parametreye tam bir dosya yolu veya dosya adı verilebilir. Ayrıca, alt dizinleri de dahil ederek farklı klasörlere kaydetmek için dosya yolu belirtirken dizin adı da kullanılabilir.

- normal şekilde kayıt


```python
calisan_verileri.to_csv('./data/calisan_verileri.csv', index=False)
```

Bu örnekte, ./data yolunu kullanarak calisan_verileri.csv dosyasını data klasörü altında oluşturduk. Bu örneğin çalışabilmesi için çalışma klasörününün içerisine data adında bir klasör oluşturmak gerekmektedir. index=False parametresi, DataFrame'in satır dizinlerinin CSV dosyasına yazılmamasını sağlar. Eğer index=True olarak ayarlanırsa, satır dizinleri CSV dosyasına yazdırılacaktır.

Klasörlerin konumları ile ilgili şunları bilmek gereklidir.

'./' dizini, bulunduğumuz çalışma dizinini temsil eder. Bu nedenle, './data' ifadesi, bulunduğunuz dizin içindeki 'data' adlı bir alt dizine işaret eder. '.' karakteri, mevcut dizini ifade etmek için kullanılır.

'..' ise bir üst dizini ifade eder. Örneğin, '../data' ifadesi, mevcut dizinin bir üstündeki dizindeki 'data' adlı bir alt dizine işaret eder.

'\' karakteri, Windows işletim sistemlerinde dosya yollarında kullanılan bir kaçış karakteridir. Bu karakter, dosya yolu bölümlerini ayırmak için kullanılır. Örneğin, "C:\Users\kullanici_adi\Desktop" ifadesinde, '\' karakterleri "C:", "Users", "kullanici_adi" ve "Desktop" gibi dosya yolu bölümlerini ayırmak için kullanılır. Unix tabanlı işletim sistemlerinde ise '/' karakteri kullanılır.

Python'da da '\' karakteri kaçış karakteri olarak kullanılır. Ancak, Windows işletim sistemlerinde olduğu gibi dosya yollarında kullanılan '\' karakterleri yerine, Python'da Unix tabanlı işletim sistemlerinde olduğu gibi '/' karakterleri kullanılır. Bunun nedeni, Windows işletim sisteminde '\' karakterinin kaçış karakteri olarak kullanılmasıdır ve dosya yollarında kullanılan '' karakteri tek başına bir kaçış karakteri olarak algılandığından, dosya yolu yazımında hatalara yol açabilmektedir.

Bununla birlikte Python'da iki tane arka arkaya '\' karakteri, bir tanesi normal bir karakter olarak kabul edilip diğerinin kaçış karakteri olarak kabul edilmesini sağlamak için kullanılır. Örneğin, "\\server\path\filename" ifadesinde, iki tane '\' karakteri, dosya yolunda kullanılan normal '' karakterleri ve kaçış karakterleri arasında bir ayırıcı olarak işlev görür. Bu ifadede, ilk iki '\' karakteri, '\server' dizini için normal '' karakterleridir. Sonraki iki '\' karakteri, '\path' dizini için normal '' karakterleridir. Ve son olarak, son '\' karakteri, dosya adı olan 'filename' için normal '' karakteridir.

- `os` modülü kullanarak kayıt

`os` modülü kullanarak da dosyaları farklı klasörlere kaydedebilirsiniz. Eğer data klasörü yoksa oluştur komutunu da burada verebilirsiniz. Örneğin:


```python
import os

folder_path = './data'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, 'calisan_verileri.csv')
calisan_verileri.to_csv(file_path, index=False)
```

Bu örnekte, os modülü kullanılarak öncelikle ./data klasörü oluşturulur. Daha sonra, os.path.join() yöntemi kullanarak calisan_verileri.csv dosyasının tam yolu oluşturulur ve DataFrame to_csv() yöntemi kullanılarak bu dosyaya yazdırılır.

`to_excel`: Bu metot, verileri bir Excel dosyasına yazdırmak için kullanılır. Örnek kullanımı:


```python
# DataFrame'i bir Excel dosyasına yazdır
calisan_verileri.to_excel('calisan_verileri.xlsx', index=False)
```

Elde edilen Excel dosyası açıldığında aşağıdaki gibi düzgün bir çıktı alınacaktır.

|   ![](https://bit.ly/3GSSYbx)   |
| :-----------------------------: |
| Şekil 6 - Excel Ekran Görüntüsü |



`to_sql`: Bu metot, verileri bir SQL veritabanına yazdırmak için kullanılır.

## pandas Veri Tipleri

Pandas veri yapıları, aşağıdaki veri tiplerini içerebilir:

- float: Ondalık sayıları temsil eder. Örneğin, 3.14 gibi.
- int: Tam sayıları temsil eder. Örneğin, 42 gibi.
- bool: True ve False mantıksal değerlerini temsil eder.
- datetime: Tarih ve zaman değerlerini temsil eder. Örneğin, "2022-01-01 12:00:00" gibi.
- timedelta: İki tarih veya zaman arasındaki farkı temsil eder.
- object: Stringler, listeler, sözlükler, vb. nesneleri temsil eder.

Pandas, bu temel veri yapılarına ek olarak, Categorical ve Sparse veri yapıları da sunar. Categorical veri yapısı, kategorik verileri temsil etmek için kullanılır ve Sparse veri yapısı, verilerin seyrek veya büyük olduğu durumlarda bellek kullanımını optimize etmek için kullanılır.

`dtypes`, bir veri çerçevesinin tüm sütunlarının veri tiplerini gösteren bir özelliktir. Pandas DataFrame'i, farklı veri tiplerini (int, float, bool, string, datetime vb.) içeren sütunlardan oluşabilir. Her bir sütunun veri tipi, o sütundaki verilerin nasıl işleneceğini belirler.

`dtypes`, DataFrame'deki sütunların veri tiplerini gösteren bir Seri nesnesi döndürür. Bu özellik, DataFrame'deki her sütunun veri tipini belirlemek ve herhangi bir sütunun veri tipini değiştirmek gibi işlemler yapmak için kullanılabilir. Ayrıca, farklı veri tiplerine sahip sütunların DataFrame'deki verileri nasıl işlediğini anlamak için de kullanılabilir. Örneğin, bir sütunun tamsayı değerleri taşıması ve daha sonra ondalık sayılara dönüştürülmesi isteniyorsa, bu özellik, ilgili sütunun veri tipini değiştirmek için kullanılabilir.


```python
calisan_verileri.dtypes
```

| ![](https://i.vgy.me/EaxeJm.png) |
| :------------------------------: |
| Şekil 7 - dtypes ekran görüntüsü |

`info()` metodu ise, DataFrame'in bellekteki boyutunu, sütunların isimlerini, dolu hücrelerin sayısını ve her sütundaki veri tiplerinin sayısını görüntüler. Bu metot ayrıca bellekteki DataFrame'in bellek kullanımı ve veri tipleri hakkında da bilgi sağlar.

Ayrıca, her bir sütundaki eksik değerlerin sayısını ve veri tiplerinin bellek boyutunu da verir. Bu bilgi, veri seti üzerinde eksik değerlerin olduğu veya yanlış veri tipleri kullanıldığı durumlarda hataların nedenini anlamak için kullanılabilir.


```python
calisan_verileri.info()# non-null sayılarını görmek için
```

![](https://i.vgy.me/Un0Upa.png)

Bununla birlikte bazı durumlarda veri tipleri arasında değişiklik yapılmak istenebilir. Bunun için `astype()` metodu kullanılabilir. Bu metot, Pandas DataFrame sütunlarının veri tiplerini değiştirmek için kullanılır. Bu yöntem, mevcut bir DataFrame'deki bir veya daha fazla sütunun veri tipini değiştirerek, veri analizi veya veri manipülasyonu için daha uygun bir formata dönüştürmeye olanak tanır.

Örneğin, bir sütunun veri tipini sayısal bir formattan tarih veya saat formatına dönüştürmek isteyebilirsiniz. Bu durumda, `astype()` yöntemini kullanarak sütunun veri tipini değiştirebilirsiniz.

Ayrıca, `astype()`, sayısal sütunları float veya integer veri tiplerine dönüştürerek hesaplama işlemlerinin hızını arttırmaya da yardımcı olabilir.


```python
calisan_verileri['Salary'] = calisan_verileri['Salary'].astype(float)
```

Yukarıdaki örnekte, `astype()` yöntemi kullanılarak 'Salary' sütununun veri tipi integer'dan float'a değiştirildi.


```python
calisan_verileri.dtypes
```

## Veri Seti Üzerinde İşlemler
Veri seti çok sayıda veriden oluşmaktadır. Bu nedenle veri setinin doğru şekilde alındığını göstermek açısından ilk satırlarının yazdırılması faydalı olacaktır. Bunun için `head()` metodu kullanılabilir.


```python
calisan_verileri.head()
```

|      ![](https://bit.ly/3MTEBaS)       |
| :------------------------------------: |
| Şekil 6 - Veri setinin ekran görüntüsü |


```python

```


```python
calisan_verileri.head(2) # ilk 2 veri
print(calisan_verileri.empty)  # False
print(calisan_verileri.shape)  # (1000, 7),
print(type(calisan_verileri))  # <class 'pandas.core.frame.DataFrame'>
print(calisan_verileri.columns) 
```


```python
print(
    "bu veri setinde {} adet veri vardır. Ayrıca özellik sayısı {}'dir.".
    format(calisan_verileri.shape[0], calisan_verileri.shape[1]))
```

Pandas kütüphanesi DataFrame ve Series veri tiplerinde kullanılan `describe()` fonksiyonu, temel istatistiksel bilgileri özetleyen bir tablo oluşturur. Bu istatistiksel bilgiler arasında ortalama, standart sapma, minimum değer, maksimum değer, medyan, çeyreklikler ve veri sayısı yer alır.

`describe()` fonksiyonu, özellikle veri setinin özetini hızlı bir şekilde elde etmek istediğinizde kullanışlıdır. Fonksiyon, sayısal verilerin yanı sıra kategorik veriler hakkında da bazı temel istatistiksel bilgiler sağlar.


```python
calisan_verileri.describe() # veri özetleme
```

Bu örnekte, `describe()` fonksiyonu calisan_verileri DataFrame'ine uygulanmış ve istatistiksel bilgileri özetleyen bir tablo oluşturulmuştur.

Bu tablo, maaş ve Bonus sütunları için temel istatistiksel bilgileri özetlemektedir. Çıktı aşağıdaki gibi görünecektir:

![](https://i.vgy.me/vjCarD.png)

`describe()` fonksiyonu, varsayılan olarak sadece sayısal sütunlar için çalışır. Bununla birlikte, include parametresi kullanılarak belirli sütun türleri de tanımlanabilir. Örneğin, tüm sütunlar için istatistiksel özet bilgileri almak için `include='all'` parametresi kullanılabilir.

`describe()` fonksiyonunun ayrıca percentiles parametresi de vardır. Bu parametre, özet istatistiklerindeki çeyreklikleri belirlemek için kullanılan yüzde değerleri tanımlamak için kullanılabilir. Varsayılan olarak, `percentiles` parametresi [0.05, 0.95] olarak ayarlanmıştır.

Ayrıca, bu fonksiyonu varsayılan olarak tüm sütunlardaki eksik değerleri atlar. Bu davranış, `include='all'` parametresiyle aşılabileceği gibi, ayrıca dropna=False parametresi kullanılarak da değiştirilebilir. Bu, eksik değerlerin de dahil edilmesini sağlar ve eksik değerlerin sayısını özet istatistiklerinde gösterir.


```python
calisan_verileri.describe(percentiles=[0.05, 0.95]) # diğer dilimleri de görüntülemek için
```

Veri çerçevesinde veri manipülasyonu, analizi ve temizliği için kullanılan pandas kütüphanesi, veri çerçevesi objeleriyle ilgili birçok metot içermektedir. Bu metotlar, veri işleme sürecinde oldukça yararlıdır. Aşağıda, bazı önemli veri çerçevesi metotları ve kısa açıklamaları yer almaktadır:

- `head()`: Veri çerçevesinin ilk birkaç satırını görüntüler.
- `tail()`: Veri çerçevesinin son birkaç satırını görüntüler.
- `drop()`: Veri çerçevesinden belirtilen sütun veya satırları çıkarır.
- `groupby()`: Belirli bir sütuna göre verileri gruplar.
- `merge()`: İki veya daha fazla veri çerçevesini belirtilen sütuna göre birleştirir.
- `sort_values()`: Belirli bir sütuna göre verileri sıralar.
- `pivot_table()`: Veri çerçevesindeki verileri bir tablo halinde yeniden düzenler.
- `isna() / isnull()`: Veri çerçevesindeki boş değerleri (NaN) tespit eder.
- `fillna()`: Veri çerçevesindeki boş değerleri belirli bir değerle doldurur.
- `drop_duplicates()`: Veri çerçevesindeki tekrarlayan satırları çıkarır.
- `apply()`: Veri çerçevesinde belirtilen işlevi sütunlar veya satırlar üzerinde uygular.
- `map()`: Belirtilen bir işlevi veri çerçevesinin belirli bir sütununa veya serisine uygular.
- `replace()`: Belirli bir değeri başka bir değerle değiştirir.
- `count()`: Her sütundaki non-null (boş olmayan) veri sayısını verir.
- `nunique()`: Her sütundaki benzersiz (tekrar etmeyen) veri sayısını verir.
- `sum()`: Her sütundaki sayısal verilerin toplamını verir. Eğer sütunda sayısal veri yoksa o sütun atlanır.
- `corr()`: Sütunlar arasındaki korelasyon matrisini oluşturur. Korelasyon, iki değişken arasındaki ilişkinin gücünü ve yönünü ölçer. Değerler -1 ile 1 arasındadır. -1 mükemmel negatif korelasyonu, 1 mükemmel pozitif korelasyonu ve 0 korelasyon olmadığını gösterir.


```python
calisan_verileri.count()
```

`count()`, `sum()`, `mean()`, `min()`, `max()`, `std()` ve `corr()` fonksiyonları hem Series hem de DataFrame veri yapıları için kullanılabilirken `nunique()`, `value_counts()` gibi fonksiyonlar ise yalnızca Series veri yapısı için kullanılabilirdir.


```python
calisan_verileri.Team.value_counts() # hangi takımda kaç kişi var?
```


```python
# Takımlara ait istatistikler
calisan_verileri.groupby('Team').mean()
```


```python
calisan_verileri.groupby('Team').Team.count()
```


```python
calisan_verileri.Team.unique() # Tekil verileri getirir.
```


```python
calisan_verileri_kopya = calisan_verileri_kopya.drop(['Gender'], axis=1)
```

### Formül Uygulama

Pandas kütüphanesi, `map()` ve `apply()` gibi fonksiyonlar aracılığıyla veri işleme işlevselliği sağlar.

`map()` fonksiyonu, bir pandas Serisi'ndeki tüm öğeleri değiştirmek için kullanılır. Bu işlev, bir sözlük, işlev veya Seri nesnesi alabilir ve Seri öğelerini değiştirmek için bu nesneleri kullanır. Örneğin aşağıdaki kod, Salary Serisi'deki tüm öğelere 200.000 artırarak ve sonucu ekrana yazdıracaktır:


```python
calisan_verileri.Salary.map(lambda x: x+200000) # Salary lere toplu artış
```

`apply()` fonksiyonu ise, bir DataFrame'in bir sütununda veya satırında işlevleri uygulamak için kullanılır. `apply()` fonksiyonu, `map()` fonksiyonuna benzer şekilde işlevlerin uygulanmasında kullanılır ancak, DataFrame veri yapısında uygulanır. Aşağıdaki kod, istenilen DataFrame sütununda bir yazılan fonksiyonun işlemini yapacak ve sonucu ekrana yazdıracaktır.


```python
def fonksiyon_ismi(x):
    return x + 200000
```


```python
calisan_verileri.Salary.apply(fonksiyon_ismi)
```


```python
def sayi_formatla(x):
    return f"{x:.1f}"

calisan_verileri["Bonus %"].apply(sayi_formatla)
```

Aşağıdaki örneklerde ise pandas veri çerçevelerine yeni bir sütun eklemek için işlemler gösterilmiştir. Yeni bir sütun oluşturmak için iki aşama gereklidir:

- Yeni bir sütun oluşturmak ve ona bir ad vermek
-  Yeni sütunun her bir hücresine değer atamak

Bunun için [] operatörü ve atama işlemi = kullanılır. Örneğin, aşağıdaki kod bir veri çerçevesine yeni bir sütun ekleyecek ve içerisine sabit bir "herhangi bir değer" yazdıracaktır:


```python
calisan_verileri['yeni_sutun'] = 'herhangi bir değer'
calisan_verileri.head()
```

![](https://i.vgy.me/aIJrRt.png)


```python
calisan_verileri['Yeni Sütun'] = np.random.randint(
    low=10, high=20,
    size=calisan_verileri.shape[0])  # yeni sütun rassal verilerden oluşturuldu
```

Örneğin, aşağıdaki kod "Yeni Sütun" sütunundaki her bir değeri 2 ile çarpacaktır:


```python
calisan_verileri['Yeni Sütun'] = calisan_verileri['Yeni Sütun'] * 2
```

Burada, calisan_verileri['Yeni Sütun'] * 2 ifadesi, Yeni Sütun sütunundaki her bir değeri 2 ile çarpar ve sonucunu tekrar calisan_verileri['Yeni Sütun'] sütununa atar. 

Nüfusu yüksek olan şehirleri bir sütunda tutmak istersek şu şekilde bir kod yazabiliriz.


```python
sehirler['nufusu_yuksek'] = sehirler.nufuslar >1000000
```

`sort_values()` fonksiyonu, bir veri çerçevesindeki sütunlara göre sıralama yapmaya yarayan bir fonksiyondur. Bu fonksiyon, veri çerçevesindeki belirli bir sütuna göre verileri küçükten büyüğe veya büyükten küçüğe doğru sıralama yapar.


```python
calisan_verileri.sort_values(by=['Salary', 'Bonus %'], ascending=False)
```

`rename()` fonksiyonu, bir veya daha fazla ekseni, satır veya sütun etiketlerini yeniden adlandırmak için kullanılır.

Fonksiyonun genel kullanımı aşağıdaki gibidir:


```python
calisan_verileri.rename(columns={'Bonus %':'Bonus__%', 'Team':'Teams'}).head()
```

## Veri Seçme ve Verilere Ulaşma

Dosya yüklendikten ve veri setini anladıktan sonra, bazı verilere erişmek isteyebiliriz. Pandas, veri seçme, indeksleme ve filtreleme işlemleri için birçok farklı yöntem sunar. Bu yöntemlerin en sık kullanılanları şunlardır:

- `İndeksleme operatörü ([])` : Bu operatör ile belirli bir sütun ya da satır seçilebilir. Örneğin, veri çerçevesindeki 'Name' sütununu seçmek için df['Name'] kullanılır.
- `.loc[]` : Bu metot ile satır ve sütun isimleri veya konumlarına göre seçim yapılabilir. Örneğin, veri çerçevesindeki 3. satırı ve 'Age' sütununu seçmek için df.loc[3, 'Age'] kullanılır.
- `.iloc[]` : Bu metot ile satır ve sütun konumlarına göre seçim yapılabilir. Örneğin, veri çerçevesindeki 2. satırı ve 3. sütunu seçmek için df.iloc[1, 2] kullanılır.
- `Boolean indeksleme` : Bu metot ile belirli koşulları sağlayan satırlar seçilebilir. Örneğin, veri çerçevesindeki yaş değeri 30'dan büyük olan satırların seçimi için df[df['Age'] > 30] kullanılır.
- `.query()` : Bu metot ile belirli koşullara göre satırlar seçilebilir. Örneğin, veri çerçevesindeki yaş değeri 30'dan büyük olan satırların seçimi için df.query('Age > 30') kullanılır.
- `.isin()` : Bu metot ile belirli bir değere sahip olan satırlar seçilebilir. Örneğin, veri çerçevesindeki 'Gender' sütununda 'Female' değerine sahip olan satırların seçimi için df[df['Gender'].isin(['Female'])] kullanılır.
- `.between()` : Bu metot ile belirli bir aralıkta olan değerlere sahip olan satırlar seçilebilir. Örneğin, veri çerçevesindeki yaş değeri 20 ile 30 arasında olan satırların seçimi için df[df['Age'].between(20, 30)] kullanılır.

Bu yöntemlerin her biri, farklı durumlar için kullanışlıdır ve veri çerçevelerinde veri seçimi, indeksleme ve filtreleme işlemlerinin kolay ve esnek bir şekilde yapılmasına olanak tanır.


```python
print(calisan_verileri["Team"]) # sadece Team sütununu getirir.
calisan_verileri[["Team", "Bonus %"]] # iki sütunu birlikte getirir
```


```python
# Örneğin
calisan_verileri['First Name'].iloc[0]  # İlk satırdaki "isim" sütununun değeri
```

Ayrıca, belli bir koşulu sağlayan satırlara erişmek için de `loc[]` fonksiyonunu kullanabiliriz. Bu fonksiyon, koşulu sağlayan satırları getirir.


```python
# Koşulu sağlayan satırlara erişim
# df.loc[df['sütun_adı'] == 'koşul']

# Örneğin
calisan_verileri.loc[calisan_verileri['First Name'] == 'Douglas']  # "First name" sütununda "Douglas" değerine sahip tüm satırlar
```

### iloc

`iloc` fonksiyonu, verilerin indeks numaralarına göre erişim sağlar. İndeks numarası, satırın konumunu belirtir ve sütun adı belirtilmezse tüm sütunlar döndürülür. Örneğin, aşağıdaki DataFrame nesnesinde, "isim", "yaş" ve "şehir" sütunlarındaki 1. indeksteki satırlara erişmek istediğimizi varsayalım:


```python
data = {'isim': ['Ahmet', 'Mehmet', 'Ali', 'Ayşe'],
        'yaş': [28, 22, 30, 25],
        'şehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa']}

df = pd.DataFrame(data)

# İlk satırlara erişim
print(df.iloc[1])           # Sadece bir satır döndürür
print(df.iloc[[1]])         # Bir DataFrame nesnesi döndürür
print(df.iloc[[1, 2]])      # İki satırı içeren bir DataFrame nesnesi döndürür

# İlk satırlara ve belirli sütunlara erişim
print(df.iloc[1, 0])        # Sadece bir değer döndürür
print(df.iloc[[1, 2], 0:2]) # İki satırı ve ilk iki sütunu içeren bir DataFrame nesnesi döndürür

```

### loc

`loc` fonksiyonu, satırların etiket veya koşullara göre erişim sağlar. Etiket veya koşul belirtilmezse, tüm satırlar döndürülür. Örneğin, aşağıdaki DataFrame nesnesinde, "isim", "yaş" ve "şehir" sütunlarındaki "Mehmet" ve "Ali" isimli satırlara erişmek istediğimizi varsayalım:


```python
data = {'isim': ['Ahmet', 'Mehmet', 'Ali', 'Ayşe'],
        'yaş': [28, 22, 30, 25],
        'şehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa']}

df = pd.DataFrame(data)

# Etiket veya koşullara göre erişim
print(df.loc[df['isim'] == 'Mehmet'])             # Bir DataFrame nesnesi döndürür
print(df.loc[df['isim'].isin(['Mehmet', 'Ali'])]) # İki satırı içeren bir DataFrame nesnesi döndürür

# Etiket veya koşullara göre erişim ve belirli sütunlar
print(df.loc[df['isim'] == 'Mehmet', 'yaş'])           # Sadece bir değer döndürür
print(df.loc[df['isim'].isin(['Mehmet', 'Ali']), ['yaş', 'şehir']]) #

```

- df[sütun]: DataFrame'den tek bir sütun veya sütun dizisi seçin; özel durum kolaylıkları: Boolean array (satırları filtreleme), slice (satırları dilimleme) veya Boolean DataFrame (bir kriterle değerleri ayarlama)
- df.loc[satırlar]: Etiketleme ile DataFrame'den tek bir satır veya alt küme seçin
- df.loc[:, sütunlar]: Etiketleme ile tek bir sütun veya sütun alt kümesini seçin
- df.loc[satırlar, sütunlar]: Hem satır(lar) hem de sütun(lar) etiketle seçin
- df.iloc[satırlar]: DataFrame'den tek bir satır veya satır alt kümesini konumla seçin
- df.iloc[:, sütunlar]: Tamsayı pozisyonu ile tek bir sütun veya sütun alt kümesini seçin
- df.iloc[satırlar, sütunlar]: Hem satır(lar) hem de sütun(lar) tamsayı pozisyonu ile seçin
- df.at[satır, sütun]: Bir satır ve sütun etiketiyle tek bir skaler değeri seçin
- df.iat[satır, sütun]: Bir satır ve sütun pozisyonu (tamsayılar) ile tek bir skaler değeri seçin

Bu bölümde, pandas'ın önemli bir araç olmasını sağlayan temel özelliklerini inceledik. Uygulamalı örneklerle kütüphanenin yeteneklerini keşfettik. Seriler ve Veri Çerçeveleri gibi veri nesneleri, int64, float ve object gibi veri tipleri ve veri dönüştürme işlemleri için farklı yöntemler hakkında bilgi sahibi olduk. Daha sonra, veri seçimi ve indeksleme gibi farklı yöntemlerle veri manipülasyonu gerçekleştirdik.
