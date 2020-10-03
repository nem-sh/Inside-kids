config=$1
modeldir=$2

cd ./monotonic_align
python setup.py build_ext --inplace
cd ..

python init.py -c $config -m $modeldir
python train.py -c $config -m $modeldir
