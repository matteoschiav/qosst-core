# qosst-core - Core module of the Quantum Open Software for Secure Transmissions.
# Copyright (C) 2021-2024 Yoann Piétri

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
This module contains the necessary codes to generate the synchronization sequence.

Here are some examples of use

.. code-block:: python

    from qosst_core.synchronization import MaximumLengthSequence, ZadoffChuSequence

    # Create a Zadoff-Chu sequence of root 5 and length 3990
    zc = ZadoffChuSequence(root=5, length=3989)
    sequence = zc.sequence()

    # Create a Maximum Length sequence with number of bits 16
    mls = MaximumLengthSequence(nbits=16)
    sequence = mls.sequence()
"""
from .synchronization import SynchronizationSequence

from .mls import MaximumLengthSequence
from .zc import ZadoffChuSequence