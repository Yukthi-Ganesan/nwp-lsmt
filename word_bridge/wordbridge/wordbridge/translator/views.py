from django.shortcuts import render
from django.http import JsonResponse
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import pytesseract
import cv2
import os

# Initialize Google Translator
translator = Translator()

# Text Translation
def translate_text(request):
    text = request.POST.get('text')
    src_lang = request.POST.get('src_lang', 'auto')
    dest_lang = request.POST.get('dest_lang', 'en')
    
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return JsonResponse({'translated_text': translated.text})

# Speech to Text (Convert Audio to Text)
def speech_to_text(request):
    recognizer = sr.Recognizer()
    audio_file = request.FILES['audio']
    with open('audio.wav', 'wb') as f:
        for chunk in audio_file.chunks():
            f.write(chunk)
    
    with sr.AudioFile('audio.wav') as source:
        audio = recognizer.record(source)
    
    text = recognizer.recognize_google(audio)
    return JsonResponse({'text': text})

# Text to Speech (Convert Text to Audio)
def text_to_speech(request):
    text = request.POST.get('text')
    lang = request.POST.get('lang', 'en')
    
    tts = gTTS(text=text, lang=lang)
    tts.save('static/speech.mp3')
    
    return JsonResponse({'audio_url': '/static/speech.mp3'})

# Image to Text (OCR)
def image_to_text(request):
    image = request.FILES['image']
    with open('uploads/image.png', 'wb') as f:
        for chunk in image.chunks():
            f.write(chunk)
    
    img = cv2.imread('uploads/image.png')
    extracted_text = pytesseract.image_to_string(img)
    
    return JsonResponse({'text': extracted_text})
