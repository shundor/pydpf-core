"""
fields_factory
==============

Contains functions to make easy fields creation.
"""

from ansys.dpf import core
from ansys.dpf.core.common import natures, locations
from ansys.dpf.core import Field
from ansys.dpf.core.field import Dimensionality
from ansys.grpc.dpf import field_pb2, field_pb2_grpc, base_pb2

import numpy as np

def field_from_array(arr):
    """Creates DPF vector or scalar field from a numpy array or a
    Python list.

    Parameters
    ----------
    arr : np.ndarray or List
        Numpy array or Python List containing either 1 or 3 dimensions.

    Returns
    -------
    field : Field
        Field constructed from numpy array.
    """
    from ansys.dpf.core import Field, natures
    arr = np.asarray(arr)

    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError('Array must be a numeric type')

    shp_err = ValueError('Array must be either contain 1 dimension or '
                         '2 dimensions with three components.')
    if arr.ndim == 1:
        nature = natures.scalar
    elif arr.ndim == 2:
        if arr.shape[1] == 1:
            arr = arr.ravel()
            nature = natures.scalar
        elif arr.shape[1] == 3:
            nature = natures.vector
        elif arr.shape[1] == 6:
            nature = natures.symmatrix
        else:
            raise shp_err
    else:
        raise shp_err

    n_entities = arr.shape[0]
    field = Field(nentities=n_entities, nature=nature)
    field.data = arr
    field.scoping.ids = np.arange(1, n_entities + 1)
    return field

def create_matrix_field(num_entities, num_lines, num_col, location = locations.nodal, server=None):
    """Helper function to create a specific ``ansys.dpf.core.Field``.
    The returned field will contain entities that have matrix format. 
    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow up the size of your field. 

    Parameters
    ----------
    num_entities : int
        Number of entities reserved
        
    num_lines : int
        Number of matrix lines 
    
    num_col : int
        Number of matrix columns

    location : str, optional
        Location of the field. Default: ``"Nodal"``. For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ansys.dpf.core.natures.elemental_nodal
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    field : Field
        Dpf field at the requested format.

    Examples
    --------
    Create field containing 3 matrix entities of a col*lines = 2*5 size with
    nodal location (default). 

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_matrix_field(3, 5, 2)
    
    """
    return _create_field(server, natures.matrix, num_entities, location, num_col, num_lines)

def create_3d_vector_field(num_entities, location = locations.nodal, server=None):
    """Helper function to create a specific ``ansys.dpf.core.Field``.
    The returned field will contain entities that have 3d vector format. 
    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow up the size of your field. 

    Parameters
    ----------
    num_entities : int
        Number of entities reserved

    location : str, optional
        Location of the field. Default: ``"Nodal"``. For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ansys.dpf.core.natures.elemental_nodal
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    field : Field
        Dpf field at the requested format.

    Examples
    --------
    Create field containing 4 3d vector entities with nodal location (default). 

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_3d_vector_field(4)
    
    """
    return _create_field(server, natures.vector, num_entities, location)

def create_tensor_field(num_entities, location = locations.nodal, server=None):
    """Helper function to create a specific ``ansys.dpf.core.Field``.
    The returned field will contain entities that have 3*3 format. 
    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow up the size of your field. 

    Parameters
    ----------
    num_entities : int
        Number of entities reserved

    location : str, optional
        Location of the field. Default: ``"Nodal"``. For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ansys.dpf.core.natures.elemental_nodal
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    field : Field
        Dpf field at the requested format.

    Examples
    --------
    Create field containing 4 tensor entities with nodal location (default). 

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_tensor_field(4)
    
    """
    return _create_field(server, natures.symmatrix, num_entities, location)

def create_scalar_field(num_entities, location = locations.nodal, server=None):
    """Helper function to create a specific ``ansys.dpf.core.Field``.
    The returned field will contain entities that are scalar. 
    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow up the size of your field. 

    Parameters
    ----------
    num_entities : int
        Number of entities reserved

    location : str, optional
        Location of the field. Default: ``"Nodal"``. For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ansys.dpf.core.natures.elemental_nodal
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    field : Field
        Dpf field at the requested format.

    Examples
    --------
    Create field containing 4 scalars with nodal location (default). 

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_scalar_field(4)
    
    """
    return _create_field(server, natures.scalar, num_entities, location)

def create_vector_field(num_entities, num_comp, location = locations.nodal, server=None):
    """Helper function to create a specific ``ansys.dpf.core.Field``.
    The returned field will contain entities that have vector format. 
    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow up the size of your field. 

    Parameters
    ----------
    num_entities : int
        Number of entities reserved
        
    num_comp : int
        Number of vector's components 

    location : str, optional
        Location of the field. Default: ``"Nodal"``. For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ansys.dpf.core.natures.elemental_nodal
    
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server.   
        
    Returns
    -------
    field : Field
        Dpf field at the requested format.

    Examples
    --------
    Create field containing 3 vectors entities of 5 components each with
    nodal location (default). 

    >>> from ansys.dpf.core import fields_factory
    >>> field = fields_factory.create_vector_field(3, 5)
    
    """
    return _create_field(server, natures.vector, num_entities, location, ncomp_n = num_comp)

def _connect(server):
    """Connect to the grpc instance"""
    if server is None:
        server = core._global_server()
    stub = field_pb2_grpc.FieldServiceStub(server.channel)
    return stub

def _create_field(server, nature, nentities, location = locations.nodal, 
                  ncomp_n = 0, ncomp_m = 0):
    """Private helper function to create a specific ``ansys.dpf.core.Field``.
    This is a "reserve" mechanism, not a resize one. This means that you
    need to append data to grow up the size of your field. 

    Parameters
    ----------
    server : server.DPFServer, optional
        Server with channel connected to the remote or local instance. When
        ``None``, attempts to use the the global server. 
    
    snature : str 
        Defines the nature of the field entity data. For example: 
            
        - ansys.dpf.core.natures.matrix
        - ansys.dpf.core.natures.scalar
        
        
    num_entities : int
        Number of entities reserved

    location : str optional
        Location of the field.  For example:

        - ``"Nodal"``
        - ``"Elemental"``
        - ansys.dpf.core.locations.elemental_nodal    
            
    ncomp_n : int
        Number of lines 
    
    ncomp_m : int
        Number of columns
        
    Returns
    -------
    field : Field
        Dpf field at the requested format."""
    # ncomp_n is number of column components
    # ncomp_m is number of line components
    # connect to grpc
    stub = _connect(server)
    # set nature
    if hasattr(nature, 'name'):
        snature = nature.name
    else:
        snature = nature
        
    if snature == natures.vector.name:
        elem_data_size = 3
    elif snature == natures.symmatrix.name:
        elem_data_size = 6
    elif snature == natures.scalar.name:
        elem_data_size=1
    elif snature == natures.matrix.name: 
        elem_data_size = ncomp_n * ncomp_m
    else:
        elem_data_size = ncomp_n 
    if (ncomp_n != 0 and ncomp_m != 0):
        dimensionality = Dimensionality([ncomp_n, ncomp_m], nature)
    elif (ncomp_n != 0 and ncomp_m == 0):
        dimensionality = Dimensionality([ncomp_n], nature)
    else: 
        dimensionality = None        
    # set request
    request = field_pb2.FieldRequest()
    nature = base_pb2.Nature.Value(snature.upper())
    request.nature = nature
    request.location.location = location
    request.size.scoping_size = nentities
    if dimensionality is not None:
        request.dimensionality.CopyFrom(dimensionality._parse_dim_to_message())
    request.size.data_size = nentities*elem_data_size
    # get field
    message = stub.Create(request)
    field = Field(field = message, server = server)
    return field