"""
Collection of tools

Xaratustrah
2017
"""

from scipy.signal import hilbert
import xml.etree.ElementTree as et
from iqtools.iqbase import IQBase
import numpy as np


# ------------ TOOLS ----------------------------

def get_eng_notation(value, unit='', decimal_place=2):
    """
    Convert numbers to scientific notation
    Parameters
    ----------
    value input number float or integer
    decimal_place How many decimal places should be left
    unit The unit will be shown, otherwise powers of ten

    Returns
    -------

    """
    ref = {24: 'Y', 21: 'Z', 18: 'E', 15: 'P',
           12: 'T', 9: 'G', 6: 'M', 3: 'k', 0: '',
           -3: 'm', -6: 'u', -9: 'n', -12: 'p',
           -15: 'f', -18: 'a', -21: 'z', -24: 'y',
           }
    if value == 0:
        return '{}{}'.format(0, unit)
    flag = '-' if value < 0 else ''
    num = max([key for key in ref.keys() if abs(value) >= 10 ** key])
    if num == 0:
        mult = ''
    else:
        mult = ref[num] if unit else 'e{}'.format(num)
    return '{}{}{}{}'.format(flag, int(abs(value) / 10 ** num * 10 ** decimal_place) / 10 ** decimal_place, mult,
                             unit)


def make_test_signal(f, fs, length=1, nharm=0, noise=False):
    """Make a sine signal with/without noise."""

    t = np.arange(0, length, 1 / fs)
    x = np.zeros(len(t))
    for i in range(nharm + 2):
        x += np.sin(2 * np.pi * i * f * t)

    if noise:
        x += np.random.normal(0, 1, len(t))
    return t, x


def write_signal_as_binary(filename, x, fs, center):
    # 32-bit little endian floats
    # insert header
    x = np.insert(x, 0, complex(fs, center))
    x = x.astype(np.complex64)
    x.tofile(filename)


def write_signal_as_ascii(filename, x, fs, center):
    # insert ascii header which looks like a complex number
    x = np.insert(x, 0, complex(fs, center))
    with open(filename, 'w') as f:
        for i in range(len(x)):
            f.write('{}\t{}\n'.format(np.real(x[i]), np.imag(x[i])))


def make_analytical(x):
    """Make an analytical signal from the real signal"""

    yy = hilbert(x)
    ii = np.real(yy)
    qq = np.imag(yy)
    x_bar = np.vectorize(complex)(ii, qq)
    ins_ph = np.angle(x_bar) * 180 / np.pi
    return x_bar, ins_ph


def read_result_csv(filename):
    """
    Read special format CSV result file from RSA5100 series output
    :param filename:
    :return:
    """
    p = np.genfromtxt(filename, skip_header=63)
    with open(filename) as f:
        cont = f.readlines()
    for l in cont:
        l = l.split(',')
        if 'Frequency' in l and len(l) == 3:
            center = float(l[1])
        if 'XStart' in l and len(l) == 3:
            start = float(l[1])
        if 'XStop' in l and len(l) == 3:
            stop = float(l[1])
    f = np.linspace(start - center, stop - center, len(p))
    return f, p


def read_result_xml(filename):
    """
    Read the resulting saved trace file SpecAn from the RSA5000 series
    :param filename:
    :return:
    """
    with open(filename, 'rb') as f:
        ba = f.read()
    xml_tree_root = et.fromstring(ba)
    for elem in xml_tree_root.iter(tag='Count'):
        count = int(elem.text)
    for elem in xml_tree_root.iter(tag='XStart'):
        start = float(elem.text)
    for elem in xml_tree_root.iter(tag='XStop'):
        stop = float(elem.text)
    for elem in xml_tree_root.iter(tag='y'):
        pwr = float(elem.text)
    p = np.zeros(count)
    i = 0
    for elem in xml_tree_root.iter(tag='y'):
        p[i] = float(elem.text)
        i += 1
    f = np.linspace(start, stop, count)
    # return watts for compatibility
    return f, IQBase.get_watt(p)


def read_data_csv(filename):
    """
    Read special format CSV data file from RSA5100 series output.
    Please note that 50 ohm power termination is already considered
    for these data.
    :param filename:
    :return:
    """
    data = np.genfromtxt(filename, skip_header=10, delimiter=",")
    data = np.ravel(data).view(dtype='c16')  # has one dimension more, should use ravel
    return data


def parse_filename(filename):
    """
    Parses filenames of experimental data in the following format:
    58Ni26+_374MeVu_250uA_pos_0_0.tiq
    :param filename:
    :return:
    """
    filename = filename.split('_')
    descr = filename[0]
    energy = float(filename[1].replace('MeVu', 'e6'))
    current = float(filename[2].replace('uA', 'e-6'))
    return descr, energy, current

