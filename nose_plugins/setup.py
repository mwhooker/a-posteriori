from setuptools import setup


setup(name='Test plugin',
    entry_points = {
        'nose.plugins.0.10': [
            'test = plugin:TestPlugin'
            ]
        },
    )
