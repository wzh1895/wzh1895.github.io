#!/bin/bash
# Generate thumbnails using macOS built-in sips command
# No additional dependencies required

input_dir="assets/Glasgow_Hundred_Views"
output_dir="assets/Glasgow_Hundred_Views/thumbnails"

# Create thumbnails directory
mkdir -p "$output_dir"

echo "Generating thumbnails..."

# Process all JPEG files from 001 to 101
for i in {1..101}; do
    filename=$(printf "%03d.jpeg" $i)
    input_path="$input_dir/$filename"
    output_path="$output_dir/$filename"
    
    if [ -f "$input_path" ]; then
        # Use sips to resize image to max 300px width/height, maintaining aspect ratio
        sips -Z 300 "$input_path" --out "$output_path" > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "Generated thumbnail: $filename"
        else
            echo "Error processing: $filename"
        fi
    else
        echo "File not found: $filename"
    fi
done

echo "Thumbnail generation complete!"
