import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_document():
    doc = docx.Document()
    
    # Page setup - Standard 0.75" Margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # ------------------ COVER PAGE ------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(10)
    p_inst.paragraph_format.space_after = Pt(2)
    run_inst = p_inst.add_run("THE MAHARAJA SAYAJIRAO UNIVERSITY OF BARODA\n")
    run_inst.font.name = "Arial"
    run_inst.font.size = Pt(16)
    run_inst.font.bold = True
    run_inst.font.color.rgb = RGBColor(20, 41, 77)

    run_fac = p_inst.add_run("FACULTY OF TECHNOLOGY AND ENGINEERING\nDEPARTMENT OF COMPUTER SCIENCE & ENGINEERING\n")
    run_fac.font.name = "Arial"
    run_fac.font.size = Pt(13)
    run_fac.font.bold = True
    run_fac.font.color.rgb = RGBColor(0, 119, 182)

    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_before = Pt(4)
    p_div.paragraph_format.space_after = Pt(25)
    p_div.add_run("―" * 45).font.color.rgb = RGBColor(230, 126, 34)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(30)
    
    r_sub = p_title.add_run("LABORATORY WORK SUBMISSION\n")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(22)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(20, 41, 77)

    r_course = p_title.add_run("BASIC WEB PROGRAMMING (BWP)\n")
    r_course.font.name = "Arial"
    r_course.font.size = Pt(16)
    r_course.font.bold = True
    r_course.font.color.rgb = RGBColor(230, 126, 34)

    r_term = p_title.add_run("Academic Year: 2025 – 2026")
    r_term.font.name = "Arial"
    r_term.font.size = Pt(12)
    r_term.font.color.rgb = RGBColor(100, 100, 100)

    # Student Details Table - Clean Word Table Format
    details_table = doc.add_table(rows=6, cols=2)
    details_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    details_data = [
        ("Student Name:", "Om Kumar Khatri"),
        ("PRN:", "8024056707"),
        ("Roll No:", "36"),
        ("Class:", "BE-III (GIA)"),
        ("Branch:", "Computer Science & Engineering"),
        ("Subject:", "Basic Web Programming (BWP)")
    ]
    for i, (label, val) in enumerate(details_data):
        row = details_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.2)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.font.name = "Arial"
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = RGBColor(20, 41, 77)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name = "Arial"
        r1.font.size = Pt(11)
        if label in ["PRN:", "Roll No:", "Class:"]:
            r1.font.bold = True
        
        set_cell_background(c0, "F4F6F9")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 70, 70, 120, 120)
        set_cell_margins(c1, 70, 70, 120, 120)

    doc.add_page_break()

    # ------------------ TABLE OF CONTENTS / INDEX ------------------
    p_idx = doc.add_paragraph()
    p_idx.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_idx = p_idx.add_run("INDEX / LIST OF EXPERIMENTS")
    r_idx.font.name = "Arial"
    r_idx.font.size = Pt(16)
    r_idx.font.bold = True
    r_idx.font.color.rgb = RGBColor(230, 126, 34)
    p_idx.paragraph_format.space_after = Pt(15)

    base = r"c:\Users\KHATRI OM KUMAR\Desktop\final submission\final submission"
    ss_dir = r"c:\Users\KHATRI OM KUMAR\Desktop\final submission\screenshots"

    lab_catalog = [
        # Lab 1
        ("Lab-1", "1.1", "Design side menu using list like following (Computers & Accessories, Price)", "lab-1.1", ["index.html"], "1.1.png"),
        ("Lab-1", "1.2", "Design first page of Faculty of Technology and Engineering using table", "lab-1.2", ["index.html"], "1.2.png"),
        
        # Lab 2
        ("Lab-2", "2.1", "Design a simple static website using HTML with Header, Left sidebar, and Content area Home.html", "lab-2.1", ["index.html", "Home.html", "About.html", "Contact.html"], "2.1.png"),
        ("Lab-2", "2.2", "Create a student registration form using <form>, <input>, <textarea>, <button>, <select>, <option>", "lab-2.2", ["index.html"], "2.2.png"),
        ("Lab-2", "2.3", "Design MSU Home page using HTML5 and also include collage video in it", "lab-2.3", ["index.html"], "2.3.png"),

        # Lab 3
        ("Lab-3", "3.1", "Design vertical navigation bar like following", "lab-3.1", ["index.html"], "3.1.png"),
        ("Lab-3", "3.2", "Design horizontal navigation bar like following", "lab-3.2", ["index.html"], "3.2.png"),
        ("Lab-3", "3.3", "Create art and craft photo album using bootstrap", "lab-3.3", ["index.html"], "3.3.png"),
        ("Lab-3", "3.4", "Create student marksheet using bootstrap", "lab-3.4", ["index.html"], "3.4.png"),
        ("Lab-3", "3.5", "Create employment application form like below", "lab-3.5", ["index.html"], "3.5.png"),
        ("Lab-3", "3.6", "Design home of flipKart in which Navigation bar with dropdown is available using bootstrap", "lab-3.6", ["index.html"], "3.6.png"),

        # Lab 4
        ("Lab-4", "4.1", "Play video in your web page and play/pause, change the dimension of it using javascript using button(small,normal,large)", "lab-4.1", ["index.html"], "4.1.png"),
        ("Lab-4", "4.2", "Implement Type Writer using DHTML and Javascript", "lab-4.2", ["index.html"], "4.2.png"),
        ("Lab-4", "4.3", "Write down java script code to validate user name and password", "lab-4.3", ["index.html"], "4.3.png"),
        ("Lab-4", "4.4", "Write an HTML file with Javascript that finds position of first occurrence of vowel 'a', last occurrence of vowel 'a' in a given word and returns the string between them", "lab-4.4", ["index.html"], "4.4.png"),
        ("Lab-4", "4.5", "Write a JavaScript that handles key events: key code, vowel announcement, and background change to blue on release", "lab-4.5", ["index.html"], "4.5.png"),
        ("Lab-4", "4.6", "Design a webpage which demonstrate snow fall using javascript", "lab-4.6", ["index.html"], "4.6.png"),

        # Lab 5
        ("Lab-5", "5.1", "Use a jQuery method to toggle between sliding up and down a <div> element, when clicking on a button", "lab-5.1", ["index.html"], "5.1.png"),
        ("Lab-5", "5.2", "Use the animate() method to move a <div> element 250 pixels to the right", "lab-5.2", ["index.html"], "5.2.png"),
        ("Lab-5", "5.3", "Use the animate() method to set CSS properties for <div>: opacity:0.4, height:500px, width:500px", "lab-5.3", ["index.html"], "5.3.png"),
        ("Lab-5", "5.4", "Use the animate() method to set the font-size of a <div> element to 100 pixels with slow duration", "lab-5.4", ["index.html"], "5.4.png"),
        ("Lab-5", "5.5", "Create cartoon animation using jQuery", "lab-5.5", ["index.html"], "5.5.png"),

        # Lab 6
        ("Lab-6", "6.1", "Create Stock market web page using AJAX in which stock price come form .txt file", "lab-6.1", ["index.html", "stocks.txt"], "6.1.png"),
        ("Lab-6", "6.2", "Display cricket live score using AJAX", "lab-6.2", ["index.html", "score.json"], "6.2.png"),
        ("Lab-6", "6.3", "Implement Server clock using AJAX", "lab-6.3", ["index.html", "time.txt"], "6.3.png"),

        # Lab 7
        ("Lab-7", "7.1", "Develop XML document that will hold player collection with fields for player-name, age, batting-average and highest-score, write suitable schema for the XML", "lab-7.1", ["players.xml", "players.xsd", "index.html"], "7.1.png"),
        ("Lab-7", "7.2", "Write an XML file to store your semester mark sheet. Write an XSL file using XSLT to display it in XHTML table form", "lab-7.2", ["marksheet.xml", "marksheet.xsl", "index.html"], "7.2.png"),
        ("Lab-7", "7.3", "Develop an XML document that will hold a book collection with fields for book name, author, ISBN number and quantity. Write suitable schema for the XML", "lab-7.3", ["books.xml", "books.xsd", "index.html"], "7.3.png"),
        ("Lab-7", "7.4", "Write an XSL file to print list of products which has price< 300Rs. For item.xml file in tabular structure", "lab-7.4", ["item.xml", "item.xsl", "index.html"], "7.4.png"),
        ("Lab-7", "7.5", "Develop XML File for book record and also write XSL for it to display in table format", "lab-7.5", ["bookrecord.xml", "bookrecord.xsl", "index.html"], "7.5.png"),

        # Node.js Lab
        ("Node.js Lab", "Node.1", "Create a module for area calculation in node.js for circle, rectangle, and square. Use this module in your current file to find area of all shape", "node-lab.1", ["areaModule.js", "app.js", "index.html"], "node.1.png"),
        ("Node.js Lab", "Node.2", "Write a program to read a file from server and check whether no read from file is armstrong or not using node.js", "node-lab.2", ["app.js", "number.txt", "index.html"], "node.2.png"),
        ("Node.js Lab", "Node.3", "Write a program to read student.json file from a server and display the information of student for given PRN no in tabular format", "node-lab.3", ["server.js", "student.json", "index.html"], "node.3.png")
    ]

    # Index Table
    idx_table = doc.add_table(rows=1, cols=3)
    idx_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = idx_table.rows[0].cells
    hdr[0].text = "Sr No."
    hdr[1].text = "Aim / Experiment Title"
    hdr[2].text = "Technology"
    
    for c in hdr:
        set_cell_background(c, "14294D")
        for p in c.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Arial"
                r.font.bold = True
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(255, 255, 255)

    for i, (lab, ex, title, folder, files, ss_file) in enumerate(lab_catalog, 1):
        row = idx_table.add_row().cells
        row[0].text = f"Exp {ex}"
        row[1].text = title
        
        tech = "HTML/CSS"
        if "bootstrap" in title.lower() or "flipkart" in title.lower():
            tech = "Bootstrap 5"
        elif "javascript" in title.lower() or "dhtml" in title.lower() or "vowel" in title.lower() or "snow" in title.lower() or "key" in title.lower() or "video" in title.lower() or "validation" in title.lower():
            tech = "JavaScript"
        elif "jquery" in title.lower() or "cartoon" in title.lower():
            tech = "jQuery"
        elif "ajax" in title.lower():
            tech = "AJAX"
        elif "xml" in title.lower() or "xsl" in title.lower():
            tech = "XML / XSLT"
        elif "node" in title.lower() or "Node" in lab:
            tech = "Node.js"
        row[2].text = tech

        row[0].width = Inches(1.1)
        row[1].width = Inches(4.5)
        row[2].width = Inches(1.4)

        for j, c in enumerate(row):
            set_cell_margins(c, 40, 40, 60, 60)
            if j in [0, 2]:
                c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in c.paragraphs[0].runs:
                r.font.name = "Arial"
                r.font.size = Pt(9)

    doc.add_page_break()

    # ------------------ EXPERIMENT SECTIONS ------------------
    current_lab = ""
    for idx, (lab, ex, title, folder, files, ss_file) in enumerate(lab_catalog, 1):
        
        # PROPER CENTER HEADING IN ORANGE COLOR for each Lab
        if lab != current_lab:
            current_lab = lab
            p_sec = doc.add_paragraph()
            p_sec.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_sec.paragraph_format.space_before = Pt(28)
            p_sec.paragraph_format.space_after = Pt(14)
            
            # Format clean Lab heading: LAB - 1, LAB - 2, etc.
            lab_heading_text = current_lab.upper()
            if not "LAB" in lab_heading_text:
                lab_heading_text = "LAB - " + lab_heading_text
            else:
                lab_heading_text = lab_heading_text.replace("-", " - ")

            r_sec = p_sec.add_run(f"― {lab_heading_text} ―")
            r_sec.font.name = "Arial"
            r_sec.font.size = Pt(16)
            r_sec.font.bold = True
            r_sec.font.color.rgb = RGBColor(230, 126, 34)  # Orange Color

        # Experiment Heading
        p_ex = doc.add_paragraph()
        p_ex.paragraph_format.space_before = Pt(14)
        p_ex.paragraph_format.space_after = Pt(6)
        r_ex = p_ex.add_run(f"Experiment {ex}: {title}")
        r_ex.font.name = "Arial"
        r_ex.font.size = Pt(12)
        r_ex.font.bold = True
        r_ex.font.color.rgb = RGBColor(20, 41, 77)

        # CODE SECTION - Natural Student Style
        p_c_lbl = doc.add_paragraph()
        p_c_lbl.paragraph_format.space_before = Pt(8)
        p_c_lbl.paragraph_format.space_after = Pt(3)
        r_clbl = p_c_lbl.add_run("Code:")
        r_clbl.font.name = "Arial"
        r_clbl.font.size = Pt(10.5)
        r_clbl.font.bold = True
        r_clbl.font.color.rgb = RGBColor(50, 50, 50)

        dir_path = os.path.join(base, folder)
        for fname in files:
            fpath = os.path.join(dir_path, fname)
            code_content = ""
            if os.path.exists(fpath):
                try:
                    with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                        code_content = f.read()
                except Exception as e:
                    code_content = f"Error reading code: {e}"
            else:
                code_content = f"// Code file: {fname}"

            # Code table container (clean light-gray box)
            code_table = doc.add_table(rows=1, cols=1)
            code_table.alignment = WD_TABLE_ALIGNMENT.CENTER
            code_cell = code_table.rows[0].cells[0]
            code_cell.width = Inches(6.8)
            set_cell_background(code_cell, "F8F9FA")
            set_cell_margins(code_cell, 80, 80, 100, 100)
            
            p_code = code_cell.paragraphs[0]
            
            # Truncate if extremely long (e.g. over 6000 chars) for clean Word printing
            code_display = code_content
            if len(code_display) > 6000:
                code_display = code_display[:6000] + "\n\n... [Code truncated for print length. Complete source in project files] ..."

            r_code = p_code.add_run(code_display)
            r_code.font.name = "Consolas"
            r_code.font.size = Pt(8)
            r_code.font.color.rgb = RGBColor(35, 35, 35)

        # OUTPUT SECTION - Natural Student Style with Real Browser Screenshot
        p_o_lbl = doc.add_paragraph()
        p_o_lbl.paragraph_format.space_before = Pt(12)
        p_o_lbl.paragraph_format.space_after = Pt(6)
        r_olbl = p_o_lbl.add_run("Output:")
        r_olbl.font.name = "Arial"
        r_olbl.font.size = Pt(10.5)
        r_olbl.font.bold = True
        r_olbl.font.color.rgb = RGBColor(50, 50, 50)

        # Embed Single Browser Output Screenshot
        ss_path = os.path.join(ss_dir, ss_file)
        if os.path.exists(ss_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(4)
            p_img.paragraph_format.space_after = Pt(14)
            p_img.add_run().add_picture(ss_path, width=Inches(6.0))
        else:
            p_no_img = doc.add_paragraph()
            p_no_img.add_run(f"[Output screenshot: {ss_file}]").font.italic = True

        p_div2 = doc.add_paragraph()
        p_div2.paragraph_format.space_before = Pt(6)
        p_div2.paragraph_format.space_after = Pt(14)
        p_div2.add_run("―" * 55).font.color.rgb = RGBColor(220, 225, 230)

    output_path = r"C:\Users\KHATRI OM KUMAR\Desktop\Final_Lab_Submission.docx"
    doc.save(output_path)
    print(f"Updated Word Document created at:\n{output_path}")

if __name__ == "__main__":
    create_document()
