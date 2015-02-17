from setuptools import setup

if __name__ == '__main__':
    setup(
        name='bettertutors_rest_api',
        version='0.2.4',
        author='Samuel Marks',
        py_modules=['bettertutors_rest_api'],
        test_suite='tests',
        install_requires=[
            'bottle', 'webtest', 'gunicorn', 'bettertutors_user_api'
        ],
        dependency_links=[
            'https://github.com/bettertutors/user-api/archive/master.zip#egg=bettertutors_user_api'
        ]
    )
