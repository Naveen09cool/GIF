from gtts import gTTS
def gen(text):
	my_audio = gTTS(text)
	my_audio.save('genrated.mp3')
user_input=input("Enter the text to be converted\n")
gen(user_input)
