import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from bilibili import DmSpider, InfoSpider
# configuration
DEBUG = True
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/getBv', methods=['GET'])
def get_bv():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        bv = request.args.get('bv')
        print(bv)
        info = InfoSpider.getVideoInfo(bv)
        video = {'info': info}
        response_object['video'] = video
        response_object['message'] = 'Get Success'
    else:
        response_object['message'] = 'Get Failed'
    return jsonify(response_object)


@app.route('/getDm', methods=['GET'])
def get_Dm():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        bv = request.args.get('bv')
        print(bv)
        Dm_Info = DmSpider.get_dm_history(bv)
        response_object['Dm_Info'] = Dm_Info
        response_object['message'] = 'Get Success'
    else:
        response_object['message'] = 'Get Failed'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
