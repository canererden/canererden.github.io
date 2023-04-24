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

# Görsel Veri Analizine Giriş

Bu bölümde, Python'da en yaygın kullanılan ve güçlü veri görselleştirme kitaplıklarından biri olan Matplotlibkullanarak veri görselleştirme dünyasına giriş yapacağız. Matplotlib, Python programlama dili için bir grafik çizme kütüphanesidir ve verilerinizi görsel olarak temsil etmek için kullanılır. Bu kütüphane, doğrusal grafikler, dağılım grafikleri, pasta grafikleri, çubuk grafikleri ve daha birçok grafik türü oluşturmanızı sağlar. Matplotlib, ücretsiz ve açık kaynaklı bir yazılımdır ve Python'da veri analizi, makine öğrenimi, yapay zeka ve daha birçok alanda sıklıkla kullanılır. Bu eğitimde, Matplotlib kütüphanesinin temellerini öğreneceksiniz ve verilerinizi nasıl etkileyici grafiklere dönüştürebileceğinizi öğreneceksiniz.

## Matplotlib Kütüphanesi
Matplotlib, 2 ve 3 boyutlu grafiklerin çizilmesi için geliştirilmiş, anasayfası (http://matplotlib.org) adresinde bulunan, özellikle bilimsel ve mühendislik alanlarındaki veri görselleştirmelerinde sıklıkla kullanılan bir kütüphanedir. Veri görselleştirme ihtiyacı verinin olduğu her alanda geçerlidir. Çünkü büyük veri kümelerindeki veriyi nitelendiren özelliklere ve ölçülere genel çerçeveden bakılmak istendiğinde görsel araçlara ihtiyaç duyulur. Örneğin bir veri setinin dağılımı ile ilgili histogram grafikleri hızlı bir izlenim imkanı sunar. Aşağıdaki görselde tablo ile sunulamayacak bilgilerin veri görselleştirme ile göze hitap edecek şekilde sunulması için araçlar gösterilmiştir. 

![](https://uploads-ssl.webflow.com/61488f4f65be16b5ebbd450b/61b74ab1d55fa17b82d7ed89_Data%20Visualization.jpg)

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

![](https://matplotlib.org/stable/_images/anatomy.png)

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

<img src="https://i.vgy.me/2pVPDQ.png" withd = "75%" height = "75%">

Bu örnekte, öncelikle `matplotlib.pyplot` modülü import edilir. Daha sonra, "x" ve "y" verileri tanımlanır. `plt.plot(x, y)` çağrısı ile, bu verileri içeren bir grafik oluşturulur.

Daha sonra, `plt.title()`, `plt.xlabel()` ve `plt.ylabel()` çağrıları ile grafik başlığı ve eksen etiketleri belirtilir. Son olarak, `plt.show()` çağrısı ile, oluşturulan grafik ekranda gösterilir.

Bu örnek, Matplotlib'in temel kullanımını göstermektedir. Grafik oluşturma sürecinde, "Axes" özelliklerini ve diğer özelleştirme seçeneklerini kullanarak grafikleri daha fazla özelleştirebilirsiniz.


```python
plt.plot([1,2,3],[7,3,9]) # (1,7), (2,3), (3,9) noktalarını birleştirir
```

<img src="https://i.vgy.me/BByAQm.png">


```python
plt.plot([3, 5, 2])  # x ekseni verilmez ise varsayılan olarak 0-1-2... gelir
```

<img src="https://i.vgy.me/moQFrc.png">


```python
x = np.linspace(-np.pi, np.pi, 20)  # -pi ile +pi arasında 20 adet değer
plt.plot(x, np.sin(x))
```

<img src="https://i.vgy.me/90ygnH.png">

## Grafiklere Özellik Ekleme

Az önce çizdirilen grafikler x, y eksenleri ve alınan değerlerin birleştirilmesi ile oluşturuldu. Matplotlib kütüphanesinde eğer bir özellik tanımı yapılmaz ise grafikler yalın halde gelir. Ancak grafikler yalın halde anlamsızdır. x, y eksenlerinin neyi gösterdiği, grafiğin başlığının ne olduğu, verilerin neler olduğu grafik üzerinde gösterilmelidir. 

### Eksen etiketi, seri etiketi ve başlık özelliği ekleme

`label` özelliği verilerin neler olduğunu gösterir. label özelliğinin grafik içerisinde gösterilmesi için `plt.legend()` fonksiyonu eklenmiştir.


```python
plt.plot(x,np.sin(x), label = 'sin(x)')
plt.plot(x,np.cos(x), label = 'cos(x)')
plt.legend()
```

<img src="https://i.vgy.me/0gM4Ig.png">


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
plt.legend(loc=7); # upper left upper right
plt.title('Sinüs Fonksiyonu')
plt.show()
```

<img src="https://i.vgy.me/Qh7xP4.png">

### Etiket fontlarını değiştirme

Aşağıdaki örnekte birden fazla çizim aynı grafik üzerinde gerçekleştirilmiştir. Buna göre 3 farklı çizimi gösterdikten sonra etiketlerin fontları üzerinde değişiklikler gerçekleştirdik.

Renk kullanımında `plot()` işlevi, color parametresi ile çizgi rengini belirleyebilir. Ayrıca, hex renk kodlarını veya RGB veya RGBA renk değerlerini de kullanabilirsiniz. Örneğin:


```python
# Ya da aynı figür üzerinde şekil çizmek istersek
plt.plot(x, np.sin(x), x, np.cos(x), x, x**2);  # ; fonksiyon yazmak istemezsek
```

<img src="https://i.vgy.me/6Jj6jT.png">


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

<img src="https://i.vgy.me/aswWtT.png">

Fontlarla ilgili daha detaylı bilgi [şu adresten](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo_kw.html) alınabilir.

### Izgaraları gösterme


```python
plt.plot(x, np.sin(x), x, np.cos(x), x, x**2)
plt.grid(True, axis='y') # axis='x' sadece x ekseninde ızgaralar gösterir
```

<img src="https://i.vgy.me/6JSlb2.png">

### Renk ve çizgi stillerini değiştirme

Bu örnekte, "color", "linestyle" ve "linewidth" parametreleri kullanılarak çizgi rengi, stil ve kalınlığı belirtilir.


```python
# çizgilerin kalınlıklarının ayarlanması
plt.plot(x, np.sin(x), x, np.cos(x), x, x**2, linewidth=5);
plt.grid()
```

<img src="https://i.vgy.me/iYjbfd.png">


```python
# çizgi stilleri
plt.plot(x, np.sin(x), linestyle='dashed', label='sin')
plt.plot(x, np.cos(x), linestyle='--', label='cos')
plt.plot(x, x**2, label='kare', linestyle='-.')
plt.grid()
plt.legend()
```

<img src="https://i.vgy.me/3lgUGM.png">

![image.png](https://matplotlib.org/stable/_images/sphx_glr_linestyles_001.png)

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

<img src="https://i.vgy.me/v47PXv.png">

Matplotlib, çizgi komutlarının marker parametresi kullanılarak seçilen birden fazla kategoriye sahip markerları destekler:

- Doldurulmamış markerlar
- Doldurulmuş markerlar
- TeX sembollerinden oluşturulan markerlar
- Yollardan oluşturulan markerlar


**Doldurulmamış markerlar (Unfilled markers)**
![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_001.png)
**Doldurulmuş markerlar (Filled)**
![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_002.png)
**Marker fill styles**
![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_003.png)
**TeX sembollerinden oluşturulan markerlar**
![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_004.png)
**Yollardan oluşturulan markerlar**
![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_005.png)

### Eksenleri sınırlandırma ve işaretleme

`xlim` ve `ylim`, bir grafikte gösterilen x ve y eksenlerinin sınırlarını belirlemek için kullanılan fonksiyonlardır.

`xlim` ve `ylim` fonksiyonlarına verilen değerler, belirtilen eksenin en küçük ve en büyük değerlerini belirler. Örneğin, aşağıdaki kod bloğunda, xlim ve ylim kullanarak bir çizgi grafiğinin x ve y eksenlerinin sınırlarını ayarladık:


```python
# x ve y verileri
x = np.linspace(0, 10, 100)
y = np.sin(x)

# çizgi grafiği çizdirme
plt.plot(x, y)

# x ve y eksenlerinin sınırlarını belirleme
plt.xlim([2, 8])
plt.ylim([-1.2, 1.2])

# grafiği gösterme
plt.show()
```

<img src="https://i.vgy.me/uFqMxO.png">

Bu örnekte, xlim([2, 8]) fonksiyonuyla x ekseni sınırları 2 ve 8 arasına, ylim([-1.2, 1.2]) fonksiyonuyla y ekseni sınırları -1.2 ve 1.2 arasına ayarlandı.

`xticks` ve `yticks`, bir grafikteki x ve y eksenlerinin işaretlenmesini (tick) kontrol etmek için kullanılan fonksiyonlardır.

`xticks` ve `yticks` fonksiyonları, aşağıdaki gibi kullanılabilir:


```python
plt.plot(x, y)

# x ve y ekseni işaretlerini ayarlama
plt.xticks(np.arange(0, 11, step=2))
plt.yticks([-1, 0, 1])

# grafiği gösterme
plt.show()
```

<img src="https://i.vgy.me/KLgh8s.png">

Bu örnekte, xticks fonksiyonu ile x ekseni işaretlerinin aralıklarını belirliyoruz. np.arange(0, 11, step=2) ifadesi, x ekseni işaretlerinin 0'dan başlayarak 2'şer arttırılarak 10'a kadar olan sayılar olduğunu belirtir. yticks fonksiyonu ise, y ekseni işaretlerini belirliyoruz. [-1, 0, 1] ifadesi ile y ekseni işaretlerinin -1, 0 ve 1 olduğunu belirtiyoruz.

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

<img src="https://i.vgy.me/vDCJ9E.png">

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

<img src="https://i.vgy.me/FSwmci.png">


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

<img src="https://i.vgy.me/6Y6MkD.png">


```python
fig, axs = plt.subplots(nrows= 3, ncols=2, sharex=True)  # 2x1 li bir grafik ve ortak x axis i
```

<img src="https://i.vgy.me/RU7JKp.png">


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

<img src="https://i.vgy.me/wk9c8J.png">


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

<img src="https://i.vgy.me/F0XUfP.png">


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

<img src="https://i.vgy.me/f9libC.png">


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

<img src="https://i.vgy.me/sxFnK3.png">

Başka bir örnekte MATLAB stili pyplot grafik çizdirmede birden fazla eksende grafik çizdirilmek istenirse aşağıdaki yapı kullanılabilir.


```python
plt.subplot(121) # Bir satır iki sütunlu bir yapıda birinci grafiği çizdir.
plt.plot(x, np.sin(x))
plt.subplot(122) # İkinci grafik
plt.plot(x, np.cos(x))
```

<img src="https://i.vgy.me/U3If1L.png">

### Izgaralar ile Subplot çizdirme

Yaygın kullanım için benzer ölçülerde eksenler ile çalışmak her ne kadar yeterli olsa da Matplotlib istenilen boyutlarda eksenler oluşturmak için imkan sunmaktadır. `plt.subplot()` fonksiyonu satır, sütun ve indeks değerlerinden oluşan 3 tam sayı değeri almaktaydı. Tam sayı değerleri eksenin kapsayacağı ızgara dilimi ile ilgili bilgiyi vermemektedir.  


```python
for i in range(1,5):
    print(i)
    plt.subplot(2,2,i) # 2 satır 2 sütun eksenlerin i. ekseni
    plt.text(0.5, 0.5, str(i))
```

<img src="https://i.vgy.me/IFliaG.png">

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

<img src="https://i.vgy.me/6n0FsN.png">

## Grafiklere Farklı Elemanlar Ekleme

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

<img src="https://i.vgy.me/AMB7jw.png">


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

<img src="https://i.vgy.me/dTUChI.png">

Bu örnek, bir sinüs grafiğine metin eklemeyi göstermektedir. `text()` fonksiyonu, Sinüs Grafiği metnini belirtilen koordinatlarda eklerken, annotate() fonksiyonu, maksimum noktaya işaretçi ile birlikte bir metin ekler.

### Legend() fonksiyonu

Daha önce kullanılan bu fonksiyon ile daha önceden etiket verilmemiş olan grafiklere sırası ile etiket verilebilir. Konumu ile ilgili loc parametresine (best, upper right, upper left, right, center, lower center) gibi değerler verilebilir.


```python
plt.plot(x, np.sin(x))  
plt.plot(x, np.cos(x))  
plt.plot(x, x**2) 
plt.legend(['sinüs', 'cosinüs', 'kare'], loc = 'upper left')
```

<img src="https://i.vgy.me/CHFxUw.png">

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

- dpi=None: Görüntünün çözünürlüğü, örneğin 300 dpi(inç başına düşen nokta sayısı) <img src="https://i.vgy.me/Ty1ESY.png">
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

## Grafik Çeşitleri ve Stiller

Matplotlib kütüphanesi, birçok farklı grafik türü için çeşitli çizim fonksiyonları içerir. Bazı popüler grafik türleri şunlardır:

1. Çizgi grafikleri (Line plots): Değişkenler arasındaki ilişkiyi göstermek için kullanılır.
2. Dağılım grafikleri (Scatter plots): İki değişken arasındaki ilişkiyi göstermek için kullanılır.
3. Histogramlar: Değişkenlerin dağılımını göstermek için kullanılır.
4. Kutu grafikleri (Box plots): Değişkenlerin istatistiksel özelliklerini göstermek için kullanılır.
5. Alan grafikleri (Area plots): Değişkenlerin zamana bağlı olarak değişimini göstermek için kullanılır.
6. Pasta grafikleri (Pie charts): Kategorik verilerin oranlarını göstermek için kullanılır.
7. Çubuk grafikleri (Bar charts): Kategorik verilerin karşılaştırılması için kullanılır.

Matplotlib'de birkaç grafik çeşidi özel tanımlı fonksiyonlar vardır. Bu fonksiyonlar, çeşitli grafik türlerini veya özellikleri oluşturmak için birkaç satır kodla çağrılabilen önceden tanımlanmış işlevlerdir. Bu fonksiyonlar, hızlı bir şekilde grafikler oluşturmak için yararlıdır.

Bu fonksiyonlardan bazıları şunlardır:

- `subplots()`: Bu fonksiyon, birden fazla grafik içeren bir figür oluşturmak için kullanılır. Belirtilen sayıda alt grafik oluşturur ve her alt grafik, figürün bir parçasıdır. Örneğin, fig, axs = plt.subplots(2, 3) kodu, 2 satır ve 3 sütundan oluşan bir alt grafik düzeni oluşturur.
- `scatter()`: Bu fonksiyon, nokta bulutu grafikleri oluşturmak için kullanılır. Her bir nokta, verilerdeki iki boyutlu bir noktayı temsil eder. Örneğin, plt.scatter(x, y) kodu, x ve y verilerine dayalı bir nokta bulutu grafik oluşturur.
- `bar()`: Bu fonksiyon, sütun grafikleri oluşturmak için kullanılır. Her bir sütun, verilerdeki bir değeri temsil eder. Örneğin, plt.bar(x, y) kodu, x değerlerine göre yüksekliği belirtilen sütunlar oluşturur.
- `hist()`: Bu fonksiyon, histogramlar oluşturmak için kullanılır. Histogram, verilerin dağılımını göstermek için kullanılan bir grafik türüdür. Örneğin, plt.hist(x, bins=10) kodu, x verilerine dayalı 10 bölümlü bir histogram oluşturur.
- `pie()`: Bu fonksiyon, pasta grafikleri oluşturmak için kullanılır. Her bir dilim, verilerdeki bir değeri temsil eder. Örneğin, plt.pie(x, labels=labels) kodu, x değerlerine göre etiketlenmiş bir pasta grafiği oluşturur.

### Çizgi grafikleri

Çizgi grafikleri veri setlerindeki değişimleri zaman içinde izlemek ve trendleri belirlemek için kullanılır. İşletme verilerinde, finansal verilerde ve ekonomik verilerde sıklıkla kullanılırlar. Ayrıca, çok sayıda veri noktası arasındaki ilişkiyi göstermek için de yararlıdırlar.

Çizgi grafiklerinin avantajları şunlardır:

- Verilerin zaman içindeki değişimini net bir şekilde gösterirler.
- Birden fazla veri seti arasındaki ilişkiyi kolayca anlamamızı sağlar.
- Verilerin trendlerini ve değişimlerini hızlı bir şekilde anlayabiliriz.
- Basit ve anlaşılır bir grafik türüdür.
- Bu nedenlerle, işletmelerde, finansal kurumlarda ve ekonomi alanında sıklıkla kullanılan bir grafik türüdür.

Tablo verilerinin belirli bir zaman aralığındaki değişimini görselleştirmek için çizgi grafikleri sıkça kullanılır. Örnek olarak, aylık gelirleri gösteren bir veri seti üzerinden bir çizgi grafiği çizelim.


```python
aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran']
gelirler = [20000, 25000, 30000, 28000, 32000, 35000]
plt.plot(aylar, gelirler, marker='o')
plt.title('Aylık Gelirler')
plt.xlabel('Aylar')
plt.ylabel('Gelirler')
plt.ylim(0, 40000)
```

<img src="https://i.vgy.me/SqZn9t.png">

Bu kodları çalıştırdığımızda, aylık gelirlerimizi gösteren bir çizgi grafiği elde ederiz. Grafikte her ay için bir nokta ve bu noktaları birleştiren bir çizgi görüntülenir. Ayrıca grafiğimizde başlık, etiketler ve y-ekseni sınırları da vardır.

### Dağılım grafikleri

Dağılım grafikleri, verilerin dağılımını görselleştirmek için kullanılır. Bu grafik türü, verilerin merkezi eğilimlerini, dağılımını ve aykırı değerlerini göstermek için kullanışlıdır. Dağılım grafikleri, veri setlerindeki değişkenlikleri ve dağılımları anlamak için özellikle yararlıdır.

### Histogram grafikleri

Histogramlar, veri dağılımını görselleştirmek için kullanılan bir grafik türüdür. Özellikle büyük veri kümelerinde kullanılmaktadır. Histogramlar, verilerin belirli bir aralıktaki sıklığını ve yoğunluğunu gösterir.

Histogramlar, birçok alanda kullanılabilir. Örneğin, finansal verileri incelemek için, hisse senedi fiyatlarının belirli bir aralıktaki dağılımını analiz etmek için kullanılabilirler. Ayrıca, tıp alanında, hastaların belirli bir özelliklerinin (örneğin, yaş veya kan basıncı) dağılımını incelemek için de kullanılabilirler.

Histogramlar, veri dağılımını anlamak için oldukça yararlıdır. Verilerin nasıl dağıldığı, hangi aralıklarda yoğunlaştığı veya dağıldığı, hangi değerlerin daha yaygın olduğu gibi bilgileri görselleştirerek anlamak kolaylaşır. Ayrıca, histogramlar, veri setindeki aykırı değerleri de tespit etmek için kullanılabilir.

Histogramların bir diğer avantajı, veri kümesinin şekil ve boyutuna göre özelleştirilebilmesidir. Böylece, verilerin daha iyi anlaşılmasını sağlayacak bir histogram oluşturulabilir.


```python
kadin_yaslar = np.random.randint(low=1,high=75,size=100)
plt.hist(kadin_yaslar,label='kadın yaşları')
plt.legend()
```

<img src="https://i.vgy.me/l8GVeP.png">

Bu örnekte histogram, `plt.hist()` fonksiyonu ile çizildi. Histogramda kullanılan parametreler arasında, `density=True` seçeneği histogramın yoğunluk çizimini gösterirken, facecolor parametresi histogramın dolgu rengini belirler. 


```python
plt.hist(kadin_yaslar,label='kadın yaşları', alpha=0.5)
plt.hist(erkek_yaslar,label='erkek yaşları', alpha=0.5)
plt.legend()
```

<img src="https://i.vgy.me/p4itVz.png">


```python
plt.hist([erkek_yaslar, kadin_yaslar], label=['erkek', 'kadin'])
plt.legend()
```

<img src="https://i.vgy.me/BLU1r1.png">

Aynı şekilde histogram grafikleri olasılık yoğunluk fonksiyonlarının çizdirilmesinde de kullanılabilir. Örneğin normal dağılıma uyan bir veri dizisinin grafiği aşağıdaki çizdirilebilir.


```python
np.random.seed(12345)
x_normal = np.random.normal(size=100) # normal dağılıma uyan 100 veri
plt.hist(x_normal, density=True, bins=30)  # `density=False` sayıları alacaktı. Oranları aldık
plt.ylabel('Olasılıklar')
plt.xlabel('Veriler');
```

<img src="https://i.vgy.me/QELnA3.png">


```python
np.random.seed(12345)
x_normal = np.random.normal(size=1000000) # normal dağılıma uyan 10000 veri
plt.hist(x_normal, density=True, bins=30)  # `density=False` sayıları alacaktı. Oranları aldık
plt.ylabel('Olasılıklar')
plt.xlabel('Veriler');
```

<img src="https://i.vgy.me/C878WF.png">

### Kutu grafikleri

Kutu grafiği, verilerin dağılımını ve değişkenliğini görselleştirmek için kullanılan bir grafik türüdür. En yaygın kullanımı, farklı kategoriler veya gruplar arasındaki sayısal verilerin karşılaştırılmasıdır. Ayrıca, verilerin aykırı (outlier) değerlerini belirlemek ve ortalamadan sapmaları görselleştirmek için de kullanılabilir.

Kutu grafikleri, aşağıdaki avantajlara sahiptir:

- Görselleştirme açısından kolaydır ve verilerin dağılımını hızlı bir şekilde anlamamızı sağlar.
- Aykırı değerleri (outlier) belirlemede ve veriler arasındaki değişkenliği göstermede etkilidir.
- Farklı gruplar veya kategoriler arasındaki sayısal verilerin karşılaştırılması için idealdir.

Kullanım örneği olarak, bir şirketin farklı bölümlerinin aylık satış verilerini karşılaştırmak istediğimizi düşünelim. Kutu grafiği, farklı bölümlerin satış verilerinin ortalamasını, medyanını, minimum ve maksimum değerlerini, ayrık değerlerini ve verilerin dağılımını göstererek kolayca karşılaştırmamıza olanak sağlayacaktır.


```python
# Verileri oluşturma
bolumler = ['Finans', 'Satış', 'Pazarlama', 'Muhasebe']
veriler = [[25000, 35000, 40000, 45000, 50000], 
           [30000, 35000, 40000, 45000, 55000],
           [20000, 25000, 35000, 40000, 45000],
           [15000, 20000, 25000, 30000, 35000]]

# Kutu grafiği oluşturma
plt.boxplot(veriler)
plt.xticks(range(len(bolumler)), bolumler)
plt.xlabel('Bölümler')
plt.ylabel('Aylık Satış')
plt.title('Bölümler Arasındaki Aylık Satış Farklılıkları')
plt.show()

```

<img src="https://i.vgy.me/vQWXGI.png">

Bu kod, farklı bölümlerin aylık satış verilerinin kutu grafiğini oluşturacak ve her bir bölüm için ayrı bir kutu oluşturarak verilerin karşılaştırılmasına olanak sağlayacaktır.

### Alan grafikleri

Alan grafiği, verilerin belirli bir aralıktaki değişimlerini göstermek için kullanılan bir grafik türüdür. Genellikle zamana bağlı değişimlerin gösterilmesinde tercih edilir ve verilerin toplamını veya yüzdesini de gösterir.

Alan grafiklerinin avantajları şunlardır:

- Zamanla değişen verilerin görselleştirilmesi için idealdir.
- Verilerin toplamını veya yüzdesini göstererek, toplamın ne kadarını hangi kategoride harcadığımızı anlamamızı sağlar.
- Birden fazla veri seti arasındaki ilişkiyi göstermek için kullanılabilir.
- Verilerin dağılımını gösterirken, grafikteki renkler ve gölgelendirme yardımıyla görsel olarak daha çekici hale getirilebilir.

Örnek kullanımı aşağıdaki gibi olabilir:


```python
# Verileri oluşturma
yil = [2016, 2017, 2018, 2019, 2020]
gelir = [10000, 15000, 20000, 25000, 30000]
gider = [5000, 8000, 10000, 15000, 20000]

# Alan grafiği oluşturma
plt.stackplot(yil, gelir, gider, labels=['Gelir', 'Gider'])
plt.legend(loc='upper left')
plt.title('Gelir ve Giderler')
plt.xlabel('Yıl')
plt.ylabel('Tutar')
plt.show()
```

<img src="https://i.vgy.me/K1J9rG.png">

Bu örnekte, yıllara göre gelir ve gider verileri bir alan grafiği ile gösterilir. Renkli ve gölgeli alanlar yardımıyla, gelirin ve giderin ne kadar olduğu ve bunların yıllar içindeki değişimleri kolayca görülebilir.

### Pasta grafikleri

Pasta grafikleri, bir veri kümesindeki oranları görselleştirmek için kullanılan grafik türleridir. Pasta grafikleri, her bir veri kategorisi için yüzde veya mutlak sayısal değerler kullanarak, her bir kategori arasındaki oranları kolayca anlamamızı sağlar.

Pasta grafikleri ayrıca şunlara da yardımcı olabilir:

- Bir veri kümesindeki dağılımı anlamak
- Toplamın ne kadarını her kategorinin temsil ettiğini anlamak
- Farklı veri kategorileri arasındaki oranları karşılaştırmak

Örneğin, bir şirketin müşterilerinin demografik dağılımını göstermek istediğinizi varsayalım. Pasta grafikleri bu verileri kolayca görselleştirmenize yardımcı olabilir. Ayrıca, bir ürün veya hizmetin farklı pazar segmentleri arasındaki payını göstermek için de kullanılabilir.

İşte bir pasta grafik örneği:


```python
# Verileri oluşturma
kategoriler = ['Erkek', 'Kadın', 'Diğer']
oranlar = [60, 35, 5]

# Pasta grafik oluşturma
plt.pie(oranlar, labels=kategoriler, autopct='%1.1f%%')

# Grafik özellikleri
plt.title('Müşteri Demografisi')
plt.axis('equal')

# Grafiği gösterme
plt.show()

```

<img src="https://i.vgy.me/hEav5i.png">

Bu örnek, bir şirketin müşteri tabanının demografik dağılımını göstermek için bir pasta grafik kullanır. "Erkek", "Kadın" ve "Diğer" kategorileri için oranları gösterir ve her bir dilimde yüzde değerlerini görüntüler.

### Çubuk grafikleri

Çubuk grafikleri yaygın bir kullanıma sahiptir. Histogram grafiklerinden farklı yanı x aksisindeki değerlerin kategorik değil nümerik değerler almasıdır. bar() fonksiyonu ile çizim yapılabilir. Diğer grafiklerdeki benzer parametreler burada da geçerlidir. Örneğin align parametresi ile verinin çubuğun ortasından geçmesi istendiği durumda kullanılabilir. Ya da orientation parametresi ile çubuklar dikey eksende mi olsun yatay eksende mi bununla ilgili ayarlama için kullanılabilir. Genellikle ölçüm değerinin nasıl değiştiği görülmek için kullanılır. x değerlerine karşılık gelen y değerlerine kadar bir çubuk çizilir. 


```python
x1_koordinatlari = np.random.randint(10, size=20)
y1_koordinatlari = np.random.randint(5,size=20)

x2_koordinatlari = np.random.randint(10, size=20)
y2_koordinatlari = np.random.randint(5,size=20)

plt.bar(x1_koordinatlari,y1_koordinatlari,label='grup 1') 
```

<img src="https://i.vgy.me/vBcU1r.png">

Bunun yanı sıra çubuk grafikleri kategorik veriler için de kullanılabilir. Bunun için; 


```python
x_bar = np.random.randint(5,size=5)
plt.barh(x_bar, np.arange(5))
plt.xticks(np.arange(5),['bir','iki','üç','dört','beş']) # kategoriler ayrıca verilebilir.
```

<img src="https://i.vgy.me/yiJ4Ck.png">

Diğer grafik çeşitleri

- pie pasta grafikleri
- scatter dağılım grafikleri 
- boxplot kutu grafikleri

### Kelime bulutları

Kelime bulutu, bir metin belgesinde geçen kelimelerin frekans dağılımını görselleştirmek için kullanılır. Genellikle, kelime bulutu oluşturma işlemi şu adımları içerir:

1. Metnin yüklenmesi ve işlenmesi: Kelime bulutu oluşturmak için öncelikle metin belgesinin yüklenmesi ve işlenmesi gerekir. Bu işlem, metnin önceden belirlenmiş bir dil işleme adımından geçirilmesi ile gerçekleştirilir. Bu adım, kelime ayıklama, özel karakterlerin kaldırılması ve ayrıştırma işlemlerini içerebilir.
2. Kelime frekanslarının hesaplanması: Metnin işlenmesinden sonra, belgedeki her kelimenin frekansı hesaplanır. Bu, kelimenin belgedeki toplam sayısıdır.
3. Kelime bulutu oluşturma: Hesaplanan kelime frekansları, kelime bulutu oluşturmak için kullanılır. Kelimeler, büyükten küçüğe doğru sıralanır ve en sık kullanılan kelimeler daha büyük yazı tipiyle gösterilir.
4. Kelime bulutları, özellikle sosyal medya analizi, web sayfası içeriği analizi ve pazarlama kampanyalarında kullanılan bir veri görselleştirme aracıdır.

### 3D grafikler

Matplotlib kütüphanesi, 3 boyutlu verileri görselleştirmek için de kullanılabilir. Bu işlem için `mplot3d` alt paketi kullanılır. Bu alt paket sayesinde, 3 boyutlu grafikler oluşturmak için gerekli araçlar sağlanır.

Öncelikle, `mplot3d` paketini kullanarak 3 boyutlu grafikler için gerekli araçları içe aktaralım:


```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1,2,3,4,5]
y = [2,3,4,5,6]
z = [0,1,2,3,4]
ax.scatter(x, y, z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
```

<img src="https://i.vgy.me/vTVAqM.png">

Bir başka örnek verelim. Burada `add_subplot()` fonksiyonu kullanılarak, 1 satır ve 1 sütundan oluşan bir alt çizim alanı oluşturulur ve projection parametresine "3d" değeri verilerek, 3 boyutlu bir alt çizim alanı oluşturulur.

3 boyutlu bir grafik çizdirmek için, `plot()` fonksiyonunun yerine `plot_wireframe()` fonksiyonu kullanılabilir. Bu fonksiyon, bir kablosuz çerçeve (wireframe) çizgisi şeklinde verileri görselleştirir.

Örneğin, aşağıdaki kod bloğunda, `plot_wireframe()` fonksiyonu kullanılarak bir kürenin yüzeyi çizdirilir:


```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_wireframe(x, y, z, color="b")

plt.show()
```

<img src="https://i.vgy.me/mx88wW.png">

Bu örnekte, `np.outer()` fonksiyonu kullanarak, kürenin yüzeyine ait x, y ve z koordinatları hesaplanır ve `plot_wireframe()` fonksiyonu kullanılarak bu koordinatlar kullanılarak bir kablosuz çerçeve çizdirilir. Son olarak, `show()` fonksiyonu kullanılarak grafik ekrana çizdirilir.

Bu şekilde, mplot3d paketi ile 3 boyutlu grafikler oluşturabilirsiniz.

### Stil dosyaları

Matplotlib kütüphanesinde bir dokümanda düzenli bir şekilde renk ve görsel seçenekleri kullanmak için stiller kullanılmaktadır. Kütüphane içerisindeki stil dosyaları `plt.style.available` komutu ile gösterilebilir. Tercih edilen stil `plt.style.use()` komutu ile seçilebilir. Bir dokümanda çizilen grafiklerin renkleri, yazı fontları, font büyüklükleri, ızgara şekilleri gibi tasarım özelliklerinin benzer şekilde olması beklenir. 

Diğer stiller ile ilgili bilgi [şu adresten](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html) alınabilir.


```python
plt.style.available
```


```python
plt.style.use('seaborn')
```


![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_001.png)
![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_002.png)
![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_003.png)
![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_004.png)
![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_005.png)
![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_006.png)
![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_008.png)


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
plt.rcParams['lines.linewidth']=2.0 # tüm çizgiler bu çizgi genişliğine sahip olur
```

## Veri görselleştirmede ipuçları

Matplotlib'i veri görselleştirme için kullanmak, verilerinizdeki bilgileri ve desenleri etkili bir şekilde iletmek için güçlü bir araç olabilir. Ancak, herhangi bir araç gibi, en iyi sonucu elde etmek için doğru kullanmak önemlidir. Matplotlib kullanırken aklınızda bulundurmanız gereken bazı en iyi uygulamalar şunlardır:

1. Basit tutun: Grafiklerinizi fazla sayıda öğe veya gereksiz ayrıntı ile karmaşık hale getirmekten kaçının. Mesajınızı iletmeye yardımcı olan temel bilgilerle sınırlı kalın.
2. Doğru grafik türünü seçin: Farklı grafik türleri, farklı veri türleri ve mesajlar için daha uygun olabilir. Örneğin, bir çizgi grafiği zaman içindeki eğilimleri göstermek için daha iyidir, bir bar grafiği ise kategorileri karşılaştırmak için daha iyidir.
3. Renkleri etkili kullanın: Renk, önemli bilgileri vurgulamak için güçlü bir araç olabilir, ancak ölçülü kullanılmalıdır. Kolayca ayırt edilebilen renkler seçin ve çok fazla farklı renk kullanmaktan kaçının.
4. Eksenlerinizi etiketleyin: Eksenlerinizdeki birimleri ve ölçekleri net bir şekilde etiketleyin, böylece izleyicileriniz verileri anlayabilirler. 
5. Başlık ve açıklama ekleyin: Başlık ve açıklama, grafiğinizin ana mesajını açıklamanıza ve bağlam sağlamanıza yardımcı olabilir.
6. Bu en iyi uygulamaları aklınızda bulundurarak, veri görselleştirmelerinizin net, etkili ve anlaşılır olduğundan emin olabilirsiniz.

Ayrıca, veri görselleştirmede Matplotlib'i kullanırken performansı da göz önünde bulundurmak önemlidir. Büyük miktarda veri ile uğraşırken, çizim süresi ve bellek kullanımını dikkate almak önemlidir.

Performansı iyileştirmenin bir yolu, `matplotlib.pyplot.xlim()` ve `matplotlib.pyplot.ylim()` yöntemlerini kullanarak sırasıyla x ve y eksenlerinin sınırlarını belirlemektir. Bu, çizilecek veri miktarını azaltarak çizim performansını iyileştirebilir.

Başka bir yol, birden çok figür yerine tek bir figürde birden çok grafik oluşturmak için `matplotlib.pyplot.subplots()` işlevini kullanmaktır. Bu, bellek kullanımını azaltarak çizim performansını artırabilir.

Bu en iyi uygulamaları ve ipuçlarını takip ederek, Matplotlib kullanırken veri görselleştirmelerinizin hem etkili hem de verimli olmasını sağlayabilirsiniz.

### Doğru görselleştirme şeklini belirleme

Veriler için doğru görselleştirme şekli, verilerin türüne, boyutuna, özelliklerine ve anlatmak istediğiniz hikayeye bağlı olarak değişebilir. Bazı veriler, örneğin sayısal veriler, çizgi grafiği veya histogram gibi nicel grafiklerle daha iyi anlaşılabilirken, diğerleri, örneğin kategorik veriler, pasta grafikleri veya kutu grafikleri gibi nitel grafiklerle daha iyi anlaşılabilir.

Doğru görselleştirme şeklini belirlemek için aşağıdaki faktörleri dikkate alabilirsiniz:

- Verilerin tipi: Sayısal veriler, kategorik veriler, zaman serileri vb. farklı görselleştirme teknikleri gerektirir.
- Verilerin boyutu: Verileriniz ne kadar büyükse, daha karmaşık görselleştirme teknikleri gerektirebilirsiniz.
- Verilerin dağılımı: Verilerinizin dağılımı, verilerinizi nasıl görselleştireceğinizi etkileyebilir. Örneğin, normal dağılıma sahip veriler için histogram kullanmak doğru olabilirken, çarpık dağılıma sahip veriler için kutu grafikleri daha uygun olabilir.
- Mesajınız: Görselleştirmenin amacı nedir? Verilerinizde hangi mesajı vermek istiyorsunuz? Verilerinizin hikayesini en iyi anlatan görselleştirmeyi seçmelisiniz.

Doğru görselleştirme şeklini seçmek, verilerinizin en iyi şekilde anlaşılmasını sağlar ve hikayenizi en iyi şekilde anlatmanıza yardımcı olacaktır.

## Seaborn Kütüphanesi

Seaborn, Python'da veri görselleştirme için kullanılan bir kütüphanedir. Matplotlib kütüphanesi temelde kullanılan grafiklerin yanı sıra, Seaborn kütüphanesi daha özel ve daha karmaşık grafiklerin oluşturulmasına yardımcı olur.


### Seaborn ve Matplotlib

Seaborn ve Matplotlib, veri görselleştirme için Python dilinde kullanılan iki popüler kütüphanedir. Matplotlib, Python topluluğunun uzun süredir kullandığı bir kütüphanedir ve temel grafik türlerini çizmek için kullanılır. Seaborn ise Matplotlib'e dayanarak, daha karmaşık görselleştirme tekniklerine odaklanan daha yeni bir kütüphanedir.

- Seaborn, Matplotlib'in üzerine inşa edildiği için Matplotlib'i de kullanır. Ancak Seaborn, daha yüksek seviye araçlar sunar ve Matplotlib'den daha az kod yazmayı gerektirir. Örneğin, Seaborn ile daha karmaşık görselleştirmeleri yapmak daha kolaydır ve daha az ayarlama gerektirir. Seaborn, renkli grafikleri kolayca oluşturmak için önceden tanımlanmış renk paletleri de içerir.
- Matplotlib daha esnek bir yapıya sahiptir ve daha özelleştirilmiş grafikler oluşturmak için kullanılabilir. Matplotlib ile çok daha fazla özelleştirme yapılabilir ve her yönü tam olarak kontrol edilebilir.
- Seaborn, Matplotlib'in daha yüksek seviye araçlarına odaklanırken, Matplotlib daha özelleştirilmiş grafikler için daha fazla seçenek sunar. Seaborn ve Matplotlib birlikte kullanılabilir ve veri görselleştirme için güçlü bir kombinasyon sağlar.
- Seaborn, özellikle istatistiksel veri görselleştirmesi için tasarlanmıştır ve Matplotlib'den daha yüksek seviyeli bir arayüz sağlar. Buna ek olarak, Seaborn, renk paletleri, özel grafikler ve istatistiksel gösterimler için önceden tanımlanmış tema ve stiller gibi birçok özellik sunar.
- Seaborn ayrıca, regresyon analizi, faktör analizi ve kümeleme analizi gibi veri analizi tekniklerini de içeren birçok özel grafik fonksiyonuna sahiptir.


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

<img src="https://i.vgy.me/SSFwUV.png">


```python
sns.relplot(x='total_bill', y = 'tip', data = tips, hue = 'day') # günlere göre ayrı tipler
```

<img src="https://i.vgy.me/xdDnTP.png">


```python
sns.relplot(x='total_bill', y = 'tip', data = tips, hue = 'day', style='time') # zamana göre de ayrılmış
```

<img src="https://i.vgy.me/AsdjXN.png">


```python
sns.relplot(x='total_bill', y = 'tip', data = tips, hue = 'day', style='time', col = 'sex') # cinsiyet de eklendi
```

<img src="https://i.vgy.me/oc3Um8.png">

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

<img src="https://i.vgy.me/3H8Jqg.png">

Bu örnekte `catplot()` fonksiyonuna x, y ve hue parametreleri verilerek, x ekseninde günler, y ekseninde hesap miktarı, hue ile de cinsiyet bilgisi görselleştirilmiştir. Ayrıca kind parametresine bar değeri verilerek, çubuk grafiği çizdirilmiştir.

Tablo veya veri kümesinin özet istatistiklerini göstermek için kullanılan boxplot, Seaborn kütüphanesi içinde yer alan `boxplot()` fonksiyonu ile çizdirilebilir. Boxplot, verilerin çeyrekliklerini (çeyrekler arası yayılma), medyanı ve aykırı değerleri grafiksel olarak gösterir.

Örneğin, tips veri kümesindeki bahşiş miktarları ile boxplot çizdirelim:


```python
sns.boxplot(x='day', y='tip', data=tips)
plt.show()
```

<img src="https://i.vgy.me/2i30l3.png">


```python

```
