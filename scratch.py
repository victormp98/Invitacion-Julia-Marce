import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract head and music bar
head_match = re.search(r'(<!DOCTYPE html>.*?<div class=\"music-bar\".*?</div>)', html, re.DOTALL)
head_content = head_match.group(1) if head_match else ""

# Extract Padrinos
padrinos_match = re.search(r'(<section id=\"padrinos\" class=\"section fade-in\">.*?</section>)', html, re.DOTALL)
padrinos_content = padrinos_match.group(1) if padrinos_match else ""

# Extract scripts at the end
scripts_match = re.search(r'(<!-- Partículas flotantes -->.*</html>)', html, re.DOTALL)
scripts_content = scripts_match.group(1) if scripts_match else "</body></html>"

new_body = f'''
    <!-- ============================================
         MÓDULO 1: HERO EDITORIAL
    ============================================ -->
    <header id="hero-editorial" class="hero-editorial fade-in">
        <div class="hero-image-wrapper">
            <!-- La imagen irá como background en CSS -->
            <div class="hero-overlay"></div>
        </div>
        <div class="hero-content-editorial">
            <p class="pre-title">Nuestra Boda</p>
            <h1 class="couple-names">Julia <span class="hero-ampersand">&amp;</span> Marcelino</h1>
            <p class="hero-subtitle">Un amor con banda sonora.<br>Nos casamos, y queremos celebrarlo contigo.</p>
            
            <div class="hero-chips">
                <span class="chip">🗓️ 22 · Agosto · 2026</span>
                <span class="chip">⏰ 12:00 hrs</span>
                <span class="chip">📍 Complejo El Olivar</span>
            </div>
            
            <div class="hero-story">
                <p>“Todo comenzó bajo las luces de Madrid. Nos conocimos cerca de Gran Vía, con la ciudad como escenario y esa sensación de ‘esto tiene algo’. Lo que empezó como una casualidad bonita se convirtió en nuestro guion. Y ahora, después de tantos capítulos, toca el mejor: el del ‘sí, quiero’.”</p>
            </div>
        </div>
        <div class="scroll-hint" aria-hidden="true">
            <span>✦</span>
            <span class="scroll-hint-line"></span>
        </div>
    </header>

    <!-- ============================================
         MÓDULO 2: ITINERARIO + GUÁRDATE LA FECHA
    ============================================ -->
    <section id="programa" class="section fade-in">
        <div class="container">
            <div class="section-header">
                <div class="ornament-divider" aria-hidden="true">✦ ✦ ✦</div>
                <h2 class="section-title">El plan del día</h2>
                <p class="section-subtitle">Para que vengas a disfrutar sin pensar en nada (más que en brindar).</p>
            </div>

            <div class="timeline">
                <div class="timeline-item fade-in" style="--delay: 0.1s">
                    <div class="timeline-dot"><span>⛪</span></div>
                    <div class="timeline-content">
                        <p class="timeline-time">12:00 p. m.</p>
                        <h3 class="timeline-event">Ceremonia</h3>
                        <p class="timeline-desc">Promesas, emoción y abrazos.</p>
                    </div>
                </div>

                <div class="timeline-item fade-in" style="--delay: 0.2s">
                    <div class="timeline-dot"><span>🥂</span></div>
                    <div class="timeline-content">
                        <p class="timeline-time">2:00 p. m.</p>
                        <h3 class="timeline-event">Cóctel</h3>
                        <p class="timeline-desc">Música, charlas y aperitivos.</p>
                    </div>
                </div>

                <div class="timeline-item fade-in" style="--delay: 0.3s">
                    <div class="timeline-dot"><span>🍽️</span></div>
                    <div class="timeline-content">
                        <p class="timeline-time">4:00 p. m.</p>
                        <h3 class="timeline-event">Banquete</h3>
                        <p class="timeline-desc">Cena y brindis.</p>
                    </div>
                </div>

                <div class="timeline-item fade-in" style="--delay: 0.4s">
                    <div class="timeline-dot"><span>🌙</span></div>
                    <div class="timeline-content">
                        <p class="timeline-time">Hasta que el cuerpo aguante</p>
                        <h3 class="timeline-event">Fiesta</h3>
                        <p class="timeline-desc">Baile y diversión.</p>
                    </div>
                </div>
                
                <div class="calendar-card glass-accent glow-border fade-in" style="--delay: 0.5s">
                    <div class="calendar-card-content">
                        <h3>Guárdate la fecha</h3>
                        <p class="calendar-date">22 de Agosto de 2026 · 12:00 hrs</p>
                        <div class="calendar-buttons">
                            <a href="#" class="btn btn-outline" onclick="alert('Google Calendar link próximamente'); return false;">Google Calendar</a>
                            <a href="#" class="btn btn-outline" onclick="alert('Apple Calendar link próximamente'); return false;">Apple Calendar</a>
                            <a href="#" class="btn btn-outline" onclick="alert('ICS link próximamente'); return false;">Descargar .ICS</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         MÓDULO 3: UBICACIÓN
    ============================================ -->
    <section id="ubicacion" class="section fade-in">
        <div class="container">
            <div class="section-header">
                <div class="ornament-divider" aria-hidden="true">✦ ✦ ✦</div>
                <h2 class="section-title">Cómo llegar</h2>
            </div>
            
            <div class="location-grid">
                <div class="location-info fade-in" style="--delay: 0.1s">
                    <h3>Complejo El Olivar</h3>
                    <p class="location-address">Alcalá de Henares</p>
                    <ul class="location-tips">
                        <li><strong>Si vienes en coche:</strong> Ruta recomendada por la A-2 y parking disponible.</li>
                        <li><strong>Si vienes en transporte:</strong> Cercanías hasta Alcalá y taxi al complejo.</li>
                    </ul>
                    <p class="location-phrase">"Ven con tiempo… y con ganas, lo demás lo ponemos nosotros."</p>
                    <a href="#" class="btn btn-primary pulse" target="_blank" rel="noopener noreferrer">Abrir en Google Maps</a>
                </div>
                
                <div class="location-map map-wrapper glow-border fade-in" style="--delay: 0.2s">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3034.425126307777!2d-3.3468832846014493!3d40.48785867935706!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd424eb0e31e5125%3A0x6e9f5e3e3b3b4f!2sComplejo%20El%20Olivar!5e0!3m2!1ses!2ses!4v1689000000000!5m2!1ses!2ses" width="100%" height="100%" style="border:0; min-height: 300px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         DRESS CODE
    ============================================ -->
    <section id="detalles" class="section fade-in">
        <div class="container">
            <div class="extra-info">
                <div class="info-box glass-accent">
                    <span class="card-icon" aria-hidden="true">👗</span>
                    <h3>Código de vestimenta</h3>
                    <p class="dress-code-title">Formal · Etiqueta</p>
                    <p class="reserved">
                        Los colores reservados para la novia son el <strong>Blanco</strong> y el <strong>Morado</strong>.<br>
                        Gracias por lucir tan espectacular como merece esta noche.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================
         MÓDULO 5: RSVP
    ============================================ -->
    <section id="rsvp" class="section fade-in">
        <div class="container">
            <div class="section-header">
                <div class="ornament-divider" aria-hidden="true">✦ ✦ ✦</div>
                <h2 class="section-title">Confirmación de asistencia</h2>
                <p class="section-subtitle">Por favor, confirmad antes del <strong>15 de julio de 2026</strong> para organizar menús y detalles.</p>
                <p class="rsvp-note" style="font-size: 0.9rem; color: #a58e65; margin-bottom: 2rem;">En el formulario podréis indicar alergias, intolerancias y alguna canción imprescindible.</p>
            </div>
            
            <div class="rsvp-embed-wrapper glow-border">
                <div style="width: 100%; min-height: 500px; display: flex; align-items: center; justify-content: center; background: rgba(197, 160, 89, 0.05);">
                    <p style="color: #c5a059; font-style: italic;">[Formulario de RSVP Embed Aquí]</p>
                </div>
            </div>
            
            <div class="rsvp-fallback" style="margin-top: 2rem; text-align: center;">
                <p style="margin-bottom: 1rem; color: #fff8e1;">¿Tienes problemas para ver el formulario?</p>
                <a href="#" class="btn btn-outline" target="_blank">Abrir formulario en otra pestaña</a>
            </div>
        </div>
    </section>

    <!-- ============================================
         MÓDULO 4: ÁLBUM COMPARTIDO
    ============================================ -->
    <section id="album" class="section fade-in">
        <div class="container">
            <div class="section-header">
                <div class="ornament-divider" aria-hidden="true">✦ ✦ ✦</div>
                <h2 class="section-title">Vuestra mirada es nuestro mejor recuerdo</h2>
                <p class="section-subtitle">Queremos fotos naturales, selfies locos y momentos robados. Nada de posados: queremos ver la boda a través de vuestros ojos.</p>
            </div>
            
            <div class="photo-editorial-grid">
                <div class="photo-placeholder glass-accent glow-border p-large">
                    <span aria-hidden="true">📸</span>
                </div>
                <div class="photo-placeholder glass-accent glow-border p-small">
                    <span aria-hidden="true">✨</span>
                </div>
                <div class="photo-placeholder glass-accent glow-border p-small">
                    <span aria-hidden="true">🤍</span>
                </div>
            </div>
            
            <div class="actions" style="margin-top: 3rem; text-align: center;">
                <a href="#" class="btn btn-primary pulse" target="_blank">Subir fotos al álbum</a>
            </div>
        </div>
    </section>

    <!-- ============================================
         REGALOS
    ============================================ -->
    <section id="gifts" class="section fade-in">
        <div class="container">
            <div class="section-header">
                <div class="ornament-divider" aria-hidden="true">✦ ✦ ✦</div>
                <h2 class="section-title">Sugerencia de regalo</h2>
            </div>
            <div class="info-box glass-accent">
                <span class="card-icon" aria-hidden="true">✨</span>
                <p class="gift-main">Tu presencia ya es el regalo más grande.</p>
                <p>Si deseas celebrar con un detalle adicional, puedes hacérnoslo llegar ese día.</p>
                <div class="gift-line">
                    <p>Un sobre con efectivo el día del evento<br>es siempre bienvenido con todo nuestro agradecimiento.</p>
                </div>
            </div>
        </div>
    </section>

{padrinos_content}

    <!-- ============================================
         FOOTER
    ============================================ -->
    <footer class="footer">
        <div class="footer-names">Julia &amp; Marcelino</div>
        <p class="footer-date">22 · VIII · 2026</p>
        <p class="footer-tagline">Hecho con amor oscuro, para una noche que brillará para siempre ✦</p>
    </footer>

{scripts_content}
'''

new_full_html = head_content + new_body

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_full_html)

print('Updated index.html')
