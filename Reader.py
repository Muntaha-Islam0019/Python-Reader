import pyttsx3
speaker = pyttsx3.init()
speaker.setProperty('rate', 100)
speaker.say("Hello!")
speaker.say("Ain't it amazing?")
speaker.say("Though I wish my laptop had your voice.")
speaker.say("Lol!")
speaker.say("Oh, and, by the way!")
speaker.say("You're beautiful!")
speaker.runAndWait()
