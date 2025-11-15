<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/Scrapy-API%20Scraper-green" />
</p>

# 📘 Tokopedia Review Scraper using Scrapy

- This project retrieved **Merchant Reviews**, not individual products.  
- Used **Scrapy** to send **direct POST requests** to a backend API and extract JSON data.  
- No HTML parsing or UI crawling, this scraper communicates directly with the website API for maximum speed and accuracy.

> **Note:** This project is for educational purposes only.  
> Please follow the website’s Terms of Service and local laws when scraping data.

---

## 🔍 Overview

This Scrapy project is designed for **API web scraping**, where data is retrieved through:

- POST requests  
- JSON responses  
- Structured API endpoints  

This method is ideal for:

- Dynamic websites
- Product and price monitoring
- Fast and stable data extraction
- Avoiding complex HTML parsing

> **Note:** The website API does not provide all the reviews through its public endpoints, limited to **10,000** reviews


---

## 🧰 Requirements

- Python 3.8+ (recommended)
- Virtual environment recommended
- Scrapy

---

## ▶️ How to Use (Windows)

**1. Clone GitHub repo**
```bash
git clone https://github.com/musabIAM/Tokped-Review-Scrapy.git
```
**2. Go to the folder**
```bash
cd Tokped-Review-Scrapy
```
**3. Create a virtual environment**
```bash
python -m venv <name>
```
**4. Activate the virtual environment**
```bash
<name>\Scripts\activate
```
**5. Install scrapy**
```bash
pip install scrapy
```
**6. Go to the folder**
```bash
cd tokped
```
**7. Change the SHOP_ID**   

SHOP_ID variable in tokped_review.py:

tokped/   
│   
├── tokoped/    
│ ├── spiders/    
│ │ └── tokped_review.py    

> **Note:** How to find SHOP_ID.
 
**8. Start scrapy crawl and save to JSON**
```bash
scrapy crawl tokped_review -O reviews.json
```

---

## ⚙️ How to Find SHOP_ID

**1. Go to the merchant review page**    
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/0681a4b9-77c3-47c5-bc11-4bf40627375e" />

**2. Right click the got to inspect**    
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/d20a0b82-bf9f-49e9-baf9-b911212c14fc" />

**3. Go to Network and find ReviewList**    
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/fc555ff9-9ea3-45d3-b730-0b11edac5cc3" />
> **Note:** If ReviewList does not appear, try to go to the next page.
 
**4. Click the payload and you will find shopID**       
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/36c1297e-c42c-4039-8b37-79768470753e" />





