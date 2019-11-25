import setuptools  # noqa

from phylomill import __version__ as phylomill_version
from phylomill import __script_name__ as phylomill_script_name
from phylomill import __author__ as phylomill_author
from phylomill import __author_email__ as phylomill_author_email
from phylomill import __description__ as phylomill_description

with open('requirements.txt', 'r') as f:
    reqs = f.read()

reqs = reqs.split('\n')[0:-3]

setuptools.setup(
    name=phylomill_script_name,
    version=phylomill_version,
    author=phylomill_author,
    author_email=phylomill_author_email,
    description=phylomill_description,
    long_description=phylomill_description,
    long_description_content_type='text/markdown',
    url='https://github.com/karolisr/PhyloMill2',
    packages=setuptools.find_packages(),
    install_requires=reqs + ['ncbi-taxonomy-local @ https://github.com/karolisr/ncbi-taxonomy-local/archive/master.zip', 'kakapo @ https://github.com/karolisr/kakapo/archive/master.zip'],  # noqa
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: cc-by-sa-4.0',
        'Operating System :: OS Independent',
    ],
    entry_points={'console_scripts': ['phylomill=phylomill.__main__:main']}
)
