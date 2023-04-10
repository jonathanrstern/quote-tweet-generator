def split_transcript(transcript, chunk_size):
    words = transcript.split()
    transcript_parts = []
    temp_list = []

    for word in words:
        temp_list.append(word)
        if len(temp_list) >= chunk_size:
            transcript_part = ' '.join(temp_list)
            transcript_parts.append(transcript_part)
            temp_list = []

    if temp_list:
        transcript_part = ' '.join(temp_list)
        transcript_parts.append(transcript_part)

    return transcript_parts
