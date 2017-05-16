try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup

	config = {
		'description' = 'Machine Learning Competition'
		'author' = 'Maximiliano, Galvan Nahuel, Pablo, Prado Maria Florencia'
		'url': 'https://github.com/Gnahue/sanFranciscoBiclas.git',
    	'download_url': 'https://github.com/Gnahue/sanFranciscoBiclas.git',
    	'version': '0.1',
    	'install_requires': ['nose'],
    	'packages': ['modelo'],
    	'scripts': [],
    	'name': 'timePrediction'
}
	