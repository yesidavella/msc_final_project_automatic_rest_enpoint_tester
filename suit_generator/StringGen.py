import random


class StringGen:

    def __init__(self, name, required, value, size, dict_poss_val):
        self.name = name
        self.required = required
        self.value = value
        self.size = size
        self.dict_poss_val = dict_poss_val

    def get_required(self):
        return self.required

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def mutate(self):
        size = self.get_size()
        # chars = string.ascii_lowercase + size*" "
        # chars = string.ascii_lowercase
        chars = ["lot","tjl","vfx","fmq","obw","xxm","ttc","xzi","ygh","bmp","hsy","phw","udz","guu","nvr","ava","vwd","iyv","ixu","mkv","pko","sbk","qbg","gvu","uvq","usw","cgn","xmf","yjr","dox","wqg","svi","now","gyo","gct","lbx","zzk","wkk","bei","knr","bvv","thx","qnk","ctk","wqa","tsd","erz","mfi","rup","pci","ngo","dua","hwv","hib","tmf","vip","wmm","swa","ytp","zkn","vba","rkb","tfi","ckd","iaf","kvo","hjy","lsi","pps","vmm","bjv","qzj","ina","kel","jkq","gku","bcs","qmy","cvy","ahz","atq","sgm","lwo","fhj","wjg","nvr","yvw","srk","ljc","rwu","ntq","bnv","pcx","drz","xdc","zgs","kbx","xuk","qxz","jem"]
        # self.set_value(''.join(random.choice(chars) for _ in range(size)))
        self.set_value(random.choice(list(self.dict_poss_val.keys())))
        return self.get_value()