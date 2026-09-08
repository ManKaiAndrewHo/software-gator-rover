from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rover_core'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Gator Rover Software Team',
    maintainer_email='swe@gatorrover.org',
    description='Core starter node and launch scripts for Gator Rover.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'status_node = rover_core.status_node:main',
        ],
    },
)
