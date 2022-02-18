class cl_math:
    mv_debug = 0
    
    def switch_debug(self):
        if self.mv_debug == 0:
            self.mv_debug = 1
        else:
            self.mv_debug = 0
        return self.mv_debug

    def switch_debug9(self):
        if self.mv_debug == 0:
            self.mv_debug = 9
        else:
            self.mv_debug = 0
        return self.mv_debug

    def dprint(self, iv_output):
        if self.mv_debug > 0:
            print( iv_output )
    def dprint9(self, iv_output):
        if self.mv_debug == 9:
            print( iv_output )
