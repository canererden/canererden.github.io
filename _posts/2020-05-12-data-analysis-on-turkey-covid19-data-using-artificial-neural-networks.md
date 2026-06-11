---
layout: post
title: "Data Analysis on Turkey COVID19 Data using Artificial Neural Networks"
date: 2020-05-12
giscus_comments: true
permalink: /2020/05/12/data-analysis-on-turkey-covid19-data-using-artificial-neural-networks
tags:
  - blog
description: "--..."
---

--

--


![Image 2](https://miro.medium.com/v2/resize:fit:700/1*uA-O-zEbUFGGjRgmibwYhw.jpeg)

Nowadays, everyone is talking about COVID19 which has been identified as pandemic in the whole world. By April 21, 2020, Turkey is in the top 10th countries list in terms of the number of cases of COVID-19. Despite the high number of cases in Turkey, the death rate is low. In addition, the number of patients recovered has been 18491 in total so far. In this article, Turkey’s data and performance against COVID19 will be analyzed.




Artificial intelligence tools has been used for i) early warnings and alerts, ii) tracking and prediction, iii) data dashboards, iv) diagnosis and prognosis, v) treatments, and cures, and vi) social control against COVID-19 so far. This study can be classified in ii)tracking and prediction. Here, COVID19 data from Turkey is collected for a data analysis and modelling study until the date of April 21, 2020.

> First of all, I should state that I am not a healthcare professional or epidemiologist. This study is based on data science and machine learning studies only. You can learn more about coronavirus pandemic from [here](https://slack-redir.net/link?url=https%3A%2F%2Fwww.who.int%2Femergencies%2Fdiseases%2Fnovel-coronavirus-2019).

The data were combined with the data from [here](https://www.worldometers.info/coronavirus/) (Worldometer) and data from the Ministry of Health of Turkey and transferred to the table. The data table is shown as follows. New data will be added to the model as it arrives. Also, the data set used from [here](https://drive.google.com/uc?export=view&id=11SJRu_ghaKQCmKTNP6avuSgOr_RqB7tx) can be downloaded as a csv file.

![Image 3](https://miro.medium.com/v2/resize:fit:473/1*gi-cF-oorShJVQi7vXF2_A.png)

Information about the features in the data set is given below.


![Image 4](https://miro.medium.com/v2/resize:fit:700/1*bMNTFY5OiczAdoDpZa5qbg.png)

Let’s move on to the codes. First of all, let’s call the libraries to be used in the study.

Let’s get our data to pandas.

![Image 5](https://miro.medium.com/v2/resize:fit:659/1*EVdpwX5mD5MN1grxbtO8-Q.png)

We can pull the data from the Worldometers daily as follows.


![Image 6](https://miro.medium.com/v2/resize:fit:700/1*mqcPgCamF7j-DXbMugwnnQ.png)

Let’s visualize the dataset.

![Image 7](https://miro.medium.com/v2/resize:fit:557/1*Q8RDfVD85Ey-P5C2925xPg.png)

num_recovered and num_case are taken as input variable, total_intubated, total_intensive_care are the output variable.

mean_squared_error: 0.00545122621311585

r2_score: 0.9619569390759679

![Image 8](https://miro.medium.com/v2/resize:fit:432/1*Me_dherp4xRGDuN8ZSp-7g.png)

### **References**

> Artificial Intelligence against COVID-19: An Early Review
> 
> 
> “| COVID-19 Türkiye Web Portalı.” Accessed April 18, 2020. [https://covid19.tubitak.gov.tr/offline](https://covid19.tubitak.gov.tr/offline).
> 
> 
> “1.17. Neural Network Models (Supervised) — Scikit-Learn 0.22.2 Documentation.” Accessed April 18, 2020. [https://scikit-learn.org/stable/modules/neural_networks_supervised.html](https://scikit-learn.org/stable/modules/neural_networks_supervised.html).
> 
> 
> Springboard Blog. “A Beginner’s Guide to Neural Networks in Python,” March 21, 2017. [https://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/](https://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/).
> 
> 
> _Coronavirus Outbreak Prediction Using Machine Learning | Covid-19 Outbreak Prediction | Simplilearn_. Accessed April 18, 2020. [https://www.youtube.com/watch?v=sHWKN5dakPw](https://www.youtube.com/watch?v=sHWKN5dakPw).
> 
> 
> “Coronavirus Update (Live): 2,252,651 Cases and 154,331 Deaths from COVID-19 Virus Pandemic — Worldometer.” Accessed April 18, 2020. [https://www.worldometers.info/coronavirus/#countries](https://www.worldometers.info/coronavirus/#countries).
> 
> 
> Simplilearn. “Coronavirus Outbreak Prediction Using Machine Learning | Covid-19 Out….” Education, 15:29:25 UTC. [https://www.slideshare.net/Simplilearn/coronavirus-outbreak-prediction-using-machine-learning-covid19-outbreak-prediction-simplilearn/Simplilearn/coronavirus-outbreak-prediction-using-machine-learning-covid19-outbreak-prediction-simplilearn](https://www.slideshare.net/Simplilearn/coronavirus-outbreak-prediction-using-machine-learning-covid19-outbreak-prediction-simplilearn/Simplilearn/coronavirus-outbreak-prediction-using-machine-learning-covid19-outbreak-prediction-simplilearn).
> 
> 
> “T.C Sağlık Bakanlığı Korona Tablosu.” Accessed April 18, 2020. [https://covid19.saglik.gov.tr/](https://covid19.saglik.gov.tr/).
> 
> 
> “Türkiye Cumhuriyeti Cumhurbaşkanlığı Dijital Dönüşüm Ofisi — Anasayfa.” Accessed April 18, 2020. [https://corona.cbddo.gov.tr/](https://corona.cbddo.gov.tr/).