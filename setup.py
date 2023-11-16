from setuptools import setup, find_packages

setup(
    name='gmt_to_shp',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'geopandas',
        'shapely',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'gmt2shp=gmt2shp.gmt2shp:main',
        ],
    },
    python_requires='>=3.6',
    description='Command line tool to convert GMT files to Shapefiles',
    author='okaragoz',
    author_email='mail@okarargoz.com'
)
