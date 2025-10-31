document.addEventListener('DOMContentLoaded', () => {
    const title = document.querySelector('.main_title h2');
    if (!title) return;

    const text = title.textContent.trim();
    title.innerHTML = '';

    const textSpan = document.createElement('span');
    textSpan.className = 'typed-text';
    title.appendChild(textSpan);

    const cursor = document.createElement('span');
    cursor.className = 'typed-cursor';
    title.appendChild(cursor);

    const sleep = ms => new Promise(res => setTimeout(res, ms));

    async function typeLoop() {
        while (true) {
            // Type
            for (let i = 0; i < text.length; i++) {
                textSpan.textContent += text.charAt(i);
                await sleep(Math.random() * 80 + 50); // 50-130ms
            }
            // Pause with full text visible
            await sleep(2000);

            // Delete
            for (let i = text.length; i > 0; i--) {
                textSpan.textContent = textSpan.textContent.slice(0, -1);
                await sleep(Math.random() * 40 + 30); // 30-70ms
            }
            // short pause before retyping
            await sleep(500);
        }
    }

    // start the loop
    setTimeout(typeLoop, 300);
});