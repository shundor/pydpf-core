"""
elements_volumes_over_time
==========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "geo" category
"""

class elements_volumes_over_time(Operator):
    """Calculation of the volume of each element over time of a mesh for each specified time step.

      available inputs:
        - scoping (Scoping) (optional)
        - displacement (FieldsContainer) (optional)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.geo.elements_volumes_over_time()

      >>> # Make input connections
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_displacement = dpf.FieldsContainer()
      >>> op.inputs.displacement.connect(my_displacement)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.geo.elements_volumes_over_time(scoping=my_scoping,displacement=my_displacement,mesh=my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, scoping=None, displacement=None, mesh=None, config=None, server=None):
        super().__init__(name="volumes_provider", config = config, server = server)
        self._inputs = InputsElementsVolumesOverTime(self)
        self._outputs = OutputsElementsVolumesOverTime(self)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)
        if displacement !=None:
            self.inputs.displacement.connect(displacement)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Calculation of the volume of each element over time of a mesh for each specified time step.""",
                             map_input_pin_spec={
                                 1 : PinSpecification(name = "scoping", type_names=["scoping"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "displacement", type_names=["fields_container"], optional=True, document="""Displacement field's container. Must contain the mesh if mesh not specified in input."""), 
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "volumes_provider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementsVolumesOverTime 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementsVolumesOverTime 
        """
        return super().outputs


#internal name: volumes_provider
#scripting name: elements_volumes_over_time
class InputsElementsVolumesOverTime(_Inputs):
    """Intermediate class used to connect user inputs to elements_volumes_over_time operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.elements_volumes_over_time()
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
      >>> my_displacement = dpf.FieldsContainer()
      >>> op.inputs.displacement.connect(my_displacement)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(elements_volumes_over_time._spec().inputs, op)
        self._scoping = Input(elements_volumes_over_time._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._scoping)
        self._displacement = Input(elements_volumes_over_time._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._displacement)
        self._mesh = Input(elements_volumes_over_time._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        Parameters
        ----------
        my_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

    @property
    def displacement(self):
        """Allows to connect displacement input to the operator

        - pindoc: Displacement field's container. Must contain the mesh if mesh not specified in input.

        Parameters
        ----------
        my_displacement : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> op.inputs.displacement.connect(my_displacement)
        >>> #or
        >>> op.inputs.displacement(my_displacement)

        """
        return self._displacement

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: Mesh must be defined if the displacement field's container does not contain it, or if there is no displacement.

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsElementsVolumesOverTime(_Outputs):
    """Intermediate class used to get outputs from elements_volumes_over_time operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.geo.elements_volumes_over_time()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(elements_volumes_over_time._spec().outputs, op)
        self._fields_container = Output(elements_volumes_over_time._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.geo.elements_volumes_over_time()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container
