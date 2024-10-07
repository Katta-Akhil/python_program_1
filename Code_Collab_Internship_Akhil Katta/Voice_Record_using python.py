import sounddevice as sd
import wavio

sample_rate = 44100 
duration = 5  
output_file = "Output_Recording.wav"  

def record_audio(duration, sample_rate):
    print("Recording...")
    
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
    sd.wait()  
    print("Recording finished!")
    return audio_data

def save_audio(audio_data, sample_rate, output_file):
    
    wavio.write(output_file, audio_data, sample_rate, sampwidth=2)
    print(f"Audio saved as {output_file}")

def main():
    
    audio_data = record_audio(duration, sample_rate)
    
    
    save_audio(audio_data, sample_rate, output_file)

if __name__ == "__main__":
    main()
