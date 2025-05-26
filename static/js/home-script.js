
    // Prevent clicking on locked courses
    document.querySelectorAll('.course-box.locked').forEach(box => {
        box.addEventListener('click', function (e) {
            e.preventDefault();
            const courseName = this.querySelector('.course-name').textContent;
            const launchDate = this.querySelector('.status-badge').textContent;
            alert(`${courseName} courses are ${launchDate === 'Coming Soon' ? 'coming soon' : 'in development'}. Please check back later!`);
        });
    });







    // Show the section when it scrolls into view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.3
    });

    const section = document.querySelector('.learning-opportunities');
    observer.observe(section);



    

document.addEventListener("DOMContentLoaded", function() {
    const tips = [
        // 🧠 Brain Hacks
        "Chew gum while studying - it wakes up your brain and helps you remember better!",
        "Study in different places - your bedroom, library, café. Your brain will remember more!",
        
        // ⏰ Time Tricks
        "Study like a video game - 25 mins focus, 5 mins break. Repeat for maximum power!",
        "Morning = Magic! Study before noon and you'll remember way more with less effort",
        
        // ✍ Note-Taking
        "Use colors in your notes! Blue for facts, red for important stuff, green for examples",
        "Doodle while listening - simple drawings help your brain remember the lesson better",
        
        // 📚 Study Smart
        "Teach your pet or stuffed animal - explaining out loud is the BEST way to learn",
        "Make silly songs or rhymes for things you need to memorize - your brain loves fun!",
        
        // 💪 Health Boosters
        "Drink water every 30 mins - your brain works better when it's hydrated!",
        "Do 10 jumping jacks when tired - gets blood flowing to your brain again",
        
        // 🎯 Test Tips
        "Smell the same scent while studying and testing (like peppermint) - helps recall!",
        "Pretend you're making a TikTok tutorial about what you're learning - works wonders!",
        
        // 😴 Sleep Secrets
        "Review tough stuff right before bed - your brain practices while you sleep!",
        "Sleep 8 hours before a test - all-nighters actually make you do worse",
        
        // 🎉 Fun Fact
        "Laugh before studying - it reduces stress and helps your brain absorb information",
        // 🍫 Study Fuel
    "Dark chocolate (70%+) while studying = brain booster! Just 2-3 pieces helps focus",
    
    // 🎵 Music Trick
    "Instrumental music (no lyrics) at low volume helps concentration - try lo-fi or classical!",
    
    // 📱 Phone Hack
    "Turn your phone to grayscale mode (black & white) - makes it 50% less distracting!",
    
    // ✨ Memory Magic
    "Link new info to weird memories (like your friend dancing) - your brain won't forget!",
    
    // 🤝 Study Buddy
    "Find a 'study twin' - teach each other for 2x learning power!",
    
    // 🌿 Nature Boost
    "Study near a window/plant - nature views increase focus by 20%!"
    ];

    const tipText = document.querySelector('.tip-text');
    let currentIndex = 0;

    // Pehla tip dikhado
    tipText.textContent = tips[currentIndex];

    setInterval(() => {
        // Pehle fade-out
        tipText.style.opacity = 0;

        // 500ms ke baad text change karen
        setTimeout(() => {
            currentIndex = (currentIndex + 1) % tips.length;
            tipText.textContent = tips[currentIndex];
            tipText.style.opacity = 1;
        }, 500);
    }, 5000); // Har 10 second baad tip change hoga
});