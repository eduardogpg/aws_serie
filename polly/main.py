import boto3

def polly(text, lenguage_code, voice_id):
    polly = boto3.client('polly')

    response = polly.synthesize_speech(
        LanguageCode=lenguage_code,
        OutputFormat='mp3',
        SampleRate='22050',
        Text=text,
        VoiceId=voice_id
    )

    with open('tmp/example.mp3', 'wb') as file:
        file.write(response['AudioStream'].read())

if __name__ == '__main__':
    polly(
        'La función ya funciona de forma correcta. Ya es posible generar el archivo.',
        'es-MX',
        'Penelope'
    )