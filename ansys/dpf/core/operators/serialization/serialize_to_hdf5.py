"""
serialize_to_hdf5
=================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Hdf5 plugin, from "serialization" category
"""

class serialize_to_hdf5(Operator):
    """Serialize the inputs in an hdf5 format.

      available inputs:
        - file_path (str)
        - export_floats (bool)
        - export_flat_vectors (bool)
        - data1 (Any)
        - data2 (Any)

      available outputs:


      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.serialize_to_hdf5()

      >>> # Make input connections
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)
      >>> my_export_floats = bool()
      >>> op.inputs.export_floats.connect(my_export_floats)
      >>> my_export_flat_vectors = bool()
      >>> op.inputs.export_flat_vectors.connect(my_export_flat_vectors)
      >>> my_data1 = dpf.Any()
      >>> op.inputs.data1.connect(my_data1)
      >>> my_data2 = dpf.Any()
      >>> op.inputs.data2.connect(my_data2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.serialize_to_hdf5(file_path=my_file_path,export_floats=my_export_floats,export_flat_vectors=my_export_flat_vectors,data1=my_data1,data2=my_data2)

      >>> # Get output data"""
    def __init__(self, file_path=None, export_floats=None, export_flat_vectors=None, data1=None, data2=None, config=None, server=None):
        super().__init__(name="serialize_to_hdf5", config = config, server = server)
        self._inputs = InputsSerializeToHdf5(self)
        self._outputs = OutputsSerializeToHdf5(self)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)
        if export_floats !=None:
            self.inputs.export_floats.connect(export_floats)
        if export_flat_vectors !=None:
            self.inputs.export_flat_vectors.connect(export_flat_vectors)
        if data1 !=None:
            self.inputs.data1.connect(data1)
        if data2 !=None:
            self.inputs.data2.connect(data2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Serialize the inputs in an hdf5 format.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""output file path with .h5 extension"""), 
                                 1 : PinSpecification(name = "export_floats", type_names=["bool"], optional=False, document="""converts double to float to reduce file size (default is true)"""), 
                                 2 : PinSpecification(name = "export_flat_vectors", type_names=["bool"], optional=False, document="""if true, vectors and matrices data are exported flat (x1,y1,z1,x2,y2,z2..) (default is false)"""), 
                                 3 : PinSpecification(name = "data", type_names=["any"], optional=False, document="""only the data set explicitly to export is exported"""), 
                                 4 : PinSpecification(name = "data", type_names=["any"], optional=False, document="""only the data set explicitly to export is exported""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "serialize_to_hdf5")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSerializeToHdf5 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSerializeToHdf5 
        """
        return super().outputs


#internal name: serialize_to_hdf5
#scripting name: serialize_to_hdf5
class InputsSerializeToHdf5(_Inputs):
    """Intermediate class used to connect user inputs to serialize_to_hdf5 operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.serialize_to_hdf5()
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)
      >>> my_export_floats = bool()
      >>> op.inputs.export_floats.connect(my_export_floats)
      >>> my_export_flat_vectors = bool()
      >>> op.inputs.export_flat_vectors.connect(my_export_flat_vectors)
      >>> my_data1 = dpf.Any()
      >>> op.inputs.data1.connect(my_data1)
      >>> my_data2 = dpf.Any()
      >>> op.inputs.data2.connect(my_data2)
    """
    def __init__(self, op: Operator):
        super().__init__(serialize_to_hdf5._spec().inputs, op)
        self._file_path = Input(serialize_to_hdf5._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._file_path)
        self._export_floats = Input(serialize_to_hdf5._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._export_floats)
        self._export_flat_vectors = Input(serialize_to_hdf5._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._export_flat_vectors)
        self._data1 = Input(serialize_to_hdf5._spec().input_pin(3), 3, op, 0) 
        self._inputs.append(self._data1)
        self._data2 = Input(serialize_to_hdf5._spec().input_pin(4), 4, op, 1) 
        self._inputs.append(self._data2)

    @property
    def file_path(self):
        """Allows to connect file_path input to the operator

        - pindoc: output file path with .h5 extension

        Parameters
        ----------
        my_file_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serialize_to_hdf5()
        >>> op.inputs.file_path.connect(my_file_path)
        >>> #or
        >>> op.inputs.file_path(my_file_path)

        """
        return self._file_path

    @property
    def export_floats(self):
        """Allows to connect export_floats input to the operator

        - pindoc: converts double to float to reduce file size (default is true)

        Parameters
        ----------
        my_export_floats : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serialize_to_hdf5()
        >>> op.inputs.export_floats.connect(my_export_floats)
        >>> #or
        >>> op.inputs.export_floats(my_export_floats)

        """
        return self._export_floats

    @property
    def export_flat_vectors(self):
        """Allows to connect export_flat_vectors input to the operator

        - pindoc: if true, vectors and matrices data are exported flat (x1,y1,z1,x2,y2,z2..) (default is false)

        Parameters
        ----------
        my_export_flat_vectors : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serialize_to_hdf5()
        >>> op.inputs.export_flat_vectors.connect(my_export_flat_vectors)
        >>> #or
        >>> op.inputs.export_flat_vectors(my_export_flat_vectors)

        """
        return self._export_flat_vectors

    @property
    def data1(self):
        """Allows to connect data1 input to the operator

        - pindoc: only the data set explicitly to export is exported

        Parameters
        ----------
        my_data1 : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serialize_to_hdf5()
        >>> op.inputs.data1.connect(my_data1)
        >>> #or
        >>> op.inputs.data1(my_data1)

        """
        return self._data1

    @property
    def data2(self):
        """Allows to connect data2 input to the operator

        - pindoc: only the data set explicitly to export is exported

        Parameters
        ----------
        my_data2 : Any, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.serialize_to_hdf5()
        >>> op.inputs.data2.connect(my_data2)
        >>> #or
        >>> op.inputs.data2(my_data2)

        """
        return self._data2

class OutputsSerializeToHdf5(_Outputs):
    """Intermediate class used to get outputs from serialize_to_hdf5 operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.serialize_to_hdf5()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(serialize_to_hdf5._spec().outputs, op)
        pass 
