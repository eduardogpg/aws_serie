import boto3

def translate(text, source_language_code, tarte_language_code):
    translate = boto3.client('translate')

    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=tarte_language_code
    )

    return response['TranslatedText']

if __name__ == '__main__':
    response = translate(
        'Hola, nos encontramos en un vídeo más',
        'es',
        'en'
    )

    print(response)