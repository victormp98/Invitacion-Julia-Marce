document.addEventListener('DOMContentLoaded', () => {

    // Detectar preferencia de movimiento reducido una sola vez
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const introPhoto = document.getElementById('intro-photo');

    if (introPhoto) {
        document.body.classList.add('intro-active');

        const hideIntro = () => {
            introPhoto.classList.add('is-hidden');
            document.body.classList.remove('intro-active');
        };

        window.setTimeout(hideIntro, reducedMotion ? 900 : 2400);
    }

    // =========================================
    // COUNTDOWN TIMER — Con animación de "pop"
    // ISO 8601 con zona horaria explícita (CDT México = UTC-05:00 en agosto)
    // Evita parsing ambiguo entre navegadores y regiones
    // =========================================
    const targetDate = new Date('2026-08-08T17:00:00-05:00').getTime();

    const els = {
        days:    document.getElementById('days'),
        hours:   document.getElementById('hours'),
        minutes: document.getElementById('minutes'),
        seconds: document.getElementById('seconds'),
    };

    // Guarda el valor anterior para animar solo cuando cambia
    const prevValues = { days: '', hours: '', minutes: '', seconds: '' };

    function setWithPop(el, key, value) {
        if (!el) return;
        const padded = String(value).padStart(2, '0');
        if (padded !== prevValues[key]) {
            el.textContent = padded;
            el.classList.remove('updated');
            void el.offsetWidth; // reflow para reiniciar animación
            el.classList.add('updated');
            prevValues[key] = padded;
        }
    }

    function updateCountdown() {
        const now      = Date.now();
        const distance = targetDate - now;

        if (distance < 0) {
            clearInterval(timerInterval);
            const countdown = document.getElementById('countdown');
            if (countdown) {
                countdown.innerHTML = `
                    <p style="
                        font-family:'Cinzel Decorative',serif;
                        font-size:clamp(1.4rem,4vw,2rem);
                        color:var(--gold-bright);
                        text-align:center;
                        grid-column:1/-1;
                        padding:2rem;
                        text-shadow:0 0 20px rgba(240,192,96,0.5);
                    ">✦ ¡Es el día! ✦</p>`;
            }
            return;
        }

        setWithPop(els.days,    'days',    Math.floor(distance / 86400000));
        setWithPop(els.hours,   'hours',   Math.floor((distance % 86400000) / 3600000));
        setWithPop(els.minutes, 'minutes', Math.floor((distance % 3600000)  / 60000));
        setWithPop(els.seconds, 'seconds', Math.floor((distance % 60000)    / 1000));
    }

    const hasCountdown = Object.values(els).every(Boolean);
    let timerInterval;

    if (hasCountdown) {
        timerInterval = setInterval(updateCountdown, 1000);
        updateCountdown();
    }


    // =========================================
    // PARTÍCULAS FLOTANTES
    // Desactivadas si el usuario prefiere movimiento reducido
    // =========================================
    if (!reducedMotion) {
        const particlesContainer = document.getElementById('particles-container');
        const palette = [
            { color: '#c5a059', glow: 'rgba(197, 160, 89, 0.6)' },
            { color: '#a855f7', glow: 'rgba(168, 85, 247, 0.5)' },
            { color: '#f0c060', glow: 'rgba(240, 192, 96, 0.5)' },
            { color: '#e0aaff', glow: 'rgba(224, 170, 255, 0.4)' },
            { color: '#ffffff', glow: 'rgba(255, 255, 255, 0.3)' },
        ];

        function getScrollLimit() {
            return document.body.scrollHeight * 0.75;
        }

        function createParticle() {
            if (!particlesContainer) return;
            if (window.scrollY > getScrollLimit()) return;

            const particle = document.createElement('div');
            particle.className = 'particle';

            const size  = Math.random() * 3.5 + 1;
            const entry = palette[Math.floor(Math.random() * palette.length)];
            const dur   = Math.random() * 14 + 10;
            const drift = (Math.random() - 0.5) * 80;

            Object.assign(particle.style, {
                width:             `${size}px`,
                height:            `${size}px`,
                left:              `${Math.random() * 99}vw`,
                backgroundColor:   entry.color,
                boxShadow:         `0 0 ${size * 3}px ${entry.glow}`,
                animationDuration: `${dur}s`,
                opacity:           String(Math.random() * 0.5 + 0.2),
                '--drift':         `${drift}px`,
            });

            particlesContainer.appendChild(particle);
            setTimeout(() => particle.remove(), dur * 1000);
        }

        for (let i = 0; i < 35; i++) {
            setTimeout(createParticle, i * 60);
        }
        setInterval(createParticle, 600);
    }


    // =========================================
    // INTERSECTION OBSERVER — Scroll animations
    // =========================================
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // No se desconecta para respetar el --delay CSS
            }
        });
    }, { threshold: 0.12 });

    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });


    // =========================================
    // PARALLAX SUAVE EN EL FONDO
    // Solo en desktop con pointer fino (mouse) y sin prefers-reduced-motion
    // background-attachment:fixed ya hace el efecto en desktop; el JS
    // solo añade un desplazamiento extra sutil.
    // =========================================
    const isDesktop   = window.matchMedia('(pointer: fine) and (min-width: 769px)').matches;

    if (isDesktop && !reducedMotion) {
        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    document.body.style.backgroundPositionY =
                        `${-(window.scrollY * 0.04)}px`;
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }


    // =========================================
    // ÁLBUM VIVO — Cambio automático de imágenes
    // =========================================
    const albumSlider = document.querySelector('[data-album-slider]');

    if (albumSlider) {
        const slides = Array.from(albumSlider.querySelectorAll('.album-slide'));
        const dots = Array.from(albumSlider.querySelectorAll('.album-dot'));
        const prevButton = albumSlider.querySelector('[data-album-prev]');
        const nextButton = albumSlider.querySelector('[data-album-next]');
        let activeIndex = slides.findIndex(slide => slide.classList.contains('is-active'));
        let albumTimer;
        const hoverPauseEnabled = window.matchMedia('(pointer: fine)').matches;

        if (activeIndex < 0) activeIndex = 0;

        function showSlide(nextIndex) {
            slides.forEach((slide, index) => {
                slide.classList.toggle('is-active', index === nextIndex);
            });

            dots.forEach((dot, index) => {
                dot.classList.toggle('is-active', index === nextIndex);
            });

            activeIndex = nextIndex;
        }

        function restartAlbum() {
            if (reducedMotion) return;
            startAlbum();
        }

        function goToSlide(nextIndex) {
            showSlide(nextIndex);
            restartAlbum();
        }

        function goToAdjacentSlide(direction) {
            const nextIndex = (activeIndex + direction + slides.length) % slides.length;
            goToSlide(nextIndex);
        }

        function startAlbum() {
            if (slides.length < 2 || reducedMotion) return;
            stopAlbum();
            albumTimer = setInterval(() => {
                const nextIndex = (activeIndex + 1) % slides.length;
                showSlide(nextIndex);
            }, 4200);
        }

        function stopAlbum() {
            if (albumTimer) clearInterval(albumTimer);
        }

        showSlide(activeIndex);
        startAlbum();

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => goToSlide(index));
        });

        if (prevButton) {
            prevButton.addEventListener('click', () => goToAdjacentSlide(-1));
        }

        if (nextButton) {
            nextButton.addEventListener('click', () => goToAdjacentSlide(1));
        }

        if (hoverPauseEnabled) {
            albumSlider.addEventListener('mouseenter', stopAlbum);
            albumSlider.addEventListener('mouseleave', startAlbum);
        }
    }


    // =========================================
    // REPRODUCTOR DE MÚSICA
    // aria-pressed sincronizado para accesibilidad
    // =========================================
    const audioToggle = document.getElementById('audio-toggle');
    const audioIcon   = document.getElementById('audio-icon');
    const bgMusic     = document.getElementById('bg-music');
    const musicBar    = document.getElementById('music-bar');
    const musicText   = document.getElementById('music-text');

    if (audioToggle && bgMusic) {
        let isPlaying = false;

        function setPlayState(playing) {
            isPlaying = playing;
            audioToggle.setAttribute('aria-pressed', String(playing));
            if (audioIcon) audioIcon.textContent = playing ? '⏸' : '▶';
            if (musicBar) musicBar.classList.toggle('playing', playing);
            if (musicText) {
                musicText.textContent = playing ? 'Reproduciendo melodía' : 'Toca para escuchar nuestra cancion';
            }
        }

        audioToggle.addEventListener('click', () => {
            if (isPlaying) {
                bgMusic.pause();
                setPlayState(false);
            } else {
                bgMusic.play()
                    .then(() => setPlayState(true))
                    .catch(() => {
                        if (musicText) musicText.textContent = 'Toca aquí para escuchar';
                    });
            }
        });

        // Sincronizar si el audio se pausa externamente (ej. otra pestaña)
        bgMusic.addEventListener('pause', () => {
            if (isPlaying) setPlayState(false);
        });

        bgMusic.addEventListener('play', () => {
            if (!isPlaying) setPlayState(true);
        });

        bgMusic.addEventListener('error', () => {
            if (musicText) musicText.textContent = 'Pega tu audio en /audio/melodia-boda.mp4';
            audioToggle.setAttribute('disabled', 'disabled');
        });
    }


    // =========================================
    // CURSOR GLOW — Solo en desktop y sin reduced-motion
    // =========================================
    if (!reducedMotion && window.matchMedia('(pointer: fine)').matches) {
        const glow = document.createElement('div');
        Object.assign(glow.style, {
            position:      'fixed',
            width:         '320px',
            height:        '320px',
            borderRadius:  '50%',
            background:    'radial-gradient(ellipse, rgba(168, 85, 247, 0.07) 0%, transparent 70%)',
            pointerEvents: 'none',
            zIndex:        '0',
            transform:     'translate(-50%, -50%)',
            top:           '-999px', // empieza fuera de pantalla
            left:          '-999px',
            willChange:    'top, left',
        });
        document.body.appendChild(glow);

        document.addEventListener('mousemove', e => {
            glow.style.left = `${e.clientX}px`;
            glow.style.top  = `${e.clientY}px`;
        }, { passive: true });
    }

});
