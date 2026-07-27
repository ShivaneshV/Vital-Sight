import streamlit as st
import os
import base64

# Helper function to convert local image to base64 for HTML injection
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

logo_base64 = get_base64_image("logo.png")

# Set page configuration
st.set_page_config(
    page_title="VitalSight | Remote Patient Monitoring",
    page_icon="logo.png" if os.path.exists("logo.png") else "❤️",
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
        gap: 0.85rem;
        font-size: 1.85rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        color: #202124;
    }
    
    /* Fix input text visibility and override dark-mode styles */
    input, textarea, select, div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #ffffff !important;
        color: #202124 !important;
    }
    
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #202124 !important;
        border: 1px solid #dadce0 !important;
    }
    
    .stTextInput label, .stTextArea label {
        color: #202124 !important;
        font-weight: 600 !important;
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
logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="height:56px; width:auto; border-radius:4px; vertical-align:middle; margin-right:8px;">' if logo_base64 else '<span>❤️</span>'

st.markdown(f"""
<div class="nav-bar-container">
    <div class="nav-logo">
        {logo_html}
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
    
    st.markdown("""
    <div style="display: flex; gap: 1rem; margin-top: 1rem;">
        <button onclick="try { (window.parent.document.getElementById('contact') || document.getElementById('contact')).scrollIntoView({behavior: 'smooth'}) } catch(e) { document.getElementById('contact').scrollIntoView({behavior: 'smooth'}) }" style="padding: 0.85rem 2rem; border: none; font-weight: 600; font-size: 0.95rem; border-radius: 9999px; background-color: #1a73e8; color: white; cursor: pointer; display: inline-flex; align-items: center; gap: 0.5rem;">🏥 Request Demo</button>
        <button onclick="try { (window.parent.document.getElementById('how-it-works') || document.getElementById('how-it-works')).scrollIntoView({behavior: 'smooth'}) } catch(e) { document.getElementById('how-it-works').scrollIntoView({behavior: 'smooth'}) }" style="padding: 0.85rem 2rem; border: 1px solid #dadce0; font-weight: 600; font-size: 0.95rem; border-radius: 9999px; background-color: transparent; color: #1a73e8; cursor: pointer; display: inline-block;">Learn More</button>
    </div>
    """, unsafe_allow_html=True)

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

# 3.5 Technology Section
st.markdown('<h2 style="text-align: center; margin-bottom: 1rem;" id="technology">The Science of Contactless AI Health Triage</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #5f6368; max-width: 700px; margin: 0 auto 3rem auto; font-size: 1.1rem;">VitalSight leverages advanced computer vision and neural networks to extract diagnostic vitals without physical sensor contact.</p>', unsafe_allow_html=True)

col_tech1, col_tech2 = st.columns(2, gap="large")

with col_tech1:
    st.markdown("""
    <div class="custom-card" style="border-radius: 20px;">
        <h3 style="border-bottom: 1px solid #dadce0; padding-bottom:0.75rem; margin-bottom:1.5rem;">📸 Remote Photoplethysmography (rPPG)</h3>
        <div style="display:flex; flex-direction:column; gap:1.25rem;">
            <div>
                <strong style="color:#1a73e8; font-size:1.05rem; display:block;">■ Facial Capillary Analysis</strong>
                <span style="font-size:0.9rem; color:#5f6368;">Using any standard smartphone camera or webcam, our algorithm tracks microscopic color fluctuations in facial skin tissue. These fluctuations are caused by sub-visual blood volume changes during cardiac cycles.</span>
            </div>
            <div>
                <strong style="color:#1a73e8; font-size:1.05rem; display:block;">■ Three-Channel Sensor Fusion</strong>
                <span style="font-size:0.9rem; color:#5f6368;">The system separates light reflections into RGB channels, filters ambient lighting interference, and calculates heart rate (HR), respiration rate (RR), and blood oxygen saturation (SpO2) concurrently with clinical-grade precision.</span>
            </div>
            <div>
                <strong style="color:#1a73e8; font-size:1.05rem; display:block;">■ Motion & Blink Artifact Rejection</strong>
                <span style="font-size:0.9rem; color:#5f6368;">Adaptive filters track facial landmarks in real time, filtering out speech movements, head rotations, and blinks to isolate the true underlying photoplethysmogram wave.</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_tech2:
    st.markdown("""
    <div class="custom-card" style="border-radius: 20px;">
        <h3 style="border-bottom: 1px solid #dadce0; padding-bottom:0.75rem; margin-bottom:1.5rem;">🧠 Predictive Neural Triage Core</h3>
        <div style="display:flex; flex-direction:column; gap:1.25rem;">
            <div>
                <strong style="color:#1e8e3e; font-size:1.05rem; display:block;">■ Multimodal Temporal Classifiers</strong>
                <span style="font-size:0.9rem; color:#5f6368;">Recurrent Neural Networks (RNN) and LSTM layers evaluate vital time-series sequences to forecast patient deterioration patterns over 24-hour windows.</span>
            </div>
            <div>
                <strong style="color:#1e8e3e; font-size:1.05rem; display:block;">■ MEWS Scoring Automation</strong>
                <span style="font-size:0.9rem; color:#5f6368;">VitalSight automatically calculates patient Modified Early Warning Scores (MEWS). It flags critical vital anomalies, helping clinics prioritize patients based on diagnostic risk levels.</span>
            </div>
            <div>
                <strong style="color:#1e8e3e; font-size:1.05rem; display:block;">■ Secure Clinical Alerting</strong>
                <span style="font-size:0.9rem; color:#5f6368;">When alert thresholds are crossed, encrypted warning payloads are routed to on-duty providers, enabling immediate virtual consultations or emergency interventions.</span>
            </div>
        </div>
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
                <span style="font-size:0.9rem; color:#5f6368;">shivanesh995@gmail.com</span>
            </div>
        </div>
        <div style="display:flex; gap:1rem; align-items:flex-start;">
            <div style="font-size:1.25rem; color:#1a73e8;">📞</div>
            <div>
                <strong style="display:block;">Phone Support</strong>
                <span style="font-size:0.9rem; color:#5f6368;">+91 6382892269</span>
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
        
        submitted = st.form_submit_button("Send Demo Request", type="primary", use_container_width=True)
        
        if submitted:
            if not f_name or not f_email or not f_org or not f_msg:
                st.error("Please fill in all the fields before submitting.")
            else:
                import urllib.parse
                st.success(f"Thank you, {f_name}! Please click the button below to send your request directly to shivanesh995@gmail.com.")
                subject = urllib.parse.quote(f"VitalSight Demo Request - {f_org}")
                body = urllib.parse.quote(f"Name: {f_name}\nEmail: {f_email}\nOrganization: {f_org}\nMessage: {f_msg}")
                mailto_url = f"mailto:shivanesh995@gmail.com?subject={subject}&body={body}"
                st.link_button("✉️ Open Mail Client to Send Request", mailto_url, type="primary", use_container_width=True)

# 7. Corporate Footer
st.markdown("""
<div style="background-color:#f8f9fa; border-top:1px solid #dadce0; margin-top:5rem; padding: 2.5rem 1rem; text-align:center; color:#5f6368; font-size:0.85rem; width:100%;">
    <p style="margin-bottom:0.25rem;">&copy; 2026 VitalSight Systems Inc. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
