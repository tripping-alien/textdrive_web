/**
 * TextDrive Landing Page — Interactive Particle Field
 * Vanilla JavaScript (HTML5 / WebGL via Three.js)
 */

(function () {
    'use strict';

    // Verify Three.js availability and canvas support
    const canvas = document.getElementById('bg');
    if (!canvas || typeof THREE === 'undefined') {
        return;
    }

    // Check user preference for reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let scene, camera, renderer, mesh, animFrameId;
    let isPageVisible = true;

    function init() {
        try {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            
            renderer = new THREE.WebGLRenderer({
                canvas: canvas,
                alpha: true,
                antialias: false,
                powerPreference: 'low-power'
            });

            const dpr = Math.min(window.devicePixelRatio || 1, 2);
            renderer.setPixelRatio(dpr);
            renderer.setSize(window.innerWidth, window.innerHeight);

            // Construct 2,500 Starfield Particles
            const count = 2500;
            const geometry = new THREE.BufferGeometry();
            const positions = new Float32Array(count * 3);

            for (let i = 0; i < count * 3; i++) {
                positions[i] = (Math.random() - 0.5) * 6;
            }

            geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

            const material = new THREE.PointsMaterial({
                size: 0.007,
                color: 0x5DADE2,
                transparent: true,
                opacity: 0.8,
                blending: THREE.AdditiveBlending
            });

            mesh = new THREE.Points(geometry, material);
            scene.add(mesh);
            camera.position.z = 2.5;

            // Initial render
            renderer.render(scene, camera);

            // Start animation loop if motion is allowed
            if (!prefersReducedMotion) {
                const clock = new THREE.Clock();

                function animate() {
                    if (isPageVisible) {
                        const elapsedTime = clock.getElapsedTime();
                        mesh.rotation.y = elapsedTime * 0.05;
                        mesh.rotation.x = Math.sin(elapsedTime * 0.2) * 0.1;
                        renderer.render(scene, camera);
                    }
                    animFrameId = requestAnimationFrame(animate);
                }

                animate();
            }
        } catch (err) {
            console.warn('WebGL initialization failed, falling back to static background:', err);
        }
    }

    // Window Resize Handling
    function onWindowResize() {
        if (!camera || !renderer) return;
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
        if (mesh && scene) {
            renderer.render(scene, camera);
        }
    }

    window.addEventListener('resize', onWindowResize, { passive: true });

    // Battery / Resource Conservation: pause render loop when tab is hidden
    document.addEventListener('visibilitychange', function () {
        isPageVisible = !document.hidden;
    });

    // Initialize on DOM load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
