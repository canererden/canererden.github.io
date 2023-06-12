---
layout: post
title: Bibliyometrik Analiz Araçları
date: 2023-06-01
giscus_comments: true
permalink: 
tags:
  - bibliyometrik
  - akademik
  - literatür
  - tarama
  - kaynak bulma
  - bibliometrix
  - vosviewer
---

Konuya geçmeden önce bu blog yazısı ile birlikte hazırladığım videoya göz atmanızı öneririm.

---
**Bibliyometrik Analiz Nedir? Nasıl Kullanılır?**
<iframe width="560" height="315" src="https://www.youtube.com/embed/OXw2jo7_4HY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Bibliyometrik Analiz Araçlar VOSviewer ve Bibliometrix Kullanımı**
<iframe width="560" height="315" src="https://www.youtube.com/embed/7Y687ALw-lU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


---

# Bibliometrik Araçları
Bibliometrik analizi ve network gösterimleri için çeşitli araçlar geliştirilmiştir. Bu araçlar; veri kaynakları, çalışma ortamları açısından farklılıklar göstermektedir. Örneğin, popüler olan araçlardan VOSviewer Dimensions, PubMed, Scopus, WoS gibi veri kaynaklarından yayın alabilir ve Windows, Mac veya Linux ortamında çalışabilir. Ancak Bibliometrix uygulaması ise R tabanlı çalışır ve Cochrane, Dimensions, PubMed, Scopus, WoS veritabanlarından veri alır.
## Vosviewer
VOSviewer, bibliyometrik analiz için kullanılan bir görselleştirme aracıdır. VOSviewer'ı indirmek ve kurmak için aşağıdaki adımları takip edebilirsiniz:

1. VOSviewer'ı İndirme:
   - Tarayıcınızda "VOSviewer" kelimesiyle bir arama yapın.
   - İlk sırada çıkan "VOSviewer - Download" sayfasına gidin.
   - VOSviewer'ın resmi web sitesine erişeceksiniz: https://www.vosviewer.com/download
   - İndirmek istediğiniz işletim sistemine uygun olan sürümü seçin (Windows, macOS veya Linux).

2. VOSviewer'ı Kurma:
   - İndirilen kurulum dosyasını çalıştırın.
   - VOSviewer'ı kurmak için yönergeleri izleyin.
   - Kurulum işlemi tamamlandığında, VOSviewer başlatılabilir dosyası veya kısayolu masaüstünde veya başlat menüsünde görünecektir.

3. Java Kurulumu:
   - VOSviewer, Java Runtime Environment (JRE) yazılımını gerektirir. Eğer bilgisayarınızda JRE yüklü değilse, VOSviewer'ı kullanmadan önce Java'yı indirmeniz ve kurmanız gerekebilir.
   - Tarayıcınızda "Java indir" veya "Java Runtime Environment indir" gibi bir arama yaparak Java'nın resmi web sitesine gidin.
   - Java'nın indirme sayfasından işletim sisteminize uygun olan JRE sürümünü seçin ve indirin.
   - İndirilen kurulum dosyasını çalıştırarak Java'yı kurun.

Artık VOSviewer'ı indirmiş ve kurmuş olduk.
Bibliometrik analiz ile sorulacak sorular:
- Soru 1: İlgili alan için yayın ve alıntı eğilimleri nelerdir?
- Soru 2: İlgili alan üzerine yapılan çalışmalara en çok katkı sağlayan yazarlar, kurumlar ve ülkeler kimlerdir?
- Soru 3: İlgili alan araştırmalarında en çok alıntı yapılan makale ve dergiler hangileridir?
- Soru 4: İlgili alan çalışmalarında kullanılan anahtar kelimeler nelerdir?
- Soru 5: İlgili alan çalışmalarında ana temalar ve konular nelerdir?
- Soru 6: İlgili alanda gelecekte yapılacak araştırmalar için fırsatlar ve öneriler nelerdir? 

## Bibliometrix

Bibliometrix, Massimo Aria ve Corrado Cuccurullo tarafından geliştirilmiştir ve tüm ana bibliyometrik analiz yöntemlerini içeren scientometrics ve bibliyometrikte kantitatif araştırmalar için açık kaynaklı bir araçtır [makale]([bibliometrix: An R-tool for comprehensive science mapping analysis - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1751157717300500)). Bu paket, SCOPUS, Clarivate Analytics'in Web of Science, PubMed ve Cochrane veritabanlarından bibliyografik verileri içe aktarmak, bibliyometrik analiz yapmak ve ortak alıntı, birleştirme, bilimsel işbirliği analizi ve eş kelime analizi için veri matrisleri oluşturmak için çeşitli rutinler sağlar. Bu paket ile birlikte [Bibiloshiny](https://www.bibliometrix.org/home/index.php/layout/biblioshiny) paketi de bir arayüz olarak yüklenebilir.

**biblioshiny**: bibliometrix için bir web arayüzü sağlayan bir uygulamadır. Bibliometrix'in temel özelliklerinin kolay kullanımında akademisyenleri destekler:

- Veri içe aktarma ve veri çerçevesi koleksiyonuna dönüştürme
- Dimensions, PubMed ve Scopus API'leri koleksiyonunu kullanarak veri toplama
- Veri filtreleme

Dört farklı düzey metriği için Analitikler ve Grafikler:

- kaynaklar
- Yazarlar
- Belgeler
- Bağlantı ile Kümeleme

Üç Bilgi yapısının analizi:

- Kavramsal Yapı
- Entelektüel Yapı
- Sosyal Yapı

### Nasıl Kurulur?
Kurulum için [şuradaki](https://bibliometrix.org/biblioshiny/biblioshiny1.html) link takip edilebilir.

1. R'yi indirin ve yükleyin: [Kapsamlı R Arşiv Ağı'ndan](https://cran.r-project.org/bin/windows/base/) R'yi indirin. İndirilen dosyaya çift tıklayın ve kurun (varsayılanları kabul edin).
2. RStudio'yu İndirin ve Kurun: [RStudio Desktop](https://www.rstudio.com/products/rstudio/#rstudio-desktop)'ı indirin ve kurun. Open Source Edition veya RStudio Desktop Pro çalışacaktır.
3. Bibliometrix ve Shiny R Paketlerini Kurun: Windows'ta RStudio'yu arayın ve RStudio'yu açmak için çift tıklayın. Konsola (solda), aşağıdaki kodu kopyalayıp yapıştırın ve ardından enter tuşuna tıklayın:

```
install.packages("shiny")
install.packages("bibliometrix")
```

4. Web of Science'tan veri dışa aktarma: Literatür aramanızı Web of Science'ta (WoS) gerçekleştirin, "Dışa Aktar" düğmesini tıklayın ve "BibTex"i seçin. "Kayıtları BibTeX Dosyasına Aktar" ekranında, "Kayıt İçeriği:" etiketi altında, "Tam Kayıt ve Atıf Yapılan Referanslar"ı seçin. Ardından, 'Kayıt kaynağı' alanında ilk 500 kaydı seçin (500'den fazla kaydınız varsa veya tüm kayıtları indirmeyi seçin). 500'den fazla kaydınız varsa, toplamda WoS'taki tüm kayıtları içeren birden çok .bib dosyanız olana kadar işlemi tekrarlayın.
5. BibTeX dosyalarını birleştirin: WoS'tan birden çok .bib dosyasını dışa aktarmanız gerekiyorsa, tek bir .bib dosyanız olacak şekilde dosyaları birleştirmeniz gerekir. BibTeX dosyalarını birleştirmek için, en kolayının bir metin düzenleyicide (Notepad gibi) yeni bir dosya açmak ve bu dosyayı .bib dosya uzantısıyla bilgisayarınıza kaydetmek olduğunu düşünüyorum. Ardından, WoS'tan indirdiğiniz .bib dosyalarının her birini açın ve indirilen dosyaların her birinin içeriğini kopyalayıp oluşturduğunuz yeni .bib dosyasına yapıştırın. Burada yaptığımız şey, WoS'tan indirilen birden çok dosyadaki tüm verileri içeren tek bir dosya oluşturmaktır.
6. Bibliometrix'i bir uygulama olarak çalıştırın: Bibliyometrik analiz için Biblometrix'i açıp kullanmaya başlamak için, aşağıdakini kopyalayıp RStudio konsoluna yapıştırın ve ardından klavyenizdeki enter tuşuna tıklayın:
```
library(bibliometrix)
biblioshiny()
```
7. Bibliometrix yakında bir tarayıcı penceresinde yüklenecektir.

Not: Bibliometrix'i kullanmak istediğinizde, hemen yukarıdaki kodu kopyalayıp RStudio konsoluna yapıştırmanız yeterli olacaktır, yani Bibliometrix'i her kullandığınızda yukarıdaki 1,2 ve 3. adımları gerçekleştirmeniz gerekmeyecektir.

8. BibTeX dosyanızı yükleyin: Bibliometrix'te 'Veri'yi ve ardından 'Verileri Yükle'yi tıklayın. "Lütfen, ne yapılacağını seçin" etiketinin altında "Ham dosyaları içe aktar" öğesini seçin ve "Veritabanı" etiketinin altında "Web of Science (WoS/WoK)" öğesini seçin. Gözat'ı tıklayarak .bib dosyanızı seçin ve ardından "BAŞLAT" düğmesini tıklayın. Artık bibliyometrik analiziniz için Bibliometrix'i kullanmaya hazırsınız.

9. Bibliyometrik analizler gerçekleştirin: Verileri analiz etmek amacıyla Bibliometrix'i kullanmak için ekranın solunda gerçekleştirmek istediğiniz kapsayıcı analiz türlerini seçin, örneğin 'Kaynaklar' ve ardından 'En İlgili Kaynaklar' gibi alt menü öğesini seçin. Ekranın sağ tarafından tercih ettiğiniz seçenekleri seçin ve ardından "Çalıştır" düğmesini tıklayın. Artık sonuçları görecek ve sonuçların bir görüntüsünü ve sonuçları içeren bir tabloyu dışa aktarabileceksiniz.