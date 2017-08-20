# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Create lists of sky coordinates."""
from __future__ import absolute_import, division, print_function

import logging
import numpy as np
import click
from astropy.table import Table
from .. import utils


def make_skycoord_table(n_samples=1000):
    """Generate table of random sky coordinates.

    TODO: change this to make an Astropy table.

    Columns:
    - lon      : longitude in deg
    - lat      : latitude in deg
    """
    np.random.seed(12345)

    # Sample uniformly on the unit sphere
    table = Table()
    table['lon'] = np.random.uniform(0., 360., n_samples)
    table['lat'] = np.degrees(np.arcsin(np.random.uniform(-1., 1., n_samples)))

    for col in ['lon', 'lat']:
        table[col].format = utils.FLOAT_FORMAT_INPUT

    return table


@click.command(name='make_skycoord_table')
def make_skycoord_table_command():
    """Generate table of random sky coordinates."""
    table = make_skycoord_table()

    filename = 'input/skycoords.txt'
    logging.info('Writing {}'.format(filename))
    table.write(filename, format=utils.TABLE_FORMAT, overwrite=True)
