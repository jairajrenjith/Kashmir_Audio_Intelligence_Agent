from pydub import AudioSegment

def convert_to_wav(input_path, output_path="temp.wav"):
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path, format="wav")
    return output_path
