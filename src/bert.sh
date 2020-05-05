#!/bin/bash
BERT_BASE_DIR=$1
run_bert () {
python3 bert/extract_features.py \
  --input_file=draft/output.hi \
  --output_file=draft/bert.jsonl \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --layers=-1,-2,-3,-4 \
  --max_seq_length=128 \
  --batch_size=8
}
run_bert
