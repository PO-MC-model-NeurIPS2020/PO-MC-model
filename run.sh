#!/bin/bash
# test code with small samples
python -u main.py --data nba --n_GorS 1 --n_roles 5 --batchsize 32 --n_epoch 3 -ev_th 200 --numProcess 16 --model MACRO_VRNN --attention 3 --body --jrk 0.2 --lam_acc 0.2 --pretrain 2 

# attention = -1: w/o embedding 
# attention =  3: individual binary observation

# actual training and test code
# python -u main.py --data nba --n_GorS 100 --n_roles 5 --batchsize 256 --n_epoch 15 -ev_th 200 --numProcess 16 --model MACRO_VRNN --attention 3 --body --jrk 0.1 --lam_acc 0.2 --pretrain 50 