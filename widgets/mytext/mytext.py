import tkinter as tk
from widgets.undo_buffer import UndoBuffer


class MyText(tk.Text):
    undo_buffer = UndoBuffer()
    undo_bind_funs = {}
    bind_funs = {}

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.init_undo_buff_by_curr_state()
        
        self.undo_bind_funs = {
            "<<Modified>>": [self.do],
            "<Control-z>": [self.undo],
            "<Control-y>": [self.redo],
        }
        super().bind("<<Modified>>", self.modified_trigger)
        super().bind("<Control-z>", lambda evnt: self.run_bind_funs("<Control-z>", evnt))
        super().bind("<Control-y>", lambda evnt: self.run_bind_funs("<Control-y>", evnt))
        
        self.skip_modify_by_undo_redo = False    # avoid undo redo triggers self.modified_trigger()

    def bind(self, sequence=None, func=None, add=False):
        if add is True:
            self.bind_funs[sequence] = self.bind_funs.get(sequence, []) + [func]
        else:
            self.bind_funs[sequence] = [func]
        
        known_sequences = list(self.bind_funs.keys()) + list(self.undo_bind_funs.keys())
        if sequence not in known_sequences:
            self.bind(
                sequence,
                lambda evnt: self.run_bind_funs(sequence, evnt),
            )
    
    def run_bind_funs(self, seq, evnt):
        funs = self.undo_bind_funs.get(seq, []) + self.bind_funs.get(seq, [])
        for f in funs:
            f(evnt)
    
    def modified_trigger(self, evnt):
        is_modified = self.edit_modified()
        if is_modified and not self.skip_modify_by_undo_redo:
            self.run_bind_funs("<<Modified>>", evnt)
        self.skip_modify_by_undo_redo = False
        self.edit_modified(False)
    
    def get_cursor_idx(self):
        row, col = self.index(tk.INSERT).split(".")
        row = int(row) - 1
        col = int(col)

        txt = self.get_text()
        lines = txt.split("\n")

        idx = -1
        for _row in range(0, row):
            idx += len(lines[_row]) + 1     # the "+1" is for "\n"
        idx += col
        return idx  # return -1 for no text
    
    def get_cursor_position(self) -> str:
        return self.index(tk.INSERT)
    
    def set_cursor_position(self, position) -> str:
        return self.mark_set(tk.INSERT, position)

    def get_text(self):
        return self.get("1.0", "end")[:-1]
    
    def set_text(self, string: str, clear_undo_buff=True):
        self.delete("1.0", "end")
        self.insert(1.0, string)
        if clear_undo_buff is True:
            self.init_undo_buff_by_curr_state()
        
    def init_undo_buff_by_curr_state(self):
        self.undo_buffer.Initialize(
            (self.get_cursor_position(), self.get_text())
        )
    
    def do(self, *w, **kw):
        cursor = self.get_cursor_position()
        txt = self.get_text()
        self.undo_buffer.AppendChange(
            (cursor, txt)
        )

    def undo(self, *w, **kw):
        undo_info = self.undo_buffer.Undo()
        if undo_info is not None:
            print(undo_info.__repr__())
            cursor, last_txt = undo_info
            self.set_text(last_txt, clear_undo_buff=False)
            self.set_cursor_position(cursor)
        self.skip_modify_by_undo_redo = True
    
    def redo(self, *w, **kw):
        redo_info = self.undo_buffer.Redo()
        if redo_info is not None:
            print(redo_info.__repr__())
            cursor, prev_txt = redo_info
            self.set_text(prev_txt, clear_undo_buff=False)
            self.set_cursor_position(cursor)
        self.skip_modify_by_undo_redo = True
