<p align="center">
  <img src="logo-source.png" alt="PixelSource" width="200">
</p>

<h1 align="center">PixelSource</h1>
<p align="center">Source Code Marketplace — Landing Page</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Static_Site-FF6B6B?style=flat" alt="Static Site">
</p>

---

## 📁 Struktur File

```
pixelsource-landing/
├── index.html              ← Landing page utama (single-file, all-in-one)
├── logo.png                ← Logo PixelSource (full, untuk hero/header)
├── logo-source.png         ← Logo versi kecil (README, favicon source)
├── favicon.svg             ← Favicon utama (SVG, crisp di semua size)
├── favicon.ico             ← Favicon fallback (legacy browser)
├── favicon-16x16.png       ← Favicon 16x16 (tab kecil)
├── favicon-32x32.png       ← Favicon 32x32 (bookmark bar)
├── apple-touch-icon.png    ← Favicon iOS (180x180, homescreen)
├── android-chrome-192.png  ← PWA icon 192x192
├── android-chrome-512.png  ← PWA icon 512x512
├── site.webmanifest        ← PWA manifest (app name, icons, theme)
├── generate_favicons.py    ← Script generate semua favicon dari 1 source
├── .gitignore
└── README.md               ← File ini
```

### Penjelasan Tiap File

| File | Fungsi | Ukuran |
|------|--------|--------|
| `index.html` | Single-file landing page — CSS + JS inline, zero dependency kecuali Google Fonts | ~27KB |
| `logo.png` | Logo full resolusi, dipakai di hero section | ~178KB |
| `logo-source.png` | Logo versi kecil untuk social preview / README | ~16KB |
| `favicon.svg` | Favicon utama (vector, scalable) | ~1KB |
| `favicon.ico` | Favicon legacy untuk browser lama | <1KB |
| `favicon-16x16.png` | Tab icon kecil | <1KB |
| `favicon-32x32.png` | Bookmark bar icon | ~2KB |
| `apple-touch-icon.png` | iOS home screen icon (180x180) | ~8KB |
| `android-chrome-192.png` | Android home screen icon | ~9KB |
| `android-chrome-512.png` | Android splash screen icon | ~24KB |
| `site.webmanifest` | PWA metadata (nama, warna tema, icon references) | <1KB |

---

## 🎨 Cara Generate / Replace Favicon & Logo

### Dari 1 Logo Source → Semua Favicon

Edit `generate_favicons.py`:

```python
SOURCE = "logo-source.png"  # Ganti dengan file logo baru kamu
```

Lalu jalankan:

```bash
pip install Pillow
python3 generate_favicons.py
```

Akan meng-generate ulang semua file favicon secara otomatis:
- `favicon.svg` (auto-traced vector)
- `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`
- `apple-touch-icon.png` (180x180)
- `android-chrome-192.png`, `android-chrome-512.png`

### Manual Replace

Kalau mau ganti manual, tinggal replace file-file ini dengan nama yang sama:

```
favicon.svg          → SVG vector (recommended, crisp di semua size)
favicon.ico          → ICO format (legacy fallback)
favicon-16x16.png    → PNG 16×16px
favicon-32x32.png    → PNG 32×32px
apple-touch-icon.png → PNG 180×180px
android-chrome-192.png → PNG 192×192px
android-chrome-512.png → PNG 512×512px
```

> **Tips:** Favicon SVG paling penting — browser modern优先 pakai SVG. PNG hanya fallback.

---

## 🚀 Hosting Options

Landing page ini **pure static** (single HTML file, no build step, no server). Bisa di-hosting di mana aja:

### 1. Vercel (Recommended — Currently Active)
**URL:** `pixelsource.my.id`

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy dari folder ini
cd pixelsource-landing
vercel --prod
```

- ✅ Auto-deploy dari GitHub (connect repo ini ke Vercel)
- ✅ Custom domain gratis
- ✅ Global CDN, HTTPS otomatis
- ✅ Sudah ter-setup (CF proxy → Vercel)

### 2. Cloudflare Pages
```bash
# Push ke GitHub, lalu connect di dash.cloudflare.com
# Build command: (kosong — pure HTML)
# Output directory: /
```

- ✅ Unlimited bandwidth
- ✅ Custom domain + CF proxy
- ✅ Workers bisa ditambahin kalau butuh backend

### 3. Netlify
```bash
# Drag & drop folder ini ke app.netlify.com/drop
# Atau connect GitHub repo
```

- ✅ Form handling built-in
- ✅ Serverless functions available

### 4. GitHub Pages
```bash
# Settings → Pages → Source: main branch → / (root)
# URL: BokuLabs.github.io/pixelsource-landing
```

- ✅ Gratis, langsung dari repo ini
- ⚠️ Private repo butuh GitHub Pro untuk Pages
- ⚠️ Custom domain perlu setup DNS manual

### 5. Any Static Host
File-file ini bisa di-upload ke hosting manapun yang support static files:
- **Nginx / Apache** — taruh di document root
- **S3 + CloudFront** — upload ke bucket
- **Firebase Hosting** — `firebase deploy`
- **Surge.sh** — `npx surge ./ pixelsource.my.id`

---

## 🔧 Customization

### Ganti Warna Tema

Edit CSS variables di `<style>` bagian `:root`:

```css
:root {
  --bg: #0a0a0f;        /* Background utama */
  --bg2: #111118;       /* Background secondary */
  --card: #1a1a28;      /* Card background */
  --border: #2a2a40;    /* Border color */
  --accent: #00e5a0;    /* Accent hijau (primary CTA) */
  --accent2: #00c8ff;   /* Accent biru (links) */
  --pixel: #ff3c6f;     /* Pixel pink (highlights) */
  --text: #e8e8f0;      /* Text utama */
  --text2: #8080a0;     /* Text secondary */
  --text3: #505068;     /* Text muted */
}
```

### Ganti Font

```html
<!-- Pixel font untuk heading pixel -->
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
<!-- Body font -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
```

### Tambah Produk Baru

Cari section `<!-- PRODUCT CARDS -->` di `index.html`, copy-paste card yang ada, ganti:
- `data-name` → nama produk
- `data-price` → harga (format: "Rp 300.000")
- `data-img` → URL gambar produk
- Card content (title, description, tags)

---

## 📌 Links

- **Live:** [pixelsource.my.id](https://pixelsource.my.id)
- **Owner:** [@accustor](https://t.me/accustor)

---

<p align="center">
  <sub>Built with ❤️ by BokuLabs</sub>
</p>
