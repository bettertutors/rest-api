from setuptools import setup

if __name__ == '__main__':
    package_name = 'bettertutors_rest_api'
    setup(
        name=package_name,
        version='0.2.16',
        author='Samuel Marks',
        py_modules=[package_name],
        test_suite='tests'
    )
