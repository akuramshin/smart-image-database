from imageai.Detection import ObjectDetection
from imageai.Classification import ImageClassification



class Detector:

    def __init__(self, model_path, speed):
        self.detector = ObjectDetection()

        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath(model_path)
        self.detector.loadModel(detection_speed=speed)


    # Run object detection and return the two tags with highest probability.
    # In the case of no objects detected, tag="None"
    def detect(self, input_path):
        _, detection = self.detector.detectObjectsFromImage(input_image=input_path, output_type="array", minimum_percentage_probability=30)

        detection = sorted(detection, key=lambda item: item["percentage_probability"], reverse=True)

        objects = []
        for eachItem in detection:
            if eachItem["name"] not in objects:
                objects.append(eachItem["name"])
                if len(objects) == 2: break
        
        while len(objects) != 2:
            objects.append("None")
        
        return objects


