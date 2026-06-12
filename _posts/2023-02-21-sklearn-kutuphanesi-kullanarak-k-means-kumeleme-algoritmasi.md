---
layout: post
title: "Sklearn Kütüphanesi Kullanarak K-Means Kümeleme Algoritması"
date: 2023-02-21
giscus_comments: true
permalink: /2023/02/21/sklearn-kutuphanesi-kullanarak-k-means-kumeleme-algoritmasi
redirect_from: /sklearn-kutuphanesi-kullanarak-k-means-kumeleme-algoritmasi/
tags:
  - blog
description: "Makine öğrenmesindeki öğrenmeler gözetimli, gözetimsiz ve takviyeli öğrenme olarak ayrılabilir. Gözetimli öğrenmede sınıflandırma ve regresyon çalışma..."
---

Makine öğrenmesindeki öğrenmeler gözetimli, gözetimsiz ve takviyeli öğrenme olarak ayrılabilir. Gözetimli öğrenmede sınıflandırma ve regresyon çalışmaları yer alır ve hedef değerleri algoritmaya verilerek makine öğrenmesi sağlanır. Gözetimsiz öğrenmede ise en sık çalışılan konu kümeleme çalışmasıdır. Gözetimsiz öğrenmede ayrıca özellik çıkarımı (Feature Extraction), birincil etken analizi (Principle Component Analysis), ya da aykırı veri analizi (Outlier Analysis) gibi çalışmalar bulunur. Bu yazıda gözetimsiz öğrenmedeki kümeleme çalışmalarına örnek olarak K-Means algoritması ve uygulaması gösterilecektir.

## Gözetimli ve Gözetimsiz Öğrenme


![Image 2](https://miro.medium.com/v2/resize:fit:700/0*ES7ZzePmGKB1roQD.png)

Sınıflandırma grafiğinde kırmızı ve daire şeklinde noktalar görülebilir. Başlangıçta bu noktaların sınıfları ya da renkleri ve şekilleri makineye veriliyor. Ardından makinenin bunları öğrenmesi ve yeni gelecek verileri bu öğrenmeye göre sınıflandırması isteniyor. Sınıflandırma çalışmasında sınıfları birbirinden ayıracak en uygun çizgi belirlenmeye çalışılır. Bu çizgiyi çizdikten sonra veri setini ne kadar iyi sınıflandırdığımız daha sonra eğitim ve test setleri üzerinden hesaplanır. Diğer grafikte sadece kırmızı ve daire şeklinde noktalar olduğu görülür. Bu veri setinde gruplar oluşturulmak istenirse kümeleme algoritmalarını kullanılabilir. Kümeleme algoritmaları veri setindeki benzer yapıda bulunan verileri bir araya getirerek gruplar oluşturmaya çalışır. Veriler arasındaki Öklid uzaklığa, Minkowski uzaklığa, Manhattan uzaklığa bakarak verilerin ne kadar benzediğini/benzemediğini hesaplamaya çalışır.

## Kümeleme Analizinde Sorulacak Sorular

Kısaca kümeleme algoritmasında şu sorular başlangıçta sorulur.

*   Gruplama denklemi olarak hangi verilerin ne kadar benzediğine nasıl karar vereceğiz?
*   Kümeleme sonucu ne kadar doğru, ne kadar hızlı verimli?
*   Veri içerisinde ne kadar küme olacağını düşüneceğiz?

## Kümeleme Algoritmalarının Örnek Uygulama Alanları

*   Benzer özellikteki müşterilerin belirlenerek reklam kampanyalarının müşteri özelliklerine göre ayrı belirlemek
*   İnternetteki benzer dokümanları gruplamak (Benzerlik raporları gibi)
*   Benzer özellikteki protein dizilimlerinin ortaya çıkarılması (COVID19 hangi virüsün protein dizisine benziyor gibi)
*   Benzer özellikteki şarkıları bir araya getirerek bir kategorizasyon yapmak

## K-Means Kümeleme Algoritması

K-means kümelemede en çok kullanılan algoritmadır. Verinin kesin bir şekilde hangi kümeye ait olduğunu söyler. Yani bulanık ya da kaba küme olduğunu belirtmez. K-means algoritması önce veriyi k adet kümeye böler. Kümelerin orta noktalarını(centroid) bulur. Her bir veriyi bölünen kümelerden verinin en yakın olduğu kümesine atar. Burada hangi uzaklık ölçüsü kullanılacaksa ona göre bir hesaplama gerçekleştirilir. K-means algoritması bulunan kümedeki orta noktanın diğer orta noktalardan olabildiğince uzak olmasını bir kümenin içerisindeki verilerin ise olabildiğince yakın olmasını amaçlar. Aşağıda akış şeması verilmiştir.

K nokta sayısı kadar orta nokta belirle

Tekrarla

Her bir noktayı en yakın orta noktanın olduğu kümeye dahil et.

Tekrar orta noktaları hesapla




Orta noktalar değişmeyene kadar devam et

## K-Means Algoritması Uygulaması

Scikit learn kütüphanesi içerisinde K-Means gibi birçok kümeleme algoritması vardır. K-means algoritması uygulamasını biraz daha kolay anlayabilmek için iris veri seti üzerinde ele alalım.

from sklearn.datasets import load_iris

import matplotlib.pyplot as plt

import pandas as pd

from sklearn import cluster

plt.style.use('ggplot')

iris = load_iris()

X, y = load_iris(return_X_y=True)# ilk 2 özelliğin serpilme grafiğ i

plt.scatter(X[:,0], X[:,1], c=y)

plt.xlabel(iris.feature_names[0])

plt.ylabel(iris.feature_names[1])

![Image 3](https://miro.medium.com/v2/resize:fit:389/0*Ur7NAPCUmG6yfQLW.png)

kmeans = cluster.KMeans(n_clusters=3, random_state=42)

kmeans.fit(X)

kmeans.cluster_centers_.round(2)
array([[5.9 , 2.75, 4.39, 1.43], [5.01, 3.43, 1.46, 0.25], [6.85, 3.07, 5.74, 2.07]])

kmeans.labels_
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0])

plt.scatter(X[:,0], X[:,1], c=kmeans.labels_)

![Image 4](https://miro.medium.com/v2/resize:fit:372/0*52udNcupyg8rVhE9.png)

# Gerçek sınıfların olduğu grafik

plt.scatter(X[:,0], X[:,1], c=y)

plt.xlabel(iris.feature_names[0])

plt.ylabel(iris.feature_names[1])

![Image 5](https://miro.medium.com/v2/resize:fit:389/0*WdgBXJhRju-0AZDS.png)

## Videosu

[https://youtu.be/RFWZWiL84gk](https://youtu.be/RFWZWiL84gk)

## Kaynaklar

*   Akküçük, Ulaş. “Veri madenciliği: kümeleme ve sınıflama algoritmaları”. _İstanbul: Yalın Yayıncılık_ 18 (2011).
*   Han, Jiawei, Jian Pei, ve Micheline Kamber. _Data mining: concepts and techniques_. Elsevier, 2011.
*   Kantardzic, Mehmed. _Data mining: concepts, models, methods, and algorithms_. John Wiley & Sons, 2011.
*   Sumathi, Sai, ve S. N. Sivanandam. _Introduction to data mining and its applications_. C. 29. Springer, 2006.
*   Tan, Pang-Ning, Michael Steinbach, ve Vipin Kumar. _Introduction to data mining_. Pearson Education India, 2016.
*   Towards Data Science. “Towards Data Science”. Erişim 29 Mart 2020. [https://towardsdatascience.com/](https://towardsdatascience.com/).VanderPlas, Jake. _Python Data Science Handbook. OReilly Media_. Inc, 2017.