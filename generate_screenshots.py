import os
import subprocess

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
base = r"c:\Users\KHATRI OM KUMAR\Desktop\final submission\final submission"
out_dir = r"c:\Users\KHATRI OM KUMAR\Desktop\final submission\screenshots"
os.makedirs(out_dir, exist_ok=True)

labs = [
    ("lab-1.1", "1.1"),
    ("lab-1.2", "1.2"),
    ("lab-2.1", "2.1"),
    ("lab-2.2", "2.2"),
    ("lab-2.3", "2.3"),
    ("lab-3.1", "3.1"),
    ("lab-3.2", "3.2"),
    ("lab-3.3", "3.3"),
    ("lab-3.4", "3.4"),
    ("lab-3.5", "3.5"),
    ("lab-3.6", "3.6"),
    ("lab-4.1", "4.1"),
    ("lab-4.2", "4.2"),
    ("lab-4.3", "4.3"),
    ("lab-4.4", "4.4"),
    ("lab-4.5", "4.5"),
    ("lab-4.6", "4.6"),
    ("lab-5.1", "5.1"),
    ("lab-5.2", "5.2"),
    ("lab-5.3", "5.3"),
    ("lab-5.4", "5.4"),
    ("lab-5.5", "5.5"),
    ("lab-6.1", "6.1"),
    ("lab-6.2", "6.2"),
    ("lab-6.3", "6.3"),
    ("lab-7.1", "7.1"),
    ("lab-7.2", "7.2"),
    ("lab-7.3", "7.3"),
    ("lab-7.4", "7.4"),
    ("lab-7.5", "7.5"),
    ("node-lab.1", "node.1"),
    ("node-lab.2", "node.2"),
    ("node-lab.3", "node.3")
]

print("Capturing screenshots for all 33 experiments...")
for folder, tag in labs:
    html_file = os.path.join(base, folder, "index.html")
    out_file = os.path.join(out_dir, f"{tag}.png")
    
    if os.path.exists(html_file):
        cmd = [
            edge,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1150,720",
            f"--screenshot={out_file}",
            html_file
        ]
        res = subprocess.run(cmd, capture_output=True, timeout=12)
        if os.path.exists(out_file):
            print(f"[OK] {tag}.png ({os.path.getsize(out_file)} bytes)")
        else:
            print(f"[ERR] Failed {tag}")
    else:
        print(f"[ERR] Not found {html_file}")

print("All screenshots generated!")
