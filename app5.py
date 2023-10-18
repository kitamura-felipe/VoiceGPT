import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning, module='pydub')


import openai
import speech_recognition as sr
import pyttsx3
import requests
import base64
from pydub import AudioSegment
import io
import json


# Initialize OpenAI API
with open('config.json', 'r') as f:
    config = json.load(f)
    openai.api_key = config['api_key']


recognizer = sr.Recognizer()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') 
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0') 

engine.setProperty('rate', 300)  

def main():
    print("Talk to GPT.")
    on = True

    messages=[
        {"role": "system", "content": "Você é um assistente prestativo. Converse como se tivesse falando com outra pessoa, inclusive udando interjeições como Ah, hum, etc."}
    ]
    
    while on:
        with sr.Microphone() as source:
            print("Diga algo:")
            audio = recognizer.listen(source)

        try:

            # Get the raw audio data in WAV format.
            wav_data = audio.get_wav_data()

            # Create an AudioSegment instance from the raw WAV data.
            audio_segment = AudioSegment.from_file(io.BytesIO(wav_data), format="wav")

            # Specify the location where you want to save the file.
            file_location = "test.wav"

            # Export the audio data as an MP3 file.
            audio_segment.export(file_location, format="wav")


            audio_file= open("test.wav", "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)

            if "SAIR" in transcript['text'].upper():
                on = False
                break
            
            if ("ENGLISH" in transcript['text'].upper()) or ("INGLÊS" in transcript['text'].upper()):
                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                continue
            if ("PORTUGUESE" in transcript['text'].upper()) or ("PORTUGUÊS" in transcript['text'].upper()):
                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0') 
                continue
                
            print("\033[92mVocê: \033[0m" + transcript['text'])

            messages.append({"role": "user", "content": transcript['text']})

            # Process text with GPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", #"gpt-3.5-turbo"
                messages=messages,
                max_tokens=3000
            )

            print("\033[93mAssistente: \033[0m" + response['choices'][0]['message']['content'])

            messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

            # Convert text to voice
            engine.say(response['choices'][0]['message']['content'])
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Error; {e}")
        except openai.error.OpenAIError as e:
            print(f"OpenAI Error: {e}")

if __name__ == "__main__":
    main()
