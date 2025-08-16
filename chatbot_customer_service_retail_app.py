#!/usr/bin/env python3
"""
Chatbot Customer Service Retail dengan Google Gemini AI
Aplikasi Streamlit untuk customer service retail yang dapat diakses masyarakat
"""

import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🛍️ Customer Service Retail",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.2rem;
        color: #000000;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 4px solid;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #000000;
    }
    .user-message {
        background-color: #E3F2FD;
        border-left-color: #2196F3;
        margin-left: 2rem;
    }
    .bot-message {
        background-color: #F3E5F5;
        border-left-color: #9C27B0;
        margin-right: 2rem;
    }
    .info-box {
        background-color: #E8F5E8;
        border: 1px solid #4CAF50;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #000000;
    }
    .warning-box {
        background-color: #FFF3E0;
        border: 1px solid #FF9800;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #000000;
    }
    .success-box {
        background-color: #E8F5E8;
        border: 1px solid #4CAF50;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #000000;
    }
    .quick-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    .quick-action-btn {
        background-color: #FF6B6B;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        cursor: pointer;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }
    .quick-action-btn:hover {
        background-color: #FF5252;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'is_initialized' not in st.session_state:
    st.session_state.is_initialized = False
if 'customer_info' not in st.session_state:
    st.session_state.customer_info = {}

# Retail knowledge base
RETAIL_KNOWLEDGE = {
    "products": {
        "elektronik": ["Laptop", "Smartphone", "Tablet", "Headphone", "Speaker"],
        "fashion": ["Pakaian", "Sepatu", "Tas", "Aksesoris"],
        "makanan": ["Snack", "Minuman", "Makanan Ringan"],
        "rumah_tangga": ["Dapur", "Kamar Mandi", "Kamar Tidur", "Ruang Tamu"]
    },
    "services": [
        "Pembelian Online",
        "Pengiriman",
        "Return & Refund",
        "Garansi",
        "Customer Support"
    ],
    "promotions": [
        "Diskon 20% untuk member",
        "Buy 2 Get 1 Free",
        "Free ongkir untuk pembelian di atas 500k",
        "Cashback 10% untuk pembayaran digital"
    ]
}

def initialize_system():
    """Initialize the customer service system with Google Gemini"""
    try:
        # Configuration
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        
        if not GOOGLE_API_KEY:
            st.error("❌ GOOGLE_API_KEY tidak ditemukan. Pastikan file .env berisi GOOGLE_API_KEY")
            return False
        
        # Initialize Google Gemini
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-flash')
        
        st.session_state.model = model
        st.session_state.is_initialized = True
        
        return True
        
    except Exception as e:
        st.error(f"❌ Error initializing system: {str(e)}")
        return False

def get_customer_service_response(query, context=""):
    """Generate customer service response using Google Gemini"""
    try:
        # Create comprehensive prompt
        prompt = f"""
Kamu adalah customer service retail yang profesional, ramah, dan sangat membantu.

KONTEKS RETAIL:
- Produk: {json.dumps(RETAIL_KNOWLEDGE['products'], ensure_ascii=False)}
- Layanan: {', '.join(RETAIL_KNOWLEDGE['services'])}
- Promosi: {', '.join(RETAIL_KNOWLEDGE['promotions'])}

INSTRUKSI:
1. Berikan jawaban yang sopan, informatif, dan membantu
2. Gunakan bahasa Indonesia yang mudah dipahami
3. Jika ada pertanyaan spesifik, berikan jawaban yang detail
4. Untuk keluhan, tunjukkan empati dan berikan solusi
5. Selalu tawarkan bantuan lebih lanjut

PERTANYAAN CUSTOMER: {query}

KONTEKS TAMBAHAN: {context}

JAWABAN:
"""
        
        # Generate response
        response = st.session_state.model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Maaf, terjadi kesalahan dalam sistem: {str(e)}"

def handle_quick_action(action):
    """Handle quick action buttons"""
    responses = {
        "produk": "Kami memiliki berbagai produk seperti elektronik, fashion, makanan, dan rumah tangga. Produk apa yang ingin Anda ketahui lebih lanjut?",
        "promo": "Saat ini kami memiliki beberapa promo menarik:\n• Diskon 20% untuk member\n• Buy 2 Get 1 Free\n• Free ongkir untuk pembelian di atas 500k\n• Cashback 10% untuk pembayaran digital",
        "layanan": "Layanan yang kami sediakan:\n• Pembelian Online\n• Pengiriman\n• Return & Refund\n• Garansi\n• Customer Support 24/7",
        "kontak": "Anda dapat menghubungi kami melalui:\n• WhatsApp: 0812-3456-7890\n• Email: cs@retailstore.com\n• Call Center: 1500-123",
        "jam_buka": "Jam operasional kami:\n• Senin-Jumat: 09:00-22:00\n• Sabtu-Minggu: 10:00-21:00\n• Hari Libur: 10:00-20:00"
    }
    
    return responses.get(action, "Maaf, aksi tersebut tidak tersedia.")

def main():
    # Header
    st.markdown('<h1 class="main-header">🛍️ Customer Service Retail</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Layanan customer service 24/7 untuk membantu Anda</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Konfigurasi")
        
        if st.button("🔄 Initialize System", type="primary"):
            with st.spinner("Initializing system..."):
                if initialize_system():
                    st.success("✅ System berhasil diinisialisasi!")
                else:
                    st.error("❌ Gagal menginisialisasi system")
        
        st.markdown("---")
        st.header("ℹ️ Informasi")
        st.markdown("""
        **Customer Service Retail** menggunakan teknologi:
        - **Google Gemini AI** untuk layanan customer service
        - **Streamlit** untuk interface web
        - **24/7 Support** untuk membantu customer
        
        **Layanan yang Tersedia:**
        - Informasi produk
        - Bantuan pemesanan
        - Penanganan keluhan
        - Informasi promo
        - Status pengiriman
        """)
        
        st.markdown("---")
        st.header("📊 Status System")
        if st.session_state.is_initialized:
            st.success("✅ System Ready")
        else:
            st.warning("⚠️ System Not Ready")
        
        st.markdown("---")
        st.header("📈 Statistik")
        st.metric("Total Chat", len(st.session_state.chat_history))
        st.metric("Customer Served", len(set([msg.get('customer_id', 'unknown') for msg in st.session_state.chat_history])))
    
    # Main content
    if not st.session_state.is_initialized:
        st.markdown("""
        <div class="info-box">
            <h3>🚀 Selamat Datang di Customer Service Retail!</h3>
            <p>Untuk memulai, silakan:</p>
            <ol>
                <li>Pastikan file <code>.env</code> berisi GOOGLE_API_KEY</li>
                <li>Klik tombol <strong>"Initialize System"</strong> di sidebar</li>
                <li>Tunggu hingga system siap</li>
                <li>Mulai bertanya atau gunakan quick actions!</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # Environment variables info
        with st.expander("🔑 Environment Variables yang Diperlukan"):
            st.code("""
# File .env
GOOGLE_API_KEY=your_google_api_key_here
            """)
            
            st.info("""
            **Cara mendapatkan API Keys:**
            1. **Google API Key**: Dapatkan dari Google AI Studio atau Google Cloud Console
            2. Pastikan API key aktif dan memiliki quota yang cukup
            """)
        
        return
    
    # Quick Actions
    st.markdown("### ⚡ Quick Actions")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🛍️ Produk", use_container_width=True):
            response = handle_quick_action("produk")
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "Tanya tentang produk",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.session_state.chat_history.append({
                "role": "bot", 
                "content": response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()
    
    with col2:
        if st.button("🎉 Promo", use_container_width=True):
            response = handle_quick_action("promo")
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "Tanya tentang promo",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.session_state.chat_history.append({
                "role": "bot", 
                "content": response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()
    
    with col3:
        if st.button("🔧 Layanan", use_container_width=True):
            response = handle_quick_action("layanan")
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "Tanya tentang layanan",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.session_state.chat_history.append({
                "role": "bot", 
                "content": response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()
    
    with col4:
        if st.button("📞 Kontak", use_container_width=True):
            response = handle_quick_action("kontak")
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "Tanya tentang kontak",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.session_state.chat_history.append({
                "role": "bot", 
                "content": response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()
    
    with col5:
        if st.button("🕒 Jam Buka", use_container_width=True):
            response = handle_quick_action("jam_buka")
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "Tanya tentang jam buka",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.session_state.chat_history.append({
                "role": "bot", 
                "content": response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.rerun()
    
    # Chat interface
    st.markdown("### 💬 Mulai Bertanya")
    
    # Chat input
    user_input = st.text_input(
        "Tanyakan apapun tentang layanan retail kami:",
        placeholder="Contoh: Saya mau tanya tentang produk, promo, atau layanan pengiriman",
        key="user_input"
    )
    
    # Send button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        send_button = st.button("🚀 Kirim Pertanyaan", type="primary", use_container_width=True)
    
    # Process user input
    if send_button and user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({
            "role": "user", 
            "content": user_input,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        
        # Generate bot response
        with st.spinner("🔍 Mencari informasi dan menghasilkan jawaban..."):
            bot_response = get_customer_service_response(user_input)
            st.session_state.chat_history.append({
                "role": "bot", 
                "content": bot_response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
        
        # Clear input
        st.rerun()
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown("### 📝 Riwayat Percakapan")
        
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>👤 Anda ({message.get('timestamp', '')}):</strong><br>
                    {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message bot-message">
                    <strong>🤖 Customer Service ({message.get('timestamp', '')}):</strong><br>
                    {message["content"]}
                </div>
                """, unsafe_allow_html=True)
    
    # Clear chat button
    if st.session_state.chat_history:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🗑️ Bersihkan Riwayat Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #000000; padding: 1rem;">
        <p>🛍️ Customer Service Retail - Powered by Google Gemini AI</p>
        <p>Melayani customer 24/7 dengan teknologi AI terdepan</p>
        <p>© 2024 Retail Store - Customer Service Excellence</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
