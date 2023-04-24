---
layout: post
title: Matplotlib ile Görsel Veri Analizi
date: 2023-04-24
permalink: 
tags:
  - blog
  - veri bilimi
  - veri madenciliği
---

Matplotlib, Python programlama dili için bir grafik çizme kütüphanesidir ve verilerinizi görsel olarak temsil etmek için kullanılır. Bu kütüphane, doğrusal grafikler, dağılım grafikleri, pasta grafikleri, çubuk grafikleri ve daha birçok grafik türü oluşturmanızı sağlar. Matplotlib, ücretsiz ve açık kaynaklı bir yazılımdır ve Python'da veri analizi, makine öğrenimi, yapay zeka ve daha birçok alanda sıklıkla kullanılır. Bu eğitimde, Matplotlib kütüphanesinin temellerini öğreneceksiniz ve verilerinizi nasıl etkileyici grafiklere dönüştürebileceğinizi öğreneceksiniz.

## Matplotlib Kütüphanesi
Matplotlib, 2 ve 3 boyutlu grafiklerin çizilmesi için geliştirilmiş, anasayfası (http://matplotlib.org) adresinde bulunan, özellikle bilimsel ve mühendislik alanlarındaki veri görselleştirmelerinde sıklıkla kullanılan bir kütüphanedir. Veri görselleştirme ihtiyacı verinin olduğu her alanda geçerlidir. Çünkü büyük veri kümelerindeki veriyi nitelendiren özelliklere ve ölçülere genel çerçeveden bakılmak istendiğinde görsel araçlara ihtiyaç duyulur. Örneğin bir veri setinin dağılımı ile ilgili histogram grafikleri hızlı bir izlenim imkanı sunar. Aşağıdaki görselde tablo ile sunulamayacak bilgilerin veri görselleştirme ile göze hitap edecek şekilde sunulması için araçlar gösterilmiştir. 

<img src="https://uploads-ssl.webflow.com/61488f4f65be16b5ebbd450b/61b74ab1d55fa17b82d7ed89_Data%20Visualization.jpg"  width = "75%" height = "75%">

Matplotlib kütüphanesi [NumPy](https://numpy.org/) üzerine kurulmuş bir kütüphanedir. Bu nedenle Matplotlib kütüphanesinin çağrılmasından önce NumPy kütüphanesinin de yüklü kütüphaneler arasında olması gereklidir. Matplotlib, verileri görselleştirmek için kullanılan güçlü bir kütüphanedir. Bu nedenle, Matplotlib'ın sunduğu avantajları kullanarak, verilerinizi etkileyici grafiklere dönüştürebilir ve daha kolay bir şekilde analiz edebilirsiniz. Kısaca Matplotlib kütüphanesinin önemli avantajlarını şu şekilde sunabiliriz:

- Basit ve Kullanımı Kolay: Matplotlib, kullanımı kolay bir arayüze sahiptir ve temel grafik çizme işlevleri için hızlı ve basit bir şekilde kullanılabilir.
- Geniş Kapsamlı Grafikler: Matplotlib, doğrusal grafikler, dağılım grafikleri, pasta grafikleri, çubuk grafikleri ve daha birçok grafik türü oluşturmanızı sağlar. Bu nedenle, verilerinizi birçok farklı şekilde görselleştirebilirsiniz.
- Özelleştirilebilir Grafikler: Matplotlib ile grafiklerinizi özelleştirmek için birçok seçeneğe sahipsiniz. Renkler, çizgi stilleri, etiketler ve daha birçok şeyi kolayca özelleştirebilirsiniz.
- Çoklu Veri Kümeleri: Matplotlib, birçok veri kümesini aynı grafikte birleştirmenize olanak tanır. Bu, verileriniz arasındaki ilişkileri anlamak için çoklu grafikleri karşılaştırmanızı ve birleştirmenizi sağlar.
- Çoklu Çıktı Biçimleri: Matplotlib, grafikleri birçok farklı çıktı biçiminde kaydetmenizi sağlar. Grafikleri PNG, PDF, SVG ve daha birçok formatta kaydedebilirsiniz.
- Ücretsiz ve Açık Kaynaklı: Matplotlib, ücretsiz ve açık kaynaklı bir yazılımdır ve Python topluluğu tarafından sıkça kullanılan bir kütüphanedir. 

Matplotlib, Python dilindeki paket yöneticisi olan pip ile kolayca yüklenebilir. İlk olarak, aşağıdaki kodu kullanarak Matplotlib kütüphanesini Jupyter notebook üzerinden yükleyebilirsiniz:

```!pip install matplotlib```

veya

```!conda install matplotlib```
 

## Matplotlib Grafiklerine Giriş

Matplotlib ile görselleştirmelere geçmeden önce Matplotlib katmanlarından bahsetmekte fayda vardır. Matplotlib, çizimlerin oluşturulması ve düzenlenmesi için bir dizi katman sağlar. Aşağıda, Matplotlib'deki katmanların kısaca açıklamaları verilmiştir:

1. Figure: Figure, çizimlerin oluşturulduğu en üst düzey katmandır. Figure, genellikle birden fazla alt grafik (subplot) içerir. Birden fazla çizimi bir arada göstermek için kullanılabilir.
2. Axes: Axes, verilerin çizildiği katmandır. Grafikteki x ve y eksenleri gibi her şey, bu katmanda oluşturulur. Axes, tek bir grafik için birden fazla çizgi veya veri kümesi içerebilir.
3. Axis: Axis, x ve y eksenleri gibi her bir eksenin ayrı ayrı bulunduğu katmandır. Eksenlerdeki etiketler, işaretçiler ve çizgiler bu katmanda bulunur.
4. Artist: Artist, grafikte çizilen herhangi bir şeyi (çizgi, işaretçi, şekil, metin vb.) temsil eden bir katmandır. Grafikteki herhangi bir öğeyi özelleştirmek için bu katman kullanılabilir.

Matplotlib'deki bu katmanlar, grafik oluşturma ve özelleştirme sürecinde kullanılan araçlar ve işlevler sağlar. Bu katmanlar, Matplotlib'ın güçlü ve esnek bir grafik kütüphanesi olmasını sağlar. 

Matplotlib'de bir grafik oluşturmak için ilk adım, bir "Figure" oluşturmaktır. "Figure", en üst düzey çizim katmanıdır ve grafikteki her şeyin (eksenler, etiketler, veriler vb.) bulunduğu alanı tanımlar. Aşağıda bir "Figure" anatomisi anlatılmaktadır:

<img src="https://matplotlib.org/stable/_images/anatomy.png"  width = "75%" height = "75%">

1. Figure: Figure, en üst düzey grafik alanıdır. Eksenler, metin, çizgiler ve diğer tüm öğeler bu alan içinde bulunur.
2. Axes: Axes, Figure içindeki verilerin çizildiği alandır. Her "Figure" bir veya daha fazla "Axes" içerebilir.
3. Axis: "Axes" içindeki bir eksen. Her "Axes" nesnesi, iki veya üç eksen içerir: x eksenleri, y eksenleri ve (varsa) z eksenleri.
4. Tick: "Axis" üzerindeki işaretleyicilerdir. Eksenin konumunu ve etiketlerini belirlerler.
5. Label: "Axis" üzerindeki işaretçi etiketidir. Eksenin neyi ölçtüğünü belirtir.
6. Spine: "Axis" çerçevesi boyunca uzanan çizgi. Spine'lar, verilerin eksenlerdeki konumlarını gösteren işaretleyicilerin üzerine yerleştirilebilir.
7. Grid: Verilerin konumunu gösteren çizgiler. Grid, eksenlerin etrafında oluşturulabilir.
8. Title: "Axes" üzerindeki başlık. Grafik hakkında özet bilgi sağlar.
9. Legend: Grafikteki farklı veri kümelerini açıklayan etiketler. "Axes" içindeki bir konuma yerleştirilebilir.

Matplotlib'de, bir "Figure" oluşturduktan sonra, "Axes" nesneleri ekleyebilir ve "Axis", "Tick", "Label" vb. özellikleri özelleştirebilirsiniz.

## Matplotlib kütüphanesini çağırma
Klasik bir Matplotlib kütüphane çağrılma yöntemi aşağıda verilmiştir.

``import Matplotlib.pyplot as plt`` 

Bu kod ``pyplot`` isimli modülün çağrılmasını sağlar. Bu modül sayesinde Matplotlib grafikleri, eksenleri ve aksisleri çizdirilebilir. Aşağıdaki görselde pyplot ile çizilen figürlerin objeleri gösterilmiştir.

Aşağıdaki kodlar ile matplotlib kütüphanesi çağrılmış olunur. Aynı zamanda NumPy ve Pandas kütüphanelerinin de başlangıçta çağrılmasında fayda vardır.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
```

Basit bir Matplotlib grafiği kodları aşağıda paylaşılmıştır. plt.plot() ile x değerlerine karşılık gelen y değerleri çizdirilebilir. 


```python
# x ve y verileri
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Grafik oluşturma
plt.plot(x, y)

# Grafik özellikleri
plt.title("Örnek Grafik")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

# Grafik gösterimi
plt.show()
```

Bu örnekte, öncelikle `matplotlib.pyplot` modülü import edilir. Daha sonra, "x" ve "y" verileri tanımlanır. `plt.plot(x, y)` çağrısı ile, bu verileri içeren bir grafik oluşturulur.

Daha sonra, `plt.title()`, `plt.xlabel()` ve `plt.ylabel()` çağrıları ile grafik başlığı ve eksen etiketleri belirtilir. Son olarak, `plt.show()` çağrısı ile, oluşturulan grafik ekranda gösterilir.

Bu örnek, Matplotlib'in temel kullanımını göstermektedir. Grafik oluşturma sürecinde, "Axes" özelliklerini ve diğer özelleştirme seçeneklerini kullanarak grafikleri daha fazla özelleştirebilirsiniz.


```python
plt.plot([1,2,3],[7,3,9]) # (1,7), (2,3), (3,9) noktalarını birleştirir
```


```python
plt.plot([3, 5, 2])  # x ekseni verilmez ise varsayılan olarak 0-1-2... gelir
```


```python
x = np.linspace(-np.pi, np.pi, 20)  # -pi ile +pi arasında 20 adet değer
plt.plot(x, np.sin(x))
```


```python
x
```

## Grafiklere Özellik Ekleme

Az önce çizdirilen grafikler x, y eksenleri ve alınan değerlerin birleştirilmesi ile oluşturuldu. Matplotlib kütüphanesinde eğer bir özellik tanımı yapılmaz ise grafikler yalın halde gelir. Ancak grafikler yalın halde anlamsızdır. x, y eksenlerinin neyi gösterdiği, grafiğin başlığının ne olduğu, verilerin neler olduğu grafik üzerinde gösterilmelidir. 

### Eksen etiketi, seri etiketi ve başlık özelliği ekleme

`label` özelliği verilerin neler olduğunu gösterir. label özelliğinin grafik içerisinde gösterilmesi için `plt.legend()` fonksiyonu eklenmiştir.


```python
plt.plot(x,np.sin(x), label = 'sin(x)')
plt.plot(x,np.cos(x), label = 'cos(x)')
plt.legend()
```


```python
# Veya
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.legend(('sin', 'cos'), loc='best')
```

legend() fonksiyonu içerisine tanımlanacak parametreler ile etiketlerin konumu değiştirilebilir.


```python
plt.plot(x,np.sin(x), label = 'sin(x)')
plt.plot(x,np.cos(x), label = 'cos(x)')
plt.legend(loc='best'); # upper left upper right
```

Grafiklerin üzerine başlık eklemek, grafiğin içeriği hakkında daha fazla bilgi verir. Başlık, `title()` işlevi kullanılarak eklenebilir. Örneğin:


```python
plt.plot(x,np.sin(x), label = 'sin(x)')
plt.plot(x,np.cos(x), label = 'cos(x)')
plt.legend(loc='best'); # upper left upper right
plt.title('Sinüs Fonksiyonu')
plt.show()
```

### Etiket fontlarını değiştirme

Aşağıdaki örnekte birden fazla çizim aynı grafik üzerinde gerçekleştirilmiştir. Buna göre 3 farklı çizimi gösterdikten sonra etiketlerin fontları üzerinde değişiklikler gerçekleştirdik.

Renk kullanımında `plot()` işlevi, color parametresi ile çizgi rengini belirleyebilir. Ayrıca, hex renk kodlarını veya RGB veya RGBA renk değerlerini de kullanabilirsiniz. Örneğin:


```python
# Ya da aynı figür üzerinde şekil çizmek istersek
plt.plot(x, np.sin(x), x, np.cos(x), x, x**2);  # ; fonksiyon yazmak istemezsek
```


```python
# Etiketlerin fontlarını değiştirme
plt.plot(x, np.sin(x), x, np.cos(x), x, x**2)
plt.xlabel("x değerleri")
plt.ylabel("y değerleri")
plt.title("x, y grafiği",
          fontdict={
              'family': 'serif',
              'color': 'red',
              'size': 20
          },
          loc='right')
```

Fontlarla ilgili daha detaylı bilgi [şu adresten](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo_kw.html) alınabilir.

### Izgaraları gösterme


```python
plt.plot(x, np.sin(x), x, np.cos(x), x, x**2)
plt.grid(True, axis='y') # axis='x' sadece x ekseninde ızgaralar gösterir
```

### Renk ve çizgi stillerini değiştirme

Bu örnekte, "color", "linestyle" ve "linewidth" parametreleri kullanılarak çizgi rengi, stil ve kalınlığı belirtilir.


```python
# çizgilerin kalınlıklarının ayarlanması
plt.plot(x, np.sin(x), x, np.cos(x), x, x**2, linewidth=5);
plt.grid()
```


```python
# çizgi stilleri
plt.plot(x, np.sin(x), linestyle='dashed', label='sin')
plt.plot(x, np.cos(x), linestyle='--', label='cos')
plt.plot(x, x**2, label='kare', linestyle='-.')
plt.grid()
plt.legend()
```

![image.png](https://matplotlib.org/stable/_images/sphx_glr_linestyles_001.png"  width = "75%" height = "75%">

Diğer diğer parametreler için [şu adresten](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.plot.html) bilgi alınabilir.



### Marker özellikleri

Bu örnekte, "marker" ve "markersize" parametreleri kullanılarak çizgi üzerinde işaretleyici (marker) boyutu ve şekli belirtilir. Detaylı bilgi [link](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)


```python
# Grafik oluşturma
plt.plot(x, np.sin(x), label='sin', marker = 'x')
plt.plot(x, np.cos(x), label='cos', marker= 'p')
plt.plot(x, x**2, label='kare',color='red', marker='o', markersize=8)

# Grafik özellikleri
plt.title("Örnek Grafik")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

# Grafik gösterimi
plt.show()
```

Matplotlib, çizgi komutlarının marker parametresi kullanılarak seçilen birden fazla kategoriye sahip markerları destekler:

- Doldurulmamış markerlar
- Doldurulmuş markerlar
- TeX sembollerinden oluşturulan markerlar
- Yollardan oluşturulan markerlar


**Doldurulmamış markerlar (Unfilled markers)**

<img src="https://matplotlib.org/stable/_images/sphx_glr_marker_reference_001.png"  width = "75%" height = "75%">

**Doldurulmuş markerlar (Filled)**

<img src="https://matplotlib.org/stable/_images/sphx_glr_marker_reference_002.png"  width = "75%" height = "75%">

**Marker fill styles**

<img src="https://matplotlib.org/stable/_images/sphx_glr_marker_reference_003.png"  width = "75%" height = "75%">

**TeX sembollerinden oluşturulan markerlar**

<img src="https://matplotlib.org/stable/_images/sphx_glr_marker_reference_004.png"  width = "75%" height = "75%">

**Yollardan oluşturulan markerlar**

<img src="https://matplotlib.org/stable/_images/sphx_glr_marker_reference_005.png"  width = "75%" height = "75%">

### Renk Haritası (Colormap) Özellikleri

Matplotlib kütüphanesi, renk haritaları veya colormap olarak adlandırılan, verilerin renklendirilmesi için kullanılan özel renk paletlerini destekler. Colormap'lar, veri yoğunluğu veya sıcaklık, deniz seviyesi yüksekliği veya diğer özelliklerin belirtilmesi gibi verilerin özelliklerini vurgulamak için kullanılabilir.

Matplotlib'teki çeşitli colormap'lar, farklı renk paletleri ve renk geçişleri sunar. Bazı örnek colormap'lar şunlardır:

- viridis
- plasma
- inferno
- magma
- coolwarm

Colormap'lar genellikle `plt.imshow()` veya `plt.pcolor()` gibi işlevlerle kullanılır. Colormap özellikleri, cmap parametresi veya renk paleti adı olarak belirtilerek seçilebilir.

Bunun yanı sıra, colormap'ların skalasını özelleştirmek için farklı renk dönüşüm (color map transformation) işlevleri de kullanılabilir. Örneğin, `plt.Normalize()` işlevi, renk skalasının belirli bir aralığa ölçeklendirilmesine olanak tanır.

Aşağıdaki örnekte tablo verilerini renklendirmek için colormap kullanımına örnek olarak, bir heatmap oluşturalım. Veriler, farklı bölgelerin aylık ortalama sıcaklıklarını içeren bir numpy dizisinden alınacak.


```python
# Veri dizisi oluşturma
data = np.array([[12, 13, 15, 20, 23, 27, 30, 29, 26, 21, 16, 13],
                 [8, 9, 12, 17, 21, 25, 27, 26, 23, 18, 13, 9],
                 [5, 6, 9, 14, 18, 23, 25, 25, 22, 17, 11, 7],
                 [3, 4, 7, 11, 15, 19, 21, 21, 18, 13, 8, 5],
                 [1, 2, 4, 7, 11, 15, 17, 17, 15, 11, 6, 3]])

# Renk haritası (colormap) özelleştirme
cmap = plt.cm.get_cmap('coolwarm')
norm = plt.Normalize(vmin=data.min(), vmax=data.max())

# Resim çizimi
plt.imshow(data, cmap=cmap, norm=norm)

# Renk skalası oluşturma
cbar = plt.colorbar()
cbar.ax.set_ylabel('Sıcaklık (°C)')

# Eksen etiketleri ekleme
plt.xticks(range(12), ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'])
plt.yticks(range(5), ['Bölge 1', 'Bölge 2', 'Bölge 3', 'Bölge 4', 'Bölge 5'])
plt.xlabel('Aylar')
plt.ylabel('Bölgeler')

# Başlığı ekleme
plt.title('Bölgelere Göre Aylık Ortalama Sıcaklıklar')

# Resmi gösterme
plt.show()
```

Bu kod, `imshow()` işlevi kullanarak veri dizisini bir ısı haritası olarak gösterir. Veriler, coolwarm renk haritasına göre renklendirilir. `Normalize()` işlevi, verilerin minimum ve maksimum değerlerine göre normalleştirir. `colorbar()` işlevi, renk skalasını resmin yanına ekler. Sonuç olarak, verilerin özelliklerine ve sıcaklık değişimlerine göre vurgulanarak görsel olarak daha anlaşılır bir şekilde sunulur.

## Çoklu Figürler Çoklu Matplotlib Grafikleri

Bazı durumlarda birden fazla grafik bir figür içerisinde verilmek istenebilir. Böylece tek seferde okuyucuya birden fazla durumla ilgili özet bilgi sunulmuş olunur. Daha önceden belirtilen Figure ve Axes kavramları kullanılarak Matplotlib içerisinde birden fazla grafik subplot() fonksiyonu ile yerine getirilebilir. 

Subplot() fonksiyonu ile istenilen sayıda satır ve sütunda grafikler figürlere eklenebilir.

Subplot fonksiyonundan önce matplotlib kütüphanesindeki iki farklı yaklaşımdan bahsetmekte fayda vardır. Bunlar;

### MATLAB tipi pyplot ile grafik çizdirme
Pyplot ile çizdirilen grafik bir hücre için değiştirilebilir bir grafiktir. Başka hücrede yeni bir pyplot objesi eklenirse yeni grafikler çizdirilebilir. MATLAB programındakine benzer şekilde grafik çizdirme yöntemidir. Daha önce gösterilen grafikler pyplot ile çizdirilen grafiklerdi.

### Nesne yönelimli şekilde grafik çizdirme.

Matplotlib kütüphanesinin önemli özelliklerinden birisi de nesne yönelimli programlamaya izin vermesidir. Çizim alanı anlamına gelen ``Figure`` objesi Matplotlib kütüphanesinin tepesinde yer alır. Diğer elemanlar ise ``Artist`` diye bilinir ve aşağıdaki görselde gösterilen mavi yerler Artist olarak geçmektedir. Artistler Axes(Eksenler)den oluşur. Eksenler ise Axis öğelerinden oluşur.

Eksenler(Axes) grafikleri tutan objelerdir. Bir grafik çizdirebilmek için en az bir eksenin figür içerisine eklenmesi gerekmektedir. Axis'ler ise x ve y aksis i olabilir ya da üçüncü boyut varsa z axis i de devreye girer. Bu nedenle x veya y deki limitleri veya çizgileri ayarlamak için axis özelliğini kullanmak gerekecektir. Matplotlib ile daha gelişmiş ve pratik grafik çizimleri için bu hiyerarşiyi anlamak faydalı olacaktır.

Ayrıca nesne yönelimli yapı kullanılarak çok daha hızlı ve temiz grafikler çizilebilir. Hızlı grafik çizimleri için MATLAB stili grafik çizdirmek önerilse de daha detaylı işler için nesne yönelimli yapı önerilmektedir.


```python
# basit bir matplotlib grafiği
fig, ax = plt.subplots()  # Tek eksenden oluşan bir figür oluşturmak için
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Eksen içerisine bir grafik çizdirmek için
```


```python
print(type(fig))
```


```python
help(fig)
```


```python
fig = plt.figure()  # Eksenin olmadığı bir figür
fig, ax = plt.subplots()  # Tek eksenden oluşan bir figür
fig, axs = plt.subplots(2, 2, sharex= True, sharey=True)  # 2x2 li bir grafik
```


```python
fig, axs = plt.subplots(nrows= 3, ncols=2, sharex=True)  # 2x1 li bir grafik ve ortak x axis i
```


```python
# Nesne yönelimli grafikler oluşturmak için aşağıdaki yapı kullanılabilir.
fig, ax = plt.subplots()  # Bir eksenden oluşan bir figür oluşturduk.
ax.plot(x, np.sin(x), label='sinüs')  # Eksenin içerisine grafik çizdirmek için
ax.plot(x, np.cos(x), label='cosinüs')  # Aynı eksene başka grafik çizdirmek için
ax.plot(x, x**2, label='kare')  # istenilen kadar grafik aynı eksene eklenebilir.
ax.set_xlabel('x aksisi')  # Eksene x etiketi koymak için
ax.set_ylabel('y aksisi')  # set_ylabel.
ax.set_title("x ve y Grafiği")  # Grafiğe başlık eklemek için.
ax.legend()  # Etiketleri göstermek için.
```


```python
# ya da aynı işlemi daha önce gösterdiğimiz gibi de yapabilirdik.

plt.plot(x, np.sin(x), label='sinüs')  # Eksenin içerisine grafik çizdirmek için
plt.plot(x, np.cos(x), label='cosinüs')  # Aynı eksene başka grafik çizdirmek için
plt.plot(x, x**2, label='kare')  # istenilen kadar grafik aynı eksene eklenebilir.
plt.xlabel('x aksisi')  # set_xlabel değişti
plt.ylabel('y aksisi')  # set_ylabel değişti.
plt.title("x ve y Grafiği")  # set_title değişti.
plt.legend()  # Etiketleri göstermek için.
```


```python
fig, ax = plt.subplots(1, 2) # bir satır iki sütundan oluşan iki grafik ekledik.
ax[0].plot(x, np.sin(x)) # ilk eksene grafik çizdirmek için
ax[1].plot(x, np.cos(x)) # ikinci eksene grafik çizdirdik.
```


```python
type(ax)
```


```python
fig, ax = plt.subplots(2, 2) # iki satır iki sütundan oluşan iki grafik ekledik.
ax[0,0].plot(x, np.sin(x), label='sin') # birinci satır birinci sütundaki grafik
ax[0][1].plot(x, np.cos(x)) # ikinci eksene grafik çizdirdik.
ax[1][0].plot(x, x**2)
ax[1][1].plot(x, x**3)
```


```python
type(ax) # ax nesnesi bir NumPy dizisidir. İçerisinde Matplotlib nesneleri bulunmaktadır
```


```python
type(ax[0][0])
```

Aşağıdaki örnek, birden fazla figür oluşturma işlemini göstermektedir.

Bu örnek, iki farklı figure oluşturur ve her figure içinde bir veya daha fazla subplot yerleştirir. `add_subplot()` fonksiyonu, figure içindeki subplotların yerleştirme düzenini belirlemek için kullanılır.

Bu örnekte, ilk figure'da 2 satır ve 1 sütun olarak ayarlanmıştır ve ilk subplot 1. satırda, ikinci subplot 2. satırda yerleştirilmiştir. İkinci figure'da 1 satır ve 1 sütun olarak ayarlanmıştır ve tek bir subplot içermektedir.

`plt.show()` fonksiyonu, tüm figürleri görüntülemek için kullanılır.


```python
# 1. Figure oluşturma
fig1 = plt.figure()

# 2. İlk subplot oluşturma
ax1 = fig1.add_subplot(2, 1, 1) # 2 satır, 1 sütun, 1. subplot
x = np.linspace(0, 10)
y = np.sin(x)
ax1.plot(x, y)
ax1.set_title("Sinüs")

# 3. İkinci subplot oluşturma
ax2 = fig1.add_subplot(2, 1, 2) # 2 satır, 1 sütun, 2. subplot
y = np.cos(x)
ax2.plot(x, y)
ax2.set_title("Kosinüs")

# 4. İkinci figure oluşturma
fig2 = plt.figure()

# 5. Üçüncü subplot oluşturma
ax3 = fig2.add_subplot(1, 1, 1) # 1 satır, 1 sütun, 1. subplot
y = np.tan(x)
ax3.plot(x, y)
ax3.set_title("Tanjant")

# 6. Tüm figürleri gösterme
plt.show()
```

Başka bir örnekte MATLAB stili pyplot grafik çizdirmede birden fazla eksende grafik çizdirilmek istenirse aşağıdaki yapı kullanılabilir.


```python
plt.subplot(121) # Bir satır iki sütunlu bir yapıda birinci grafiği çizdir.
plt.plot(x, np.sin(x))
plt.subplot(122) # İkinci grafik
plt.plot(x, np.cos(x))
```

### Izgaralar ile Subplot çizdirme

Yaygın kullanım için benzer ölçülerde eksenler ile çalışmak her ne kadar yeterli olsa da Matplotlib istenilen boyutlarda eksenler oluşturmak için imkan sunmaktadır. `plt.subplot()` fonksiyonu satır, sütun ve indeks değerlerinden oluşan 3 tam sayı değeri almaktaydı. Tam sayı değerleri eksenin kapsayacağı ızgara dilimi ile ilgili bilgiyi vermemektedir.  


```python
for i in range(1,5):
    print(i)
    plt.subplot(2,2,i) # 2 satır 2 sütun eksenlerin i. ekseni
    plt.text(0.5, 0.5, str(i))
```

Birden fazla subplot çizdirmek için `plt.subplots()` fonksiyonu kullanılır. Bu durumda ızgara içerisindeki tüm konumlar kullanılabilir hale gelir. Yukarıdaki örneği ortak x ve y için yapmak istersek aşağıdaki yapıyı kullanabiliriz.

### plt.subplot2grid() fonksiyonu

Izgaraların içerisine istenilen boyutlarda grafikler eklemek için subplot2grid() fonksiyonu kullanılabilir. Bu fonksiyon sırasıyla shape, location, rowspan, colspan parametrelerini alır.
- shape: satır ve sütun değerleri alır. Birinci girdi satır sayısını ikinci girdi sütun sayısını gösterir.
- loc: 2 tam sayı alır. Izgara içerisinde nereye yerleştirileceğini belirler.
- rowspan: Sağ tarafa doğru ne kadar genişleyeceğini belirtir.
- colspan: Aşağı doğru ne kadar genişleyeceğini belirler.


```python
a1 = plt.subplot2grid((3,3),(0,0),colspan = 2) # 3x3 lük bir ızgarada 1. satır birinci sütunda iki sütun git.
a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
a3 = plt.subplot2grid((3,3),(1,0),rowspan = 2, colspan = 2)
x = np.arange(1,10)
a2.plot(x, x*x)
a2.set_title('square')
a1.plot(x, np.exp(x))
a1.set_title('exp')
a3.plot(x, np.log(x))
a3.set_title('log')
plt.tight_layout()
plt.show()
```

## Grafiklere Daha Farklı Elemanlar Ekleme

Grafikler içerisinde işaretleyici, metin, şekil gibi elemanlar eklenmek istenirse aşağıdaki yapılar kullanılabilir.

### Metin Ekleme

Daha önceden göserilen xlabel(), ylabel(), title() gibi fonksiyonlar figür içerisine metin eklemekte kullanılmıştı. Metin eklemek için `text()` fonksiyonu veya `annotate()` fonksiyonu kullanılabilir.

`text()` fonksiyonu, belirtilen koordinatlara bir metin nesnesi ekler.

`text(x, y, s, **kwargs)`

Burada, x ve y koordinatları, metnin nerede başlayacağını belirler ve s argümanı, eklenecek olan metni içerir. İsteğe bağlı argümanlar arasında yazı tipi boyutu, renk, yazı tipi ve hizalama gibi metin özellikleri yer alabilir.

`annotate()` fonksiyonu ise text() fonksiyonuna benzerdir ancak belirtilen noktaya işaretçi (ok) eklemek için daha uygun bir seçenektir.

`annotate(s, xy, xytext, arrowprops=None, **kwargs)`
Burada, s argümanı, eklenen metni içerir, xy argümanı, işaretçinin gösterileceği noktayı belirler ve xytext argümanı, metnin gösterileceği noktayı belirler. İsteğe bağlı arrowprops argümanı, işaretçi özelliklerini belirlemek için kullanılabilir.


```python
plt.plot([1,2,3])
plt.text(1,2,"x=1, y=2", bbox={'facecolor': 'red', 'alpha': 0.1})
plt.grid() # Konumları daha rahat görebilmek için
```


```python
# Örnek veri
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Bir figür oluşturma ve eksenleri ayarlama
fig, ax = plt.subplots()
ax.plot(x, y)

# Metin eklemek için text() fonksiyonunu kullanma
ax.text(3, 0.5, "Sinüs Grafiği", fontsize=12, color="red")

# İşaretçi ile metin eklemek için annotate() fonksiyonunu kullanma
ax.annotate("Maksimum", xy=(np.pi/2, 1), xytext=(np.pi/2, 1.5),
            fontsize=10, color="blue",
            arrowprops=dict(facecolor="blue", arrowstyle="->"))

# Grafik gösterme
plt.show()
```

Bu örnek, bir sinüs grafiğine metin eklemeyi göstermektedir. `text()` fonksiyonu, Sinüs Grafiği metnini belirtilen koordinatlarda eklerken, annotate() fonksiyonu, maksimum noktaya işaretçi ile birlikte bir metin ekler.

### Legend() fonksiyonu

Daha önce kullanılan bu fonksiyon ile daha önceden etiket verilmemiş olan grafiklere sırası ile etiket verilebilir. Konumu ile ilgili loc parametresine (best, upper right, upper left, right, center, lower center) gibi değerler verilebilir.


```python
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
```

## Bazı Sihirli Fonksiyonlar

Jupyter notebooklarda kullanılabilecek bir takım sihirli fonksiyonlar(magic functions) ile kolay bir kullanım sağlanabilir. Matplotlib kütüphanesinde kullanılabilecek sihirli fonksiyonlardan bazıları şu şekildedir.

- %matplotlib inline sihirli komutu ile görsellerin notebook içerisinde gösterilmesi sağlanır.
- %matplotlib notebook interaktif grafikler için kullanılır.
- %matplotlib qt interaktif kullanımlar içindir.


```python
%matplotlib notebook
```


```python
%matplotlib inline
```


```python
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
```


```python
%matplotlib inline
```


```python
%pwd 
```


```python
# Diğer sihirli fonksiyonları listelemek için
%lsmagic
```


```python
# Örneğin whos sihirli fonksiyonu kullanılan değişkenleri listeler
%whos
```

## Grafiklerin Kaydedilmesi

Eğer çizilen grafikler eğitim amaçlı veya Jupyter notebook içerisinde gösterim amaçlı kullanılacaksa Jupyter notebook içerisinde bırakılabilir. Ancak grafikler, başka bir yerde örneğin yayında, raporda, dokümanda kullanılacaksa dışarı aktarılması gerekecektir. Böylece çözünürlüğü yüksek grafikler üretilerek dokümanlarda kullanılabilir. Eğer çizilen grafiklerin kodları da saklanmak isteniyorsa %save sihirli fonksiyonu kullanılabilir.

Daha fazla sihirli fonksiyonlar için [şu adres](https://ipython.readthedocs.io/en/stable/interactive/magics.html) ziyaret edilebilir.


```python
%save?
```


```python
% save sin_cos_grafigi 63 # 115. çalıştırılan hücredeki kodları kaydetmek için
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
```


```python
% load sin_cos_grafigi.py # yazılan kodların geri çağrılması için
```

### savefig() fonksiyonu

Matplotlib kütüphanesinde grafikleri resim olarak kaydetmek, grafikleri göstermek kadar kolaydır. Grafikleri jpeg, png gibi formatlarda kaydetmek için savefig() fonksiyonu kullanılabilir. savefig() fonksiyonu içerisine parametre olarak grafiğin yolu ve ismi verilmelidir, bu parametre fname olarak verilir. fname dışında kullanılabilecek diğer bazı parametreler aşağıda verilmiştir.

- dpi=None: Görüntünün çözünürlüğü, örneğin 300 dpi(inç başına düşen nokta sayısı)
- transparent=False: True değeri verildiğinde grafiğin arka planı transparan hale getirilir.
- bbox_inches=None, grafik çevresindeki sınırlar ile ilgilidir. bbox_inches='tight' genellikle ideal sonuçlar verir.

PNG formatı internet kullanımları ve çizim grafikleri için daha uygundur. JPG formatı ise daha sıkıştırılmış bir resim formatıdır. Bu nedenle daha küçük boyutlarda görüntülerin kaydedilmesini sağlar. Eğer daha küçük boyutlu resimler ile çalışılmak isteniyorsa JPG formatı tercih edilebilir. SVG formatı ise vektörel görüntülerde kullanılan ve diğer formatlara göre boyutu yüksek bir seçimdir. 


```python
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
plt.savefig('sin_cos_grafigi.png', dpi=300)
```


```python
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
plt.savefig('sin_cos_grafigi_transparent.png', dpi=300, transparent=True)
```

Renk kodları ile hızlı bir şekilde grafikteki renkler değiştirilebilir. Renk kodları aşağıda paylaşılmıştır.

- r(red)
- g(green)
- b(blue)
- c(cyan)
- k(black)
- w(white)


```python
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
plt.savefig('sin_cos_grafigi_transparent.png', dpi=300, transparent=True, facecolor='b') # ön renk mavi
```

## Grafik Çeşitleri

Matplotlib'de birkaç grafik çeşidi fonksiyonu vardır. Bu fonksiyonlar, çeşitli grafik türlerini veya özellikleri oluşturmak için birkaç satır kodla çağrılabilen önceden tanımlanmış işlevlerdir. Bu fonksiyonlar, hızlı bir şekilde grafikler oluşturmak için yararlıdır.

Bunlardan bazıları şunlardır:

- `subplots()`: Bu fonksiyon, birden fazla grafik içeren bir figür oluşturmak için kullanılır. Belirtilen sayıda alt grafik oluşturur ve her alt grafik, figürün bir parçasıdır. Örneğin, fig, axs = plt.subplots(2, 3) kodu, 2 satır ve 3 sütundan oluşan bir alt grafik düzeni oluşturur.
- `scatter()`: Bu fonksiyon, nokta bulutu grafikleri oluşturmak için kullanılır. Her bir nokta, verilerdeki iki boyutlu bir noktayı temsil eder. Örneğin, plt.scatter(x, y) kodu, x ve y verilerine dayalı bir nokta bulutu grafik oluşturur.
- `bar()`: Bu fonksiyon, sütun grafikleri oluşturmak için kullanılır. Her bir sütun, verilerdeki bir değeri temsil eder. Örneğin, plt.bar(x, y) kodu, x değerlerine göre yüksekliği belirtilen sütunlar oluşturur.
- `hist()`: Bu fonksiyon, histogramlar oluşturmak için kullanılır. Histogram, verilerin dağılımını göstermek için kullanılan bir grafik türüdür. Örneğin, plt.hist(x, bins=10) kodu, x verilerine dayalı 10 bölümlü bir histogram oluşturur.
- `pie()`: Bu fonksiyon, pasta grafikleri oluşturmak için kullanılır. Her bir dilim, verilerdeki bir değeri temsil eder. Örneğin, plt.pie(x, labels=labels) kodu, x değerlerine göre etiketlenmiş bir pasta grafiği oluşturur.

Sihirli fonksiyonlar, belirli grafik türlerini veya özellikleri oluşturmak için tasarlanmıştır, ancak esneklikleri nedeniyle bu işlevlerin çıktıları da özelleştirilebilir.


```python
kadin_yaslar = np.random.randint(low=1,high=75,size=100)
plt.hist(kadin_yaslar,label='kadın yaşları')
plt.legend()
```


```python
erkek_yaslar = np.random.randint(low=1,high=75,size=100)
plt.hist(kadin_yaslar,label='kadın yaşları', alpha=0.5)
plt.hist(erkek_yaslar,label='erkek yaşları', alpha=0.5)
plt.legend()
```


```python
plt.hist([erkek_yaslar, kadin_yaslar], label=['erkek', 'kadin'])
plt.legend()
```

Aynı şekilde histogram grafikleri olasılık yoğunluk fonksiyonlarının çizdirilmesinde de kullanılabilir. Örneğin normal dağılıma uyan bir veri dizisinin grafiği aşağıdaki çizdirilebilir.


```python
np.random.seed(12345)
x_normal = np.random.normal(size=100) # normal dağılıma uyan 100 veri
plt.hist(x_normal, density=True, bins=30)  # `density=False` sayıları alacaktı. Oranları aldık
plt.ylabel('Olasılıklar')
plt.xlabel('Veriler');
```


```python
np.random.seed(12345)
x_normal = np.random.normal(size=1000000) # normal dağılıma uyan 10000 veri
plt.hist(x_normal, density=True, bins=30)  # `density=False` sayıları alacaktı. Oranları aldık
plt.ylabel('Olasılıklar')
plt.xlabel('Veriler');
```

- Çubuk grafikleri: Yaygın bir kullanıma sahiptir. Histogram grafiklerinden farklı yanı x aksisindeki değerlerin kategorik değil nümerik değerler almasıdır. bar() fonksiyonu ile çizim yapılabilir. Diğer grafiklerdeki benzer parametreler burada da geçerlidir. Örneğin align parametresi ile verinin çubuğun ortasından geçmesi istendiği durumda kullanılabilir. Ya da orientation parametresi ile çubuklar dikey eksende mi olsun yatay eksende mi bununla ilgili ayarlama için kullanılabilir. Genellikle ölçüm değerinin nasıl değiştiği görülmek için kullanılır. x değerlerine karşılık gelen y değerlerine kadar bir çubuk çizilir. 


```python
x1_koordinatlari = np.random.randint(10, size=20)
y1_koordinatlari = np.random.randint(5,size=20)

x2_koordinatlari = np.random.randint(10, size=20)
y2_koordinatlari = np.random.randint(5,size=20)

plt.bar(x1_koordinatlari,y1_koordinatlari,label='grup 1') 
```

Bunun yanı sıra çubuk grafikleri kategorik veriler için de kullanılabilir. Bunun için; 


```python
x_bar = np.random.randint(5,size=5)
plt.barh(x_bar, np.arange(5))
plt.xticks(np.arange(5),['bir','iki','üç','dört','beş']) # kategoriler ayrıca verilebilir.
```

Diğer grafik çeşitleri

- pie pasta grafikleri
- scatter dağılım grafikleri 
- boxplot kutu grafikleri

## Stil Dosyaları ile Çalışmak

Matplotlib kütüphanesinde bir dokümanda düzenli bir şekilde renk ve görsel seçenekleri kullanmak için stiller kullanılmaktadır. Kütüphane içerisindeki stil dosyaları `plt.style.available` komutu ile gösterilebilir. Tercih edilen stil `plt.style.use()` komutu ile seçilebilir. Bir dokümanda çizilen grafiklerin renkleri, yazı fontları, font büyüklükleri, ızgara şekilleri gibi tasarım özelliklerinin benzer şekilde olması beklenir. 

Diğer stiller ile ilgili bilgi [şu adresten](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html) alınabilir.


```python
plt.style.available
```


```python
plt.style.use('seaborn')
```


<img src="https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_001.png"  width = "75%" height = "75%">
<img src="https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_002.png"  width = "75%" height = "75%">
<img src="https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_003.png"  width = "75%" height = "75%">
<img src="https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_004.png"  width = "75%" height = "75%">
<img src="https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_005.png"  width = "75%" height = "75%">
<img src="https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_006.png"  width = "75%" height = "75%">
<img src="https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_008.png"  width = "75%" height = "75%">


```python
%matplotlib inline
```


```python
np.random.seed(12345)
x_normal = np.random.normal(size=10000) # normal dağılıma uyan 10000 veri
plt.hist(x_normal, density=True, bins=30)  # `density=False` sayıları alacaktı. Oranları aldık
plt.ylabel('Olasılıklar')
plt.xlabel('Veriler')
```


```python
np.random.seed(12345)
x_normal = np.random.normal(size=10000) # normal dağılıma uyan 10000 veri
plt.hist(x_normal, density=True, bins=30)  # `density=False` sayıları alacaktı. Oranları aldık
plt.ylabel('Olasılıklar')
plt.xlabel('Veriler')
```


```python
# varsayılanlar belirlemek
matplotlib.rcParams['lines.linewidth']=2.0 # tüm çizgiler bu çizgi genişliğine sahip olur
```

## Seaborn Kütüphanesi

Seaborn, Python'da veri görselleştirme için kullanılan bir kütüphanedir. Matplotlib kütüphanesi temelde kullanılan grafiklerin yanı sıra, Seaborn kütüphanesi daha özel ve daha karmaşık grafiklerin oluşturulmasına yardımcı olur.

Seaborn, özellikle istatistiksel veri görselleştirmesi için tasarlanmıştır ve Matplotlib'den daha yüksek seviyeli bir arayüz sağlar. Buna ek olarak, Seaborn, renk paletleri, özel grafikler ve istatistiksel gösterimler için önceden tanımlanmış tema ve stiller gibi birçok özellik sunar.

Özellikle, Seaborn kütüphanesi aşağıdaki görselleştirme türlerini içerir:

- Çizgi Grafikleri
- Dağılım Grafikleri
- Çift Değişkenli Dağılım Grafikleri
- Çizgi ve Nokta Çizgileri
- Bar Grafikleri
- Isı Haritaları
- Çift Eksenli Grafikler

Seaborn aynı zamanda, veri setlerindeki ilişkileri analiz etmek ve bu verileri görselleştirmek için kullanılan regresyon analizi, faktör analizi ve kovaryans analizi gibi istatistiksel yöntemler de sunmaktadır.


```python
import seaborn as sns
```


```python
tips = sns.load_dataset("tips")
tips.head()
```

### replot()

Seaborn kütüphanesi içinde yer alan `relplot` fonksiyonu, verilerin ilişkisini incelemek ve görselleştirmek için kullanılan bir fonksiyondur. Bu fonksiyon, scatterplot ve lineplot fonksiyonlarının yerine geçebilen bir çoklu grafik çizim aracıdır.

`relplot` fonksiyonunun en önemli özelliği, veri kümesindeki iki veya daha fazla değişken arasındaki ilişkileri aynı anda göstermek için kullanılabilecek çoklu grafikler çizdirme olanağı sağlamasıdır. Bu grafiklerin türleri, kind parametresiyle belirlenebilir ve seçenekler arasında `scatter`, `line`, `strip`, `swarm`, `box`, `violin`, `bar`, `count` gibi seçenekler yer alır.

Ayrıca, col ve row parametreleri yardımıyla veri kümesinin farklı kategorilerine göre ayrılmış alt gruplarını da aynı anda görselleştirmek mümkündür. col ve row parametreleri, değişkenlerin sıralanması veya ayrılması için kullanılabilecek kategorik değişkenleri belirtmek için kullanılır.

Örneğin, aşağıdaki kod bloğu, relplot fonksiyonunu kullanarak tips veri kümesindeki `total_bill` ve `tip` değişkenleri arasındaki ilişkiyi gösteren bir scatter grafiği çizdirir:


```python
sns.relplot(x='total_bill', y = 'tip', data = tips)
```


```python
sns.relplot(x='total_bill', y = 'tip', data = tips, hue = 'day') # günlere göre ayrı tipler
```


```python
sns.relplot(x='total_bill', y = 'tip', data = tips, hue = 'day', style='time') # zamana göre de ayrılmış
```


```python
sns.relplot(x='total_bill', y = 'tip', data = tips, hue = 'day', style='time', col = 'sex') # cinsiyet de eklendi
```

### catplot()
Seaborn kütüphanesi içinde yer alan `catplot()`, kategorik verilerin görselleştirilmesi için kullanılan bir fonksiyondur. catplot(), farklı tiplerdeki kategorik verileri farklı grafik türleri ile görselleştirmek için tasarlanmıştır.

catplot(), aşağıdaki grafik tiplerini destekler:

* stripplot: nokta grafiği
* swarmplot: sinek grafiği
* boxplot: kutu grafiği
* violinplot: keman grafiği
* boxenplot: kutu ve bıyık grafiği
* pointplot: nokta grafiği
* barplot: çubuk grafiği
* countplot: sayım grafiği

Örneğin, tips veri kümesi ile catplot() fonksiyonunu kullanarak, her gün için farklı öğünlerdeki ortalama hesap miktarlarını çizdirebiliriz:


```python
g = sns.catplot(x='day', y='total_bill', hue='sex', kind='bar', data=tips)
plt.show()
```

Bu örnekte `catplot()` fonksiyonuna x, y ve hue parametreleri verilerek, x ekseninde günler, y ekseninde hesap miktarı, hue ile de cinsiyet bilgisi görselleştirilmiştir. Ayrıca kind parametresine bar değeri verilerek, çubuk grafiği çizdirilmiştir.

Tablo veya veri kümesinin özet istatistiklerini göstermek için kullanılan boxplot, Seaborn kütüphanesi içinde yer alan `boxplot()` fonksiyonu ile çizdirilebilir. Boxplot, verilerin çeyrekliklerini (çeyrekler arası yayılma), medyanı ve aykırı değerleri grafiksel olarak gösterir.

Örneğin, tips veri kümesindeki bahşiş miktarları ile boxplot çizdirelim:


```python
sns.boxplot(x='day', y='tip', data=tips)
plt.show()
```
