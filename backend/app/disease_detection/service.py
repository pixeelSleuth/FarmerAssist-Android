from ultralytics import YOLO

model = YOLO(
    "app/models/best.pt"
)
CLASS_MAPPING = {

    0:
    "Turcicum Leaf Blight",

    1:
    "Common Rust"
}


class DiseaseDetectionService:

    @staticmethod
    def detect(
        image_path
    ):

        results = model(
            image_path
        )

        detections = []

        for result in results:

            for box in result.boxes:

                class_id = int(
                    box.cls[0]
                )

                confidence = round(
                    float(
                        box.conf[0]
                    ),
                    4
                )

                detections.append(
                    {
                        "disease_name":
                            CLASS_MAPPING[
                                class_id
                            ],

                        "confidence":
                            confidence
                    }
                )

        return detections