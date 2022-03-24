# LiveListening
The tool that detects the sentence you want to transmit from your microphone with the Vosk API


## Requirements
```bash
pip install -r requirements.txt
```

## How to use?
Download model from [Vosk API Models](https://alphacephei.com/vosk/models) according to your local language. **Note that the model file is in the same directory as the project**

and the main.py extension will go from the model path

### Example:
```py
...

l = Listen(model_path="vosk-model-en-us-0.22")

...
```

Enjoy use 🎉
