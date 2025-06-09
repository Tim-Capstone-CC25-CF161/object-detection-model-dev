import tensorflow as tf
import numpy as np

export_dir = "./model"
input_image_size = (640,640)

category_index = {
    1: {'name': 'anoa'},
    2: {'name': 'babirusa'},
    3: {'name': 'biawak_pohon_biru'},
    4: {'name': 'harimau_sumatra'},
    5: {'name': 'jalak_bali'},
    6: {'name': 'kakatua_jambul_kuning'},
    7: {'name': 'kera_hitam'},
    8: {'name': 'orangutan'},
    9: {'name': 'owa_jawa'},
    10: {'name': 'rusa_bawean'},
    11: {'name': 'siamang'}
}

def load_model(model_path: str, logger):
    """Load TensorFlow SavedModel"""
    try:
        logger.info(f"Loading model from {model_path}...")
        imported = tf.saved_model.load(model_path)
        model_fn = imported.signatures['serving_default']
        logger.info("Model loaded successfully!")
        return model_fn
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise e

def detect_animals_in_image(pil_image, model_fn, category_index, input_image_size, min_score_thresh=0.30):

    image_np = np.array(pil_image)
    image_tensor = tf.convert_to_tensor(image_np)

    # Resize gambar sesuai input_image_size
    image_resized = tf.image.resize(image_tensor, input_image_size)
    image_resized = tf.cast(image_resized, tf.uint8)

    # Expand dimensions untuk batch
    image_batch = tf.expand_dims(image_resized, axis=0)

    # Inference
    result = model_fn(image_batch)

    # Extract hasil deteksi
    detection_boxes = result['detection_boxes'][0].numpy()
    detection_classes = result['detection_classes'][0].numpy().astype(int)
    detection_scores = result['detection_scores'][0].numpy()

    # Filter berdasarkan confidence threshold
    valid_detections = detection_scores >= min_score_thresh

    # Siapkan hasil
    detections = []

    for i in range(len(detection_boxes)):
        if valid_detections[i]:
            class_id = detection_classes[i]
            confidence = detection_scores[i]
            box = detection_boxes[i]

            # Ambil nama hewan dari category_index
            if class_id in category_index:
                animal_name = category_index[class_id]['name']
            else:
                animal_name = f'Unknown_Class_{class_id}'

            # Format bounding box: [ymin, xmin, ymax, xmax]
            bounding_box = [
                float(box[0]),  # ymin
                float(box[1]),  # xmin
                float(box[2]),  # ymax
                float(box[3])   # xmax
            ]

            detection_result = {
                'animal_name': animal_name,
                'bounding_box': bounding_box,
                'confidence': float(confidence)
            }

            detections.append(detection_result)

    detections.sort(key=lambda x: x['confidence'], reverse=True)

    return detections
