import streamlit as st
import json
import os
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Diagnostics Result JSON Web Viewer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Custom Styling to match the original glassmorphism
st.markdown("""
<style>
    /* Import font */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Code styling */
    code, pre, [data-testid="stCode"] {
        font-family: 'Fira Code', monospace !important;
    }

    /* Glassmorphism containers */
    div[data-testid="stMetric"] {
        background: rgba(23, 27, 54, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 15px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Status Badge styling classes */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.025em;
        text-transform: uppercase;
    }
    .badge-passed { background: rgba(16, 185, 129, 0.1); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); }
    .badge-failed { background: rgba(239, 68, 68, 0.1); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.2); }
    .badge-warning { background: rgba(245, 158, 11, 0.1); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.2); }
    .badge-nodevice { background: rgba(100, 116, 139, 0.1); color: #64748b; border: 1px solid rgba(100, 116, 139, 0.2); }

    /* Custom layout containers */
    .custom-card {
        background: rgba(23, 27, 54, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Troubleshooter styling */
    .troubleshooter-panel {
        background: rgba(239, 68, 68, 0.08);
        border: 1px dashed rgba(239, 68, 68, 0.3);
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Hide default Streamlit decoration */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Helper function to format duration
def format_duration(duration_dict):
    if not duration_dict:
        return "N/A"
    seconds = duration_dict.get("Seconds", 0)
    nanos = duration_dict.get("Nanos", 0)
    total_secs = seconds + nanos / 1e9
    if total_secs < 1:
        return f"{round(total_secs * 1000)}ms"
    return f"{total_secs:.2f}s"

# Helper function to format ISO timestamps
def format_time(iso_str):
    if not iso_str:
        return "N/A"
    try:
        # standard ISO format parsing
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%I:%M:%S %p (%Y-%m-%d)")
    except:
        return iso_str

# Get context-specific troubleshooting advice
def get_troubleshooting_tips(test_name):
    tips = []
    name = test_name.lower()
    if "keyboard" in name:
        tips.extend([
            "Verify that no keys are physically stuck or jammed.",
            "If using an external USB keyboard, try reconnecting or changing USB ports.",
            "Inspect the keyboard layouts in Windows Settings to ensure the active layout matches your physical keyboard."
        ])
    elif any(x in name for x in ["audio", "speaker", "microphone"]):
        tips.extend([
            "Check if the device is muted in Windows Volume Mixer.",
            "Check microphone access permissions in Settings > Privacy & Security.",
            "Reinstall or update the audio driver (Realtek High Definition Audio, etc.)."
        ])
    elif any(x in name for x in ["network", "wireless", "bluetooth"]):
        tips.extend([
            "Ensure Airplane Mode is toggled off and wireless hardware is enabled.",
            "Try resetting your TCP/IP settings or rebooting your network router.",
            "Verify the physical Wi-Fi/Bluetooth antennas are properly attached to the motherboard."
        ])
    elif any(x in name for x in ["battery", "charger"]):
        tips.extend([
            "Ensure you are using the official Dell power adapter supplying correct wattage.",
            "If battery warning exists, check battery health metrics inside Windows or Dell SupportAssist.",
            "Try discharging the battery fully and then recharging it uninterrupted."
        ])
    elif any(x in name for x in ["video", "display", "camera"]):
        tips.extend([
            "Verify graphics card drivers are updated to the latest stable release.",
            "If using external displays, verify HDMI/DisplayPort cable integrity.",
            "For webcam failures, check if the camera shutter slider is physically open."
        ])
    else:
        tips.extend([
            "Run the default Windows Hardware Troubleshooter.",
            "Consult the Dell System Diagnostics Code Book using the Status Codes provided in subtests."
        ])
    
    tips.extend([
        "Restart your system and rerun diagnostics to verify if it is a transient error.",
        "Check Dell SupportAssist for system updates."
    ])
    return tips

# App Header
st.title("⚡ Diagnostics Result JSON Web Viewer")
st.caption("A premium web-based diagnostics log analyzer. Upload a Dell Diagnostics JSON file to get started.")

# Sidebar File Loading Options
with st.sidebar:
    st.header("📂 Data Source")
    
    # Checkbox to load sample
    use_sample = st.checkbox("Load Sample File (FullResult.json)", value=True)
    
    # File uploader
    uploaded_file = st.file_uploader("Upload Diagnostics JSON", type=["json"])
    
    st.divider()

# Load Data logic
data = None
if uploaded_file is not None:
    try:
        data = json.load(uploaded_file)
    except Exception as e:
        st.error(f"Error parsing uploaded JSON: {e}")
elif use_sample:
    sample_path = "FullResult.json"
    if os.path.exists(sample_path):
        try:
            with open(sample_path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            st.error(f"Error loading local sample file: {e}")
    else:
        st.warning("Sample file 'FullResult.json' not found in workspace. Please upload a file manually.")

# Process and Render Dashboard if Data loaded
if data:
    # 1. System Info Parsing
    sys_info = data.get("SystemInfo", {})
    
    # Render System Info in Sidebar
    with st.sidebar:
        st.subheader("🖥️ System Information")
        st.markdown(f"**Product Name:** `{sys_info.get('ProductName', 'N/A')}`")
        st.markdown(f"**BIOS Version:** `{sys_info.get('BiosVersion', 'N/A')}`")
        st.markdown(f"**Service Tag:** `{sys_info.get('SerialNumber', 'N/A')}`")
        st.markdown(f"**Host Name:** `{sys_info.get('HostName', 'N/A')}`")
        st.markdown(f"**OS Friendly Name:** `{sys_info.get('OSFriendlyName', 'N/A')}`")
        st.markdown(f"**OS Build:** `{sys_info.get('OSVersion', 'N/A')}`")
        st.markdown(f"**Diagnostics Build:** *{sys_info.get('DellDiagnostics', 'N/A')}*")

    # 2. Parse Test Results
    tests = []
    test_index = 0
    test_set_results = data.get("AdditionalInfo", {}).get("testSetResults", [])
    
    for test_set in test_set_results:
        test_results = test_set.get("testResults", [])
        for test_res in test_results:
            test_name = test_res.get("testName", "Unknown Test")
            device_results = test_res.get("deviceResults", [])
            
            if device_results:
                for dev_res in device_results:
                    device_name = dev_res.get("deviceName", "")
                    
                    # Status determination
                    status = "Passed"
                    overall = dev_res.get("overallResults", [])
                    subtests = dev_res.get("subtestUpdates", [])
                    
                    if overall:
                        status = overall[0].get("ResultString", "Passed")
                    elif subtests:
                        status = subtests[0].get("ResultKey", "Passed")
                        
                    tests.append({
                        "id": test_index,
                        "testName": test_name,
                        "deviceName": device_name,
                        "result": status,
                        "subtests": subtests,
                        "rawJson": test_res
                    })
                    test_index += 1
            else:
                tests.append({
                    "id": test_index,
                    "testName": test_name,
                    "deviceName": "No Hardware Device Linked",
                    "result": "NoDevice",
                    "subtests": [],
                    "rawJson": test_res
                })
                test_index += 1

    # 3. Calculate metrics
    total_tests = len(tests)
    passed_tests = sum(1 for t in tests if t["result"].lower() == "passed")
    failed_tests = sum(1 for t in tests if t["result"].lower() == "failed")
    warning_tests = sum(1 for t in tests if t["result"].lower() == "warning")
    nodevice_tests = sum(1 for t in tests if t["result"].lower() == "nodevice")
    
    pass_rate = round((passed_tests / total_tests) * 100) if total_tests > 0 else 0

    # 4. Metrics Dashboard Display
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Tests", total_tests)
    with col2:
        st.metric("Passed (Green)", passed_tests, f"{pass_rate}% Pass Rate")
    with col3:
        st.metric("Failed (Red)", failed_tests, delta=f"-{failed_tests}" if failed_tests > 0 else None, delta_color="inverse")
    with col4:
        st.metric("Warnings (Amber)", warning_tests)
    with col5:
        st.metric("No Device (Slate)", nodevice_tests)

    st.divider()

    # 5. Splitscreen Search, Filter & Table View
    col_table, col_detail = st.columns([1, 1])

    with col_table:
        st.subheader("🔍 Diagnostic Test Logs")
        
        # Search and filter options
        search_query = st.text_input("Search logs by test name or device key", "").strip().lower()
        
        status_filter = st.pills(
            "Filter by status",
            options=["All", "Passed", "Failed", "Warning", "No Device"],
            default="All"
        )
        
        # Filter tests
        filtered_tests = []
        for t in tests:
            # Status filter match
            if status_filter != "All":
                status_slug = status_filter.replace(" ", "").lower()
                if t["result"].lower() != status_slug:
                    continue
            
            # Search query match
            if search_query:
                in_name = search_query in t["testName"].lower()
                in_device = search_query in t["deviceName"].lower()
                if not (in_name or in_device):
                    continue
                    
            filtered_tests.append(t)
            
        if not filtered_tests:
            st.info("No diagnostic logs match the active query.")
        else:
            # Dropdown selection representing rows
            selected_test = st.selectbox(
                "Click to select which test device to inspect:",
                options=filtered_tests,
                format_func=lambda x: f"[{x['result'].upper()}] {x['testName']} — {x['deviceName'] or 'None'}"
            )

    # 6. Detailed Inspection View (Right Panel)
    with col_detail:
        st.subheader("📋 Inspection Details")
        
        if 'selected_test' in locals() and selected_test:
            # Test Header Card
            badge_class = f"badge badge-{selected_test['result'].lower()}"
            st.markdown(f"""
            <div class="custom-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="margin:0;">{selected_test['testName']}</h3>
                    <span class="{badge_class}">{selected_test['result'].upper()}</span>
                </div>
                <div style="font-family:'Fira Code', monospace; font-size:0.85rem; color:#94a3b8; margin-top:0.5rem; word-break:break-all;">
                    <b>Hardware Key:</b> {selected_test['deviceName'] or 'No Device Mapped'}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Troubleshooter Panel if Failed or Warning
            if selected_test['result'].lower() in ["failed", "warning"]:
                tips = get_troubleshooting_tips(selected_test['testName'])
                tips_html = "".join([f"<li>{tip}</li>" for tip in tips])
                st.markdown(f"""
                <div class="troubleshooter-panel">
                    <strong style="color:#ef4444; font-size:0.9rem; text-transform:uppercase; letter-spacing:0.05em; display:block; margin-bottom:0.5rem;">
                        ⚠️ Troubleshooting Recommendations
                    </strong>
                    <ul style="font-size:0.85rem; padding-left:1.2rem; color:#94a3b8;">
                        {tips_html}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            # Subtests details
            subtests = selected_test['subtests']
            st.markdown("#### Subtest Metrics")
            if not subtests:
                st.info("No detailed progress metrics or subtest steps reported for this device result.")
            else:
                for sub in subtests:
                    sub_result = sub.get("ResultKey", "Passed")
                    sub_badge_class = f"badge badge-{sub_result.lower()}"
                    
                    with st.container(border=True):
                        st.markdown(f"""
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.5rem;">
                            <strong>{sub.get('TestName', 'Diagnostic Subtest')}</strong>
                            <span class="{sub_badge_class}">{sub_result}</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Subtest details columns
                        c_meta1, c_meta2 = st.columns(2)
                        with c_meta1:
                            st.markdown(f"**Status Code:** `{sub.get('StatusCode', 'N/A')}`")
                            st.markdown(f"**Started:** {format_time(sub.get('StartTime'))}")
                        with c_meta2:
                            st.markdown(f"**Duration:** {format_duration(sub.get('Duration'))}")
                            st.markdown(f"**Action Key:** `{sub.get('TestKey', 'N/A')}`")
                        
                        # Subtest progress bar
                        prog = sub.get("Progress", 100)
                        st.progress(prog / 100.0, text=f"Subtest completion: {prog}%")
                        
                        # Errors
                        if sub.get("ErrorCodeDescription"):
                            st.error(f"**Error Description:** {sub.get('ErrorCodeDescription')}")

            # Collapsible RAW JSON Section
            with st.expander("🔍 Inspect Raw JSON Payload"):
                st.json(selected_test['rawJson'])
        else:
            st.info("Please select a diagnostic test log from the dropdown picker on the left.")

else:
    st.info("Please upload a Dell Diagnostics JSON file or click 'Load Sample File' in the sidebar to populate the dashboard viewer.")
