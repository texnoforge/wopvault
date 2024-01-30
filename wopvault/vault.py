import csv
import time
from pathlib import Path

from wopvault import ex


class WordsOfPowerVault():
    def __init__(self,
                 path,
                 allowed_alphabets=None,
                 allowed_symbols=None,
                 allowed_tags=None,
                 min_points=5,
                 max_points=4000,
                 ):
        self.path = Path(path)
        self.allowed_alphabets = allowed_alphabets or []
        self.allowed_symbols = allowed_symbols or []
        self.allowed_tags = allowed_tags or []
        self.min_points = min_points
        self.max_points = max_points

    @property
    def abcs_path(self):
        return self.path / 'alphabets'

    def get_abc_path(self, abc):
        return self.abcs_path / abc

    def get_symbols_path(self, abc):
        return self.get_abc_path(abc) / 'symbols'

    def get_symbol_path(self, abc, symbol):
        return self.get_symbols_path(abc) / symbol

    def get_drawings_path(self, abc, symbol, tag=None):
        ddir = 'drawings'
        if tag:
            ddir += f'_{tag.lower()}'
        return self.get_symbol_path(abc, symbol) / ddir

    def get_new_drawing_path(self, abc, symbol, tag=None):
        t = int(time.time() * 1000)
        fn = f'{symbol}_{t}.csv'
        return self.get_drawings_path(abc, symbol, tag=tag) / fn

    def save_drawing(self, abc, symbol, curves, tag=None):
        if self.allowed_alphabets and abc not in self.allowed_alphabets:
            raise ex.AlphabetNotFound(abc)
        if self.allowed_symbols and symbol not in self.allowed_symbols:
            raise ex.SymbolNotFound(symbol)
        if tag and self.allowed_tags and tag not in self.allowed_tags:
            raise ex.TagNotFound(tag)

        n_curves = len(curves.curves)
        n_points = 0
        for curve in curves.curves:
            n_points += len(curve)

        if n_points < self.min_points:
            raise ex.PayloadTooSmall(n_points, self.min_points)
        if n_points > self.max_points:
            raise ex.PayloadTooLarge(n_points, self.max_points)

        drawing_path = self.get_new_drawing_path(abc, symbol, tag=tag)
        print(f"SAVING DRAWING: {abc}/{symbol}"
              " - {n_points} points in {n_curves} curves")
        print(f"  @ {drawing_path}")
        save_drawing(drawing_path, curves.curves)


def save_drawing(path, curves):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='') as f:
        writer = csv.writer(f)
        first = True
        for curve in curves:
            if first:
                first = False
            else:
                # curves separator
                writer.writerow([None, None])
            writer.writerows(curve)
