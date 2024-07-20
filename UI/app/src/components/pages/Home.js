import React, { useState, useEffect, useRef } from 'react';
import '../../App.css';
import HeroSection from '../HeroSection';
import Cards from '../Cards';
import Footer from '../Footer';
import BackgroundAudio from '../BackgroundAudio'; // Adjust path as necessary

function Home() {
    const [playAudio, setPlayAudio] = useState(false);
    const heroSectionRef = useRef(null);

    useEffect(() => {
        const observer = new IntersectionObserver(
            entries => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        setPlayAudio(true);
                    } else {
                        setPlayAudio(false);
                    }
                });
            },
            { threshold: 0.1 } // Adjust as needed
        );

        if (heroSectionRef.current) {
            observer.observe(heroSectionRef.current);
        }

        return () => {
            if (heroSectionRef.current) {
                observer.unobserve(heroSectionRef.current);
            }
        };
    }, []);

    return (
        <>
            <div ref={heroSectionRef}>
                <HeroSection />
            </div>
            <Cards />
            <Footer />
            <BackgroundAudio playAudio={playAudio} />
        </>
    );
}

export default Home;