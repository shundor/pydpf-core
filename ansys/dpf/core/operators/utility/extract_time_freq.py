"""
extract_time_freq
=================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class extract_time_freq(Operator):
    """Extract modes from a time freq support

    Parameters
    ----------
    time_freq_support : TimeFreqSupport
    set_id : int


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.extract_time_freq()

    >>> # Make input connections
    >>> my_time_freq_support = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support.connect(my_time_freq_support)
    >>> my_set_id = int()
    >>> op.inputs.set_id.connect(my_set_id)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.extract_time_freq(
    ...     time_freq_support=my_time_freq_support,
    ...     set_id=my_set_id,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, time_freq_support=None, set_id=None, config=None, server=None):
        super().__init__(name="extract_time_freq", config=config, server=server)
        self._inputs = InputsExtractTimeFreq(self)
        self._outputs = OutputsExtractTimeFreq(self)
        if time_freq_support is not None:
            self.inputs.time_freq_support.connect(time_freq_support)
        if set_id is not None:
            self.inputs.set_id.connect(set_id)

    @staticmethod
    def _spec():
        description = """Extract modes from a time freq support"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_freq_support",
                    type_names=["time_freq_support"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="set_id",
                    type_names=["int32", "vector<int32>"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(name="extract_time_freq", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtractTimeFreq
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsExtractTimeFreq
        """
        return super().outputs


class InputsExtractTimeFreq(_Inputs):
    """Intermediate class used to connect user inputs to
    extract_time_freq operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.extract_time_freq()
    >>> my_time_freq_support = dpf.TimeFreqSupport()
    >>> op.inputs.time_freq_support.connect(my_time_freq_support)
    >>> my_set_id = int()
    >>> op.inputs.set_id.connect(my_set_id)
    """

    def __init__(self, op: Operator):
        super().__init__(extract_time_freq._spec().inputs, op)
        self._time_freq_support = Input(
            extract_time_freq._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._time_freq_support)
        self._set_id = Input(extract_time_freq._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._set_id)

    @property
    def time_freq_support(self):
        """Allows to connect time_freq_support input to the operator.

        Parameters
        ----------
        my_time_freq_support : TimeFreqSupport

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.extract_time_freq()
        >>> op.inputs.time_freq_support.connect(my_time_freq_support)
        >>> # or
        >>> op.inputs.time_freq_support(my_time_freq_support)
        """
        return self._time_freq_support

    @property
    def set_id(self):
        """Allows to connect set_id input to the operator.

        Parameters
        ----------
        my_set_id : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.extract_time_freq()
        >>> op.inputs.set_id.connect(my_set_id)
        >>> # or
        >>> op.inputs.set_id(my_set_id)
        """
        return self._set_id


class OutputsExtractTimeFreq(_Outputs):
    """Intermediate class used to get outputs from
    extract_time_freq operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.extract_time_freq()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(extract_time_freq._spec().outputs, op)
        self._field = Output(extract_time_freq._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.utility.extract_time_freq()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
