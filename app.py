import streamlit as st

# Force wide layout and remove Streamlit's default margins
st.set_page_config(page_title="PurPurVR Hub", layout="centered", initial_sidebar_state="collapsed")

# Complete CSS override to apply the periwinkle cursor and style the purple bio container
st.markdown(
    """
    <style>
    /* Injects custom styles directly into the root frame */
    iframe {
        display: none !important;
    }
    
    html, body, [data-testid="stAppViewContainer"], .stApp {
        cursor: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://w3.org' width='32' height='32' viewBox='0 0 32 32'%3E%3Cpath d='M4,2 L4,26 L11,19 L19,27 L23,23 L15,15 L22,12 Z' fill='%23CCCCFF' stroke='white' stroke-width='1.5'/%3E%3C/svg%3E"), auto !important;
    }
    
    a, button, .btn-link, [role="button"] {
        cursor: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://w3.org' width='32' height='32' viewBox='0 0 32 32'%3E%3Cpath d='M4,2 L4,26 L11,19 L19,27 L23,23 L15,15 L22,12 Z' fill='%23B0C4DE' stroke='white' stroke-width='1.5'/%3E%3C/svg%3E"), pointer !important;
    }

    /* Turn off Streamlit's standard app backgrounds and header wrappers */
    .stApp, [data-testid="stHeader"], [data-testid="stMainBlockContainer"], main {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    /* Background video layer */
    .video-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -1;
        filter: brightness(0.4);
    }
    
    /* Central Purple Glassmorphism Profile Box */
    .bio-container {
        background: rgba(45, 15, 75, 0.5) !important;
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(160, 80, 240, 0.3);
        padding: 40px 30px;
        border-radius: 20px;
        text-align: center;
        max-width: 420px;
        margin: 80px auto;
        color: #ffffff !important;
        box-shadow: 0 10px 30px rgba(75, 0, 130, 0.4);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .bio-container h2 {
        color: #ffffff !important;
        margin-bottom: 5px;
        font-weight: 700;
        text-shadow: 0 0 15px rgba(180, 100, 255, 0.8);
    }
    
    .bio-container p {
        color: #e0d0f0 !important;
        font-size: 0.95rem;
        margin-bottom: 25px;
    }

    /* Interactive Purple Hyperlink Buttons */
    .btn-link {
        display: block;
        background: rgba(140, 60, 220, 0.15);
        color: #ffffff !important;
        text-decoration: none;
        padding: 14px;
        margin: 12px 0;
        border-radius: 10px;
        font-weight: 600;
        border: 1px solid rgba(180, 100, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .btn-link:hover {
        background: #a050f0 !important;
        color: #ffffff !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(160, 80, 240, 0.6);
    }
    </style>

    <!-- Moving Background Track Link -->
    <video autoplay loop muted playsinline class="video-bg">
        <source src="https://mixkit.co" type="video/mp4">
    </video>

    <!-- Center Card Panel -->
    <div class="bio-container">
        <h2>@PurPurVR</h2>
        <p>VR Modding & Creations</p>
        <a href="https://discord.gg" target="_blank" class="btn-link">EIC Modding Discord</a>
        <a href="https://youtube.com" target="_blank" class="btn-link">YouTube Channel</a>
    </div>
    """,
    unsafe_allow_html=True
)



