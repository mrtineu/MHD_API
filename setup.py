from distutils.core import setup
setup(
  name = 'mhd_api',         # How you named your package folder (MyLib)
  packages = ['mhd_api'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Used to get data about Bratislava MHD',   # Give a short description about your library
  author = 'MrTinEU',                   # Type in your name
  author_email = 'mrtineu416@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mrtineu',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mrtineu/MHD_API/archive/refs/tags/0.2.tar.gz',    # I explain this later on
  keywords = ['API', 'MHD', 'BUS', "Bratislava"],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
