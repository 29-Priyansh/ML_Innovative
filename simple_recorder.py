import sounddevice as sd
import soundfile as sf

def record_audio(filename, duration):
    print(f"Recording audio for {duration} seconds. Speak now...")
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, audio_data, 44100)
    print(f"Audio saved as {filename}")

def main():
    num_recordings = int(input("Enter the number of audio recordings to make: "))
    duration = int(input("Enter the duration of each recording (in seconds): "))
    dataset_folder = "audio_dataset/"

    for i in range(1, num_recordings + 1):
        filename = f"{dataset_folder}audio_{i}.wav"
        record_audio(filename, duration)

if __name__ == "__main__":
    main()
