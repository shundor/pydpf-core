"""
strain_from_voigt
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class strain_from_voigt(Operator):
    """Put strain field from Voigt notation to standard format.

      available inputs:
        - field (Field, FieldsContainer)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.strain_from_voigt()

      >>> # Make input connections
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.strain_from_voigt(field=my_field)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="strain_from_voigt", config = config, server = server)
        self._inputs = InputsStrainFromVoigt(self)
        self._outputs = OutputsStrainFromVoigt(self)
        if field !=None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        spec = Specification(description="""Put strain field from Voigt notation to standard format.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "strain_from_voigt")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsStrainFromVoigt 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsStrainFromVoigt 
        """
        return super().outputs


#internal name: strain_from_voigt
#scripting name: strain_from_voigt
class InputsStrainFromVoigt(_Inputs):
    """Intermediate class used to connect user inputs to strain_from_voigt operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.strain_from_voigt()
      >>> my_field = dpf.Field()
      >>> op.inputs.field.connect(my_field)
    """
    def __init__(self, op: Operator):
        super().__init__(strain_from_voigt._spec().inputs, op)
        self._field = Input(strain_from_voigt._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.strain_from_voigt()
        >>> op.inputs.field.connect(my_field)
        >>> #or
        >>> op.inputs.field(my_field)

        """
        return self._field

class OutputsStrainFromVoigt(_Outputs):
    """Intermediate class used to get outputs from strain_from_voigt operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.strain_from_voigt()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(strain_from_voigt._spec().outputs, op)
        self._field = Output(strain_from_voigt._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.strain_from_voigt()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field
