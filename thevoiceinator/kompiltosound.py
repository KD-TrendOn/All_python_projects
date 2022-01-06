from pydub import AudioSegment
sound1 = AudioSegment.from_file(r"a.wav")
sound2 = AudioSegment.from_mp3(r"b.wav")
sound3=sound1+sound2
sound3.export(r"abab.wav", format="wav")