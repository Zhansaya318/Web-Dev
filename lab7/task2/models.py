class MusicTrack:
    def __init__(self, title, artist, genre, bpm):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.bpm = bpm

    def get_info(self):
        return f"'{self.title}' by {self.artist} ({self.genre}, {self.bpm} BPM)"

    def play(self):
        print(f"Original track: {self.title}...")

    def __str__(self):
        return f"{self.artist} - {self.title}"

class RemixTrack(MusicTrack):
    def __init__(self, title, artist, genre, bpm, remixer_name):
        super().__init__(title, artist, genre, bpm)
        self.remixer_name = remixer_name

    def change_tempo(self, new_bpm):
        self.bpm = new_bpm
        return f"Tempo updated to {self.bpm} BPM."

    def play(self):
        print(f"REMIX by {self.remixer_name}: {self.title}...")

    def __str__(self):
        return f"[REMIX] {self.artist} - {self.title} (by {self.remixer_name})"

class InstrumentalVersion(MusicTrack):
    def __init__(self, title, artist, genre, bpm, main_instruments):
        super().__init__(title, artist, genre, bpm)
        self.main_instruments = main_instruments 

    def get_instruments_list(self):
        return ", ".join(self.main_instruments)

    def get_info(self):
        base_info = super().get_info()
        return f"[INSTRUMENTAL] {base_info}. Key Instruments: {self.get_instruments_list()}."

    def __str__(self):
        return f"[INSTRUMENTAL] {self.artist} - {self.title}"