import tkinter as tk


class MyText(tk.Text):
    bind_funs = {}
    def bind(self, sequence=None, func=None, add=True):
        assert isinstance(add, bool) or (add in ["", "+"])
        if sequence == "<<Modified>>":
            raise Exception("Please use bind_modified() instead when using \"<<Modified>>\"")

        if (sequence in self.bind_funs) and (add == "+" or add is True):
            self.bind_funs[sequence].append(func)
        else:
            self.bind_funs[sequence] = [func]

        super().bind(
            sequence,
            lambda evnt: [fun(evnt) for fun in self.bind_funs[sequence]],
        )

    def bind_modified(self, func=None, add=True):
        pass
