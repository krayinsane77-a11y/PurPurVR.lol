import streamlit as st

# Force wide layout and remove Streamlit's default margins
st.set_page_config(page_title="Custom Bio Hub", layout="centered", initial_sidebar_state="collapsed")

# Complete CSS override to turn the Streamlit wrapper dark/invisible and center components
st.markdown(
    """
    <style>
    /* Turn off Streamlit's standard app backgrounds and header wrappers */
    .stApp, [data-testid="stHeader"], [data-testid="stMainBlockContainer"] {
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
    
    /* Central Glassmorphism Profile Box */
    .bio-container {
        background: rgba(20, 20, 20, 0.6) !important;
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px 30px;
        border-radius: 20px;
        text-align: center;
        max-width: 420px;
        margin: 80px auto;
        color: #ffffff !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .bio-container h2 {
        color: #ffffff !important;
        margin-bottom: 5px;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(255,255,255,0.4);
    }
    
    .bio-container p {
        color: #cccccc !important;
        font-size: 0.95rem;
        margin-bottom: 25px;
    }

    /* Interactive Hyperlink Buttons */
    .btn-link {
        display: block;
        background: rgba(255, 255, 255, 0.08);
        color: #ffffff !important;
        text-decoration: none;
        padding: 14px;
        margin: 12px 0;
        border-radius: 10px;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .btn-link:hover {
        background: #ffffff !important;
        color: #000000 !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 255, 255, 0.2);
    }
    </style>

    <!-- Moving Background Track Link -->
    <video autoplay loop muted playsinline class="video-bg">
        <source src="https://mixkit.co" type="video/mp4">
    </video>

    <!-- Center Card Panel -->
    <div class="bio-container">
        <h2>@YourName</h2>
        <p>VR Modding & Creations</p>
        <a href="https://discord.gg" target="_blank" class="btn-link">Join My Discord</a>
        <a href="https://youtube.com" target="_blank" class="btn-link">YouTube Channel</a>
        <a href="https://vrchat.com" target="_blank" class="btn-link">VRChat Profile</a>
    </div>
    """,
    unsafe_allow_html=True
)
