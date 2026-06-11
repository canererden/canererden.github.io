---
layout: page
permalink: /en/teaching/
title: Teaching
description: Data Mining, Artificial Intelligence, and Optimization courses taught at Sakarya University of Applied Sciences.
nav_en: true
display_categories: [Lisans, Lisansüstü]
nav_order: 3
---

<!-- pages/teaching-en.md -->
<div class="teaching">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized teaching -->
  {%- for category in page.display_categories %}
  {%- assign display_cat = category %}
  {%- if display_cat == 'Lisans' %}{% assign display_cat = 'Undergraduate' %}{% endif %}
  {%- if display_cat == 'Lisansüstü' %}{% assign display_cat = 'Graduate' %}{% endif %}
  <h2 class="category">{{ display_cat }}</h2>
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
  <div class="row row-cols-1 row-cols-md-2 g-4 mb-5">
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
  <div class="row row-cols-1 row-cols-md-2 g-4 mb-5">
    {%- for project in sorted_teaching -%}
      {% include teaching.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>
