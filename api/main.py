#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : ..
#               ...
#----------------------------------------------------------------------------
#
# Use explicit package path so that modules may be imported from parent.
# As per: https://docs.python.org/3/tutorial/modules.html#packages
#
from api.core.service import *

# TODO: from api.services.data import *
from api.services.data.contacts import *
from api.services.data.deals import *
from api.services.data.organizations import *
from api.services.auth.auth import *
from api.services.auth.users import *

# Create the service
monolith = Service('Monolith')

# Register all of the resource models
resources = [ Auth(), Users(), Contacts(), Deals(), Organizations() ]
monolith.register(resources)
