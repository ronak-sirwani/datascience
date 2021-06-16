from gtts import gTTS

tts_english = gTTS('in engilsh we say, hello, how are you?', lang='en')
tts_spanish = gTTS('in spanish we say, hola, Cómo estás', lang='es')
tts_gujrati = gTTS('in gujrati we say, નમસ્કાર, તમે કેમ છો', lang='gu')
tts_hindi = gTTS('in hindi we say, नमस्कार, तुम कैसे हो', lang='hi')
tts_german = gTTS('in german we say, Hallo, Wie geht es dir', lang='de')
tts_japanese = gTTS('in japanese we say, こんにちは, お元気ですか', lang='ja')

with open('sentence1.mp3', 'wb') as f:
    tts_english.write_to_fp(f)
    tts_spanish.write_to_fp(f)
    tts_gujrati.write_to_fp(f)
    tts_hindi.write_to_fp(f)
    tts_german.write_to_fp(f)
    tts_japanese.write_to_fp(f)