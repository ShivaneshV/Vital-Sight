// State Management
let appState = {
    systemInfo: null,
    tests: [],
    currentFilter: 'all',
    searchQuery: '',
    selectedTestId: null
};

// UI Elements
const uploadScreen = document.getElementById('uploadScreen');
const dashboardScreen = document.getElementById('dashboardScreen');
const headerActions = document.getElementById('headerActions');
const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('fileInput');
const btnLoadSample = document.getElementById('btnLoadSample');
const btnReset = document.getElementById('btnReset');
const systemInfoRows = document.getElementById('systemInfoRows');
const testTableBody = document.getElementById('testTableBody');
const tableSearch = document.getElementById('tableSearch');
const detailPane = document.getElementById('detailPane');
const detailEmptyState = document.getElementById('detailEmptyState');
const detailContent = document.getElementById('detailContent');
const detailTestName = document.getElementById('detailTestName');
const detailStatusBadge = document.getElementById('detailStatusBadge');
const detailDeviceName = document.getElementById('detailDeviceName');
const subtestsList = document.getElementById('subtestsList');
const tipsPanel = document.getElementById('tipsPanel');
const tipsList = document.getElementById('tipsList');
const detailRawJson = document.getElementById('detailRawJson');

// Collapsible raw JSON elements
const jsonCollapsibleTrigger = document.getElementById('jsonCollapsibleTrigger');
const jsonCollapsibleContent = document.getElementById('jsonCollapsibleContent');
const jsonTriggerIcon = document.getElementById('jsonTriggerIcon');

// Metrics elements
const metricTotal = document.getElementById('metricTotal');
const metricPassed = document.getElementById('metricPassed');
const metricFailed = document.getElementById('metricFailed');
const metricWarning = document.getElementById('metricWarning');
const metricNoDevice = document.getElementById('metricNoDevice');
const pctPassed = document.getElementById('pctPassed');
const pctFailed = document.getElementById('pctFailed');
const pctWarning = document.getElementById('pctWarning');
const pctNoDevice = document.getElementById('pctNoDevice');
const radialProgressFill = document.getElementById('radialProgressFill');
const radialProgressText = document.getElementById('radialProgressText');

// Event Listeners for File Upload
dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.classList.add('dragover');
});

dropzone.addEventListener('dragleave', () => {
    dropzone.classList.remove('dragover');
});

dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFile(e.target.files[0]);
    }
});

// Load sample diagnostics file
btnLoadSample.addEventListener('click', () => {
    fetchSampleData();
});

btnReset.addEventListener('click', () => {
    resetToUploadScreen();
});

// Search functionality
tableSearch.addEventListener('input', (e) => {
    appState.searchQuery = e.target.value.toLowerCase();
    applyFilterAndRender();
});

// Collapsible Trigger for raw JSON
jsonCollapsibleTrigger.addEventListener('click', () => {
    const isVisible = jsonCollapsibleContent.style.display === 'block';
    jsonCollapsibleContent.style.display = isVisible ? 'none' : 'block';
    jsonTriggerIcon.style.transform = isVisible ? 'rotate(0deg)' : 'rotate(180deg)';
});

// Metric Cards interactive filters
document.querySelectorAll('.metric-card').forEach(card => {
    card.addEventListener('click', () => {
        document.querySelectorAll('.metric-card').forEach(c => c.classList.remove('active'));
        card.classList.add('active');
        appState.currentFilter = card.dataset.filter;
        applyFilterAndRender();
    });
});

// Fetch Sample Diagnostics JSON
function fetchSampleData() {
    fetch('FullResult.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Local file fetch blocked or failed');
            }
            return response.json();
        })
        .then(data => {
            processDiagnosticsData(data);
        })
        .catch(error => {
            console.error('Error fetching sample data relative: ', error);
            // Display instructions to select file manually if CORS/Local Fetch is blocked
            alert('Unable to load sample automatically (typically blocked by browser security/CORS when run locally via file://).\n\nPlease select the "FullResult.json" file using the file selector to run it locally!');
        });
}

// Handle File Processing
function handleFile(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
        try {
            const data = JSON.parse(e.target.result);
            processDiagnosticsData(data);
        } catch (error) {
            alert('Invalid JSON file format. Please check the file contents.');
            console.error('JSON Parse error: ', error);
        }
    };
    reader.readAsText(file);
}

// Reset view
function resetToUploadScreen() {
    appState = {
        systemInfo: null,
        tests: [],
        currentFilter: 'all',
        searchQuery: '',
        selectedTestId: null
    };
    
    // UI state reset
    fileInput.value = '';
    tableSearch.value = '';
    
    // Hide dashboard, show upload
    dashboardScreen.style.display = 'none';
    headerActions.style.display = 'none';
    uploadScreen.style.display = 'flex';
    
    // Reset selection state
    detailContent.style.display = 'none';
    detailEmptyState.style.display = 'flex';
    document.querySelectorAll('.metric-card').forEach(c => {
        c.classList.remove('active');
        if (c.dataset.filter === 'all') c.classList.add('active');
    });
}

// Process Diagnostics JSON
function processDiagnosticsData(data) {
    if (!data.SystemInfo) {
        alert('Format mismatch: Missing required SystemInfo section.');
        return;
    }
    
    appState.systemInfo = data.SystemInfo;
    appState.tests = [];
    
    let testIndex = 0;
    
    // Parse test results
    if (data.AdditionalInfo && data.AdditionalInfo.testSetResults) {
        data.AdditionalInfo.testSetResults.forEach(testSet => {
            if (testSet.testResults) {
                testSet.testResults.forEach(testResult => {
                    const testName = testResult.testName || "Unknown Test";
                    
                    if (testResult.deviceResults && testResult.deviceResults.length > 0) {
                        testResult.deviceResults.forEach(deviceResult => {
                            const deviceName = deviceResult.deviceName || "";
                            
                            // Determine test outcome
                            let status = "Passed";
                            if (deviceResult.overallResults && deviceResult.overallResults.length > 0) {
                                status = deviceResult.overallResults[0].ResultString || "Passed";
                            } else if (deviceResult.subtestUpdates && deviceResult.subtestUpdates.length > 0) {
                                // Fallback to subtest outcome
                                status = deviceResult.subtestUpdates[0].ResultKey || "Passed";
                            }
                            
                            appState.tests.push({
                                id: testIndex++,
                                testName: testName,
                                deviceName: deviceName,
                                result: status,
                                subtests: deviceResult.subtestUpdates || [],
                                rawJson: testResult
                            });
                        });
                    } else {
                        // Test has no devices listed
                        appState.tests.push({
                            id: testIndex++,
                            testName: testName,
                            deviceName: "No Hardware Device Linked",
                            result: "NoDevice",
                            subtests: [],
                            rawJson: testResult
                        });
                    }
                });
            }
        });
    }
    
    // Populate Views
    renderSystemInfo();
    renderMetrics();
    applyFilterAndRender();
    
    // Toggle Screens
    uploadScreen.style.display = 'none';
    headerActions.style.display = 'flex';
    dashboardScreen.style.display = 'block';
}

// Render System Info
function renderSystemInfo() {
    const info = appState.systemInfo;
    if (!info) return;
    
    systemInfoRows.innerHTML = `
        <div class="info-row">
            <span class="info-label">Product Name</span>
            <span class="info-value">${info.ProductName || 'Unknown Product'}</span>
        </div>
        <div class="info-row">
            <span class="info-label">BIOS Version</span>
            <span class="info-value mono">${info.BiosVersion || 'N/A'}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Service Tag / SN</span>
            <span class="info-value mono">${info.SerialNumber || 'N/A'}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Host Name</span>
            <span class="info-value">${info.HostName || 'N/A'}</span>
        </div>
        <div class="info-row">
            <span class="info-label">OS Type</span>
            <span class="info-value">${info.OSFriendlyName || 'Windows'}</span>
        </div>
        <div class="info-row">
            <span class="info-label">OS Build</span>
            <span class="info-value mono">${info.OSVersion || 'N/A'}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Diagnostics Kit</span>
            <span class="info-value" style="font-size:0.8rem; color:var(--text-secondary);">${info.DellDiagnostics || 'N/A'}</span>
        </div>
    `;
}

// Render Metrics & Counters
function renderMetrics() {
    const total = appState.tests.length;
    const passed = appState.tests.filter(t => t.result.toLowerCase() === 'passed').length;
    const failed = appState.tests.filter(t => t.result.toLowerCase() === 'failed').length;
    const warning = appState.tests.filter(t => t.result.toLowerCase() === 'warning').length;
    const nodevice = appState.tests.filter(t => t.result.toLowerCase() === 'nodevice').length;
    
    // Set counters
    metricTotal.textContent = total;
    metricPassed.textContent = passed;
    metricFailed.textContent = failed;
    metricWarning.textContent = warning;
    metricNoDevice.textContent = nodevice;
    
    // Set percentages
    pctPassed.textContent = total > 0 ? `${Math.round((passed / total) * 100)}% of total` : '0%';
    pctFailed.textContent = total > 0 ? `${Math.round((failed / total) * 100)}% of total` : '0%';
    pctWarning.textContent = total > 0 ? `${Math.round((warning / total) * 100)}% of total` : '0%';
    pctNoDevice.textContent = total > 0 ? `${Math.round((nodevice / total) * 100)}% of total` : '0%';
    
    // Update Radial Progress (Pass Rate)
    const passRate = total > 0 ? Math.round((passed / total) * 100) : 0;
    radialProgressText.textContent = `${passRate}%`;
    
    // Stroke calculation (radial offset)
    // Circumference = 2 * PI * r = 2 * 3.14159 * 36 = 226
    const strokeOffset = 226 - (226 * passRate) / 100;
    radialProgressFill.style.strokeDashoffset = strokeOffset;
}

// Apply Filters (Search and Status Selection) and Render Table
function applyFilterAndRender() {
    const filtered = appState.tests.filter(test => {
        // Status Filter
        if (appState.currentFilter !== 'all' && test.result.toLowerCase() !== appState.currentFilter) {
            return false;
        }
        
        // Search Filter
        if (appState.searchQuery) {
            const nameMatch = test.testName.toLowerCase().includes(appState.searchQuery);
            const devMatch = test.deviceName.toLowerCase().includes(appState.searchQuery);
            return nameMatch || devMatch;
        }
        
        return true;
    });
    
    renderTestTable(filtered);
}

// Render Table Rows
function renderTestTable(testsListArray) {
    testTableBody.innerHTML = '';
    
    if (testsListArray.length === 0) {
        testTableBody.innerHTML = `
            <tr>
                <td colspan="3" style="text-align: center; color: var(--text-muted); padding: 3rem 1rem;">
                    No diagnostics records match the active filters.
                </td>
            </tr>
        `;
        return;
    }
    
    testsListArray.forEach(test => {
        const row = document.createElement('tr');
        if (appState.selectedTestId === test.id) {
            row.classList.add('selected');
        }
        
        const badgeClass = `badge badge-${test.result.toLowerCase()}`;
        
        row.innerHTML = `
            <td><span class="${badgeClass}">${test.result}</span></td>
            <td style="font-weight: 500;">${test.testName}</td>
            <td class="mono" style="font-size: 0.8rem; color: var(--text-secondary); max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                ${test.deviceName || 'None'}
            </td>
        `;
        
        row.addEventListener('click', () => {
            document.querySelectorAll('#testTableBody tr').forEach(r => r.classList.remove('selected'));
            row.classList.add('selected');
            appState.selectedTestId = test.id;
            renderTestDetails(test);
        });
        
        testTableBody.appendChild(row);
    });
}

// Helper to format duration
function formatDuration(durationObj) {
    if (!durationObj) return 'N/A';
    let secs = durationObj.Seconds || 0;
    let nanos = durationObj.Nanos || 0;
    let totalSecs = secs + nanos / 1000000000;
    
    if (totalSecs < 1) {
        return `${Math.round(totalSecs * 1000)}ms`;
    }
    return `${totalSecs.toFixed(2)}s`;
}

// Helper to format timestamps
function formatTime(isoString) {
    if (!isoString) return 'N/A';
    try {
        const d = new Date(isoString);
        return d.toLocaleTimeString() + ' (' + d.toLocaleDateString() + ')';
    } catch {
        return isoString;
    }
}

// Render detailed analysis panel on the right
function renderTestDetails(test) {
    detailEmptyState.style.display = 'none';
    detailContent.style.display = 'flex';
    
    // Set Header
    detailTestName.textContent = test.testName;
    detailStatusBadge.textContent = test.result;
    detailStatusBadge.className = `badge badge-${test.result.toLowerCase()}`;
    detailDeviceName.textContent = test.deviceName || 'No device details mapped';
    
    // Populate raw JSON viewer (collapsed initially)
    detailRawJson.textContent = JSON.stringify(test.rawJson, null, 2);
    jsonCollapsibleContent.style.display = 'none';
    jsonTriggerIcon.style.transform = 'rotate(0deg)';
    
    // Populate Troubleshooter/Tips if Failed or Warning
    if (test.result.toLowerCase() === 'failed' || test.result.toLowerCase() === 'warning') {
        tipsPanel.style.display = 'block';
        tipsList.innerHTML = '';
        
        const recommendations = getTroubleshootingTips(test);
        recommendations.forEach(tip => {
            const li = document.createElement('li');
            li.textContent = tip;
            tipsList.appendChild(li);
        });
    } else {
        tipsPanel.style.display = 'none';
    }
    
    // Populate Subtests Actions List
    subtestsList.innerHTML = '';
    
    if (test.subtests.length === 0) {
        subtestsList.innerHTML = `
            <div style="color: var(--text-muted); font-size: 0.85rem; padding: 1rem 0;">
                No explicit subtests or progress logs reported for this device result.
            </div>
        `;
        return;
    }
    
    test.subtests.forEach(subtest => {
        const subtestCard = document.createElement('div');
        subtestCard.className = 'subtest-card';
        
        const subResultKey = subtest.ResultKey || 'Passed';
        const subBadgeClass = `badge badge-${subResultKey.toLowerCase()}`;
        const pct = subtest.Progress !== undefined ? subtest.Progress : 100;
        
        subtestCard.innerHTML = `
            <div class="subtest-card-header">
                <span class="subtest-name">${subtest.TestName || 'Internal Subtest Action'}</span>
                <span class="${subBadgeClass}">${subResultKey}</span>
            </div>
            
            <div class="subtest-meta">
                <div><strong>Status Code:</strong> <span class="mono">${subtest.StatusCode || 'N/A'}</span></div>
                <div><strong>Duration:</strong> ${formatDuration(subtest.Duration)}</div>
                <div><strong>Started:</strong> ${formatTime(subtest.StartTime)}</div>
                <div><strong>Action Key:</strong> <span class="mono" style="font-size:0.75rem;">${subtest.TestKey || 'N/A'}</span></div>
            </div>
            
            <div class="progress-container">
                <div class="progress-label-bar">
                    <span>Diagnostic Completion</span>
                    <span>${pct}%</span>
                </div>
                <div class="progress-track">
                    <div class="progress-fill ${subResultKey.toLowerCase()}" style="width: ${pct}%;"></div>
                </div>
            </div>
        `;
        
        if (subtest.ErrorCodeDescription) {
            const errDiv = document.createElement('div');
            errDiv.style.marginTop = '0.5rem';
            errDiv.style.padding = '0.5rem';
            errDiv.style.background = 'rgba(239, 68, 68, 0.08)';
            errDiv.style.borderLeft = '3px solid var(--color-failed)';
            errDiv.style.borderRadius = '2px';
            errDiv.style.fontSize = '0.8rem';
            errDiv.innerHTML = `<strong>Error State:</strong> <span class="mono" style="color: var(--color-failed);">${subtest.ErrorCodeDescription}</span>`;
            subtestCard.appendChild(errDiv);
        }
        
        subtestsList.appendChild(subtestCard);
    });
}

// Generate context-aware troubleshooting advice
function getTroubleshootingTips(test) {
    const tips = [];
    const testNameLower = test.testName.toLowerCase();
    
    // Look up based on subtest status codes or overall categories
    if (testNameLower.includes('keyboard')) {
        tips.push("Verify that no keys are physically stuck or jammed.");
        tips.push("If using an external USB keyboard, try reconnecting or changing USB ports.");
        tips.push("Inspect the keyboard layouts in Windows Settings to ensure the active layout matches your physical keyboard.");
    } else if (testNameLower.includes('audio') || testNameLower.includes('speaker') || testNameLower.includes('microphone')) {
        tips.push("Check if the device is muted in Windows Volume Mixer.");
        tips.push("Check microphone access permissions in Settings > Privacy & Security.");
        tips.push("Reinstall or update the audio driver (Realtek High Definition Audio, etc.).");
    } else if (testNameLower.includes('network') || testNameLower.includes('wireless') || testNameLower.includes('bluetooth')) {
        tips.push("Ensure Airplane Mode is toggled off and wireless hardware is enabled.");
        tips.push("Try resetting your TCP/IP settings or rebooting your network router.");
        tips.push("Verify the physical Wi-Fi/Bluetooth antennas are properly attached to the motherboard if desktop.");
    } else if (testNameLower.includes('battery') || testNameLower.includes('charger')) {
        tips.push("Ensure you are using the official Dell power adapter supplying correct wattage.");
        tips.push("If battery warning exists, check battery health metrics inside Windows or Dell SupportAssist.");
        tips.push("Try discharging the battery fully and then recharging it uninterrupted.");
    } else if (testNameLower.includes('video') || testNameLower.includes('display') || testNameLower.includes('camera')) {
        tips.push("Verify graphics card drivers are updated to the latest stable release.");
        tips.push("If using external displays, verify HDMI/DisplayPort cable integrity.");
        tips.push("For webcam failures, check if the camera shutter slider is physically open.");
    } else {
        tips.push("Ensure your BIOS is up to date (currently " + (appState.systemInfo?.BiosVersion || "Unknown") + ").");
        tips.push("Run the default Windows Hardware Troubleshooter.");
    }
    
    // Add default general tips
    tips.push("Restart your system and rerun diagnostics to verify if it is a transient error.");
    tips.push("Consult the Dell System Diagnostics Code Book using the Status Codes provided in subtests.");
    
    return tips;
}
