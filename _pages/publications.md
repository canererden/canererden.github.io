---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


<h2>Journal Articles</h2>
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
