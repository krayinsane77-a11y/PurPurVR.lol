import streamlit as st

# Force wide layout and remove Streamlit's default margins
st.set_page_config(page_title="PurPurVR Hub", layout="centered", initial_sidebar_state="collapsed")

# Complete CSS and JavaScript injection for the custom cursor tracer trail
st.markdown(
    """
    <style>
    /* Reset cursor back to standard look */
    *, html, body, .stApp, a, button, .btn-link {
        cursor: default !important;
    }
    
    a, button, .btn-link, [role="button"] {
        cursor: pointer !important;
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
        pointer-events: none;
    }
    
    /* Central Purple Glassmorphism Profile Box */
    .bio-container {
        background: rgba(45, 15, 75, 0.5) !important; /* Deep translucent purple */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(160, 80, 240, 0.3); /* Purple border tint */
        padding: 40px 30px;
        border-radius: 20px;
        text-align: center;
        max-width: 420px;
        margin: 80px auto;
        color: #ffffff !important;
        box-shadow: 0 10px 30px rgba(75, 0, 130, 0.4); /* Purple glow shadow */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        position: relative;
        z-index: 10;
    }
    
    .bio-container h2 {
        color: #ffffff !important;
        margin-bottom: 5px;
        font-weight: 700;
        text-shadow: 0 0 15px rgba(180, 100, 255, 0.8); /* Glowing purple text effect */
    }
    
    .bio-container p {
        color: #e0d0f0 !important; /* Light lavender-tinted description text */
        font-size: 0.95rem;
        margin-bottom: 25px;
    }

    /* Interactive Purple Hyperlink Buttons */
    .btn-link {
        display: block;
        background: rgba(140, 60, 220, 0.15); /* Translucent purple button base */
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
        background: #a050f0 !important; /* Solid vibrant purple on hover */
        color: #ffffff !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(160, 80, 240, 0.6); /* Vibrant purple hover glow */
    }

    /* Tracer Trail Elements Styling */
    .trail-dot {
        position: fixed;
        width: 8px;
        height: 8px;
        background-color: #CCCCFF; /* Periwinkle Color */
        border-radius: 50%;
        pointer-events: none;
        z-index: 99999;
        transform: translate(-50%, -50%);
        transition: transform 0.1s linear, opacity 0.4s ease-out;
        box-shadow: 0 0 8px #CCCCFF, 0 0 15px #9999FF;
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

    <!-- Mouse Tracer JavaScript Engine -->
    <script>
    const dots = [];
    const maxDots = 20; // Length of the trailing path link line

    // Create the pool of tracer dot elements
    for (let i = 0; i < maxDots; i++) {
        const dot = document.createElement('div');
        dot.className = 'trail-dot';
        dot.style.opacity = 0;
        document.body.appendChild(dot);
        dots.push({
            element: dot,
            x: 0,
            y: 0
        });
    }

    let mouseX = 0;
    let mouseY = 0;
    let isMoving = false;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        isMoving = true;
    });

    // Handle tracking math loop animation frames smoothly
    function animate() {
        let x = mouseX;
        let y = mouseY;

        dots.forEach((dot, index) => {
            const nextDot = dots[index + 1] || dots[0];
            
            dot.element.style.left = x + 'px';
            dot.element.style.top = y + 'px';
            
            // Scaled size fade out across the tail length
            const scale = (maxDots - index) / maxDots;
            dot.element.style.transform = `translate(-50%, -50%) scale(${scale})`;
            
            // If the mouse is stationary, fade out the trail
            if (isMoving) {
                dot.element.style.opacity = scale * 0.8;
            } else {
                dot.element.style.opacity = parseFloat(dot.element.style.opacity) * 0.9;
            }

            // Interpolate smooth step offsets to form the continuous curved string link
            x += (nextDot.x - x) * 0.35;
            y += (nextDot.y - y) * 0.35;
            
            dot.x = x;
            dot.y = y;
        });

        // Set moving check flag to false to catch idle frames smoothly
        isMoving = false;
        requestAnimationFrame(animate);
    }

    // Initialize layout path loop tracking
    setTimeout(animate, 500);
    </script>
    """,
    unsafe_allow_html=True
)


