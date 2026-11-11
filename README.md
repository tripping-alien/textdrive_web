# TextDrive - Landing Page

Official landing page for the **TextDrive** Android application. Built with pure **HTML5, CSS3, and JavaScript** with zero backend or runtime dependencies.

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=google-chrome&logoColor=white)](https://notextingwhiledriving.info/)
[![Studio](https://img.shields.io/badge/Studio-smalltalkapps.art-FFBE3B.svg)](https://smalltalkapps.art)

## 🚀 About The Project

This is a modern, responsive, and lightweight landing page created to showcase the TextDrive hands-free driving assistant app.

### Key Features:
*   **Pure Static HTML5, CSS3 & JS**: No Python, Flask, Node, or server process needed.
*   **Universal Compatibility**: Works immediately when opening `index.html` locally or deployed to GitHub Pages, Cloudflare Pages, Render, Vercel, Netlify, or any static web host.
*   **Animated WebGL Particle Background**: Lightweight particle starfield using Three.js with accessibility support for `prefers-reduced-motion` and visibility pause.
*   **Responsive Glassmorphism Design**: High-contrast, mobile-first design with smooth transitions and CSS variables.
*   **SEO & Rich Results Ready**: Complete Open Graph, Twitter Cards, Canonical links, and Schema.org `SoftwareApplication` + `FAQPage` structured data.
*   **Android App Links**: Includes `.well-known/assetlinks.json` for verified Android App Links.

## 🏁 Getting Started

Because this is a pure HTML5 static site, no build steps or dependencies are required.

### Local Preview

1. **Directly open in browser:**
   Double-click `index.html` or open it with any web browser.

2. **Or run with any local static server:**
   ```sh
   # Using Python's built-in HTTP server:
   python -m http.server 8000

   # Or using Node.js / npx:
   npx serve .
   ```
   Navigate to `http://localhost:8000`.

## 🌐 Deployment

The repository is pre-configured for instant zero-config static hosting:
* **GitHub Pages**: Settings > Pages > Deploy from branch `main` / root.
* **Render**: Deploys automatically as a static site via `render.yaml`.
* **Vercel / Netlify / Cloudflare**: Simply link the repository with publish directory set to root (`.`).
