import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make hero-editorial transparent and overflow hidden
css = re.sub(
    r'\.hero-editorial\s*\{[^}]*\}',
    '.hero-editorial { position: relative; width: 100%; min-height: 100vh; display: flex; flex-direction: column; align-items: center; overflow: hidden; background-color: transparent !important; }',
    css
)

# Elevate content z-index
css = re.sub(
    r'\.hero-content-editorial\s*\{[^}]*\}',
    '.hero-content-editorial { position: relative; z-index: 3; display: flex; flex-direction: column; align-items: center; text-align: center; width: 90%; max-width: 800px; margin-top: 30vh; }',
    css
)

layers = '''
.hero-bg-layer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("img/hero-bg.webp");
    background-size: cover;
    background-position: center;
    z-index: 1;
}

.hero-overlay-layer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(4, 6, 13, 0.2) 0%, rgba(4, 6, 13, 0.85) 100%);
    z-index: 2;
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css + layers)

print("CSS updated successfully")
