import requests
from bs4 import BeautifulSoup
import streamlit as st
from io import BytesIO

def scrape_links_and_images(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
        images = [img.get('src') for img in soup.find_all('img') if img.get('src')]

        return links, images

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {str(e)}")
        return [], []

# --- Streamlit UI ---
st.title("Web Scraper: Links and Images Extractor")

url = st.text_input("Enter a URL to scrape:")

if url:
    if not url.startswith("http"):
        url = "http://" + url

    st.write(f"Scraping {url}...")
    links, images = scrape_links_and_images(url)

    # --- Display Links ---
    st.subheader("🔗 Extracted Links")
    if links:
        st.write(f"Found {len(links)} links:")
        for link in links:
            st.write(link)
    else:
        st.write("No links found.")

    # --- Display Images with Download Buttons ---
    st.subheader("🖼️ Extracted Images")
    if images:
        st.write(f"Found {len(images)} images:")
        for i, img_url in enumerate(images):
            # Resolve relative image URLs
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            elif img_url.startswith("/"):
                base_url = "/".join(url.split("/")[:3])
                img_url = base_url + img_url

            try:
                img_response = requests.get(img_url, timeout=5)
                img_response.raise_for_status()
                img_bytes = BytesIO(img_response.content)

                st.image(img_bytes, caption=img_url, use_column_width=True)

                st.download_button(
                    label="Download Image",
                    data=img_bytes,
                    file_name=f"image_{i}.jpg",
                    mime="image/jpeg"
                )
            except:
                st.warning(f"Couldn't load image: {img_url}")
    else:
        st.write("No images found.")