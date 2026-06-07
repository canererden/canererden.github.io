---
layout: page
permalink: /publications/
title: Publications
description: Publications by categories in reversed chronological order.
years: [2026, 2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

<style>
  .pub-hidden { display: none !important; }
  .btn-show-more {
    display: block;
    width: 100%;
    text-align: center;
    margin-top: 2rem;
    padding: 1rem;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: var(--global-theme-color);
    background: transparent;
    border: 2px dashed var(--global-theme-color);
    border-radius: 0.5rem;
    cursor: pointer;
    transition: all 0.3s;
  }
  .btn-show-more:hover {
    background: var(--global-theme-color);
    color: #fff;
  }
  
  /* Additional aesthetic improvement for hover on bib entries */
  ol.bibliography li {
    padding: 1.5rem;
    border-radius: 0.5rem;
    transition: background-color 0.2s, transform 0.2s, box-shadow 0.2s;
    margin-bottom: 1rem;
    border: 1px solid transparent;
  }
  ol.bibliography li:hover {
    background-color: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transform: translateY(-2px);
  }
</style>

<div class="publications">

{%- for y in page.years %}
  {% capture bib_output %}{% bibliography -f papers -q @*[year={{y}}]* %}{% endcapture %}
  {% assign bib_output_stripped = bib_output | strip %}
  {% if bib_output_stripped != "" %}
    <h2 class="year" style="font-family: 'Inter', sans-serif; font-weight: 800; border-bottom: 2px solid var(--global-theme-color); padding-bottom: 0.5rem; margin-top: 2rem; margin-bottom: 1.5rem;">{{y}}</h2>
    {{ bib_output }}
  {% endif %}
{% endfor %}

</div>

<button id="showMorePubs" class="btn-show-more">Tüm Yayınları Göster <i class="fas fa-chevron-down"></i></button>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const limit = 5; // İlk 5 yayından sonrasını gizle
  const pubs = document.querySelectorAll('ol.bibliography li');
  const years = document.querySelectorAll('h2.year');
  const showMoreBtn = document.getElementById('showMorePubs');
  
  if (pubs.length <= limit) {
    showMoreBtn.style.display = 'none';
    return;
  }
  
  // Hide publications beyond the limit
  pubs.forEach((pub, index) => {
    if (index >= limit) {
      pub.classList.add('pub-hidden');
    }
  });
  
  // Hide year headers if all their publications are hidden
  years.forEach(year => {
    let nextEl = year.nextElementSibling;
    if (nextEl && nextEl.tagName === 'OL' && nextEl.classList.contains('bibliography')) {
      let allHidden = Array.from(nextEl.children).every(li => li.classList.contains('pub-hidden'));
      if (allHidden) {
        year.classList.add('pub-hidden');
      }
    }
  });
  
  showMoreBtn.addEventListener('click', function() {
    pubs.forEach(pub => pub.classList.remove('pub-hidden'));
    years.forEach(year => year.classList.remove('pub-hidden'));
    showMoreBtn.style.display = 'none';
  });
});
</script>
