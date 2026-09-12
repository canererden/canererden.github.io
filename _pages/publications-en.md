---
layout: page
permalink: /en/publications/
title: Publications
description: Peer-reviewed journal articles, conference proceedings, and academic publications by Dr. Caner Erden.
years: [2028, 2027, 2026, 2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009]
nav_en: true
nav_order: 1
---
<!-- _pages/publications-en.md -->


<div class="publications">

{%- for y in page.years %}
  {% capture bib_output %}{% bibliography -f papers -q @*[year={{y}}]* %}{% endcapture %}
  {% assign bib_output_stripped = bib_output | strip %}
  {% if bib_output_stripped != "" %}
    <h2 class="year">{{y}}</h2>
    {{ bib_output }}
  {% endif %}
{% endfor %}

</div>

<button id="showMorePubs" class="btn-show-more">Show All Publications <i class="fas fa-chevron-down"></i></button>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const limit = 5; // Hide after 5
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
