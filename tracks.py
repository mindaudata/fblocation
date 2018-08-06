from flask import Flask, render_template, request
from defs import get_coords, create_map
from werkzeug import secure_filename
tracks = Flask(__name__)


@tracks.route('/')
def index():
    return render_template('index.html')


@tracks.route('/tracked', methods=['POST'])
def tracked():
    if request.method == 'POST':
        fbfile = request.files['fbfilename']
        if fbfile.filename == 'your_location_history.html':
            fbfile.save(secure_filename('upload'))
            coords = get_coords('upload')
        print(coords)
        create_map(coords)
    return render_template('tracked.html')


if __name__ == '__main__':
    tracks.debug = True
    tracks.run(port=5050)
