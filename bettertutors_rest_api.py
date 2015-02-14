from datetime import datetime

from bottle import Bottle, response
# from namespace_user_api import user_api, __version__ as user_api_version

rest_api = Bottle(catchall=False, autojson=True)
# rest_api.merge(oauth2_app)
# rest_api.merge(user_api)

__version__ = '0.0.1'


@rest_api.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'  # Take out '*' in production!


@rest_api.route('/api')
@rest_api.route('/api/status')
def status():
    return {'rest_api_version': __version__,
            'server_time': datetime.now().strftime("%I:%M%p on %B %d, %Y")}


if __name__ == '__main__':
    rest_api.run(host='0.0.0.0', port=5555, debug=True)
