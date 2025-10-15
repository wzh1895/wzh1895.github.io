#!/usr/bin/env python3
"""
Generate thumbnails for images in a cross-platform way using Pillow.
This script replaces the bash/sips approach with a Python solution that works on all platforms.
"""

import os
from pathlib import Path
from PIL import Image

def generate_thumbnails(input_dir, output_dir, max_size=300, start=1, end=101):
    """
    Generate thumbnails for numbered JPEG files.
    
    Args:
        input_dir: Directory containing the original images
        output_dir: Directory where thumbnails will be saved
        max_size: Maximum width/height for thumbnails (maintains aspect ratio)
        start: Starting file number (inclusive)
        end: Ending file number (inclusive)
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("Generating thumbnails...")
    
    success_count = 0
    error_count = 0
    missing_count = 0
    
    # Process all JPEG files from start to end
    for i in range(start, end + 1):
        filename = f"{i:03d}.jpeg"
        input_file = Path(input_dir) / filename
        output_file = output_path / filename
        
        if not input_file.exists():
            print(f"File not found: {filename}")
            missing_count += 1
            continue
        
        try:
            # Open the image
            with Image.open(input_file) as img:
                # Handle EXIF orientation to prevent rotated thumbnails
                try:
                    from PIL import ImageOps
                    img = ImageOps.exif_transpose(img)
                except Exception:
                    # If EXIF handling fails, continue without it
                    pass
                
                # Convert RGBA to RGB if necessary (for JPEG compatibility)
                if img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = rgb_img
                
                # Calculate new size maintaining aspect ratio
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
                # Save the thumbnail
                img.save(output_file, 'JPEG', quality=85, optimize=True)
                
            print(f"Generated thumbnail: {filename}")
            success_count += 1
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            error_count += 1
    
    print(f"\nThumbnail generation complete!")
    print(f"Success: {success_count}, Errors: {error_count}, Missing: {missing_count}")

if __name__ == "__main__":
    # Configuration
    input_dir = "assets/Glasgow_Hundred_Views"
    output_dir = "assets/Glasgow_Hundred_Views/thumbnails"
    
    # Generate thumbnails
    generate_thumbnails(input_dir, output_dir, max_size=300, start=1, end=101)
