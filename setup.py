from setuptools import setup, Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True

setup(
    name='spiranet-lite',
    version='1.0.0',
    description='Wrapper for proprietary SpiraNet ML models',
    
    # 1. Tell setuptools the code is in 'src'
    package_dir={'': 'src'},
    
    # 2. explicitly list the Python modules found in src
    py_modules=['SpiraLibsPars'], 
    
    # 3. Force include the .so file. 
    # Since it's not in a proper "package" (folder with __init__.py), 
    # we use MANIFEST.in + include_package_data to grab the binary.
    include_package_data=True,
    
    # 4. Mark as platform-specific (not pure python)
    distclass=BinaryDistribution,
    zip_safe=False,
)