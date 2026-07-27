import streamlit as st
import os

# Set page configuration
st.set_page_config(
    page_title="VitalSight | Remote Patient Monitoring",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom light-theme styling to match Google-style corporate pages
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Global styles override */
    html, body, [class*="css"], .stApp {
        background-color: #ffffff !important;
        color: #202124 !important;
        font-family: 'Outfit', sans-serif;
    }
    
    /* Headings styling */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #202124 !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }

    /* Remove default Streamlit header/footer padding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stAppDeployButton {
        display: none !important;
    }

    /* Custom containers */
    .hero-title {
        font-size: 3.5rem !important;
        line-height: 1.15 !important;
        margin-bottom: 1.5rem !important;
    }

    .hero-desc {
        font-size: 1.25rem !important;
        color: #5f6368 !important;
        margin-bottom: 2rem !important;
        line-height: 1.6 !important;
    }
    
    .custom-card {
        background: #ffffff;
        border: 1px solid #dadce0;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1rem;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .custom-card:hover {
        border-color: #1a73e8;
        box-shadow: 0 4px 6px rgba(32,33,36,0.08), 0 1px 3px rgba(32,33,36,0.04), 0 10px 20px rgba(0,0,0,0.05);
    }

    .icon-box {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    
    /* Navigation Bar simulation */
    .nav-bar-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 1px solid #dadce0;
        margin-bottom: 3rem;
    }

    .nav-logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1.35rem;
        font-weight: 700;
        letter-spacing: -0.03em;
        color: #202124;
    }
    
    /* Outlined Form styling for input blocks */
    div[data-testid="stForm"] {
        border: 1px solid #dadce0 !important;
        border-radius: 24px !important;
        background-color: #ffffff !important;
        padding: 2.5rem !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02) !important;
    }
    
    .team-avatar-box {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background-color: #f8f9fa;
        margin: 0 auto 1rem auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.75rem;
        font-weight: 700;
        color: #1a73e8;
        border: 2px solid #dadce0;
    }
</style>
""", unsafe_allow_html=True)

# 1. Custom Nav Bar
st.markdown("""
<div class="nav-bar-container">
    <div class="nav-logo">
        <span>❤️</span>
        <span>VitalSight</span>
    </div>
    <div style="font-size:0.9rem; color:#5f6368; font-weight:600; text-transform:uppercase; letter-spacing:0.05em;">
        Remote Patient Monitoring
    </div>
</div>
""", unsafe_allow_html=True)

# 2. Hero Section
col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    st.markdown('<h1 class="hero-title">Healthcare that follows you home.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-desc">VitalSight connects patients with their clinical care teams through seamless, automatic remote patient monitoring (RPM). Track blood pressure, weight, and vital signs with zero technology barriers.</p>', unsafe_allow_html=True)
    
    c_btn1, c_btn2, _ = st.columns([1.2, 1, 1.5])
    with c_btn1:
        st.link_button("🏥 Request Demo", "#contact", type="primary", use_container_width=True)
    with c_btn2:
        st.link_button("Learn More", "#how-it-works", use_container_width=True)

with col_right:
    # Display the mockup generated image
    image_path = "vitalsight_hero.jpg"
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.info("Mockup image loading...")

st.divider()

# 3. How It Works Section
st.markdown('<h2 style="text-align: center; margin-bottom: 1rem;" id="how-it-works">Continuous care, made simple.</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #5f6368; max-width: 700px; margin: 0 auto 3rem auto; font-size: 1.1rem;">Our HIPAA-compliant connected medical equipment automatically transmits measurements to your care team without requiring home Wi-Fi or smartphone pairings.</p>', unsafe_allow_html=True)

col_f1, col_f2, col_f3, col_f4 = st.columns(4)

with col_f1:
    st.markdown("""
    <div class="custom-card">
        <div class="icon-box">🩸</div>
        <h4>Connected BP Cuffs</h4>
        <p style="font-size:0.9rem; color:#5f6368; margin:0;">Clinically validated blood pressure cuffs automatically record and transmit systolic, diastolic, and pulse measurements.</p>
    </div>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
    <div class="custom-card">
        <div class="icon-box">⚖️</div>
        <h4>Smart Weight Telemetry</h4>
        <p style="font-size:0.9rem; color:#5f6368; margin:0;">Cellular weight scales log changes in fluid retention and body mass, helping doctors manage heart health proactively.</p>
    </div>
    """, unsafe_allow_html=True)

with col_f3:
    st.markdown("""
    <div class="custom-card">
        <div class="icon-box">📡</div>
        <h4>Zero-Config Hub</h4>
        <p style="font-size:0.9rem; color:#5f6368; margin:0;">No bluetooth pairing or Wi-Fi configuration required. Pre-configured hubs transmit securely out-of-the-box.</p>
    </div>
    """, unsafe_allow_html=True)

with col_f4:
    st.markdown("""
    <div class="custom-card">
        <div class="icon-box">📊</div>
        <h4>EMR Integration</h4>
        <p style="font-size:0.9rem; color:#5f6368; margin:0;">Measurements sync directly with Electronic Medical Record (EMR) systems, matching clinical workflows.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. Benefits Section
st.markdown('<h2 style="text-align: center; margin-bottom: 3rem;" id="benefits">Empowering patients and clinics alike.</h2>', unsafe_allow_html=True)
col_bp, col_bd = st.columns(2, gap="large")

with col_bp:
    st.markdown("""
    <div class="custom-card" style="border-radius: 20px;">
        <h3 style="border-bottom: 1px solid #dadce0; padding-bottom:0.75rem; margin-bottom:1.5rem;">💙 For Patients</h3>
        <div style="display:flex; flex-direction:column; gap:1.25rem;">
            <div>
                <strong style="color:#1a73e8; font-size:1.05rem; display:block;">✔ Zero Tech Obstacles</strong>
                <span style="font-size:0.9rem; color:#5f6368;">No logins, passwords, or smartphone requirements. Step on the scale or apply the cuff, and the rest is automated.</span>
            </div>
            <div>
                <strong style="color:#1a73e8; font-size:1.05rem; display:block;">✔ Continuous Peace of Mind</strong>
                <span style="font-size:0.9rem; color:#5f6368;">Feel secure knowing a clinic reviews your vitals curves and gets automated alerts if readings exceed set thresholds.</span>
            </div>
            <div>
                <strong style="color:#1a73e8; font-size:1.05rem; display:block;">✔ Medicare Covered</strong>
                <span style="font-size:0.9rem; color:#5f6368;">VitalSight is a fully Medicare-reimbursable service, meaning eligible patients often pay $0 out of pocket.</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_bd:
    st.markdown("""
    <div class="custom-card" style="border-radius: 20px;">
        <h3 style="border-bottom: 1px solid #dadce0; padding-bottom:0.75rem; margin-bottom:1.5rem;">🩺 For Providers</h3>
        <div style="display:flex; flex-direction:column; gap:1.25rem;">
            <div>
                <strong style="color:#1e8e3e; font-size:1.05rem; display:block;">✔ Continuous Vitals Streams</strong>
                <span style="font-size:0.9rem; color:#5f6368;">Ditch manually recorded logs. View structured, verified diagnostic curves directly within patient charts.</span>
            </div>
            <div>
                <strong style="color:#1e8e3e; font-size:1.05rem; display:block;">✔ Preventative Health Triage</strong>
                <span style="font-size:0.9rem; color:#5f6368;">Spot trends and medication needs early, keeping patients out of high-cost emergency room beds.</span>
            </div>
            <div>
                <strong style="color:#1e8e3e; font-size:1.05rem; display:block;">✔ Automatic RPM Code Billing</strong>
                <span style="font-size:0.9rem; color:#5f6368;">Systems track monitoring times and verify billing compliance automatically, generating ready-to-use billing sheets.</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 5. Creators / Team Section
st.markdown('<h2 style="text-align: center; margin-bottom: 1rem;" id="team">Our Creators</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #5f6368; max-width: 600px; margin: 0 auto 3rem auto; font-size: 1.1rem;">VitalSight was designed by an enthusiastic student team and faculty mentor committed to bringing medical diagnostics home.</p>', unsafe_allow_html=True)

col_t1, col_t2, col_t3, col_t4 = st.columns(4)

with col_t1:
    st.markdown("""
    <div class="custom-card" style="text-align:center; padding: 2rem 1rem;">
        <div class="team-avatar-box">SV</div>
        <h5 style="margin-bottom:0.25rem;">Shivanesh V</h5>
        <span style="color:#1a73e8; font-size:0.8rem; font-weight:700; letter-spacing:0.05em; display:block; margin-bottom:0.75rem; text-transform:uppercase;">Lead Product Engineer</span>
        <p style="font-size:0.8rem; color:#5f6368; margin:0;">Oversees software architecture, EMR database schemas, and vital telemetry pipelines.</p>
    </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
    <div class="custom-card" style="text-align:center; padding: 2rem 1rem;">
        <div class="team-avatar-box">RM</div>
        <h5 style="margin-bottom:0.25rem;">Ragavendra M</h5>
        <span style="color:#1a73e8; font-size:0.8rem; font-weight:700; letter-spacing:0.05em; display:block; margin-bottom:0.75rem; text-transform:uppercase;">UX Designer</span>
        <p style="font-size:0.8rem; color:#5f6368; margin:0;">Focuses on crafting clean, intuitive patient interfaces and web application views.</p>
    </div>
    """, unsafe_allow_html=True)

with col_t3:
    st.markdown("""
    <div class="custom-card" style="text-align:center; padding: 2rem 1rem;">
        <div class="team-avatar-box">VV</div>
        <h5 style="margin-bottom:0.25rem;">Venkataraam VG</h5>
        <span style="color:#1a73e8; font-size:0.8rem; font-weight:700; letter-spacing:0.05em; display:block; margin-bottom:0.75rem; text-transform:uppercase;">IoT Hardware Lead</span>
        <p style="font-size:0.8rem; color:#5f6368; margin:0;">Implements hardware drivers, low-energy cellular boards, and diagnostic firmware.</p>
    </div>
    """, unsafe_allow_html=True)

with col_t4:
    st.markdown("""
    <div class="custom-card" style="text-align:center; padding: 2rem 1rem; border-color:#1e8e3e;">
        <div class="team-avatar-box" style="color:#1e8e3e; background-color:rgba(30,142,62,0.05);">RK</div>
        <h5 style="margin-bottom:0.25rem;">Dr. Raj Karkee (Mentor)</h5>
        <span style="color:#1e8e3e; font-size:0.8rem; font-weight:700; letter-spacing:0.05em; display:block; margin-bottom:0.75rem; text-transform:uppercase;">Faculty Advisor</span>
        <p style="font-size:0.8rem; color:#5f6368; margin:0;">Provides academic and clinical oversight, validating diagnostic pipeline research.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 6. Contact Form Section
st.markdown('<h2 style="text-align: center; margin-bottom: 3rem;" id="contact">Partner with VitalSight</h2>', unsafe_allow_html=True)

col_cinfo, col_cform = st.columns([1, 1.2], gap="large")

with col_cinfo:
    st.markdown("### Inquiry Details")
    st.write("Interested in piloting Remote Patient Monitoring in your health system? Let's discuss clinical objectives, EMR integrations, and device deployment frameworks.")
    
    st.markdown("""
    <div style="margin-top:2rem; display:flex; flex-direction:column; gap:1.5rem;">
        <div style="display:flex; gap:1rem; align-items:flex-start;">
            <div style="font-size:1.25rem; color:#1a73e8;">📧</div>
            <div>
                <strong style="display:block;">General Information</strong>
                <span style="font-size:0.9rem; color:#5f6368;">info@vitalsight.io</span>
            </div>
        </div>
        <div style="display:flex; gap:1rem; align-items:flex-start;">
            <div style="font-size:1.25rem; color:#1a73e8;">📞</div>
            <div>
                <strong style="display:block;">Phone Support</strong>
                <span style="font-size:0.9rem; color:#5f6368;">+91 8939917000 / 044 7111 9111</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_cform:
    with st.form("contact_form", clear_on_submit=True):
        f_name = st.text_input("Full Name", placeholder="Your name")
        f_email = st.text_input("Email Address", placeholder="yourname@domain.com")
        f_org = st.text_input("Organization", placeholder="Clinic or Hospital name")
        f_msg = st.text_area("How can we help you?", placeholder="Describe your clinics RPM objectives...")
        
        submitted = st.form_submit_form_button("Send Demo Request", type="primary", use_container_width=True)
        
        if submitted:
            if not f_name or not f_email or not f_org or not f_msg:
                st.error("Please fill in all the fields before submitting.")
            else:
                st.success(f"Thank you, {f_name}! Your request for {f_org} has been submitted. A clinical support specialist will email you at {f_email} within 24 hours.")

# 7. Corporate Footer
st.markdown("""
<div style="background-color:#f8f9fa; border-top:1px solid #dadce0; margin-top:5rem; padding: 2.5rem 1rem; text-align:center; color:#5f6368; font-size:0.85rem; width:100%;">
    <p style="margin-bottom:0.25rem;">&copy; 2026 VitalSight Systems Inc. All rights reserved.</p>
    <p style="font-size:0.75rem; color:#80868b;">Developed for CIT Technical Competitions (competitions@citchennai.net).</p>
</div>
""", unsafe_allow_html=True)
