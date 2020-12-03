import time
import uuid
import boto3

def transcribe(bucket, mediafile_uri, name, lenguage_code='en-US', media_format='mp4'):
    transcribe = boto3.client('transcribe')
    
    job = f'transcribe_{bucket}_{uuid.uuid4().hex}'

    transcribe.start_transcription_job(
        TranscriptionJobName=job,
        LanguageCode=lenguage_code,
        MediaFormat=media_format,
        Media={
            'MediaFileUri': mediafile_uri
        },
        OutputBucketName=bucket,
    )

    while True:
        response = transcribe.get_transcription_job(
            TranscriptionJobName=job
        )

        if response['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        
        time.sleep(10)
    
    return response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
    