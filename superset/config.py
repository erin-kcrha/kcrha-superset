# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""The main config file for Superset

All configuration in this file can be overridden by providing a superset_config
in your PYTHONPATH as there is a ``from superset_config import *``
at the end of this file.
"""

# Import all configuration from the new config structure
# We need to import the defaults module and explicitly copy all attributes
# because star imports don't always work reliably with this pattern

# Copy all public attributes from defaults to this module
import sys

import superset.config_defaults as _defaults_module
from superset.config_extensions import SupersetConfig  # noqa: F401

_this_module = sys.modules[__name__]
for _attr_name in dir(_defaults_module):
    if not _attr_name.startswith("_"):
        setattr(_this_module, _attr_name, getattr(_defaults_module, _attr_name))
