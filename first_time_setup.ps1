Remove-Item first_time_setup.ps1
git add -A
git commit -m "Initialize template"
git submodule add https://github.com/blakeNaccarato/copier-python.git template
git submodule add https://github.com/blakeNaccarato/pylance-stubs-unofficial.git typings
git add -A
git commit -m "Add submodules"
git submodule deinit --all
copier gh:blakeNaccarato/copier-python . -f
git add -A
