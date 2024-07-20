import React, { useEffect, useRef } from 'react';

const BackgroundAudio = ({ playAudio }) => {
    const audioRef = useRef(null);
    const fadeIntervalRef = useRef(null);

    useEffect(() => {
        const audio = new Audio(`${process.env.PUBLIC_URL}/audios/amazon-jungle.mp3`);
        audio.loop = true;
        audio.volume = 0;
        audioRef.current = audio;

        const fadeIn = () => {
            clearInterval(fadeIntervalRef.current);
            audio.volume = 0;
            audio.play().then(() => {
                const fade = () => {
                    if (audio.volume < 1) {
                        audio.volume = Math.min(audio.volume + 0.005, 1);
                        requestAnimationFrame(fade);
                    }
                };
                fade();
            }).catch(error => {
                console.error('Error playing audio:', error);
            });
        };

        const fadeOut = () => {
            clearInterval(fadeIntervalRef.current);
            const fade = () => {
                if (audio.volume > 0) {
                    audio.volume = Math.max(audio.volume - 0.005, 0);
                    requestAnimationFrame(fade);
                } else {
                    audio.pause();
                }
            };
            fade();
        };

        if (playAudio) {
            fadeIn();
        } else {
            fadeOut();
        }

        return () => {
            clearInterval(fadeIntervalRef.current);
            audio.pause();
            audio.currentTime = 0;
        };
    }, [playAudio]);

    return null;
};

export default BackgroundAudio;