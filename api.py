from detect_count import detect, load_model_api
from flask_restful import Resource, Api
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import base64

model, stride, imgsz = load_model_api()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


# "https://www.thespruce.com/thmb/iMt63n8NGCojUETr6-T8oj-5-ns=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/PAinteriors-7-cafe9c2bd6be4823b9345e591e4f367f.jpg"
class CApp(Resource):
    @staticmethod
    def get():
        file = request.args.get('file')
        imgs_path = detect(file,
                    model=model,
                    stride=stride)
        print(imgs_path)
        return send_file(imgs_path[0], as_attachment=True)

api.add_resource(CApp, '/yolo')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8312, threaded=True, debug=1)