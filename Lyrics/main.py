import time

# Lyrics data for "Blue" by Yung Kai
lyrics_timing = [
    # Verse 1
    {"line": "Your morning eyes, I could stare like watching stars", "char_delay": 0.1, "line_timing": 3},
    {"line": "I could walk you by, and I'll tell without a thought", "char_delay": 0.1, "line_timing": 3},
    {"line": "You'd be mine, would you mind if I took your hand tonight?", "char_delay": 0.1, "line_timing": 3},
    {"line": "Know you're all that I want this life", "char_delay": 0.1, "line_timing": 3},
    
    # Chorus
    {"line": "I'll imagine we fell in love", "char_delay": 0.1, "line_timing": 4},
    {"line": "I'll nap under moonlight skies with you", "char_delay": 0.1, "line_timing": 4},
    {"line": "I think I'll picture us, you with the waves", "char_delay": 0.1, "line_timing": 4},
    {"line": "The ocean's colors on your face", "char_delay": 0.1, "line_timing": 4},
    {"line": "I'll leave my heart with your air", "char_delay": 0.1, "line_timing": 4},
    {"line": "So let me fly with you", "char_delay": 0.1, "line_timing": 3},
    {"line": "Will you be forever with me?", "char_delay": 0.1, "line_timing": 4},
    
    # Verse 2
    {"line": "My love will always stay by you", "char_delay": 0.1, "line_timing": 3},
    {"line": "I'll keep it safe, so don't you worry a thing", "char_delay": 0.1, "line_timing": 3},
    {"line": "I'll tell you I love you more", "char_delay": 0.1, "line_timing": 3},
    {"line": "It's stuck with you forever, so promise you won't let it go", "char_delay": 0.1, "line_timing": 4},
    {"line": "I'll trust the universe will always bring me to you", "char_delay": 0.1, "line_timing": 4},
    
    # Chorus (repeated)
    {"line": "I'll imagine we fell in love", "char_delay": 0.1, "line_timing": 4},
    {"line": "I'll nap under moonlight skies with you", "char_delay": 0.1, "line_timing": 4},
    {"line": "I think I'll picture us, you with the waves", "char_delay": 0.1, "line_timing": 4},
    {"line": "The ocean's colors on your face", "char_delay": 0.1, "line_timing": 4},
    {"line": "I'll leave my heart with your air", "char_delay": 0.1, "line_timing": 4},
    {"line": "So let me fly with you", "char_delay": 0.1, "line_timing": 3},
    {"line": "Will you be forever with me?", "char_delay": 0.1, "line_timing": 4}
]

def display_lyrics(lyrics_timing):
    for lyric in lyrics_timing:
        line = lyric["line"]
        char_delay = lyric["char_delay"]
        line_timing = lyric["line_timing"]

        # Print each character with delay
        for char in line:
            print(char, end="", flush=True)
            time.sleep(char_delay)

        # Wait for the line's full timing before moving to the next
        
        print()  # Move to the next line after waiting

# Call the function to display the lyrics
display_lyrics(lyrics_timing)
