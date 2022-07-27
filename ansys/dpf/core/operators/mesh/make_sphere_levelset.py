"""
make_sphere_levelset
====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class make_sphere_levelset(Operator):
    """Compute the levelset for a sphere using coordinates.

    Parameters
    ----------
    coordinates : MeshedRegion or Field
    origin : Field
        An overall 3d vector that gives a point of
        the plane.
    radius : float
        Sphere radius.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.make_sphere_levelset()

    >>> # Make input connections
    >>> my_coordinates = dpf.MeshedRegion()
    >>> op.inputs.coordinates.connect(my_coordinates)
    >>> my_origin = dpf.Field()
    >>> op.inputs.origin.connect(my_origin)
    >>> my_radius = float()
    >>> op.inputs.radius.connect(my_radius)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.make_sphere_levelset(
    ...     coordinates=my_coordinates,
    ...     origin=my_origin,
    ...     radius=my_radius,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self, coordinates=None, origin=None, radius=None, config=None, server=None
    ):
        super().__init__(name="levelset::make_sphere", config=config, server=server)
        self._inputs = InputsMakeSphereLevelset(self)
        self._outputs = OutputsMakeSphereLevelset(self)
        if coordinates is not None:
            self.inputs.coordinates.connect(coordinates)
        if origin is not None:
            self.inputs.origin.connect(origin)
        if radius is not None:
            self.inputs.radius.connect(radius)

    @staticmethod
    def _spec():
        description = """Compute the levelset for a sphere using coordinates."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="coordinates",
                    type_names=["abstract_meshed_region", "field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="origin",
                    type_names=["field"],
                    optional=False,
                    document="""An overall 3d vector that gives a point of
        the plane.""",
                ),
                2: PinSpecification(
                    name="radius",
                    type_names=["double"],
                    optional=False,
                    document="""Sphere radius.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="levelset::make_sphere", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMakeSphereLevelset
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMakeSphereLevelset
        """
        return super().outputs


class InputsMakeSphereLevelset(_Inputs):
    """Intermediate class used to connect user inputs to
    make_sphere_levelset operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.make_sphere_levelset()
    >>> my_coordinates = dpf.MeshedRegion()
    >>> op.inputs.coordinates.connect(my_coordinates)
    >>> my_origin = dpf.Field()
    >>> op.inputs.origin.connect(my_origin)
    >>> my_radius = float()
    >>> op.inputs.radius.connect(my_radius)
    """

    def __init__(self, op: Operator):
        super().__init__(make_sphere_levelset._spec().inputs, op)
        self._coordinates = Input(make_sphere_levelset._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._coordinates)
        self._origin = Input(make_sphere_levelset._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._origin)
        self._radius = Input(make_sphere_levelset._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._radius)

    @property
    def coordinates(self):
        """Allows to connect coordinates input to the operator.

        Parameters
        ----------
        my_coordinates : MeshedRegion or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.make_sphere_levelset()
        >>> op.inputs.coordinates.connect(my_coordinates)
        >>> # or
        >>> op.inputs.coordinates(my_coordinates)
        """
        return self._coordinates

    @property
    def origin(self):
        """Allows to connect origin input to the operator.

        An overall 3d vector that gives a point of
        the plane.

        Parameters
        ----------
        my_origin : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.make_sphere_levelset()
        >>> op.inputs.origin.connect(my_origin)
        >>> # or
        >>> op.inputs.origin(my_origin)
        """
        return self._origin

    @property
    def radius(self):
        """Allows to connect radius input to the operator.

        Sphere radius.

        Parameters
        ----------
        my_radius : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.make_sphere_levelset()
        >>> op.inputs.radius.connect(my_radius)
        >>> # or
        >>> op.inputs.radius(my_radius)
        """
        return self._radius


class OutputsMakeSphereLevelset(_Outputs):
    """Intermediate class used to get outputs from
    make_sphere_levelset operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.make_sphere_levelset()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(make_sphere_levelset._spec().outputs, op)
        self._field = Output(make_sphere_levelset._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.make_sphere_levelset()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field