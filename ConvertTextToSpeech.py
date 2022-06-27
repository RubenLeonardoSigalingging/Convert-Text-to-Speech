#!/usr/bin/env python3


def Convert_Text_to_Speech(created_by="Ruben Leonardo Sigalingging."):
	import gtts
	from gtts import gTTS
	from os import system
	system("clear")
	system("chmod 777 ConvertTextToSpeech.py")
	from pyfiglet import figlet_format
	tema=figlet_format("CTTS",font="slant")
	print(tema)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Senin, 27 Juni 2022, Pukul 20:42 PM.")
	print("[!] Fungsi: Alat Pengkonversi Teks Ke Audio.\n")


	text=str(input("[!] Enter Text: "))
	language=str(input("[!] Enter Language: "))


	text_converter=gTTS(text=text,lang=language,slow=False)
	# Simpan hasil file konversi
	text_converter.save("ConverterResults.mp3")


Convert_Text_to_Speech()