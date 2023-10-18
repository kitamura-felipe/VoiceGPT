
* * *

VoiceGPT 🎙️
============

VoiceGPT allows you to interact with OpenAI's GPT models using your voice. You can speak in English or Portuguese, and the assistant will respond audibly in the selected language.

Features:
---------

*   **Voice Recognition**: Utilizes the `speech_recognition` module.
*   **Text-to-voice Output**: Employs `pyttsx3`.
*   **OpenAI Integration**: Uses OpenAI API to get chat-based responses.
*   **Language Switching**: Switch between English and Portuguese voices with vocal commands.

Installation:
-------------

1.  **Clone the Repository**:
    
    
    `git clone https://github.com/kitamura-felipe/VoiceGPT.git`
    
2.  **Navigate to the Cloned Directory**:
    
    
    `cd VoiceGPT`
    
3.  **Install Required Packages**:
    
    
    `pip install openai speech_recognition pyttsx3 pydub requests`
    

Setup:
------

1.  **API Key Configuration**:
    *   Create a `config.json` in the root directory with the following format:
        
        
        `{     "api_key": "YOUR_OPENAI_API_KEY" }`
        
    *   Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

Usage:
------

1.  **Run the Script**:
    
    
    `python VoiceGPT.py`
    
2.  **Voice Interaction**:
    
    *   Start speaking when prompted with "Diga algo:".
    *   To switch to English voice, say "English" or "Inglês".
    *   To switch to Portuguese voice, say "Portuguese" or "Português".
    *   To exit, say "Sair".

Known Issues:
-------------

*   Ensure that you have the necessary voice packages installed on your system for `pyttsx3`.

Contributing:
-------------

Feel free to fork the project, make changes, and submit a pull request. All contributions are welcome!

License:
--------

MIT License.

* * *

