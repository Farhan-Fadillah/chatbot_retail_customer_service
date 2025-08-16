# 🛍️ Chatbot Customer Service Retail dengan Google Gemini AI

## Overview

Chatbot Customer Service Retail yang cerdas dan responsif menggunakan teknologi AI terdepan dari Google Gemini. Chatbot ini dirancang untuk memberikan layanan customer service 24/7 yang profesional, ramah, dan sangat membantu untuk bisnis retail.

## Fitur Utama

- **🤖 AI-Powered**: Menggunakan Google Gemini AI untuk layanan customer service yang cerdas
- **🛍️ Retail-Focused**: Didesain khusus untuk kebutuhan bisnis retail
- **⚡ Quick Actions**: Tombol aksi cepat untuk pertanyaan umum
- **🌐 Web Interface**: Interface web yang user-friendly dengan Streamlit
- **🇮🇩 Bahasa Indonesia**: Didesain khusus untuk pengguna Indonesia
- **📱 Responsive**: Dapat diakses dari berbagai perangkat
- **🕒 24/7 Support**: Layanan customer service non-stop

## Arsitektur Sistem

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Query   │───▶│  Google Gemini  │───▶│   AI Response   │
└─────────────────┘    │      (AI)       │    └─────────────────┘
                       └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  Retail Context │
                       │   Knowledge     │
                       └─────────────────┘
```

## Prerequisites

Sebelum menjalankan chatbot, pastikan Anda memiliki:

1. **Python 3.8+** terinstall
2. **Google AI API Key** dari [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Internet connection** untuk akses Google Gemini API

## Installation

### 1. Clone Repository
```bash
git clone <repository-url>
cd EnergiHijau2025
```

### 2. Install Dependencies
```bash
pip install -r requirements_retail_chatbot.txt
```

### 3. Setup Environment Variables
Buat file `.env` berdasarkan template `env_template_retail.txt`:

```bash
# Copy template
cp env_template_retail.txt .env

# Edit file .env dengan API key Anda
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Jalankan Chatbot
```bash
streamlit run chatbot_customer_service_retail_app.py
```

## 🎮 Cara Penggunaan

### Development & Testing
1. **Jalankan Jupyter Notebook**:
   ```bash
   jupyter notebook chatbot_customer_service_retail_development.ipynb
   ```

2. **Test AI Responses**:
   - Initialize Google Gemini
   - Test berbagai skenario customer service
   - Validasi response quality

### Production App
1. **Jalankan Streamlit App**:
   ```bash
   streamlit run chatbot_customer_service_retail_app.py
   ```

2. **Akses Web Interface**:
   - Buka browser di `http://localhost:8501`
   - Klik "Initialize System"
   - Gunakan Quick Actions atau tanyakan langsung


## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: API key untuk Google AI (Gemini)

### AI Model Configuration
- **Model**: `gemini-pro`
- **Language**: Indonesian
- **Context**: Retail customer service
- **Response Style**: Professional, friendly, helpful

### Retail Knowledge Base
```python
RETAIL_KNOWLEDGE = {
    "products": {
        "elektronik": ["Laptop", "Smartphone", "Tablet", "Headphone", "Speaker"],
        "fashion": ["Pakaian", "Sepatu", "Tas", "Aksesoris"],
        "makanan": ["Snack", "Minuman", "Makanan Ringan"],
        "rumah_tangga": ["Dapur", "Kamar Mandi", "Kamar Tidur", "Ruang Tamu"]
    },
    "services": [
        "Pembelian Online", "Pengiriman", "Return & Refund", 
        "Garansi", "Customer Support"
    ],
    "promotions": [
        "Diskon 20% untuk member", "Buy 2 Get 1 Free",
        "Free ongkir untuk pembelian di atas 500k",
        "Cashback 10% untuk pembayaran digital"
    ]
}
```

## Contoh Pertanyaan

Berikut beberapa contoh pertanyaan yang dapat diajukan ke chatbot:

### **Produk**
1. "Apa saja produk elektronik yang tersedia?"
2. "Berapa harga laptop gaming?"
3. "Ada stok iPhone 15?"
4. "Produk apa yang sedang diskon?"

### **Promo & Layanan**
1. "Ada promo apa saja saat ini?"
2. "Bagaimana cara menjadi member?"
3. "Berapa minimum pembelian untuk free ongkir?"
4. "Apakah ada cashback untuk pembayaran digital?"

### **Pemesanan & Pengiriman**
1. "Saya mau pesan barang online"
2. "Bagaimana cara tracking order?"
3. "Bisa ganti alamat pengiriman?"
4. "Berapa lama waktu pengiriman?"

### **Keluhan & Support**
1. "Barang yang saya beli rusak"
2. "Pelayanan kasir lambat"
3. "Harga tidak sesuai dengan yang di display"
4. "Barang tidak sesuai dengan yang dipesan"

## Quick Actions

Chatbot dilengkapi dengan tombol Quick Actions untuk pertanyaan umum:

- **🛍️ Produk**: Informasi produk yang tersedia
- **🎉 Promo**: Promo dan diskon terkini
- **🔧 Layanan**: Layanan yang disediakan
- **📞 Kontak**: Informasi kontak customer service
- **🕒 Jam Buka**: Jam operasional toko

## Troubleshooting

### Common Issues

1. **API Key Error**:
   ```
   ❌ GOOGLE_API_KEY tidak ditemukan
   ```
   **Solution**: Pastikan file `.env` berisi API key yang benar

2. **Google Gemini Error**:
   ```
   ❌ Error initializing system
   ```
   **Solution**: Periksa API key dan quota Google AI

3. **Streamlit Error**:
   ```
   ❌ Module not found
   ```
   **Solution**: Install dependencies dengan `pip install -r requirements_retail_chatbot.txt`

### Performance Tips

- **API Quota**: Monitor penggunaan Google AI API
- **Response Time**: Optimasi prompt untuk response yang lebih cepat
- **Error Handling**: Implementasi fallback responses
- **Caching**: Simpan response umum untuk efisiensi

## Security Considerations

1. **API Keys**: Jangan commit API keys ke repository
2. **Environment Variables**: Gunakan file `.env` untuk sensitive data
3. **Input Validation**: Validasi input user untuk keamanan
4. **Rate Limiting**: Implementasi rate limiting untuk API calls

## Monitoring & Analytics

### Metrics yang Di-track
- Total chat conversations
- Customer satisfaction
- Response time
- Error rates
- Popular questions

### Logging
- Chat history dengan timestamp
- User interactions
- System errors
- Performance metrics

## Deployment

### Local Development
```bash
streamlit run chatbot_customer_service_retail_app.py
```

### Production Deployment
1. **Streamlit Cloud**: Deploy langsung dari GitHub
2. **Docker**: Container deployment
3. **Cloud Platforms**: AWS, GCP, Azure
4. **VPS**: Manual deployment di server

### Docker Example
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements_retail_chatbot.txt
EXPOSE 8501
CMD ["streamlit", "run", "chatbot_customer_service_retail_app.py"]
```

## Contributing

1. Fork repository
2. Buat feature branch
3. Commit changes
4. Push ke branch
5. Buat Pull Request

## License

Project ini dibuat untuk tujuan edukasi dan membantu bisnis retail memberikan layanan customer service yang lebih baik.

## Support

Jika mengalami masalah atau memiliki pertanyaan:

1. Periksa troubleshooting section
2. Buat issue di repository
3. Hubungi tim development

## Acknowledgments

- **Google AI** untuk Gemini AI
- **Streamlit** untuk web framework
- **Python Community** untuk libraries
- **Retail Industry** untuk use cases

---

**🛍️ Customer Service Retail - Powered by Google Gemini AI** 🚀

*Melayani customer 24/7 dengan teknologi AI terdepan*
