---
layout: post
title: "Dengeli Ulaştırma Problemini Çözümü"
date: 2021-12-29
giscus_comments: true
permalink: /2021/12/29/dengeli-ulastirma-problemini-cozumu
tags:
  - blog
description: "Ulaştırma problemleri belirli sayıdaki kaynak noktasından belirli sayıdaki hedef noktasına en uygun maliyetle taşımanın nasıl yapılması gerektiği ile ..."
---

Ulaştırma problemleri belirli sayıdaki kaynak noktasından belirli sayıdaki hedef noktasına en uygun maliyetle taşımanın nasıl yapılması gerektiği ile ilgili problemlerdir. Ulaştırma problemleri doğrusal programlama problemleri içerisinde ele alınır. Kendine özgü bir yapısı olduğu için ulaştırma problemlerini doğrusal programlama problemleri için kullanılan Simplex algoritması ile çözmek yerine daha pratik çözümler geliştirilmiştir. Bu çözümler iki aşamalıdır. Birinci aşamada olurlu bir başlangıç çözüm bulunur. Başlangıç çözümü için kuzeybatı köşe yöntemi, en küçük maliyetler yöntemi ve Vogel yaklaşım metodu yöntemi kullanılabilir. Başlangıç çözümü bulunan problem için en uygun çözüm atlama taşı yöntemi ile en uygun çözüm bulunabilir.

Bu yazıda örnek bir ulaştırma problemi ele alınacak ve başlangıç çözüm için Vogel yaklaşım yöntemi, en uygun çözüm için de atlama taşı yöntemi kullanılacaktır.

## 1.1. Örnek Problem

Ele alınan problemin 3 kaynağı ve 4 hedef noktası bulunmaktadır. Kaynak ve hedef noktaları arasındaki maliyetler ile arz ve talep miktarları maliyetler tablosunda verilmiştir.


![Image 2](https://miro.medium.com/v2/resize:fit:700/1*INNGZzWRYowC65qE6tVskQ.png)

Bu bilgilere göre problemin Vogel Yaklaşım Yöntemini kullanarak başlangıç çözümünü ve atlama taşı yöntemini kullanarak da en iyi çözümünü bulunuz.

## Çözüm

Ulaştırma problemlerini çözümüne başlamadan önce problemin dengeli olup olmamasına bakılmalıdır. Dengeli ulaştırma problemlerinde toplam arz toplam talebe eşittir. Örnek problemde arz ve talep toplamları eşit olduğu için problem dengededir denilir.


![Image 3](https://miro.medium.com/v2/resize:fit:700/1*v5e12R7t7ooL4bVmLLcQwQ.png)

VAM yöntemine göre başlangıç çözümünün belirlenmesi işleminde öncelikle tüm satır ve sütunların farkları alınır.


![Image 4](https://miro.medium.com/v2/resize:fit:700/1*GmoIYGxLcuygoNbUnBZY5A.png)

Alınan farklardan en yüksek olan maliyete atama yapılacağı belirtilir.


![Image 5](https://miro.medium.com/v2/resize:fit:700/1*UUWU44-snThJm7kCbN8bqA.png)

Örnekte en yüksek maliyet 2. Satırda çıkmıştır. 2. Satırdaki maliyetler 650, 800, 400 ve 600 arasındaki en düşük maliyetli hücre seçilir. Bu hücre 400 maliyeti olan hücredir. Bu hücreye yapılabilecek maksimum atama yani arz ve talepteki minimum değer kadar atama yapılır. Bu nedenle 10 birimlik atama buraya yapılır.


![Image 6](https://miro.medium.com/v2/resize:fit:700/1*WPCBC7zz3UviOPXiHl3z0A.png)

Bu atama ile üçüncü sütundaki hücreler kaldırılır. İlgili talep ve arz miktarları güncellenir.


![Image 7](https://miro.medium.com/v2/resize:fit:700/1*jKyH-znAEnE-L7PbtOuFTw.png)

Tekrar satır sütun farklarına bakılır.


![Image 8](https://miro.medium.com/v2/resize:fit:700/1*jMnj1r9r3mx5NUbBZC-zEg.png)

En yüksek 3. Satırda çıktığı için 3. Satırın minimum hücresine yapılabilecek maksimum atama yapılır. Arz ve talep değerleri güncellenir.

Yeni durumdaki satır ve sütun farkları aşağıdaki gibi gelir.


![Image 9](https://miro.medium.com/v2/resize:fit:700/1*q0VU-_jB3acmB02tKdqTow.png)

Yeni farklara göre birinci satır seçilir. Buradaki 450 maliyetli hücreye 10 birimlik atama yapılır. Bundan sonraki atamalar sadece 2. Sütunda olacaktır. Bu nedenle en düşük maliyetli hücreye bakmadan geri kalan arz ve talepler dağıtılır.

VAM yöntemine göre başlangıç çözümü bulunmuş oldu. Çözümün geçerli olduğunun tespiti için atama miktarının satır sayısı + sütun sayısı -1 adet olduğu kontrol edilir. Buradaki atama sayısı 6 olduğu için çözüm geçerlidir denilir. Şimdi en iyi çözüm için atlama taşı yöntemine geçilir. Başlangıç çözüm tablosunu temizledikten sonra boş kalan hücreler için maliyetler hesaplanır. Eğer maliyetlerden negatif çıkan olursa buraya atama yapılır. Önce birinci satır birinci sütundaki hücreden başlanır. Hücreden atamaların olduğu hücreler köşe olacak şekilde kapalı bir döngü oluşturulur.




Birinci hücrenin maliyeti;


![Image 10](https://miro.medium.com/v2/resize:fit:700/1*pL4YM7nFE1qCb8jDEA2mug.png)

İkinci hücrenin maliyeti;


![Image 11](https://miro.medium.com/v2/resize:fit:700/1*AfOZ1wTKdArSfbDymowQqw.png)

Üçüncü ve diğer hücreler;


![Image 12](https://miro.medium.com/v2/resize:fit:675/1*RJgN85g7QW654LHoKyfzqg.png)

Sadece d13 negatif çıktığı için bu hücreye atama yapılmalıdır denilir. Eğer birden fazla negatif maliyetli hücre çıksaydı bunlar arasından mutlak değerce yüksek olan alınırdı. Tüm maliyetlerin negatif olmayan değerler çıkması durumunda en iyi çözüme ulaşılmıştır denilirdi. Birinci satır 3. Sütun hücresine atama yapılacaktır. Atama miktarı döngüdeki negatif işaretli hücreler arasından tercih edilir. Negatif 2 ve 10 olduğu için minimum olan 2 tercih edilir. 2 değeri negatif hücrelerden çıkarılır pozitif hücrelere eklenir.


![Image 13](https://miro.medium.com/v2/resize:fit:700/1*3xLCZ-N4b8euo5dkomYy6g.png)


![Image 14](https://miro.medium.com/v2/resize:fit:700/1*-k1yeAW3VYojwJW83PGZBw.png)

Yeni atamalara göre yeniden boşta kalan hücreler arasında maliyet hesabı yapılır. Bu hesaplara göre yeni maliyetler arasında negatif hücre olmadığı için sonuç optimumdur denilir.

![Image 15](https://miro.medium.com/v2/resize:fit:698/1*C8-EOZJxCNnkraAJRswGlg.png)

Toplam maliyet = 2*(300)+10*(450)+9*(800)+8*(400)+10*(400)+1*(700) = 20200

## 1.2. Excel Solver Çözümü

Maliyetler girilir

![Image 16](https://miro.medium.com/v2/resize:fit:622/1*B_mZcuLIWDiDjiMrrgLBog.png)

Karar değişkenlerinin yeri belirlenir.


![Image 17](https://miro.medium.com/v2/resize:fit:700/1*5wtF-CotZqDx6rQMlmf1Kg.png)

Toplam atamalar formülde gösterilir.


![Image 18](https://miro.medium.com/v2/resize:fit:700/1*fAHkuX-V50UnQe3dO-6Cuw.png)

Toplam maliyet formülü yazılır.


![Image 19](https://miro.medium.com/v2/resize:fit:700/1*MFgCBMD7c_RU1eM56CRGPw.png)

Excel solver açılır.


![Image 20](https://miro.medium.com/v2/resize:fit:700/1*6auF_Nrzu9fDeQ1Ou9ZoXw.png)


![Image 21](https://miro.medium.com/v2/resize:fit:700/1*KkqGmTl8G-wMnVGjNVChnw.png)

Toplam maliyet 20200 TL olarak bulunur.