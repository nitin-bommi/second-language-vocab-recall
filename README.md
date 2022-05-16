# Second Language Vocabulary Recall

As a part of [Alexia Larchen's](https://www.researchgate.net/profile/Alexia-Larchen) experimentation. 

> Note: use python3.8 asthe dependencies are not to support python3.8+

## Steps to deploy the app
* Clone the repository and `cd` into that directory.
* Open a virtual environment in a server or localhost.
* Install the dependencies via `pip install -r requirements.txt`.
* Create 3 directories to store the intermediate files.
  * `mkdir temp uploaded_images model`
* Download the `.h5` model from [here](https://drive.google.com/file/d/1L4UZv-_VtWP2yWkTQZo9OIP5c4T8vl5F/view?usp=sharing).
* Run the application via `streamlit run main.py`

## Using the app
* After starting the streamlit service, you will be redirected to `localhost:8501`.
* Upload an image.
* Use maximize feature to enlarge the image.
* All the images uploaded will be stored in `temp` and `upload_images` directories.
* *The final image is not stored.*

## Debugging errors
In case of any errors, create an issue and I'll try to solve at the earliest. 

*Will create a docker image for easy access soon...*
