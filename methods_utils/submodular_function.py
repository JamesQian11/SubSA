import numpy as np

class SubSA(object):
    def __init__(self, index, similarity_kernel=None, similarity_matrix=None, lam: float = 1.,):
        self.lam = lam
        self.index = index
        self.n = len(index)

        assert similarity_kernel is not None or similarity_matrix is not None
        if similarity_kernel is not None:
            assert callable(similarity_kernel)
            self.similarity_kernel = self._similarity_kernel(similarity_kernel)
        else:
            assert similarity_matrix.shape[0] == self.n and similarity_matrix.shape[1] == self.n
            self.similarity_matrix = similarity_matrix
            self.similarity_kernel = lambda a, b: self.similarity_matrix[np.ix_(a, b)]
        self.all_idx = np.ones(self.n, dtype=bool)

    def _similarity_kernel(self, similarity_kernel):
        self.sim_matrix = np.zeros([self.n, self.n], dtype=np.float32)
        self.sim_matrix_cols_sum = np.zeros(self.n, dtype=np.float32)
        self.if_columns_calculated = np.zeros(self.n, dtype=bool)
        
        def _func(a, b):
            if not np.all(self.if_columns_calculated[b]):
                if b.dtype != bool:
                    temp = ~self.all_idx
                    temp[b] = True
                    b = temp
                not_calculated = b & ~self.if_columns_calculated
                
                self.sim_matrix[:, not_calculated] = similarity_kernel(self.all_idx, not_calculated)
                self.sim_matrix_cols_sum[not_calculated] = np.sum(self.sim_matrix[:, not_calculated], axis=0)
                self.if_columns_calculated[not_calculated] = True
            return self.sim_matrix[np.ix_(a, b)]
        return _func

    def calc_gain(self, idx_gain, selected):
        gain = -2. * np.sum(self.similarity_kernel(selected, idx_gain), axis=0) + self.lam * self.sim_matrix_cols_sum[idx_gain]
        return gain

    def update_state(self, new_selection, total_selected):
        pass