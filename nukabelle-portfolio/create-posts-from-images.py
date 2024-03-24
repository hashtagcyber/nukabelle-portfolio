import os

# Directory paths
img_dir = 'static/img'
gallery_dir = 'content/portfolio'

# Ensure gallery directory exists
os.makedirs(gallery_dir, exist_ok=True)

# List all images in the img directory
img_files = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]

# Create markdown file for each image if it doesn't already exist
for img_file in img_files:
    # Extract the file name without extension to use as the title
    file_name_without_ext = os.path.splitext(img_file)[0]
    markdown_file_path = os.path.join(gallery_dir, f"{file_name_without_ext}.md")
    
    # Skip if markdown file already exists
    if os.path.exists(markdown_file_path):
        continue
    
    # Set the title to the file name and the image path relative to the static directory
    content = f"""---
title: "{file_name_without_ext}"
date: {os.path.getmtime(os.path.join(img_dir, img_file))}
image: "img/{img_file}"
description: "A beautiful piece."
---"""
    
    # Write the markdown file
    with open(markdown_file_path, 'w') as md_file:
        md_file.write(content)
