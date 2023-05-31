---
layout: post
title: Bibliyometrik Analiz
date: 2023-06-01
giscus_comments: true
permalink: 
tags:
  - bibliyometrik
  - akademik
  - literatür
  - bibliometrix
  - vosviewer
---

Bibliyometrik analiz, belirli bir alanda belirli bir dönemde ve belirli bir bölgede üretilen yayınların ve bu yayınlar arasındaki ilişkilerin sayısal olarak analiz edilmesini sağlayan bir yöntemdir. Bu analiz, bilimsel yayınların metrik verilerini kullanarak bilimsel araştırma alanlarını, yazarları, kurumları ve çalışmalar arasındaki ilişkileri anlamamızı sağlar. Bibliyometrik analiz, yayın veritabanlarından toplanan bibliyografik verileri kullanarak çeşitli analizler yapmayı içerir.

Yayınların toplanması aşamasında, araştırma konusuna uygun bir veritabanı seçilir. Örneğin, Web of Science, Scopus veya PubMed gibi popüler veritabanları tercih edilebilir. Bu anlatımda Web of Science (WoS) veritabanı üzerine odaklanacağız. Ancak öncelikle birkaç tanım ile başlayalım (https://cabim.ulakbim.gov.tr/bibliyometrik-analiz/bibliyometrik-analiz-sikca-sorulan-sorular/).

## Kavramlar

### Bibliyometri Nedir ?

Belirli bir alanda belirli bir dönemde ve belirli bir bölgede kişiler ya da kurumlar tarafından üretilmiş yayınların ve bu yayınlar arasındaki ilişkilerin sayısal olarak analizidir.

### Atıf Nedir ?

Bir yayın çalışmasında kendinden önceki başka bir yayın çalışmasına değinilmesine atıf denir.

### Atıf Oranı Nedir ?

Yazar, doküman ya da derginin belirli bir periyotta aldığı atıf sayısıdır.

### Etki Faktörü (Impact Factor =IF) Nedir ?

Bir dergide o yıl alınan atıfların, önceki iki yılda çıkan yayın sayısına bölümü ile elde edilen değere denir.

### Etki Ortalaması Nedir?

Atıf sayısının, yayın sayısına bölünerek elde edilen değere  denir.

### Atıf Ağı Nedir ?

Bir grup yazar, yayın, dergi ve konu arasındaki atıf ilişkisidir.

### Anındalık İndeksi (Immediacy Index) Nedir ve Nasıl Hesaplanır ?

Bir dergide o yıl alınan atıfların, aynı yıl dergide çıkan yayınlara bölünmesiyle elde edilinen  değere denir.

### H-Göstergesi “H-index” Nedir ?

Jorge E. Hirsch tarafından 2005 yılında her bilim insanının araştırma performansını değerlendirmek için önerdiği göstergedir. Yazar değerlendirmesinde kullanılmaktadır. Detaylı bilgi için **[Wikipedia](http://en.wikipedia.org/wiki/H-index)** linkine tıklayınız.

### Enformetri Nedir ?

Sadece belgeler ve bibliyografyalarla değil, her türlü formdaki bilginin sayısal durumunu inceler.

### Bilimetri (Scientometrics) Nedir ?

Bilim politikası oluşturma ve geliştirmeye yönelik araştırmalarda Bilimetrik çalışmalardan yararlanılmaktadır.

### Webometri Nedir ?

Webometri en basit ifadeyle enformetrik yöntemlerin World Wide Web’ e uygulanmasıdır.

### Web of Science (WoS) Veri Tabanı Nedir ?

Dünya çapında etki değeri (impact factor) yüksek bilimsel dergileri kapsayan, Clarivate Analytics firmasına ait çok disiplinli atıf indekslerinden oluşmaktadır.

### Journal Citation Report (JCR) Nedir ?

Dergilerin WOS Atıf İndekslerine bağlı Impact Factor (IF) değerlerini konu, yayıncı, ülke bilgilerini içeren veri tabanıdır.

### WOS’ da Hangi Türkiye Adresli Dergilerimiz Yer Almaktadır ?

WoS indeksinde yer alan Türkiye adresli dergilerin listesine **[buradan](https://cabim.ulakbim.gov.tr/bibliyometrik-analiz/thomson-reuters-web-of-science-wosda-indekslenen-turkiye-adresli-bilimsel-dergiler/)** erişebilirsiniz.

### SCOPUS Veri Tabanı Nedir?

Elsevier Yayınevi’ne ait çok disiplinli bibliyografik bir veri tabanıdır. 1996′ dan itibaren atıf analizleri de yapılabilmektedir.

## Bibliometrik Analiz Nedir?
Bibliyometrik analiz, bilimsel yayınlar üzerinde desenleri, eğilimleri ve ilişkileri analiz etmeyi amaçlayan bir yöntemdir. Bu analiz, yayınlanan makalelerin metrik verilerini kullanarak bilimsel araştırma alanlarını, yazarları, kurumları ve çalışmalar arasındaki ilişkileri anlamamızı sağlar. Bibliyometrik analiz, yayın veritabanlarından toplanan bibliyografik verileri kullanarak çeşitli analizler yapmayı içerir. Bu analizler arasında yayın sayıları, atıf analizleri, yazarlık ağları, anahtar kelime co-occurrence analizleri ve diğer görselleştirmeler yer alır. Bibliyometrik analiz, bilimsel araştırma performansının değerlendirilmesi, araştırma trendlerinin belirlenmesi ve araştırma alanları arasındaki işbirliklerinin anlaşılması gibi birçok alanda kullanılır.

## Arama Stratejisi

Arama stratejisi oluşturmak için anahtar kelimeleri kullanmanız gerekmektedir. Arama operatörleri kullanarak etkili bir arama stratejisi oluşturabilirsiniz. WoS veritabanında yaygın olarak kullanılan arama operatörleri şunlardır:

1. AND Operatörü: "AND" operatörü, iki veya daha fazla terimin birlikte geçtiği sonuçları bulmak için kullanılır. Örneğin, "climate change AND adaptation" sorgusu, hem "climate change" hem de "adaptation" terimlerini içeren makaleleri bulur.

2. OR Operatörü: "OR" operatörü, iki veya daha fazla terimden herhangi birinin geçtiği sonuçları bulmak için kullanılır. Örneğin, "renewable energy OR solar power" sorgusu, ya "renewable energy" ya da "solar power" terimlerini içeren makaleleri bulur.
3. NOT Operatörü: "NOT" operatörü, belirli bir terimi içeren sonuçları hariç tutmak için kullanılır. Örneğin, "cancer NOT breast" sorgusu, "cancer" terimini içeren ancak "breast" terimini içermeyen makaleleri bulur.
4. Parantez Kullanımı: Parantezler, arama sorgusunda belirli terimleri bir grup olarak tanımlamak için kullanılır ve operatörlerin önceliğini belirlemeye yardımcı olur. Örneğin, "(climate change OR global warming) AND adaptation" sorgusu, ya "climate change" ya da "global warming" terimlerini içeren ve aynı zamanda "adaptation" terimini içeren makaleleri bulur.
5. Tırnak İşaretleri: Tırnak işaretleri, terimlerin tam bir ifade olarak aranmasını sağlar. Örneğin, "renewable energy" sorgusu, tam olarak "renewable energy" terimini içeren makaleleri getirir.

Ayrıca arama yaparken kullanılan özel karakterler şu şekilde verilebilir:
1. "*" (yıldız işareti): sıfır veya daha fazla karakteri temsil eder, \*carbon\* hidrokarbon veya polikarbonat anlamına gelebilir.
2. $ (dolar işareti): sadece sıfır veya bir karakteri temsil eder, eight$ eight, eighth veya eighty anlamlarına gelebilir.
3.  ? (soru işareti): sadece bir karakteri temsil eder ve tekrar edebilir, wom?n woman veya women anlamlarına gelebilir.
4.  ! (Ünlem işareti): Sadece Web of Science'da kullanılabilen bir özel karakterdir. Sonuçların tersini almak için kullanılır. Örneğin, "renewable energy!" sorgusu, "renewable energy" terimini içermeyen sonuçları bulur.

## Yayınların Toplanması

Araştırma yapılacak konunun belirlenmesinin ardından hangi veritabanından yayın toplanacağına karar verilmelidir. Bu durumda genellikle Web of Science, Scopus, PubMed gibi popüler veritabanları tercih edilebilir. Buradaki anlatım WOS üzerine olacaktır.  

Web of Science'da bibliyometrik analiz yapmak için aşağıdaki adımları izleyebilirsiniz:

1. Araştırma konusuna uygun anahtar kelimeler belirleyin: Bibliyometrik analiz yapmak istediğiniz konuyu belirleyin ve o konuyla ilişkili anahtar kelimeleri tespit edin. Örneğin, "climate change" (iklim değişikliği), "renewable energy" (yenilenebilir enerji), "sustainable development" (sürdürülebilir kalkınma) gibi terimler.

2. Web of Science veritabanına erişin: Web of Science veritabanına erişiminiz olduğunu varsayıyorum. Web of Science'ı açın ve "Advanced Search" (Gelişmiş Arama) seçeneğini seçin.

3. Arama stratejisi oluşturun: Belirlediğiniz anahtar kelimeleri kullanarak etkili bir arama stratejisi oluşturun. Arama operatörlerini ve parantezleri doğru şekilde kullanmaya dikkat edin. Örneğin, "(climate change OR global warming) AND adaptation" sorgusuyla iklim değişikliği veya küresel ısınma terimlerini içeren ve aynı zamanda uyum terimini içeren makaleleri bulabilirsiniz.

4. Arama sonuçlarını filtreleyin: Arama sonuçlarınızı filtrelemek için çeşitli seçenekler kullanabilirsiniz. Örneğin, yayın tarihine, yayın türüne, dergi adına, yazarlara veya kurumlara göre filtreleme yapabilirsiniz. Bu filtreleme seçenekleri size istediğiniz analiz için daha spesifik veriler sağlayabilir.

5. Sonuçları indirin: İlgilendiğiniz makaleleri veya bibliyografik verileri indirebilirsiniz. Bu veriler, daha fazla analiz yapmak için kullanabileceğiniz metin dosyaları veya Excel tabloları şeklinde olabilir.

6. Analiz yapın: İndirdiğiniz verileri analiz etmek için istatistiksel veya veri analizi yazılımlarını kullanabilirsiniz. Örneğin, yayınların yıllara göre dağılımını, en çok atıf yapılan makaleleri, yazarların ve kurumların yayın performansını, dergi veya konferansların etkisini vb. analiz edebilirsiniz.

Bibliyometrik analiz yaparken, analiz yöntemlerini ve istatistiksel araçları kullanırken dikkatli olmak önemlidir. Ayrıca, veri kaynaklarını doğru bir şekilde yorumlamak ve analiz sonuçlarını genel bir bakış açısıyla değerlendirmek de önemlidir.

### Uygulama Adımları

Öncelikle kütüphane erişimi üzerinden giriş yapacağım.
[Veritabanı Erişim ve İstatistik Sistemi (subu.edu.tr)](https://ekutuphane.subu.edu.tr/vetisbt/)

bu sayfadan şifremi unuttum ile şifremi aldım. Ardından aşağıdaki gibi documents search ten advanced search seçeneğine tıkladım. 

[Advanced Search - Web of Science Core Collection (vetisonline.com)](https://a8f59890210bb2a36cc265c34c80a801c14e01d5.vetisonline.com/wos/woscc/advanced-search)

<img src="https://i.vgy.me/MUsMHX.png">

Anahtar kelimelerin oluşturulması ve stratejinin oluşturulması için anahtar kelimeleri kullanarak etkili bir arama stratejisi oluşturmak gerekiyor. 

Örneğin hava kalitesi tahmin çalışmalarını incelemek istiyorum. Bunun için bir liste oluşturuyorum. Önemli anahtar kelimeler neler? Hangi anahtar kelimeler birlikte kullanılacak, hangileri ayrı kullanılacak ya da hangi anahtar kelimelerden neler türetilebilir? gibi soruların yanıtlarını vererek bir liste yapılabilir. Önce üst başlıkları belirledim (Air quality, Air pollution, Methods). Ardından alt başlıkları ve alt başlıklardan türetilecek kelimeleri listeledim.
Air quality
- air quality prediction
	- Air quality evaluation, data-driven air quality evaluation, Predictive models, Atmospheric modeling
- Air outdoor prediction
- Air quality Index
Air pollution
- Air pollutants
- Particulate Matter
	- PM, PM2_5, PM 2 5, Particulate matter, PM10, PM1
- carbon monoxide
	- CO
- Nitrogen Oxides
- Ozone
	- O3
- Sulfur Dioxide
	- SO2
Methods
- Artificial neural network
- Regression
	- Linear Regression , Multivariate polynomial regression, Generalized regression neural, regularization
- Support vector machine
- Decision tree
- time series
- statistical analysis
- Fuzzy Logic
- Long-Short term memory unit
	- LSTM
- Gated Recurrent Unit
	- GRU
- recurrent neural network
	- RNN
- big data analytics
- autoencoder
Üst başlıklar birbirine AND ile bağlanacak, alt başlıklar ise OR ile bağlanacak. Bazı yerlerde özel karakterler kullanmak gerekiyor.
Yazılan arama kodu şu şekilde gerçekleşti.
```python
(TS=("*air quality*" OR "*air pollution*")) AND (TS=("machine learning" OR "deep learning" OR "artificial neural network")) AND (TS=("Air pollutant" OR "Particulate Matter" OR "carbon monoxide" OR "Nitrogen Oxides" OR "Ozone" OR "Sulfur Dioxide"))
```
Bu komutu gelişmiş aramaya yazarak ara diyorum.

<img src="https://i.vgy.me/Irif2K.png">

1,379 yayın bulundu. Yayınların bir yayın yılı, yayınlandığı yer gibi sınırlamalarını da yapıyorum. 2010dan öncekileri exclude ettim. Sadece article ları aldım. Topiclerde environmental science olanları tercih ettim. Böylece 978 adet makale kalmış oldu. Bu makaleleri bibtex dosyası olarak export ettim.

<img src="https://i.vgy.me/A7Nlrn.png">

All records seçeneği ile indirdiğim dosyayı air_quality_wos.bib olarak kaydettim.
Veri setini JabRef ile açtım. Quality >> Find Dublicates ile tekrar eden makaleleri arattım. Veri setinin temiz olduğundan emin olduktan sonra veri setini Vosviewer programına aktarabiliriz.