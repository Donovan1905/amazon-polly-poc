import boto3

# Create a Polly client
polly = boto3.client('polly')

# The text you want to convert to speech
text = "Hello, this is an example of using Amazon Polly to speak a sentence."

# Generate the speech audio
response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)

# Save the audio to a file
with open('output.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())

print('Speech audio saved to output.mp3. You can now play the file on your computer.')
