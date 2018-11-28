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
from api.services.data.contacts import *

# Create the service
data = Service('Data')

# Register all of the resource models
# resources = [ Contacts(), Deals(), Organizations() ]
resources = Contacts()
data.register(resources)
