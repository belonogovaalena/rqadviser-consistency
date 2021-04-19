from setuptools import setup, find_packages


def get_version_from_git_tag():
    # TBD: parse git tags to find last version
    return '0.1'

setup(
    name='rqadviser-consistency',
    version=get_version_from_git_tag(),
    description='Requirements adviser for consistency',
    url='https://github.com/belonogovaalena/rqadviser-consistency',
    author='Belonogova Alena',
    author_email='alena.belonogova1997@gmail.com',
    packages=find_packages(
        include=['rqadviser', 'rqadviser.*'],
        exclude=['*.tests.*']
    ),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    license='Proprietary',
    entry_points={
        'console_scripts': [
            'view = rqadviser.view.view:main',
        ]
    },
    classifiers=[
        'Private :: Do not Upload',  # Prevents uploading to pypi
    ]
)
