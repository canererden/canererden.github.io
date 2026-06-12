Title: Zaman Serisi Tahminleri ve ARIMA Modelleri

URL Source: https://cerden.medium.com/zaman-serisi-tahminleri-ve-arima-modelleri-d7398d63f346

Published Time: 2023-02-15T09:06:01Z

Markdown Content:
[![Image 1: Caner Erden](https://miro.medium.com/v2/resize:fill:32:32/1*MubH1N9K7NIi_FijP1nMzw.jpeg)](https://cerden.medium.com/?source=post_page---byline--d7398d63f346---------------------------------------)

7 min read

Feb 15, 2023

Bu yazıda zaman serisi analizlerinde kullanılan tahmin çalışmalarından ve ARIMA modellerinden bahsedilecektir. Minitab üzerinde bir zaman serisi analizi uygulaması gerçekleştirilecektir.

## Kavramlar

Zaman serisi analizlerinde amaç olarak geçmiş veriler ile şimdiki veriler arasındaki ilişkiler anlaşılarak gelecekteki veriler tahmin edilmeye çalışılır. Yapılacak iyi tahminler sayesinde gelecekle ilgili yapılan hedefler, planlar daha tutarlı hale gelebilir. Ya da bir olay hakkında karar vermek için zaman serisi tahminlerine ihtiyaç duyabiliriz. Zaman serisi analizlerinde önemli kavramlardan bazıları şunlardır.

**Durağanlık(Stationary):** Durağan serinin ortalaması sabit bir değer civarındadır ve varyansı çok değişken değildir. Yani herhangi andaki değerlerin ortalamaları birbirlerine hemen hemen eşittir. Durağan olmayan seriyi durağan hale getirmek için genellikle serideki değerlerin geçmişteki değerleriyle farkı alınır.

**Düzleştirme (smoothing):** Serinin dalgalanma olan kısımlarını düzleştirmek demektir. Düzleştirme daha iyi modellemeler yapabilmemizi sağlar. Düzleştirmeye örnek olarak hareketli ortalamalar ya da üstel düzleştirme verilebilir.

**Fark Alma(Differences)**: Serinin değerlerini önceki değerlerden çıkartılarak gerçekleştirilir. Derecesi d ile gösterilir. Örneğin d=1 ise serideki değerler bir önceki değerlerden çıkartılarak işlem gerçekleştirilir.

**Ayrıştırma(Decomposition):** Seriyi trend ve mevsimsellik etkilerine ayırma işlemi.

## Durağanlık

Durağanlık zaman serisi analizlerinde önemli bir yer tutar. Çünkü durağanlık durumuna göre yapılan analizler de farklılık gösterir. Örneğin eğer seride bir trend varsa durağanlık ortadan kalkabilir ve kurulan regresyon modelinde yüksek bir doğruluk değeri çıkabilir. Ancak bu değer sahte bir değerdir çünkü trendden kaynaklanan bir ilişki göz ardı edilmiş olabilir. Yani kurulan model ilişkiyi iyi yansıtmamış olur. Bu nedenle serinin durağan hale getirilmesi gereklidir. Durağan olmayan serilerin de analizleri yapılabilir. Durağan olmayan seriler şimdiki ve gelecekteki değerlerin geçmiş değerlerden çok farklı olduğu durumdur. Yani tamamen bir rassallık söz konusudur. Biz bu yazıda sadece durağan zaman serilerinde gerçekleştirilecek olan analizlerden ve tahminlerden bahsedeceğiz. Durağan olmayan seriler ile ilgilenmeyeceğiz.

![Image 2](https://miro.medium.com/v2/resize:fit:584/0*uapXjRKsSFiDkrjU.png)

Şekilde 3 tip zaman serisi ortalama ve varyans değerlendirmesi var. Birinci grafikte ortalamaların belirli bir çerçeve içerisinde hareket etmiş. Burada hem ortalama hem de varyanslar durağan şekildedir. Ancak ortadaki grafikte ortalamanın değişken hareketler sergilemiş. Diğer grafikte de ortalama ve varyans ikisi birlikte durağan bir yapıda değil. Durağanlığın grafikler üzerinden görülebileceği gibi bazı testler ile de testi mümkündür. Örneğin Dickey-Fuller Testi durağanlığın test edilmesi için geliştirilmiştir. Ya da otokorelasyon fonksiyonu grafikleri de çizilerek durağanlık veya durağan olmayan yapı görülebilir. Durağanlık konusuna tahmin modellerinde tekrar geleceğiz. Tanımları kısaca gördükten sonra bir zaman serisi üzerinde bu tanımları ve zaman serisi analizlerini birlikte görelim.

Uygulama için kullanılacak olan veri setini [şu adresten](https://drive.google.com/a/sakarya.edu.tr/file/d/1GkuXTBnNoS3SMZkTLHxRC9Ebxq4VmR-Q/view?usp=sharing) indirebirip Minitab ile açabilirsiniz. Stat>>Time Series>>Plot ile grafiğini çizelim.

Press enter or click to view image in full size

![Image 3](https://miro.medium.com/v2/resize:fit:700/0*dZ-zABUF_fE5e9OL.png)

Zaman serisindeki aylık verileri görmek istersek Minitab’de

1. Yeni bir sütun açılır. Calc >> Make Pattern Data ile ay sayıları oluşturulur.

2. Data >> Unstack Column ile veriler aylık olarak yeni bir sayfada gösterilir.

![Image 4](https://miro.medium.com/v2/resize:fit:447/0*fvyZ6GxPOYxgVm5U.png)

Aylık sayıların olduğu tabloda yeni bir sütunda aylık toplam yolcu sayıları gösterilebilir. Toplam sayılar için Calc >> Row Statistics menüsü kullanılabilir.

Zaman serisi grafiğinden senelik grafik çizilebilir.

Press enter or click to view image in full size

![Image 5](https://miro.medium.com/v2/resize:fit:700/0*ITdbql989azYTX0n)

## Ayrıştırma

Şimdi zaman serisi tahminleri için birkaç notasyon gösterelim. Y değerleri t zamanında değişkenin aldığı değeri göstersin. Y ile gösteriyoruz çünkü bu değerler zamana bağımlı değerler. T zamanları 1,2,3..n diye devam eden bir seri olsun.

Öncelikle eğer serimizde trend ve mevsimsellik varsa biz bunları toplayarak bir model ortaya koyabiliriz.

![Image 6](https://miro.medium.com/v2/resize:fit:156/0*QTKnZ3VmWCqwbcZ4.png)

Bu model eklemeli ya da toplamsal model olarak geçer ve trend ile mevsimsellik etkisi modele toplama işlemi ile eklenmiştir. Bir diğer model de ise çarpımsal model olarak geçen trend ve mevsimsellik etkisinin birbirleri ile çarpıldığı model söz konusudur.

![Image 7](https://miro.medium.com/v2/resize:fit:152/0*ovV10a6Wp0PNA4PC.png)

Burada trend ve mevsimsellik etkisi birbiriyle çarpılır. Bu model eğer mevsimsellik ve trend etkisi birlikte artma eğiliminde ise kullanılır. Ayrıştırma işlemi ile zaman serisi işte buradaki trend ve mevsimsellik etkilerinden arındırılabilir. Ya da varsa döngüsellik veya düzensizlik etkileri de modele eklenebilir. Biz ayrıştırma işlemini işte bu bileşenleri ortaya çıkarmak daha görülebilir hale getirmek için yapıyoruz. Oldukça sezgisel bir yöntem ve teorisi çok sağlam değil. Yani araştırmacının yorumlarına açık bir yöntem. Toplamsal ya da çarpımsal modellerden hangisinin kullanılacağı iki modelden hangisi daha iyi bir hata oranı verdiğine bağlıdır.

## Minitab’de Ayrıştırma

Minitab’de mevsimsellik ve trend etkisinin bulunması için Time Series >> Decomposition menüsü kullanılır.

Press enter or click to view image in full size

![Image 8](https://miro.medium.com/v2/resize:fit:700/0*sTFTT9TbfzBbasM1)

Aşağıdaki grafikten 7.ve 8. Aydaki yolcu sayısının diğer aylara göre daha fazla olduğu görülebilir.

![Image 9](https://miro.medium.com/v2/resize:fit:576/0*eeNblIsCPs8FEeWs.png)

## Düzleştirme(Smoothing) — Hareketli Ortalamalar

Aylık bir veri ile çalışıyorsak 12li hareketli ortalama almak isteyebiliriz. Bu durumda MA(12) ile çalışırız.

![Image 10](https://miro.medium.com/v2/resize:fit:180/0*muhww0I1mnbZJ76D.png)

formülü ile 7. aya ait hareketli ortalamayı bulabiliriz. Minitab’de Stat>>Time Series >> Moving Average

Press enter or click to view image in full size

![Image 11](https://miro.medium.com/v2/resize:fit:700/0*q1535AMxGQcJVeHH.png)

Kırmızı kısımda hareketli ortalamaları gösterilmiştir. Veriler daha düz bir hale geldi. Mevsimsellikten arındı.

![Image 12](https://miro.medium.com/v2/resize:fit:576/0*QC5U4O0u6o36LVK7.png)

## Excel’de Hareketli Ortalamalar

Excel’e yolcu sayılarını yapıştırdıktan sonra 7. Aya gelerek aşağıdaki formülü yazarız ve aşağıya çekerek tüm değerlerin hareketli ortalamasını bulmuş oluruz.

=TOPLA(A2/2;A3:A13;A14/2)/12

![Image 13](https://miro.medium.com/v2/resize:fit:496/0*-ew146NLErQKtxX3.png)

## Üstel Düzleştirme

Önceki verilere daha az yeni verilere daha fazla ağırlık vererek şimdiki değeri hesaplama yöntemi.

## Get Caner Erden’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

Aşağıdaki formüldeki gibi düzleştirme yapar. Burada α_t o zamanki üssel hareketli ortalamanın değeridir. α_t değeri düzleşmenin miktarını belirler. Eğer α 1’e eşit olursa x üzerinde hiç düzleştirme olmaz. Eğer 0 olursa bu kez X değerini çok az kullanmış oluruz. α değerini Minitab’e bırakmak en doğrusu olabilir.

![Image 14](https://miro.medium.com/v2/resize:fit:229/0*IN6UkCclyJCGgVpF.png)

## Holt-Winters Üstel Düzleştirme Yöntemi

Başka bir üssel düzleştirme yöntemidir. Buradaki fark mevsimsellik etkisi de göz önüne alınarak bir düzleştirme işlemi yapmasıdır.

Press enter or click to view image in full size

![Image 15](https://miro.medium.com/v2/resize:fit:700/0*buUhymyFWX8ajc-C)

## Fark Alma

Durağan olmayan bir seriyi durağanlaştırmak için yapılır. Eğer serideki değerleri 1 önceki değerlerden çıkartarak yeni bir seri oluşturmak istersek bu menüyü kullanabiliriz.

![Image 16](https://miro.medium.com/v2/resize:fit:338/0*3i09sqE1X2OnSD57.png)

## Otokorelasyon

Otokorelasyon aynı değişkenin kendi değerleri arasındaki korelasyon için kullanılır. Denklemi aşağıda verilmiştir.

![Image 17](https://miro.medium.com/v2/resize:fit:215/0*1NRpjlA6ek7aStlm.png)

![Image 18](https://miro.medium.com/v2/resize:fit:308/0*P9wBBDdB_vTlqMUX.png)

## Korelogram (ACF)

**Korelogram (Auto-correlation function(ACF)):**Serinin otokorelasyon katsayısı ile gecikme değerleri arasındaki ilişkiyi verir. Serinin durağanlığı ve alınması gereken p değerinin bulunmasında kullanılabilir. Eğer grafikte sınır değerlerinin üzerinde değerler varsa seri durağan değildir. Fark alınarak seri durağan hale getirilir.

**Partial auto-correlation function(PACF):**Kısmi otokorelasyon fonksiyonu 2 gecikme arasındaki gecikmeleri verir diğer gecikmeler kısmi korelasyonda önemli değildir.

## Korelogram Okuması

![Image 19](https://miro.medium.com/v2/resize:fit:586/0*8j3EwW9zKE6cipoX.png)

## ACF ve PACF grafikleri

Şimdi yolcu sayıları serisindeki ACF ve PACF grafiklerine bakalım.

Press enter or click to view image in full size

![Image 20](https://miro.medium.com/v2/resize:fit:700/0*jd52gMO7D3rMwBje.png)

Azalma yavaş yavaş gerçekleşmiş. Serinin durağanlaştırılması gerekir. Bir kez fark alınıp tekrar incelenmesi gerekir.

## 1 Derece Fark Alma

Minitab’de 1 derece fark aldıktan sonra grafikler tekrar incelenir. Şimdi serinin durağan hale geldiğini söyleyebiliriz. Korelogram okumasından hatırlanacağı gibi ACF ve PACF grafiklerinden çıkan sonuç seride yüksek otokorelasyon olduğu yönündedir.

Press enter or click to view image in full size

![Image 21](https://miro.medium.com/v2/resize:fit:700/0*JfFkV4871pLgHtNW)

## ARIMA Modelleri

Tek değişkenli zaman serisi analizi ve tahmini yapmaya yarayan bir yöntemdir. AutoRegressive Integrated Moving Average ifadesinin kısaltmasıdır. ARIMA modelinde zaman serisindeki değerler geçmiş değerleri üzerinden modellenir ve tahmin gerçekleştirilir. İlk olarak Box ve Jenkins tarafından bulunmuş ve Box-Jenkins modelleri olarak da bilinmektedir.

Mevsimsel olmayan Box-Jenkins Modelleri ARIMA(p,d,q)

p: otoregresyon modelinin derecesi,

d: fark alma işlemi,

q: hareketli ortalama modelinin derecesi

## ARIMA Aşamaları

![Image 22](https://miro.medium.com/v2/resize:fit:579/0*KJZrW8L_21Th-7dq.png)

## P,d,q değerlerinin belirlenmesi

Durağan olan ya da durağan hale dönüştürülen serinin ACF ve PACF grafiklerine göre uygun olan model belirlenir.

*   ACF grafiğindeki ilişki miktarları gecikme sayısı arttıkça yavaş yavaş azalıyor ama PACF grafiğindeki bu azalma hızlı bir şekilde oluyorsa **AR** modeli
*   PACF grafiğindeki ilişki miktarı yavaş yavaş azalırken ACF grafiğindeki ilişki miktarı hızlı bir şekilde azalıyorsa hareketli ortalama **MA** modeli
*   Hem ACF hem de PACF grafiklerinde ilişki miktarının azalışı yavaş yavaş olursa otoregresif hareketli ortalama **ARMA** modeli kurulmalıdır.

![Image 23](https://miro.medium.com/v2/resize:fit:303/0*TO21y17LoXUalCsU.png)

## ARIMA Tahmin Sonuçları

P,d,q değerleri belirlendikten sonra modelin tahmin aşamasına geçilir. Bunun için Stat>>Time Series>>ARIMA seçeneği seçilir.

AR(1)’in p-değeri 0,05’ten küçük çıkmış yani AR modeli anlamlıdır. Sabit değer ise 0,05’ten büyük çıktığı için anlamsızdır modelden çıkarılmalıdır.

![Image 24](https://miro.medium.com/v2/resize:fit:465/0*nCrG8VWdxlWfKkCl.png)

## Modelin Uygunluğu

Ortalama Karesel Hatalar(MS) modelin performans ölçüsü olarak kullanılır. Düşük MS değeri daha iyidir. Diğer ARIMA modelleri de uygulanarak MS değerleri karşılaştırılabilir.

![Image 25](https://miro.medium.com/v2/resize:fit:544/0*6EpROfAwYtb9VrGW.png)

## Tahmin Değerleri

Tahmin değerlerini göstermek istediğimiz uzunluğu Forecasts menüsünden ayarlayabiliriz. Lead time değeri kaç aylık ileriyi tahmin etmek istediğimizin değeridir. Bu değeri bir sütuna kaydedip yorumlayabiliriz.

![Image 26](https://miro.medium.com/v2/resize:fit:544/0*jHsvOeR_8mghwLKc.png)

## Ders Videosu

[https://www.youtube.com/watch?v=cVNHdrzRNoA](https://www.youtube.com/watch?v=cVNHdrzRNoA)

## Kaynaklar

*   Cintas, Pedro Grima, Lluis Marco-Almagro, ve Javier Tort-Martorell Llabres. _Industrial statistics with Minitab_. Wiley Online Library, 2012.
*   Erhardt, Erik B., Edward J. Bedrick, ve Ronald M. Schrader. “Advanced Data Analysis-Lecture Notes”, 2016.
*   Karagöz, Murat. _İstatistik Yöntemleri_. 9. bs. Ekin Kitabevi Yayınları, 2015.
*   Khan, Rehman M. _Problem solving and data analysis using minitab: A clear and easy guide to six sigma methodology_. John Wiley & Sons, 2013.
*   Lesik, Sally A. _Applied statistical inference with MINITAB®_. CRC Press, 2018.
*   Newton, Isaac. _Minitab cookbook_. Packt Publishing Ltd, 2014.
*   “Support | Minitab”. Erişim 29 Mart 2020. [https://www.minitab.com/en-us/support/](https://www.minitab.com/en-us/support/).
