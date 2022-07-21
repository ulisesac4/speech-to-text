from gtts import gTTS
import json

json_data = open('input-text.json')
data = json.load(json_data)
print('Doing ', data['fileName'])
voice_data = gTTS(data['text'], lang=data['language'])
destination = "dist/" + data['fileName'] + ".mp3"
voice_data.save(destination)
print('Finishing ', data['fileName'])
