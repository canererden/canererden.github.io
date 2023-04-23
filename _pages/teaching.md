---
layout: page
permalink: /teaching/
title: Teaching
description: 
nav: true
display_categories: [Lisans, Yüksek Lisans]
nav_order: 3
horizontal: false
---

<!-- pages/teaching.md -->
<div class="teaching">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized teaching -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_teaching = site.teaching | where: "category", category -%}
  {%- assign sorted_teaching = categorized_teaching | sort: "importance" %}
  <!-- Generate cards for each teaching -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_teaching -%}
      {% include teaching_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_teaching -%}
      {% include teaching.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display teaching without categories -->
  {%- assign sorted_teaching = site.teaching | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_teaching -%}
      {% include teaching_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_teaching -%}
      {% include teaching.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

## Geçmiş Dönemler

| Ders Adı                              | Akademik Yıl | Öğrenim Adı   |
| ------------------------------------- | ------------ | ------------- |
| Benzetim                              | 2021-2022    | Lisans        |
| Benzetim                              | 2020-2021    | Lisans        |
| Girişimcilik ve Proje Yönetimi        | 2021-2022    | Lisans        |
| İstatistikte Bilgisayar Uygulaması    | 2019-2020    | Lisans        |
| Lojistik ve Tedarik Zinciri Yönetimi  | 2021-2022    | Lisans        |
| Lojistik ve Tedarik Zinciri Yönetimi  | 2020-2021    | Lisans        |
| Uluslararası Tedarik Zinciri Yönetimi | 2021-2022    | Yüksek Lisans |
| Uluslararası Tedarik Zinciri Yönetimi | 2020-2021    | Yüksek Lisans |
| Üretim Yönetimi                       | 2022-2023    | Lisans        |
| Veri Madenciliği                      | 2019-2020    | Lisans        |
| Veri Madenciliği                      | 2020-2021    | Lisans        |
| Yöneylem Araştırması                  | 2022-2023    | Lisans        |
| Yöneylem Araştırması                  | 2021-2022    | Lisans        |
| Yöneylem Araştırması                  | 2020-2021    | Lisans        |
