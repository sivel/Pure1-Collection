# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Simon Dodsley <simon@purestorage.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    # Standard Pure Storage documentation fragment
    DOCUMENTATION = r"""
options:
  - See separate platform section for more details
requirements:
  - See separate platform section for more details
notes:
  - Ansible modules are available for the following Pure Storage products: FlashArray, FlashBlade, Pure1
"""

    # Documentation fragment for Pure1
    P1 = r"""
options:
  key_file:
    description:
      - Path to the private key file
      - Defaults to the set environment variable under PURE1_PRIVATE_KEY_FILE.
    type: str
    required: true
  app_id:
    description:
      - Application ID from Pure1 Registration page
      - eg. pure1:apikey:dssf2331sd
      - Defaults to the set environment variable under PURE1_APP_ID
    type: str
    required: true
  password:
    description:
      - The password of the private key, if encrypted.
      - Defaults to the set environment variable under PURE1_PRIVATE_KEY_FILE.
    type: str
    required: true
notes:
  - This module requires the C(py-pure-client) Python library
  - You must set C(PURE1_APP_ID) and C(PURE1_PRIVATE_KEY_FILE) environment variables
    if I(app_id) and I(key_file) arguments are not passed to the module directly
requirements:
  - python >= 3.4
  - py-pure-client >= 1.14.1
"""
