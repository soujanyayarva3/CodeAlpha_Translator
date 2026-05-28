from deep_translator import GoogleTranslator

print("\n🌍 Language Translation Tool\n")

text = input("Enter text: ")

print("\nLanguage codes: en=English, hi=Hindi, fr=French, es=Spanish")

src = input("Source language: ")
dest = input("Target language: ")

translated = GoogleTranslator(source=src, target=dest).translate(text)

print("\nTranslated Text:", translated)