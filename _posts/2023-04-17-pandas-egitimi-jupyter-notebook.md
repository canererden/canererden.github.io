---
title: 'Pandas Kütüphanesine Giriş Eğitimi Jupyter Notebook ile'
date: 2023-04-17
permalink: 
tags:
  - blog
  - veri bilimi
  - veri madenciliği
---

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

## Pandas'taki Veri Yapıları

Pandas kütüphanesi, üç temel veri yapısı olan DataFrame, İndeks ve Series sınıflarına dayanmaktadır.

### Indexes - İndeksler

Pandas Serilerini numpy tek boyutlu dizilerden ayıran nokta index değerleridir. Index veri tipi sayesinde satır kayıtlarına etiket ile ulaşılabilir.


```python
indexler = seri_ornegi2.index
print(indexler) # Index(['a', 'b', 'c'], dtype='object')
print(type(indexler)) # <class 'pandas.core.indexes.base.Index'>
print(indexler.is_unique) # indeksler tekil verilerden mi oluşuyor mu? True

# indeksler -- Değiştirilemez listelerdir

indeks_1 = pd.Index([1,2,3,4])
indeks_2 = pd.Index([3,4,5])

print(indeks_1.intersection(indeks_2)) # Kesişim: Int64Index([3, 4], dtype='int64')
print(indeks_1.union(indeks_2)) # Birleşim Int64Index([1, 2, 3, 4, 5], dtype='int64')
print(indeks_2.difference(indeks_1)) # Fark Int64Index([5], dtype='int64')
```


### Pandas Series
Series, bir boyutlu bir veri yapısıdır ve sadece bir sütun içerir. Series, bir liste, dizi veya sözlük gibi bir veri yapısından oluşturulabilir. Series, bir DataFrame'in sütununu temsil eder.

Aşağıdaki örnekte, bir Series nesnesi oluşturuyoruz:

Bu kod, [28, 22, 30, 25] verilerinden oluşan bir Series nesnesi oluşturur.


```python
import pandas as pd

data = [28, 22, 30, 25]
s = pd.Series(data)

print(s)
```


```python

```


```python
seri_ornegi = pd.Series([1,2,5,8]) 
print(s.dtype) # int64
seri_ornegi2 = pd.Series([2,3,4], index= ['a','b','c'], name='seri_ornegi') 
print(seri_ornegi.values) # [1 2 5 8]
print(seri_ornegi2.name) # seri_ornegi
print(s.shape) # (4,)
print(seri_ornegi2.index) # Index(['a', 'b', 'c'], dtype='object')
# pandas serilerinde toplama yapıldığında
print(seri_ornegi[seri_ornegi>2]) # 2den büyük veriler
sayilar = np.linspace(0, 10, num=5)
x = pd.Series(sayilar) # indeksler [0, 1, 2, 3, 4]
y = pd.Series(sayilar, index=pd.Index([1, 2, 3, 4, 5]))
print(x + y) # indekslere göre toplama yapılır.
# numpy da iki diziyi toplayınca
print(np.array([1, 1, 1]) + np.array([-1, 0, 1]))
```


```python
print(2 in seri_ornegi) # seri örneğinde 2 değeri var mı?
print(10 in seri_ornegi)
```

### DataFrame Veri Çerçevesi
DataFrame, iki boyutlu bir veri yapısıdır ve sütunlar ve satırlar şeklinde organize edilir. DataFrame, tablo benzeri bir yapıya sahiptir ve her sütun bir Series nesnesidir. DataFrame'in her bir satırı, bir gözlem veya bir veri noktasını temsil eder. DataFrame, verileri işlemek ve manipüle etmek için birçok yöntem sağlar.

Aşağıdaki örnekte, "isim", "yas" ve "sehir" sütunları olan bir DataFrame nesnesi oluşturur.


```python
data = {'isim': ['Ahmet', 'Mehmet', 'Ali', 'Ayşe'],
        'yas': [28, 22, 30, 25],
        'sehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa']}

df = pd.DataFrame(data)

print(df)
```


```python
# Veri Çerçevesi oluşturma 1. yöntem
veri_cercevesi = pd.DataFrame(np.random.rand(3, 2),
                              columns=['Sütun 1', 'Sütun 2'],
                              index=['a', 'b', 'c'])
veri_cercevesi
```


```python
# Veri çerçevesi oluşturma 2. yöntem
# sözlükler key value lardan oluşur
plakalar = {'istanbul':'34','sakarya':'54','kmaraş':'46'}
nufus_sayilari = {'istanbul':20000000,'sakarya':1000000,'kmaraş':900000}
sehirler = pd.DataFrame({'plaka kodları':plakalar,'nufuslar':nufus_sayilari})
print(sehirler)
```


```python
# eğer index ve sütun değerleri eşleşirse toplama gerçekleşir
sehirler + sehirler
```


```python
print(sehirler.columns) # Index(['plaka kodları', 'nufuslar'], dtype='object')
print(sehirler.values)
print(sehirler.values)
sehirler_numpy = sehirler.to_numpy()
```


```python
# Veri çerçevesi oluşturma yöntem 3. Liste oluşturarak
veri_listesi = [(n, n**2, n**3) for n in range(5)] # list comprehensions
pd.DataFrame(veri_listesi, columns=['n', 'karesi', 'kubu'])
```


```python
# Veri çerçevesi oluşturma yöntem 4. Numpy dizileri ile
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
```


```python
print(disari_cikma["karar"]) # dışarı çıkma kararı series oldu
print(disari_cikma.karar)# yukarıdaki ile aynı kullanıma sahiptir.
```

## Pandas ile Dosyadan Veri Almak
- text dosyası `genfromtxt`
- csv dosyası `read_csv`
- Excel dosyası `read_excel`
- json dosyası `read_json()`
- Veritabanından `read_sql()`


```python
calisan_verileri = pd.read_csv("employees.csv", skiprows=0)
```

![resim.png](attachment:resim.png)


```python
calisan_verileri.empty
```


```python
calisan_verileri.head()
```


```python
calisan_verileri.shape
```


```python
type(calisan_verileri)
```


```python
print(
    "bu veri setinde {} adet veri vardır. Ayrıca özellik sayısı {}'dir.".
    format(calisan_verileri.shape[0], calisan_verileri.shape[1]))
```


```python
calisan_verileri.columns
```


```python
calisan_verileri.describe() # veri özetleme
```


```python
calisan_verileri.info() # non-null sayılarını görmek için
```


```python
calisan_verileri.describe(percentiles=[0.05, 0.95]) # diğer dilimleri de görüntülemek için
```


```python
calisan_verileri.describe(include=np.object)
```


```python
calisan_verileri.count()
```

![resim.png](attachment:resim.png)

seriler için kullanılabilecek diğer fonksiyonlar
- `unique`
- `value_counts`

## Verilere ulaşma

Dosya yüklendikten sonra, verilere erişebiliriz. DataFrame nesnesi, her bir sütunu bir Series nesnesi olarak temsil eder. 

Sütunun belirli bir değerine erişmek için, `iloc[]` fonksiyonunu kullanabiliriz. Bu fonksiyon, sütunun ilgili satırının indeks numarasını kullanarak değere erişir.

- sütunları seçme
- loc (location) - Etiketlerle ulaşacağız.
- iloc - Sayılarla ulaşacağız


```python
# İlgili değere erişim
# df['sütun_adı'].iloc[satır_indeksi]

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

- df[column]: Select single column or sequence of columns from the DataFrame; special case conveniences: Boolean array (filter rows), slice (slice rows), or Boolean DataFrame (set values based on some criterion)
- df.loc[rows]: Select single row or subset of rows from the DataFrame by label
- df.loc[:, cols]: Select single column or subset of columns by label
- df.loc[rows, cols]: Select both row(s) and column(s) by label
- df.iloc[rows]: Select single row or subset of rows from the DataFrame by integer position
- df.iloc[:, cols]: Select single column or subset of columns by integer position
- df.iloc[rows, cols]: Select both row(s) and column(s) by integer position
- df.at[row, col]: Select a single scalar value by row and column label
- df.iat[row, col]: Select a single scalar value by row and column position (integers) 
- reindex method: Select either rows or columns by labels

## Fitreleme



```python
sehirler.loc[sehirler.nufuslar>1000000]['plaka kodları']
```


```python
sehirler.loc[sehirler.nufuslar>1000000, 'plaka kodları']
```

## Yeni satır/sütun oluşturma


```python
sehirler['yeni_sutun'] = 'herhangi bir değer'
sehirler.yeni_sutun # bu yapı kullanılmaz çünkü sütun henüz yok..
```


```python
sehirler
```


```python
sehirler['nufusu_yuksek'] = sehirler.nufuslar >1000000
```


```python
sehirler
```

## Pandas'ta işlemler


```python
calisan_verileri_kopya = calisan_verileri.copy(deep=True)
```


```python
calisan_verileri_kopya
```


```python
calisan_verileri_kopya.head()
```


```python
calisan_verileri_kopya = calisan_verileri_kopya.drop(['Gender'], axis=1)
```


```python
calisan_verileri.head(2)
```


```python
# hangi takımda kaç kişi var?
# value_counts()
calisan_verileri.Team.value_counts()
```


```python
# describe()
calisan_verileri.describe()
```


```python
calisan_verileri.mean()
```


```python
calisan_verileri.Team.unique() # Tekil verileri getirir.
```


```python
# Takımlara ait istatistikler - groupby()
calisan_verileri.groupby('Team').mean()
```


```python
calisan_verileri.groupby('Team').Team.count()
```


```python
def fonksiyon_ismi(x):
    return x + 200000
```


```python
fonksiyon_ismi(5)
```


```python
# apply ve map fonksiyonları
calisan_verileri.Salary.map(lambda x: x+200000)
```


```python
calisan_verileri.Salary.apply(fonksiyon_ismi)
```


```python
calisan_verileri.sort_values(by=['Salary', 'Bonus %'], ascending=False)
```


```python
calisan_verileri.columns
```


```python
calisan_verileri.rename(columns={'Bonus %':'Bonus__%', 'Team':'Teams'}).head()
```


```python
calisan_verileri.head()
```


```python
calisan_verileri['Yeni Sütun'] = np.random.randint(
    low=10, high=20, size=calisan_verileri.shape[0])
```


```python
calisan_verileri.head()
```


```python
calisan_verileri.nunique()
```


```python
calisan_verileri.select_dtypes(include='float').head()
```


```python
def sayi_formatla(x):
    return f"{x:.1f}"
```


```python
calisan_verileri["Bonus %"].apply(sayi_formatla)
```


```python

```
