cd bilm-tf
python3 bin/train_elmo.py \
    --train_prefix='../../corpus/preprocess.hi' \
    --vocab_file ../elmo_vocab.txt \
    --save_dir elmo_model