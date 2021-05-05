from imageai.Detection import ObjectDetection
from imageai.Classification import ImageClassification

detector = ObjectDetection()
#detector = ImageClassification()

model_path = "./models/yolo-tiny.h5"
#model_path = "./models/resnet50_imagenet_tf.2.0.h5"
input_path = "./input/cat.jpg"

detector.setModelTypeAsTinyYOLOv3()
# detector.setModelTypeAsResNet50()
detector.setModelPath(model_path)
detector.loadModel(detection_speed="fastest")




def detect(input_path):
    _, detection = detector.detectObjectsFromImage(input_image=input_path, output_type="array", minimum_percentage_probability=30)

    detection = sorted(detection, key=lambda item: item["percentage_probability"], reverse=True)

    objects = []
    for eachItem in detection:
        if eachItem["name"] not in objects:
            objects.append(eachItem["name"])
            if len(objects) == 2: break
    
    while len(objects) != 2:
        objects.append("None")
    
    return objects

def classify(input_path):
    predictions, probabilities = detector.classifyImage(input_path, result_count=5 )

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)