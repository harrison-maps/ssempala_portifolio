import os
import shutil
import re

base_dir = r"c:\Users\DELL\OneDrive\Desktop\portifolio"
stitch_dir = os.path.join(base_dir, "stitch")

# Copy the user's image
src_img = r"C:\Users\DELL\OneDrive\Desktop\ssempa.png"
dst_img = os.path.join(base_dir, "ssempa.png")
if os.path.exists(src_img):
    shutil.copy(src_img, dst_img)
    print("Copied user image.")
else:
    print(f"Warning: Could not find image at {src_img}")

files = {
    "index.html": os.path.join(stitch_dir, "portfolio_home_emerald", "code.html"),
    "about.html": os.path.join(stitch_dir, "about_skills_emerald_1", "code.html"),
    "work.html": os.path.join(stitch_dir, "portfolio_projects_emerald", "code.html")
}

for name, path in files.items():
    if not os.path.exists(path):
        print(f"Skipping {name}: {path} not found.")
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. User Name replacements
    content = content.replace("PORTFOLIO_MONOLITH", "SSEMPALA HARRISON SOLOMON")
    content = content.replace("PORTFOLIO MONOLITH", "SSEMPALA HARRISON SOLOMON")

    # 2. Add hyperlink to the logo
    content = re.sub(
        r'>\s*SSEMPALA HARRISON SOLOMON\s*</div>',
        r'>\n            <a href="index.html" class="hover:text-white transition-colors">SSEMPALA HARRISON SOLOMON</a>\n        </div>',
        content,
        count=1
    )

    # 3. Update Nav Links
    content = content.replace('href="#">WORK</a>', 'href="work.html">WORK</a>')
    content = content.replace('href="#">ABOUT</a>', 'href="about.html">ABOUT</a>')

    if name == "index.html":
        # Remove active state from WORK in index
        content = content.replace(
            'text-[#10B981] border-b-2 border-[#10B981] pb-1" href="work.html">WORK',
            'text-white/60 hover:text-white transition-colors" href="work.html">WORK'
        )
        # Add active state to none for now, index is home.
        
        # Replace the hero image in index
        content = re.sub(
            r'<img class="(.*?)" data-alt="[^"]*" src="[^"]*"/>',
            r'<img class="\1" alt="Ssempala Harrison Solomon" src="./ssempa.png"/>',
            content,
            count=1
        )
        
    elif name == "about.html":
        content = re.sub(
            r'<img alt="Professional portrait" class="(.*?)" data-alt="[^"]*" src="[^"]*"/>',
            r'<img alt="Ssempala Harrison Solomon" class="\1" src="./ssempa.png"/>',
            content
        )
        
    elif name == "work.html":
        # Project preview images left alone for now
        pass
        
    out_path = os.path.join(base_dir, name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully processed files and stored them in {base_dir}")
