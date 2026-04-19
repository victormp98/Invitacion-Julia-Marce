css_to_append = """

/* =========================================
   NUEVOS MÓDULOS - REESTRUCTURACIÓN EDITORIAL
========================================= */

/* =========================================
   MÓDULO 1: HERO EDITORIAL
========================================= */
.hero-editorial {
    position: relative;
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #04060d;
}

.hero-image-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 75vh;
    background-image: url('img/hero-bg.webp'); /* Asumiendo que esta imagen existe */
    background-size: cover;
    background-position: center;
    z-index: 0;
}

.hero-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 60%;
    background: linear-gradient(to top, #04060d 0%, transparent 100%);
}

.hero-content-editorial {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 90%;
    max-width: 800px;
    z-index: 2;
    margin-top: 30vh;
}

.hero-subtitle {
    font-family: 'Raleway', sans-serif;
    font-size: 1.2rem;
    color: #fff8e1;
    margin-top: 1rem;
    font-weight: 300;
}

/* CHIPS */
.hero-chips {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 2rem;
}

.chip {
    background: rgba(197, 160, 89, 0.15);
    border: 1px solid rgba(197, 160, 89, 0.3);
    padding: 0.5rem 1rem;
    border-radius: 50px;
    font-family: 'Raleway', sans-serif;
    font-size: 0.9rem;
    color: #c5a059;
    backdrop-filter: blur(5px);
}

.hero-story {
    margin-top: 3rem;
    max-width: 600px;
    font-family: 'Raleway', sans-serif;
    color: rgba(255, 255, 255, 0.7);
    line-height: 1.6;
    font-size: 1rem;
    position: relative;
}

@media (max-width: 768px) {
    .hero-content-editorial {
        margin-top: 20vh;
    }
    .hero-image-wrapper {
        height: 65vh;
    }
    .hero-chips {
        margin-top: 2rem;
    }
    .hero-story {
        margin-top: 2rem;
        padding: 0 1rem;
    }
}

/* =========================================
   MÓDULO 2: CALENDARIO
========================================= */
.calendar-card {
    margin-top: 3rem;
    padding: 2rem;
    text-align: center;
    border-radius: 12px;
}
.calendar-card h3 {
    font-family: 'Cinzel Decorative', serif;
    color: #c5a059;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}
.calendar-date {
    font-family: 'Raleway', sans-serif;
    color: #fff8e1;
    margin-bottom: 1.5rem;
}
.calendar-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}
.btn-outline {
    display: inline-block;
    padding: 0.6rem 1.2rem;
    border: 1px solid #c5a059;
    color: #c5a059;
    text-decoration: none;
    border-radius: 50px;
    font-family: 'Raleway', sans-serif;
    font-size: 0.9rem;
    transition: all 0.3s ease;
}
.btn-outline:hover {
    background: rgba(197, 160, 89, 0.1);
}

/* =========================================
   MÓDULO 3: UBICACIÓN
========================================= */
.location-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
    margin-top: 2rem;
}
.location-info h3 {
    font-family: 'Cinzel Decorative', serif;
    color: #c5a059;
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
}
.location-address {
    font-family: 'Raleway', sans-serif;
    color: #fff8e1;
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
}
.location-tips {
    list-style: none;
    padding: 0;
    margin-bottom: 1.5rem;
}
.location-tips li {
    margin-bottom: 1rem;
    font-family: 'Raleway', sans-serif;
    color: rgba(255, 255, 255, 0.7);
    line-height: 1.5;
}
.location-tips strong {
    color: #c5a059;
}
.location-phrase {
    font-style: italic;
    color: #fff8e1;
    margin-bottom: 2rem;
}
.map-wrapper {
    border-radius: 12px;
    overflow: hidden;
    aspect-ratio: 1 / 1;
    filter: sepia(15%) hue-rotate(180deg) brightness(80%) contrast(110%);
}
@media (max-width: 768px) {
    .location-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}

/* =========================================
   MÓDULO 4: ÁLBUM EDITORIAL
========================================= */
.photo-editorial-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}
.photo-placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    color: rgba(197, 160, 89, 0.5);
    font-size: 2rem;
}
.p-large {
    min-height: 250px;
    grid-column: span 2;
}
.p-small {
    min-height: 180px;
}
@media (max-width: 480px) {
    .p-large {
        grid-column: span 1;
        min-height: 200px;
    }
}

/* =========================================
   MÓDULO 5: RSVP EMBED
========================================= */
.rsvp-embed-wrapper {
    border-radius: 12px;
    overflow: hidden;
    margin: 0 auto;
    max-width: 600px;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_append)

print('Updated style.css')
