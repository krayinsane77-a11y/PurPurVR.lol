import streamlit as st

# Force wide layout and remove Streamlit's default margins
st.set_page_config(page_title="PurPurVR Hub", layout="centered", initial_sidebar_state="collapsed")

# Complete CSS override using an animated glowing target cursor setup
st.markdown(
    """
    <style>
    /* Premium Pulsing Neon Crosshair with Center Hotspot Alignment (16 16) */
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] * {
        cursor: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPSczMicgaGVpZ2h0PSczMicgdmlld0JveD0nMCAwIDMyIDMyJz48c3R5bGU+QGtleWZyYW1lcyBwdWxzZSB7IDAlLCAxMDAlIHsgdHJhbnNmb3JtOiBzY2FsZSgxKTsgb3BhY2l0eTogMC44OyB9IDUwJSB7IHRyYW5zZm9ybTogc2NhbGUoMS4yKTsgb3BhY2l0eTogMTsgfSB9IC5nbG93IHsgdHJhbnNmb3JtLW9yaWdpbjogMTZweCAxNnB4OyBhbmltYXRpb246IHB1bHNlIDEuNXMgaW5maW5pdGUgZWFzZS1pbi1vdXQ7IH08L3N0eWxlPjxjaXJjbGUgY3g9JzE2JyBjeT0nMTYnIHI9JzUnIGZpbGw9J25vbmUnIHN0cm9rZT0nI0NDQ0NGRicgc3Ryb2tlLXdpZHRoPScxLjUnIGNsYXNzPSdnbG93Jy8+PGNpcmNsZSBjeD0nMTYnIGN5PScxNicgcj0nMS41JyBmaWxsPScjQ0NDQ0ZGJy8+PGxpbmUgeDE9JzE2JyB5MT0nMicgeDI9JzE2JyB5Mj0nNycgc3Ryb2tlPScjQ0NDQ0ZGJyBzdHJva2Utd2lkdGg9JzEuNScvPjxsaW5lIHgxPScxNicgeTE9JzI1JyB4Mj0nMTYnIHkyPSczMCcgc3Ryb2tlPScjQ0NDQ0ZGJyBzdHJva2Utd2lkdGg9JzEuNScvPjxsaW5lIHgxPScyJyB5MT0nMTYnIHgyPSc3JyB5Mj0nMTYnIHN0cm9rZT0nI0NDQ0NGRicgc3Ryb2tlLXdpZHRoPScxLjUnLz48bGluZSB4MT0nMjUnIHkxPSIxNicgeDI9JzMwJyB5Mj0nMTYnIHN0cm9rZT0nI0NDQ0NGRicgc3Ryb2tlLXdpZHRoPScxLjUnLz48L3N2Zz4=") 16 16, auto !important;
    }
    
    /* Interactive Hover Element - Inner Target locks tighter and glows a deeper purple */
    a, button, .btn-link, [role="button"], a * {
        cursor: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPSczMicgaGVpZ2h0PSczMicgdmlld0JveD0nMCAwIDMyIDMyJz48Y2lyY2xlIGN4PScxNicgY3k9JzE2JyByPSczJyBmaWxsPSdub25lJyBzdHJva2U9JyNCOTg0RkYnIHN0cm9rZS13aWR0aD0nMicvPjxjaXJjbGUgY3g9JzE2JyBjeT0nMTYnIHI9JzInIGZpbGw9J0NDQ0NGRicvPjxsaW5lIHgxPScxNicgeTE9JzInIHgyPScxNicgeTI9JzYnIHN0cm9rZT0nI0I5ODRGRicgc3Ryb2tlLXdpZHRoPScxLjUnLz48bGluZSB4MT0nMTYnIHkxPSIyNicgeDI9IjE2IiB5Mj0iMzAiIHN0cm9rZT0iI0I5ODRGRicgc3Ryb2tlLXdpZHRoPScxLjUnLz48bGluZSB4MT0nMicgeTE9JzE2JyB4Mj0nNicgeTI9JzE2JyBzdHJva2U9JyNCOTg0RkYnIHN0cm9rZS13aWR0aD0nMS41Jy8+PGxpbmUgeDE9IjI2IiB5MT0iMTYiIHgyPSIzMCIgeTI9IjE2IiBzdHJva2U9I0I5ODRGRiIgc3Ryb2tlLXdpZHRoPScxLjUnLz48L3N2Zz4=") 16 16, pointer !important;
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
