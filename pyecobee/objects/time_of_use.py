"""
This module is home to the TimeOfUse class
"""
from pyecobee.ecobee_object import EcobeeObject


class TimeOfUse(EcobeeObject):
    """
    This class has been manually generated by reverse engineering

    Attribute names have been generated by converting ecobee property
    names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value
    of READONLY is "no".

    An __init__ argument without a default value has been generated if
    the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated
    if the value of REQUIRED is "no".
    """
    __slots__ = ['_feature_state', '_savings']

    attribute_name_map = {
        'feature_state': 'featureState',
        'featureState': 'feature_state',
        'savings': 'savings'}

    attribute_type_map = {'feature_state': 'six.text_type', 'savings': 'six.text_type'}

    def __init__(self, feature_state=None, savings=None):
        """
        Construct a TimeOfUse instance
        """
        self._feature_state = feature_state
        self._savings = savings

    @property
    def feature_state(self):
        """
        Gets the feature_state attribute of this TimeOfUse instance.

        :return: The value of the feature_state attribute of this TimeOfUse
        instance.
        :rtype: six.text_type
        """

        return self._feature_state

    @property
    def savings(self):
        """
        Gets the savings attribute of this TimeOfUse instance.

        :return: The value of the savings attribute of this TimeOfUse
        instance.
        :rtype: six.text_type
        """

        return self.savings