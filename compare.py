import matplotlib.pyplot as plt
class Compare:
    def __init__(self, colname = None, synt_data = None, real_data = None):
        self.colname = colname
        self.synt_data = synt_data
        self.real_data = real_data
        
    def set_real(self, real_data):
        self.real_data = real_data
        return None
    
    def set_synt(self, synt_data):
        self.synt_data = synt_data
        return None

    def box(self):
        assert(self.real_data != None, "No real data")
        assert(self.synt_data != None, "No synt data")

        fig, axis = plt.subplots(2,1, figsize = (10,5))
        axis[0].boxplot(self.real_data[self.colname])
        axis[0].set_title("Real data")

        axis[1].boxplot(self.synt_data[self.colname])
        axis[1].set_title("synthetic data")


    def hist(self):
        
        assert(self.real_data != None, "No real data")
        assert(self.synt_data != None, "No synt data")

        fig, axis = plt.subplots(3,1, figsize = (10,5))
        axis[0].hist(self.real_data[self.colname],bins=100)
        axis[0].set_title("Real data")

        axis[1].hist(self.synt_data[self.colname],color="red", bins=100)
        axis[1].set_title("synthetic data")

        axis[2].hist(self.synt_data[self.colname],color="red",bins=100, alpha = 0.5)
        axis[2].hist(self.real_data[self.colname],color="blue",bins=100, alpha =0.5)
        axis[2].set_title("real data vs synthetic data")

