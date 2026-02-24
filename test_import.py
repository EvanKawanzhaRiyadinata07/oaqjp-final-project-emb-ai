from EmotionDetection.emotion_detection import emotion_detector

if __name__ == "__main__":
    print("Mengimpor dan menguji fungsi emotion_detector...")
    test_text = "Aku sangat senang belajar hal baru hari ini!"
    result = emotion_detector(test_text)
    print("Hasil deteksi emosi:")
    print(result)