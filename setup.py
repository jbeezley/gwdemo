from setuptools import setup, find_packages

setup(name='gobig-demo',
      version='0.0.1',
      description='An example girder worker extension for gobig 1-25-2018',
      entry_points={
          'girder_worker_plugins': [
              'gobig-demo = gobig_demo:GobigDemoPlugin',
          ]
      },
      packages=find_packages())
