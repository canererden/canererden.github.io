# Google Scholar indeksleme notları

## Scholar neyi indeksler, neyi indekslemez

Scholar'ın webmaster kurallarına göre uygun içerik: *dergi makaleleri, konferans
bildirileri, teknik raporlar veya taslakları, tezler, ön/son baskılar ve özetler.*
Kitaplar için Google Book Search'e yönlendiriliyor. Dolayısıyla:

| İçerik | Scholar'da çıkar mı | Yol |
|---|---|---|
| Kitap tanıtım sayfası (`/buyuk-dil-modellerinin-insasi/` vb.) | **Hayır** | Google Books + Scholar profiline elle ekleme |
| CRC / Springer kitapları ve bölümleri | Evet, zaten | Yayıncının DOI'leri üzerinden |
| Açık erişimli web kitabı (`/veri-analizi-python/`) | Evet, koşullu | Tam metin PDF + citation etiketleri |
| Ders notu (PDF, teknik rapor niteliğinde) | Evet, koşullu | Aşağıya bakın |
| Ders tanıtım sayfası | Hayır | — |

PDF koşulları: metin aranabilir olmalı (taranmış görüntü değil), 5 MB'ı geçmemeli,
ilk sayfada başlık ve yazar adı açıkça yer almalı, sonda kaynakça bulunmalı.
Sayfa, anasayfadan en fazla on basit HTML bağlantısıyla erişilebilir olmalı ve
`robots.txt` engellememelidir. İkisi de bu sitede sağlanıyor.

## Bu depoda hazır olan altyapı

`_includes/metadata.html`, `citation_title` tanımlı her sayfa için Highwire Press,
Dublin Core ve schema.org etiketlerini üretir. Tanınan front matter alanları:

```yaml
citation_title:        "Başlık"
citation_authors:                      # liste
  - Caner Erden
citation_publication_date: 2026        # yıl veya yyyy/aa
citation_type:         Report          # Book | Report | Thesis | Article
citation_language:     tr
citation_keywords:     "a; b; c"
citation_pdf_url:      /assets/pdf/dosya.pdf   # Scholar'ın indekslediği tam metin
citation_abstract:     "Bir paragraf özet."
citation_abstract_html_url: /sayfa/

# türe göre
citation_isbn:, citation_publisher:                       # kitap
citation_technical_report_institution:, citation_technical_report_number:
citation_dissertation_institution:                        # tez
citation_journal_title:, citation_volume:, citation_issue:,
citation_firstpage:, citation_lastpage:                   # makale
citation_doi:
```

`citation_pdf_url` verildiğinde `citation_fulltext_world_readable` da basılır ve
ders sayfalarında (`_layouts/course.html`) künyeli bir indirme kartı görünür.

Ders notu için hazır şablon: `_teaching/TEMPLATE.md`.

## Açık web kitabını Scholar'a hazırlamak

Kitap ayrı bir depoda: `github.com/canererden/veri-analizi-python` (dal: `master`),
Jupyter Book ile üretiliyor ve `canererden.com/veri-analizi-python/` altında
yayınlanıyor.

**1. PDF üret ve yayına koy**

```bash
jupyter-book build . --builder pdflatex
mkdir -p _static
cp _build/latex/book.pdf _static/veri-analizi-python.pdf
```

`_static/` içeriği siteyle birlikte yayınlanır; dosya
`https://canererden.com/veri-analizi-python/_static/veri-analizi-python.pdf`
adresinden erişilebilir olur.

**2. Citation etiketlerini ekle**

Tercih edilen yol, etiketleri yalnızca kitabın giriş sayfasına koymaktır — böylece
Scholar tek bir eser görür. `intro.md` dosyasının en başına:

```yaml
---
myst:
  html_meta:
    "citation_title": "Veri Analizi için Python Kütüphaneleri"
    "citation_author": "Erden, Caner"
    "citation_publication_date": "2023"
    "citation_language": "tr"
    "citation_publisher": "Caner Erden"
    "citation_keywords": "veri analizi; Python; NumPy; Pandas; Matplotlib; scikit-learn"
    "citation_abstract_html_url": "https://canererden.com/veri-analizi-python/intro.html"
    "citation_pdf_url": "https://canererden.com/veri-analizi-python/_static/veri-analizi-python.pdf"
    "citation_fulltext_world_readable": ""
---
```

Tüm sayfalara birden eklemek isterseniz aynı sözlük `_config.yml` içinde de
tanımlanabilir:

```yaml
sphinx:
  config:
    myst_html_meta:
      "citation_title": "Veri Analizi için Python Kütüphaneleri"
      # ... aynı alanlar
```

`myst_html_meta` anahtarı MyST-Parser'ın belgelenmiş seçeneğidir; sayfa bazlı
karşılığı front matter'daki `myst.html_meta`'dır. Eski bir MyST sürümü
kullanıyorsanız front matter biçimi farklı olabilir — derledikten sonra
`intro.html` kaynağında `citation_title` etiketinin göründüğünü doğrulayın.

**3. Doğrula**

Yayına aldıktan sonra sayfa kaynağında etiketlerin bulunduğunu kontrol edin, sonra
Scholar'ın taraması için birkaç hafta bekleyin.

## Kitaplar için gerçek yol

1. **Scholar profiline elle ekleme** — profilde "Add" → "Add article manually" →
   tür olarak *Book*. Anında görünür, en hızlı yol.
2. **Google Books** — Türkçe yayıncı kitapları için (Seçkin, Kodlab) yayıncı
   Google Books'a gönderebilir; *Python ile Veri Madenciliği* zaten Google Books'ta
   (`books.google.com/books?id=wx9MEAAAQBAJ`).
3. **CRC ve Springer kitapları** DOI'leri üzerinden zaten indeksli.

## Kaynak

Google Scholar, Inclusion Guidelines for Webmasters:
https://scholar.google.com/intl/en/scholar/inclusion.html
