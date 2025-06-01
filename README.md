# Glasgow Hundred Views Gallery

A static photo gallery showcasing 101 views of Glasgow with bilingual descriptions (Chinese and English).

## Features

- **Optimized Loading**: Uses thumbnails for fast page loading, only loads full-resolution images when clicked
- **Responsive Design**: Grid layout that adapts to different screen sizes  
- **Full-Screen Viewing**: Click any thumbnail to view the full-resolution image
- **Bilingual Descriptions**: Chinese and English descriptions for each image
- **Static Hosting**: Runs entirely client-side, perfect for GitHub Pages

## File Structure

```
├── index.html                          # Main gallery page
├── assets/
│   ├── gallery.css                     # Styles for the gallery
│   └── Glasgow_Hundred_Views/
│       ├── index.csv                   # Image descriptions (CN & EN)
│       ├── 001.jpeg - 101.jpeg         # Full-resolution images
│       └── thumbnails/
│           └── 001.jpeg - 101.jpeg     # Optimized thumbnails (300px max)
├── generate_thumbnails.sh              # Script to generate thumbnails
└── .nojekyll                          # Disables Jekyll processing for GitHub Pages
```

## Usage

### Viewing the Gallery
Simply open `index.html` in a web browser or visit the GitHub Pages URL.

### Adding New Images
1. Add new full-resolution images to `assets/Glasgow_Hundred_Views/` 
2. Update `assets/Glasgow_Hundred_Views/index.csv` with new descriptions
3. Run `./generate_thumbnails.sh` to create thumbnails
4. Commit and push to GitHub

### Regenerating Thumbnails
If you need to regenerate all thumbnails (e.g., to change thumbnail size):

```bash
./generate_thumbnails.sh
```

The script uses macOS's built-in `sips` command to resize images to 300px maximum width/height while maintaining aspect ratio.

## GitHub Pages Setup

1. Create a repository named `username.github.io` (replace with your GitHub username)
2. Upload all files to the repository
3. In repository Settings → Pages, set Source to "Deploy from a branch" and select "main" branch
4. Your gallery will be available at `https://username.github.io`

## Performance

- **Thumbnail sizes**: ~20-50KB each (vs 1-5MB for full images)
- **Initial page load**: ~2-5MB total (thumbnails only)
- **Full images**: Loaded on-demand when clicked
- **Total bandwidth savings**: ~90% for initial page load

## Browser Compatibility

Works in all modern browsers that support:
- CSS Grid
- JavaScript ES6+
- Fetch API (used by PapaParse for CSV loading)
