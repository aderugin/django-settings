from distutils.core import setup

setup(
    name='django-settings',
    version='0.1',
    url='https://github.com/aderugin/django-settings',
    license='MIT',
    author='Derugin Anton',
    author_email='anton.derugin@gmail.com',
    description='A simple extension to make settings for Django',
    packages=['django_settings'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Django>=1.6',
    ],
)