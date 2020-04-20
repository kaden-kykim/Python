if [ $1 = "install" ]; then
  python3 setup.py sdist && python3 $1 install
elif [ $1 = "uninstall" ]; then
  rm -rf build/
  rm -rf dist/
  rm -f MANIFEST
elif [ $1 = "upload" ]; then
  python3 setup.py sdist upload
fi
