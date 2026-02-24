def emotion_detector(text_to_analyze):
    """
    Fungsi untuk mendeteksi emosi dari teks
    """
    
    # Penanganan input kosong
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Simulasi deteksi emosi berdasarkan kata kunci
    text_lower = text_to_analyze.lower()
    
    # Nilai default
    emotions = {
        'anger': 0.1,
        'disgust': 0.1,
        'fear': 0.1,
        'joy': 0.1,
        'sadness': 0.1
    }
    
    # Deteksi sederhana berdasarkan kata kunci
    if 'senang' in text_lower or 'bahagia' in text_lower or 'happy' in text_lower or 'glad' in text_lower:
        emotions['joy'] = 0.9
    elif 'marah' in text_lower or 'kesal' in text_lower or 'angry' in text_lower or 'mad' in text_lower:
        emotions['anger'] = 0.9
    elif 'takut' in text_lower or 'cemas' in text_lower or 'afraid' in text_lower or 'fear' in text_lower:
        emotions['fear'] = 0.9
    elif 'sedih' in text_lower or 'kecewa' in text_lower or 'sad' in text_lower:
        emotions['sadness'] = 0.9
    elif 'jijik' in text_lower or 'muak' in text_lower or 'disgust' in text_lower:
        emotions['disgust'] = 0.9
    
    # Tentukan emosi dominan (nilai tertinggi)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Format output
    formatted_output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return formatted_output