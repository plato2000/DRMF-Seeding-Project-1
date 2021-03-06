__author__ = "Azeem Mohammed"
__status__ = "Development"

from unittest import TestCase
from tex2Wiki import modLabel
from tex2Wiki import setup_label_links


class TestModLabel(TestCase):
    def test_modLabel(self):
        self.assertEqual('Formula:EF.EX.TM', modLabel('\\begin{equation}\label{eq:EF.EX.TM}'))
        self.assertEqual('Formula:EF.EX.TM', modLabel('\\begin{equation}\\formula{eq:EF.EX.TM}'))
        self.assertEqual('auto-number-1', modLabel('\\begin{equation}'))
        self.assertEqual('auto-number-2', modLabel('\\begin{equation}'))

    def test_modLabelsWithList(self):
        setup_label_links('testdata/llinks')
        self.assertEqual('DLMF:04.09:E', modLabel('\\begin{equation}\label{eq:EF.EX.TM}'))
        self.assertEqual('DLMF:04.09:E', modLabel('\\begin{equation}\\formula{eq:EF.EX.TM}'))
