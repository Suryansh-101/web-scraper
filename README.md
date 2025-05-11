# 🌐 Web Scraper with Streamlit

A simple but powerful **web scraper built with Streamlit** that extracts:

- 🔗 All hyperlinks (`<a href>`)
- 🖼️ All images (`<img src>`) with preview and download buttons

---

## 🚀 Features

- Extracts **all links** and displays them in a list
- Extracts and **previews all images** found on the page
- One-click **download** for each image
- Automatically handles:
  - Relative URLs (`/path/to/image.jpg`)
  - Protocol-relative URLs (`//cdn.site.com/image.png`)
- Clean, modern **Streamlit web app UI**

---

## 🛠️ Installation

Make sure you have Python 3.7+ installed.

1. **Clone the repository (or copy the script):**

```bash
git clone https://github.com/your-username/web-scraper-streamlit.git
cd web-scraper-streamlit
```

2. **Install the required libraries:**

```bash
pip install streamlit requests beautifulsoup4
```

3. **Run the app:**

```bash
streamlit run web_scraper.py
```

🌍 Example URLs to Test

Here are a few sites you can safely use for testing:

1    https://en.wikipedia.org/wiki/Cat

2    https://pixabay.com/images/search/nature/

3    https://unsplash.com/s/photos/mountains


🙌 Credits

Built using:

    Streamlit

    BeautifulSoup

    Requests
