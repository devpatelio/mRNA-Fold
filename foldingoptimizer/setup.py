from distutils.core import setup

setup(
    
    packages=['explore', 'vienna.params'],

    package_dir={
        'vienna': './explore.ipynb'},

    package_data={
        'explore': ['./data/bpps/*.npy']},

    install_requires=[
        'numpy>=1.19.0',
        'ViennaRNA>=2.4.18']
)