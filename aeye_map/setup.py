from setuptools import setup

package_name = 'aeye_map'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/aeye.launch.py']),
    ],
    install_requires=[
    'setuptools',
    'numpy',
    'rtabmap_launch',
    'octomap',
    'rclpy',
    'rclpy_components',
    'zed_wrapper'
    ],
    zip_safe=True,
    maintainer='axel',
    maintainer_email='sky.axel.lans@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
    package_data={
    'my_package': ['launch/*'],
    },
)
