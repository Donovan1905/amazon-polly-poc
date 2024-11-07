import os
import boto3
import pygame
import io

polly = boto3.client('polly')

text = "Hello, this is an example of using Amazon Polly to speak a sentence directly on your computer."

response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)

pygame.mixer.init()

sound = pygame.mixer.Sound(io.BytesIO(response['AudioStream'].read()))
sound.play()

while pygame.mixer.get_busy():
    continue

print('Finished playing the audio.')