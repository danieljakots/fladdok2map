from setuptools import setup, find_packages

setup(
    name='fladdok2map',
    version='0.1',
    install_requires = [
        'flask',
        'requests',
    ],
    include_package_data=True,
    packages = find_packages(),
    entry_points ={
        'console_scripts': ['fladdok2map = fladdok2map.fladdok2map:main'],
    },
    zip_safe=False,
)
