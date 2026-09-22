import os
import json
import html

base = r"c:\Users\KHATRI OM KUMAR\Desktop\final submission\final submission"

lab_catalog = [
    # Lab 1
    ("Lab 1", "Ex 1.1", "Side Menu using List", "Design side menu using list (Computers & Accessories, Price)", "lab-1.1", "index.html",
     "Displays a two-column bordered box with side categories, computer hardware, and price ranges formatted as bulleted lists with rupee symbols."),
    ("Lab 1", "Ex 1.2", "FTE First Page using Table", "Design first page of Faculty of Technology and Engineering using table", "lab-1.2", "index.html",
     "Renders the complete Faculty of Technology & Engineering portal using structured HTML table elements."),
    
    # Lab 2
    ("Lab 2", "Ex 2.1", "Static Website Structure", "Design a simple static website with Header, Left sidebar, and Content area Home.html", "lab-2.1", "index.html",
     "Renders the wireframe structure from the lab manual: solid blue Header, blue left navigation sidebar with links, and a right content pane dynamically loading pages."),
    ("Lab 2", "Ex 2.2", "Student Registration Form", "Create a student registration form using <form>, <input>, <textarea>, <button>, <select>, <option>", "lab-2.2", "index.html",
     "Displays a complete student registration form capturing Name, Gender, Address, Phone, Email, Hobbies, City, State, Country, and College dropdown."),
    ("Lab 2", "Ex 2.3", "MSU Home Page with Video", "Design MSU Home page using HTML5 and also include collage video in it", "lab-2.3", "index.html",
     "Renders the MSU Baroda homepage using semantic HTML5 tags with an embedded college campus video player."),

    # Lab 3
    ("Lab 3", "Ex 3.1", "Vertical Navigation Bar", "Design vertical navigation bar like following", "lab-3.1", "index.html",
     "Displays an olive green vertical navigation bar with block-level menu items (HOME, NEWS, CONTACT, ABOUT) and hover feedback."),
    ("Lab 3", "Ex 3.2", "Horizontal Navigation Bar", "Design horizontal navigation bar like following", "lab-3.2", "index.html",
     "Displays an olive green horizontal navigation bar with floating items (HOME, NEWS, CONTACT, ABOUT) centered on the page."),
    ("Lab 3", "Ex 3.3", "Art & Craft Photo Album", "Create art and craft photo album using bootstrap", "lab-3.3", "index.html",
     "Renders a responsive Bootstrap 5 image card gallery showing art and craft works with preview buttons."),
    ("Lab 3", "Ex 3.4", "Student Marksheet", "Create student marksheet using bootstrap", "lab-3.4", "index.html",
     "Displays a structured academic marksheet using Bootstrap tables with subject codes, marks obtained, grades, total summary, SGPA, and result status."),
    ("Lab 3", "Ex 3.5", "Employment Application Form", "Create employment application form like below", "lab-3.5", "index.html",
     "Faithfully replicates the scanned paper application form with blue header banner, drug test notice, applicant details grid, availability schedule, and an education records table."),
    ("Lab 3", "Ex 3.6", "Flipkart Home with Dropdown", "Design home of flipKart in which Navigation bar with dropdown is available using bootstrap", "lab-3.6", "index.html",
     "Renders a complete Flipkart home page with blue branded navbar, search bar, and active Bootstrap dropdown menus for categories."),

    # Lab 4
    ("Lab 4", "Ex 4.1", "Video Controls (JS)", "Play video in your web page and play/pause, change the dimension of it using javascript using button(small,normal,large)", "lab-4.1", "index.html",
     "Renders a video player with interactive buttons: Play/Pause toggles playback, and dimension buttons dynamically resize the video to small, normal, or large."),
    ("Lab 4", "Ex 4.2", "Type Writer Effect", "Implement Type Writer using DHTML and Javascript", "lab-4.2", "index.html",
     "Simulates a terminal typewriter effect by appending text character-by-character using setTimeout, with Start and Reset buttons."),
    ("Lab 4", "Ex 4.3", "Username & Password Validation", "Write down java script code to validate user name and password (password length must in between 6 to 12 characters. User name should not start with _, @, or any number, both are not blank)", "lab-4.3", "index.html",
     "Validates credentials: username cannot start with _, @, or digits, cannot be empty; password length must be between 6 and 12 characters."),
    ("Lab 4", "Ex 4.4", "Vowel 'a' Occurrence Finder", "Write an HTML file with Javascript that finds position of first occurrence of vowel 'a', last occurrence of vowel 'a' in a given word and returns the string between them", "lab-4.4", "index.html",
     "Demonstrates with word 'ajanta': identifies first occurrence of 'a' at position 1, last occurrence at position 6, and extracts the string between them ('jant')."),
    ("Lab 4", "Ex 4.5", "Keyboard & Mouse Events", "Write a JavaScript that handles key events: (i) key code (ii) vowel announcement (iii) key release background change to blue", "lab-4.5", "index.html",
     "Displays key name & keyCode, announces whenever a vowel is pressed, and changes background to blue on key release."),
    ("Lab 4", "Ex 4.6", "Snowfall Demonstration", "Design a webpage which demonstrate snow fall using javascript", "lab-4.6", "index.html",
     "Creates a dynamic winter snowfall animation using HTML5 Canvas and JavaScript animation loop with swaying flakes, density control, and pause/resume."),

    # Lab 5
    ("Lab 5", "Ex 5.1", "jQuery slideToggle()", "Use a jQuery method to toggle between sliding up and down a <div> element, when clicking on a button", "lab-5.1", "index.html",
     "Uses jQuery slideToggle('slow') on button click to smoothly open and close a content panel div."),
    ("Lab 5", "Ex 5.2", "jQuery animate() Move 250px", "Use the animate() method to move a <div> element 250 pixels to the right", "lab-5.2", "index.html",
     "Executes jQuery animate({ left: '250px' }) to shift a square container across an interactive stage."),
    ("Lab 5", "Ex 5.3", "jQuery animate() Properties", "Use the animate() method to set the following CSS properties for <div>: opacity:0.4, height:500px, width:500px", "lab-5.3", "index.html",
     "Demonstrates animating multiple CSS properties simultaneously: opacity reduces to 0.4 while dimensions expand to 500x500 pixels."),
    ("Lab 5", "Ex 5.4", "jQuery animate() Font Size", "Use the animate() method to set the font-size of a <div> element to 100 pixels. The duration of the effect should be slow", "lab-5.4", "index.html",
     "Smoothly transitions the text font size from 20px to 100px using jQuery animate({ fontSize: '100px' }, 'slow')."),
    ("Lab 5", "Ex 5.5", "jQuery Cartoon Animation", "Create cartoon animation using jQuery", "lab-5.5", "index.html",
     "Animates a cartoon character face across a landscape canvas with actions like jump, roll, dance, and celebrate using chained jQuery animations."),

    # Lab 6
    ("Lab 6", "Ex 6.1", "Stock Market (AJAX)", "Create Stock market web page using AJAX in which stock price come form .txt file", "lab-6.1", "index.html",
     "Uses AJAX XMLHttpRequest to asynchronously load stocks.txt containing ticker symbols, current prices, percentage changes, and renders a live financial table."),
    ("Lab 6", "Ex 6.2", "Cricket Live Score (AJAX)", "Display cricket live score using AJAX", "lab-6.2", "index.html",
     "Asynchronously retrieves match data from score.json via AJAX and dynamically displays the match summary, current batsmen, bowler stats, and recent balls."),
    ("Lab 6", "Ex 6.3", "Server Clock (AJAX)", "Implement Server clock using AJAX", "lab-6.3", "index.html",
     "Regularly polls the server via AJAX every second, parsing the server timestamp headers to render an accurate digital 12-hour clock with live date display."),

    # Lab 7
    ("Lab 7", "Ex 7.1", "XML Cricket Players & XSD", "Develop XML document that will hold player (Like Cricket) collection with field for player-name, age, batting-average and highest-score, write suitable schema for the XML", "lab-7.1", "index.html",
     "Defines players.xml holding player name, age, batting average, and highest score, validated against players.xsd XML Schema."),
    ("Lab 7", "Ex 7.2", "XML Marksheet + XSLT", "Write an XML file to store your semester mark sheet. Write an XSL file using XSLT to display it in XHTML table form", "lab-7.2", "index.html",
     "Transforms marksheet.xml into an XHTML report table using marksheet.xsl with subject names, max/min marks, obtained scores, and total percentages."),
    ("Lab 7", "Ex 7.3", "XML Book Collection & XSD", "Develop an XML document that will hold a book collection with fields for book name, author, ISBN number and quantity. Write suitable schema for the XML", "lab-7.3", "index.html",
     "Defines books.xml containing book name, author, ISBN number, and quantity, validated against books.xsd with restrictions."),
    ("Lab 7", "Ex 7.4", "XSLT Product Price Filter", "Write an XSL file to print list of products which has price< 300Rs. For item.xml file in tabular structure", "lab-7.4", "index.html",
     "Applies XSLT filter <xsl:if test='price &lt; 300'> on item.xml to filter and display only affordable items in a responsive XHTML table."),
    ("Lab 7", "Ex 7.5", "XML Book Record + XSLT", "Develop XML File for book record and also write XSL for it to display in table format", "lab-7.5", "index.html",
     "Binds bookrecord.xml with bookrecord.xsl using <xsl:for-each> to format book title, author, edition, price, and publisher in a clean tabular view."),

    # Node.js Lab
    ("Node.js Lab", "Ex Node.1", "Area Calculation Module", "Create a module for area calculation in node.js for circle, rectangle, and square. Use this module in your current file to find area of all shape", "node-lab.1", "index.html",
     "Executes Node.js areaModule.js exporting circle, rectangle, and square area functions. app.js imports the module, calculates values, outputs to console, and serves HTML via HTTP."),
    ("Node.js Lab", "Ex Node.2", "Armstrong Number Checker", "Write a program to read a file from server and check whether no read from file is armstrong or not using node.js", "node-lab.2", "index.html",
     "Node.js script reads integer from number.txt using fs.readFile, computes sum of digits raised to power of digit length, confirms Armstrong status, and outputs results."),
    ("Node.js Lab", "Ex Node.3", "Student JSON Lookup", "Write a program to read student.json file from a server and display the information of student for given PRN no in tabular format", "node-lab.3", "index.html",
     "Node.js HTTP server reads student.json, filters record matching query PRN, and dynamically renders student details in a table.")
]

# Build items data list
items_data = []
for lab, ex, short_title, q_text, folder, main_file, desc in lab_catalog:
    folder_path = os.path.join(base, folder)
    files_in_dir = os.listdir(folder_path) if os.path.exists(folder_path) else []
    
    code_files = []
    for fn in files_in_dir:
        if fn.endswith(('.html', '.js', '.xml', '.xsd', '.xsl', '.json', '.txt')) and not fn.endswith('.mp4'):
            fpath = os.path.join(folder_path, fn)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    c = f.read()
                code_files.append({
                    "filename": fn,
                    "code": c
                })
            except Exception as e:
                pass

    items_data.append({
        "lab": lab,
        "ex": ex,
        "title": short_title,
        "question": q_text,
        "folder": folder,
        "main_file": main_file,
        "desc": desc,
        "code_files": code_files
    })

data_json = json.dumps(items_data)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BWP Lab Submission Portal | Question → Code → Output</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {{
            --primary: #122b4d;
            --primary-light: #1b3d6d;
            --accent: #e67e22;
            --sidebar-bg: #0d1e36;
            --sidebar-hover: #162f54;
            --bg-light: #f4f6fa;
            --card-bg: #ffffff;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --code-bg: #1e1e1e;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        /* Header */
        header.app-header {{
            height: 60px;
            background-color: var(--primary);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.15);
            z-index: 100;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-logo {{
            width: 38px;
            height: 38px;
            background: linear-gradient(135deg, var(--accent), #d35400);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            font-weight: bold;
        }}

        .brand-text h1 {{
            font-size: 16px;
            font-weight: 700;
            letter-spacing: 0.3px;
        }}

        .brand-text p {{
            font-size: 11px;
            color: #cbd5e1;
        }}

        .header-actions {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .badge-student {{
            background: rgba(255,255,255,0.15);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
        }}

        /* Main Workspace Container */
        .workspace {{
            flex: 1;
            display: flex;
            overflow: hidden;
        }}

        /* Sidebar Navigation */
        aside.sidebar {{
            width: 320px;
            background-color: var(--sidebar-bg);
            color: #ffffff;
            display: flex;
            flex-direction: column;
            border-right: 1px solid rgba(255,255,255,0.1);
        }}

        .sidebar-search {{
            padding: 14px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }}

        .sidebar-search input {{
            width: 100%;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 6px;
            padding: 8px 12px;
            color: #ffffff;
            font-size: 13px;
            outline: none;
        }}

        .sidebar-search input::placeholder {{
            color: #94a3b8;
        }}

        .lab-list {{
            flex: 1;
            overflow-y: auto;
            padding: 10px 8px;
        }}

        .lab-group-title {{
            font-size: 11px;
            font-weight: 700;
            color: var(--accent);
            text-transform: uppercase;
            padding: 12px 10px 4px 10px;
            letter-spacing: 0.8px;
        }}

        .lab-item {{
            padding: 10px 12px;
            border-radius: 6px;
            margin-bottom: 4px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.15s ease;
            font-size: 13px;
            color: #cbd5e1;
        }}

        .lab-item:hover {{
            background-color: var(--sidebar-hover);
            color: #ffffff;
        }}

        .lab-item.active {{
            background-color: var(--accent);
            color: #ffffff;
            font-weight: 600;
        }}

        .lab-badge {{
            background: rgba(255,255,255,0.12);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: bold;
            letter-spacing: 0.5px;
        }}

        /* Content Area */
        main.main-content {{
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            padding: 24px 30px;
        }}

        /* Question Banner Box */
        .card-question {{
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-left: 5px solid var(--primary);
            border-radius: 8px;
            padding: 20px 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}

        .question-meta {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
        }}

        .question-tag {{
            font-size: 12px;
            font-weight: 700;
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .folder-tag {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            background: #f1f5f9;
            padding: 3px 8px;
            border-radius: 4px;
            color: #475569;
        }}

        .question-title {{
            font-size: 17px;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 8px;
            line-height: 1.4;
        }}

        .question-text {{
            font-size: 14px;
            color: #334155;
            line-height: 1.6;
            background: #f8fafc;
            padding: 12px 16px;
            border-radius: 6px;
            border: 1px solid #edf2f7;
        }}

        /* Section Tabs: Code vs Output */
        .tabs-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
            border-bottom: 2px solid var(--border);
            padding-bottom: 10px;
        }}

        .tab-btn {{
            background: none;
            border: none;
            padding: 8px 18px;
            font-size: 14px;
            font-weight: 600;
            color: var(--text-muted);
            cursor: pointer;
            border-radius: 6px;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }}

        .tab-btn:hover {{
            color: var(--primary);
            background-color: #e2e8f0;
        }}

        .tab-btn.active {{
            background-color: var(--primary);
            color: #ffffff;
        }}

        /* Code Viewer Container */
        .code-container {{
            background-color: var(--code-bg);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            margin-bottom: 20px;
        }}

        .code-header {{
            background-color: #2d2d2d;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #3d3d3d;
        }}

        .code-files-tabs {{
            display: flex;
            gap: 6px;
        }}

        .file-tab {{
            background: rgba(255,255,255,0.08);
            color: #cbd5e1;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 12px;
            font-family: 'JetBrains Mono', monospace;
            cursor: pointer;
        }}

        .file-tab.active {{
            background-color: var(--accent);
            color: #ffffff;
            font-weight: 600;
        }}

        .btn-copy {{
            background: rgba(255,255,255,0.1);
            border: none;
            color: #cbd5e1;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 12px;
            cursor: pointer;
            transition: background 0.2s;
        }}

        .btn-copy:hover {{
            background: rgba(255,255,255,0.25);
            color: #ffffff;
        }}

        pre.code-block {{
            margin: 0;
            padding: 20px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            line-height: 1.55;
            color: #d4d4d4;
            overflow-x: auto;
            max-height: 520px;
        }}

        /* Live Output Container */
        .output-container {{
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.06);
            display: flex;
            flex-direction: column;
            flex: 1;
            min-height: 550px;
        }}

        .output-header {{
            background-color: #f8fafc;
            padding: 12px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border);
        }}

        .output-info {{
            font-size: 13px;
            color: var(--text-muted);
            font-weight: 500;
        }}

        .btn-open-tab {{
            color: var(--primary);
            text-decoration: none;
            font-size: 12px;
            font-weight: 600;
            background: #e2e8f0;
            padding: 6px 12px;
            border-radius: 4px;
            transition: background 0.2s;
        }}

        .btn-open-tab:hover {{
            background: #cbd5e1;
        }}

        iframe.output-frame {{
            width: 100%;
            flex: 1;
            border: none;
            background-color: #ffffff;
            min-height: 520px;
        }}

        .output-note {{
            padding: 12px 18px;
            background-color: #f1f5f9;
            font-size: 12px;
            color: #475569;
            border-top: 1px solid var(--border);
        }}
    </style>
</head>
<body>

    <!-- App Header -->
    <header class="app-header">
        <div class="brand">
            <div class="brand-logo"><i class="fa-solid fa-code"></i></div>
            <div class="brand-text">
                <h1>BWP Laboratory Submission Hub</h1>
                <p>Faculty of Technology & Engineering, MSU Baroda &bull; 33 Exercises Complete</p>
            </div>
        </div>
        <div class="header-actions">
            <span class="badge-student"><i class="fa-solid fa-user-graduate"></i> Om Kumar Khatri</span>
            <a href="../../Final_Lab_Submission.docx" class="btn-copy" style="text-decoration: none; padding: 7px 14px;" download>
                <i class="fa-solid fa-file-word text-primary"></i> Download Word Doc
            </a>
        </div>
    </header>

    <!-- Main Workspace -->
    <div class="workspace">
        
        <!-- Sidebar Navigation -->
        <aside class="sidebar">
            <div class="sidebar-search">
                <input type="text" id="searchLabs" placeholder="Search lab or question..." oninput="filterLabs(this.value)">
            </div>
            <div class="lab-list" id="labList">
                <!-- Populated via JavaScript -->
            </div>
        </aside>

        <!-- Main Content Pane -->
        <main class="main-content">
            
            <!-- Question Statement Box -->
            <div class="card-question">
                <div class="question-meta">
                    <span class="question-tag" id="qLabTag">Lab 1 &bull; Exercise 1.1</span>
                    <span class="folder-tag" id="qFolderTag">lab-1.1/</span>
                </div>
                <div class="question-title" id="qTitle">Title Placeholder</div>
                <div class="question-text" id="qStatement">Question text goes here...</div>
            </div>

            <!-- Tabs: Question / Code / Live Output -->
            <div class="tabs-header">
                <button class="tab-btn active" id="btnTabOutput" onclick="switchView('output')">
                    <i class="fa-solid fa-desktop"></i> Live Output / Execution
                </button>
                <button class="tab-btn" id="btnTabCode" onclick="switchView('code')">
                    <i class="fa-solid fa-code"></i> Source Code
                </button>
                <button class="tab-btn" id="btnTabBoth" onclick="switchView('both')">
                    <i class="fa-solid fa-columns"></i> Code + Output (Split View)
                </button>
            </div>

            <!-- View 1: Live Output Pane -->
            <div class="output-container" id="outputView">
                <div class="output-header">
                    <div class="output-info">
                        <i class="fa-solid fa-circle text-success me-1"></i> Live Interactive Preview
                    </div>
                    <a href="#" target="_blank" id="btnNewTab" class="btn-open-tab">
                        <i class="fa-solid fa-arrow-up-right-from-square"></i> Open in New Window
                    </a>
                </div>
                <iframe class="output-frame" id="liveFrame" src="about:blank"></iframe>
                <div class="output-note" id="outputNote">
                    Output description goes here...
                </div>
            </div>

            <!-- View 2: Code Viewer Pane -->
            <div class="code-container" id="codeView" style="display: none;">
                <div class="code-header">
                    <div class="code-files-tabs" id="codeFileTabs">
                        <!-- File Tabs -->
                    </div>
                    <button class="btn-copy" onclick="copyActiveCode()"><i class="fa-regular fa-copy"></i> Copy Code</button>
                </div>
                <pre class="code-block"><code id="codeBlock">Code content...</code></pre>
            </div>

        </main>
    </div>

    <!-- Inject Catalog Data -->
    <script>
        const catalog = {data_json};
        let currentIndex = 0;
        let activeFileIndex = 0;
        let currentMode = 'output'; // 'output', 'code', 'both'

        function init() {{
            renderSidebar();
            loadExperiment(0);
        }}

        function renderSidebar(query = "") {{
            const list = document.getElementById("labList");
            list.innerHTML = "";
            let currentLabName = "";

            catalog.forEach((item, index) => {{
                if (query) {{
                    const fullStr = (item.lab + " " + item.ex + " " + item.title + " " + item.question).toLowerCase();
                    if (!fullStr.includes(query.toLowerCase())) return;
                }}

                if (item.lab !== currentLabName) {{
                    currentLabName = item.lab;
                    const grp = document.createElement("div");
                    grp.className = "lab-group-title";
                    grp.innerText = currentLabName;
                    list.appendChild(grp);
                }}

                const el = document.createElement("div");
                el.className = "lab-item" + (index === currentIndex ? " active" : "");
                el.onclick = () => loadExperiment(index);
                el.innerHTML = `
                    <span class="lab-badge">${{item.ex}}</span>
                    <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${{item.title}}</span>
                `;
                list.appendChild(el);
            }});
        }}

        function filterLabs(val) {{
            renderSidebar(val);
        }}

        function loadExperiment(index) {{
            currentIndex = index;
            activeFileIndex = 0;
            const item = catalog[index];

            // Update Active Class in Sidebar
            const items = document.querySelectorAll(".lab-item");
            items.forEach((el, idx) => {{
                el.classList.toggle("active", idx === index);
            }});

            // Update Question Meta
            document.getElementById("qLabTag").innerText = item.lab + " • " + item.ex;
            document.getElementById("qFolderTag").innerText = item.folder + "/" + item.main_file;
            document.getElementById("qTitle").innerText = item.ex + ": " + item.title;
            document.getElementById("qStatement").innerText = item.question;

            // Update Live Frame
            const frame = document.getElementById("liveFrame");
            const targetUrl = item.folder + "/" + item.main_file;
            frame.src = targetUrl;
            document.getElementById("btnNewTab").href = targetUrl;
            document.getElementById("outputNote").innerHTML = "<strong>Output &amp; Execution Summary:</strong> " + item.desc;

            // Render File Tabs for Code Viewer
            renderCodeTabs();
        }}

        function renderCodeTabs() {{
            const item = catalog[currentIndex];
            const tabsContainer = document.getElementById("codeFileTabs");
            tabsContainer.innerHTML = "";

            if (!item.code_files || item.code_files.length === 0) {{
                document.getElementById("codeBlock").innerText = "// No code file found.";
                return;
            }}

            item.code_files.forEach((file, fIdx) => {{
                const btn = document.createElement("div");
                btn.className = "file-tab" + (fIdx === activeFileIndex ? " active" : "");
                btn.innerText = file.filename;
                btn.onclick = () => {{
                    activeFileIndex = fIdx;
                    renderCodeTabs();
                }};
                tabsContainer.appendChild(btn);
            }});

            // Show active file code
            document.getElementById("codeBlock").innerText = item.code_files[activeFileIndex].code;
        }}

        function switchView(mode) {{
            currentMode = mode;
            const btnOutput = document.getElementById("btnTabOutput");
            const btnCode = document.getElementById("btnTabCode");
            const btnBoth = document.getElementById("btnTabBoth");
            const outView = document.getElementById("outputView");
            const codeView = document.getElementById("codeView");

            btnOutput.classList.toggle("active", mode === 'output');
            btnCode.classList.toggle("active", mode === 'code');
            btnBoth.classList.toggle("active", mode === 'both');

            if (mode === 'output') {{
                outView.style.display = "flex";
                codeView.style.display = "none";
            }} else if (mode === 'code') {{
                outView.style.display = "none";
                codeView.style.display = "flex";
            }} else if (mode === 'both') {{
                outView.style.display = "flex";
                codeView.style.display = "flex";
            }}
        }}

        function copyActiveCode() {{
            const item = catalog[currentIndex];
            if (item && item.code_files && item.code_files[activeFileIndex]) {{
                navigator.clipboard.writeText(item.code_files[activeFileIndex].code).then(() => {{
                    alert("Code for " + item.code_files[activeFileIndex].filename + " copied to clipboard!");
                }});
            }}
        }}

        window.onload = init;
    </script>

</body>
</html>
"""

output_html_path = os.path.join(base, "index.html")
with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Master Lab Submission Hub index.html generated at:\n{{output_html_path}}")
