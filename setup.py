from setuptools import setup, find_packages

setup(
    name='django-simple-comments',
    version="0.1",
    description='Simple comments for authenticated users in Django',
    author='Daniel Shapiro',
    author_email='danxshap@gmail.com',
    url='http://github.com/danxshap/django-simple-comments',
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['setuptools',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
