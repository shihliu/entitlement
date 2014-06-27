basedir = basename `pwd`
export PYTHONPATH=$PYTHONPATH:$basedir
python $basedir/testcases/installation/test_sam_installation.py
