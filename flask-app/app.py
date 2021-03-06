import os
from flask import Flask, request, jsonify, render_template

from keras.preprocessing import image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './Image_Test/test/'


@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        print(request)

        if request.files.get('file'):
            # read the file
            file = request.files['file']

            # read the filename
            filename = file.filename

            # create a path to the uploads folder
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the file to the uploads folder
            file.save(filepath)

<<<<<<< HEAD
            # Load the saved image using Keras and resize it to the
            # mnist format of 28x28 pixels
            # image_size = (28, 28)
            # im = image.load_img(filepath, target_size=image_size,
            #                     grayscale=True)
            #
            # # Convert the 2D image to an array of pixel values
            # image_array = prepare_image(im)
            # print(image_array)

            from keras.models import load_model
            from keras.preprocessing import image
            model2 = load_model('body_part_model.h5')

            test_generator = datagen.flow_from_directory(
                directory= './flask-app/Image_Test/',
                target_size=(256,256),
                color_mode='grayscale',
                batch_size=1,
                class_mode=None,
                shuffle=False,
                seed=42
            )

            test_generator.reset()
            pred = model2.predict_generator(test_generator,steps=1,verbose=1)

            predicted_class_indices=np.argmax(pred,axis=1)
            predicted_class_indices

            labels = (train_generator.class_indices)
            labels = dict((v,k) for k,v in labels.items())
            predictions = [labels[k] for k in predicted_class_indices]
            return predictions

            # return "Data Pre-processing Complete!"

=======


            return "Data Pre-processing Complete!"
>>>>>>> 1f56c689c404a68464ce0e92c64ba465581c4473
    return '''
<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<style>
body,h1 {font-family: "Raleway", sans-serif}
body, html {height: 100%}
.bgimg {
  background-image: url('/static/images/genes.jpg');
  min-height: 100%;
  background-position: center;
  background-size: cover;
}
</style>
<body>

<div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
  <div class="w3-display-topleft w3-padding-large w3-xlarge">
    Logo
  </div>
  <div class="w3-display-middle">
    <h1 class="w3-jumbo w3-animate-top">Choose X-Ray</h1>
    <hr class="w3-border-grey" style="margin:auto;width:100%">
    <p class="w3-large w3-center"></p>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </form>

  </div>
  <div class="w3-display-bottomleft w3-padding-large">
    Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a>
  </div>
</div>

</body>
</html>
'''


if __name__ == "__main__":
    app.run(debug=True)
