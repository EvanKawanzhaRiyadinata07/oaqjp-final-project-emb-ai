"""
Unit tests for emotion detector
"""
from EmotionDetection.emotion_detection import emotion_detector

def run_tests():
    """Run all test cases"""
    
    print("=" * 60)
    print("EMOTION DETECTOR UNIT TESTS")
    print("=" * 60)
    
    # Test 1: Joy test
    print("\n📝 Test 1: Testing JOY emotion...")
    print("Input: 'I am so happy and excited today!'")
    result = emotion_detector("I am so happy and excited today!")
    print(f"Output: {result}")
    if result['dominant_emotion'] == 'joy':
        print("✅ PASSED: Dominant emotion is joy")
    else:
        print("❌ FAILED: Expected joy but got", result['dominant_emotion'])
    
    # Test 2: Anger test
    print("\n📝 Test 2: Testing ANGER emotion...")
    print("Input: 'I am really angry about this situation!'")
    result = emotion_detector("I am really angry about this situation!")
    print(f"Output: {result}")
    if result['dominant_emotion'] == 'anger':
        print("✅ PASSED: Dominant emotion is anger")
    else:
        print("❌ FAILED: Expected anger but got", result['dominant_emotion'])
    
    # Test 3: Sadness test
    print("\n📝 Test 3: Testing SADNESS emotion...")
    print("Input: 'I feel so sad and depressed'")
    result = emotion_detector("I feel so sad and depressed")
    print(f"Output: {result}")
    if result['dominant_emotion'] == 'sadness':
        print("✅ PASSED: Dominant emotion is sadness")
    else:
        print("❌ FAILED: Expected sadness but got", result['dominant_emotion'])
    
    # Test 4: Fear test
    print("\n📝 Test 4: Testing FEAR emotion...")
    print("Input: 'I am terrified of what might happen'")
    result = emotion_detector("I am terrified of what might happen")
    print(f"Output: {result}")
    if result['dominant_emotion'] == 'fear':
        print("✅ PASSED: Dominant emotion is fear")
    else:
        print("❌ FAILED: Expected fear but got", result['dominant_emotion'])
    
    # Test 5: Disgust test
    print("\n📝 Test 5: Testing DISGUST emotion...")
    print("Input: 'This food tastes disgusting'")
    result = emotion_detector("This food tastes disgusting")
    print(f"Output: {result}")
    if result['dominant_emotion'] == 'disgust':
        print("✅ PASSED: Dominant emotion is disgust")
    else:
        print("❌ FAILED: Expected disgust but got", result['dominant_emotion'])
    
    print("\n" + "=" * 60)
    print("TESTS COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()