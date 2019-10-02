from distutils.core import setup

setup(
  name = 'largest_face_detector',
  packages = ['largest_face_detector'],
  version = '0.1', 
  license='MIT',
  description = 'Python package to crop largest face from images', 
  author = 'Devang Kulshreshtha',
  author_email = 'devang.kulshreshtha.cse14@itbhu.ac.in',
  url = 'https://github.com/devangkulshreshtha/largest_face_detector',
  download_url = 'https://github.com/devangkulshreshtha/largest_face_detector/archive/0.1.tar.gz',
  keywords = ['FACE_DETECTOR', 'COMPUTER_VISON', 'OOPS_DESIGN'],
  install_requires=[
          'numpy',
          'dlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2', 
    'Programming Language :: Python :: 2.7'
  ],
)