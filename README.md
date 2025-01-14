Here’s a basic README for your Jarvis project:

---

# Jarvis Voice Assistant

Jarvis is a simple voice assistant built using Python. It can respond to voice commands, perform tasks like searching Wikipedia, opening websites, playing music, and more. The assistant also features a "Wikipedia Mode" that allows users to control when Wikipedia searches are enabled.

## Features

- **Voice Commands**: Interact with Jarvis using natural voice commands.
- **Wikipedia Integration**: Search Wikipedia in "Wikipedia Mode."
- **Custom Tasks**: Perform actions like opening websites, playing music, and telling the time.
- **Flexible Interaction**: Toggle features like Wikipedia Mode on or off as needed.
- **Exit Command**: Stop Jarvis by saying "exit."

---

## Requirements

- Python 3.7 or later
- Libraries:
  - `pyttsx3`
  - `speechRecognition`
  - `wikipedia`
  - `webbrowser`
  - `os`
  - `datetime`

Install dependencies with:

```bash
pip install pyttsx3 SpeechRecognition wikipedia
```

---

## How to Run

1. Clone or download this repository to your local machine.
2. Navigate to the project folder and activate the virtual environment (if applicable).
3. Run the `main.py` file:

   ```bash
   python main.py
   ```

4. Speak commands into your microphone as prompted.

---

## Voice Commands

### General Commands
- **"Open YouTube"**: Opens YouTube in your default browser.
- **"Open Google"**: Opens Google in your default browser.
- **"Play Music"**: Plays the first song in your predefined music directory.
- **"The time"**: Tells the current time.

### Wikipedia Mode
- **"Turn on Wikipedia"**: Enables Wikipedia Mode.
- **"Search [topic]"**: Searches for the topic on Wikipedia (only in Wikipedia Mode).
- **"Turn off Wikipedia"**: Disables Wikipedia Mode.
- If Wikipedia Mode is off and you ask to search, Jarvis will ask if you'd like to enable it.

### Exit Command
- **"Exit"**: Stops the assistant.

---

## Customization

1. **Music Directory**:
   Update the `music_dir` variable in `main.py` with the path to your music folder:
   ```python
   music_dir = 'path_to_your_music_folder'
   ```

2. **Wikipedia Mode Behavior**:
   Modify the logic to suit your interaction preferences in the `main.py` script.

3. **Voice Settings**:
   Customize the voice and speed of Jarvis:
   ```python
   engine.setProperty('voice', voices[0].id)  # Use [1] for a different voice
   engine.setProperty('rate', 150)  # Adjust the speed (default: 200)
   ```

---

## Troubleshooting

1. **Microphone Not Detected**:
   Ensure your microphone is properly connected and configured as the default recording device.

2. **PyAudio Error**:
   If you encounter a `pyaudio` installation issue, install it with:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

3. **Wikipedia Page Error**:
   Ensure the topic exists on Wikipedia or try searching for a broader term.

---

## Future Improvements

- Add more voice-controlled tasks.
- Enhance the assistant's ability to understand and respond naturally.
- Integrate APIs for advanced functionalities like weather updates and news.

---

## License

This project is licensed under the MIT License. Feel free to modify and expand upon it.

--- 

Let me know if you'd like to add or modify anything! 😊