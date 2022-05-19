# Load libraries
import streamlit as st
import os
import cv2
from imageai.Detection import ObjectDetection

# Translation mapping english -> dutch
translation = {
    'bench': 'zitbank',
    'bicycle': 'fiets',
    'bird': 'vogel',
    'book': 'boek',
    'bottle': 'fles',
    'car': 'auto',
    'chair': 'stoel',
    'couch': 'canape',
    'cup': 'tas',
    'dining table': 'eettafel',
    'laptop': 'laptop',
    'mouse': 'muis',
    'person': 'persoon',
    'potted plant': 'potplant',
    'remote': 'afstandsbediening',
    'teddy bear': 'teddybeer',
    'tv': 'televisie',
    'vase': 'vaas',
}

# Load the image
def load_image(image_file):
	img = cv2.imread(image_file)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	return img

# Save the image (caching the function)
@st.cache
def save_file(file, path):
    with open(os.path.join(path, file.name), 'wb') as f:
        f.write(file.getbuffer())

# Load the model and cache it
@st.cache
def load_model(model_path):
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(model_path)
	detector.loadModel()
	return detector

st.title(':sparkles: Object Detection :sparkles:')
image_file = st.file_uploader("Upload an image to detect classes", type=["png","jpg","jpeg"])

if image_file is not None:

	# To See details
	file_details = {"filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size}
	st.write(file_details)
	save_file(image_file, 'uploaded_images')
	st.success(f'Saved file: {image_file.name} in uploaded_images')

	# To View Uploaded Image
	img = load_image(f'uploaded_images/{image_file.name}')
	st.image(img, width=720)

	st.header('Detection results')

	# Load the model
	detector = load_model('model/resnet50_coco_best_v2.1.0.h5')

	detections, objects_path = detector.detectObjectsFromImage(input_image=f'uploaded_images/{image_file.name}', 
												 output_image_path=f'temp/{image_file.name.split(".")[0]}.jpg', 
												 display_percentage_probability=False, display_box=False, display_object_name=False,
												 extract_detected_objects=True)

	# draw bounding boxes for each object
	detections_df = {'english': [], 'dutch': []}
	for eachObject in detections:
		box = eachObject['box_points']
		if eachObject['name'] in translation:
			label = eachObject['name'] + ' : ' + translation[eachObject['name']]
			detections_df['dutch'].append(translation[eachObject['name']])
		else:
			label = eachObject['name']
			detections_df['dutch'].append('-')
		cv2.rectangle(img, pt1=(box[0], box[1]), pt2=(box[2], box[3]), color=(255,0,0), thickness=10)
		cv2.putText(img, label, (box[0]+100, box[1]+100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 6)
		detections_df['english'].append(eachObject['name'])
		
	# Display results
	st.dataframe(detections_df)
	st.image(img, width=720)

