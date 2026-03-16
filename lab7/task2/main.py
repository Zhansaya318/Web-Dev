from models import MusicTrack, RemixTrack, InstrumentalVersion

def main():
    original_beat = MusicTrack("LOV3", "Sik-k", "K-Hip Hop", 90)

    remix = RemixTrack("LOV3", "Sik-k", "Trap", 145, "omgvangdale")
    
    instrumental = InstrumentalVersion("LOV3", "Sik-k", "Hip Hop", 90, ["808 Bass", "Hi-hats", "Synthesizer"])

    tracklist = [original_beat, remix, instrumental]

    print("--- MUSIC LIBRARY ---")
    
    for track in tracklist:
        print(track) 
        print(f"Details: {track.get_info()}")
        track.play() 
        print("-" * 40)

    print("\n--- DEMONSTRATING UNIQUE METHODS ---")
    
    print(f"Original Remix BPM: {remix.bpm}")
    print(remix.change_tempo(150))
    print(f"New Remix BPM: {remix.bpm}\n")
    
    print(f"Instruments used in the '{instrumental.title}' instrumental:")
    print(instrumental.get_instruments_list())

if __name__ == '__main__':
    main()