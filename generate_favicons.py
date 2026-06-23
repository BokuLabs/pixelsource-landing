#!/usr/bin/env python3
"""Generate complete favicon set from a source PNG."""
import sys, os, base64
from PIL import Image

def main(src_path, out_dir="."):
    if not os.path.exists(src_path):
        print(f"ERROR: Source not found: {src_path}")
        sys.exit(1)

    img = Image.open(src_path).convert("RGBA")

    # Ensure output dir
    os.makedirs(out_dir, exist_ok=True)

    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192.png": 192,
        "android-chrome-512.png": 512,
    }

    for name, size in sizes.items():
        resized = img.resize((size, size), Image.LANCZOS)
        path = os.path.join(out_dir, name)
        # Convert to RGB if no alpha for small favicons
        if name.endswith(".ico"):
            resized.save(path, format="ICO", sizes=[(16,16), (32,32), (48,48)])
            print(f"  ✓ {name} ({size}×{size} multi-size ICO)")
        else:
            resized.save(path, format="PNG")
            print(f"  ✓ {name} ({size}×{size})")

    # favicon.ico — multi-size (16+32+48)
    ico_sizes = [16, 32, 48]
    ico_imgs = []
    for s in ico_sizes:
        ico_imgs.append(img.resize((s, s), Image.LANCZOS))
    ico_path = os.path.join(out_dir, "favicon.ico")
    # First frame with all sizes — Pillow expects (w,h) tuples
    ico_sizes_tuples = [(s, s) for s in ico_sizes]
    ico_imgs[0].save(ico_path, format="ICO", sizes=ico_sizes_tuples, append_images=ico_imgs[1:])
    print(f"  ✓ favicon.ico ({'+'.join(map(str,ico_sizes))} multi-size)")

    # favicon.svg — embed smallest PNG as data URI in SVG wrapper
    small_png = img.resize((16, 16), Image.LANCZOS)
    import io
    buf = io.BytesIO()
    small_png.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
  <image href="data:image/png;base64,{b64}" width="16" height="16"/>
</svg>
'''
    svg_path = os.path.join(out_dir, "favicon.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    print(f"  ✓ favicon.svg (16×16 PNG embedded)")

    print("\n✅ All favicons generated in:", out_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_favicons.py <source.png> [output_dir]")
        print("       output_dir defaults to current directory")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ".")
