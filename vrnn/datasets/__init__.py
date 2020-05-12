import torch
from torch.utils.data import Dataset
from importlib import import_module
import cloudpickle

class GeneralDataset(Dataset):

    def __init__(self, args, len_seqs, train=0, normalize_data=True):
        #if normalize_data:
        #    for index in range(len(activeRole)):
        #        data_x[index] = dataset.normalize(data[index],datasets)

        self.train = train
        self.len_seqs = len_seqs
        self.game_files = args.game_files
        self.game_files_val = args.game_files_val
        self.game_files_te = args.game_files_te
        self.batchsize = args.batchsize
        self.model = args.model

        #self.normalize_data = normalize_data
        #self.datasets = args.dataset
 
    def __getitem__(self, index):
        if self.train == 1:
            batch_no = index // self.batchsize
            batch_index = index % self.batchsize
            with open(self.game_files+'_tr'+str(batch_no)+'.pkl', 'rb') as f:
                data,_,_,label = cloudpickle.load(f) # ,allow_pickle=True
        else:
            batch_no = index // int(self.len_seqs/4)
            if batch_no < 4:
                batch_index = index % int(self.len_seqs/4)
            else:
                batch_no = 3
                batch_index = index % int(self.len_seqs/4) + int(self.len_seqs/4)
            filename = self.game_files+'_val' if self.train == 0 else self.game_files +'_te'
            with open(filename+'_'+str(batch_no)+'.pkl', 'rb') as f:
                data,label = cloudpickle.load(f) 

        self.data = torch.Tensor(data)
        self.data = self.data.permute(1, 0, 2, 3)

        #if self.normalize_data:
        #    self.data = self.dataset.normalize(self.data,self.datasets)

        return self.data[batch_index], label[batch_index] # data[index] 

    def __len__(self):
        return self.len_seqs
        