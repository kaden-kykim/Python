PY_DIST_PKG_NAME="nester-kaden"

if [ $1 = "install" ]; then
  pip3 install .
elif [ $1 = "uninstall" ]; then
  pip3 uninstall -y ${PY_DIST_PKG_NAME}
elif [ $1 = "build" ]; then
  python3 setup.py sdist bdist_wheel
elif [ $1 = "upload-test" ]; then
  twine upload --repository-url https://test.pypi.org/legacy/ dist/*
elif [ $1 = "upload" ]; then
  twine upload dist/*
elif [ $1 = "clean" ]; then
  rm -rf build/
  rm -rf dist/
  rm -rf *.egg-info/
  rm -f MANIFEST
fi

PY_DIST_PKG_NAME=