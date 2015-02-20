from datetime import datetime
from os import environ, path
from sys import platform
from pkg_resources import get_distribution, DistributionNotFound

from bottle import Bottle, response

from bettertutors_static_api import static_app
from bettertutors_user_api import user_app


rest_api = Bottle(catchall=False, autojson=True)
rest_api.merge(static_app)
rest_api.merge(user_app)


def get_version_of(package):
    # Adapted from: http://stackoverflow.com/a/17638236/587021
    try:
        _dist = get_distribution(package)
        # Normalize case for Windows systems
        dist_loc = path.normcase(_dist.location)
        here = path.normcase(__file__)
        if not here.startswith(path.join(dist_loc, package)):
            # not installed, but there is another version that *is*
            raise DistributionNotFound

    except DistributionNotFound:
        if package + '.py' == __file__:
            return (lambda s: s[s.find("'") + 1:s.rfind("'")])(filter(lambda l: l.startswith('version'),
                                                                      map(lambda l: l.strip(),
                                                                          open('setup.py').readlines()))[0])
        return '"{package_name}" not found installed...'.format(package_name=package)

    return _dist.version


@rest_api.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'  # Take out '*' in production!


@rest_api.route('/api')
@rest_api.route('/api/status')
def status():
    return {'rest_api_version': get_version_of('bettertutors_rest_api'),
            'user_api_version': get_distribution('bettertutors-user-api').version,
            'sql_models_version': get_distribution('bettertutors-sql-models').version,
            'static_api_version': get_version_of('bettertutors-static-api').version,
            'server_time': datetime.now().strftime("%I:%M%p on %B %d, %Y")}


if __name__ == '__main__':
    rest_api.run(server='wsgiref' if platform == 'win32' else 'gunicorn',
                 host='0.0.0.0', port=int(environ.get('PORT', 5555)), debug=True)
