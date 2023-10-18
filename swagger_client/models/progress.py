# coding: utf-8

"""
    Public API of Mostly AI

    Public API of Mostly AI  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Progress(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'progress_value': 'int',
        'progress_maximum': 'int',
        'progress_type': 'str'
    }

    attribute_map = {
        'progress_value': 'progressValue',
        'progress_maximum': 'progressMaximum',
        'progress_type': 'progressType'
    }

    def __init__(self, progress_value=None, progress_maximum=None, progress_type=None):  # noqa: E501
        """Progress - a model defined in Swagger"""  # noqa: E501
        self._progress_value = None
        self._progress_maximum = None
        self._progress_type = None
        self.discriminator = None
        if progress_value is not None:
            self.progress_value = progress_value
        if progress_maximum is not None:
            self.progress_maximum = progress_maximum
        if progress_type is not None:
            self.progress_type = progress_type

    @property
    def progress_value(self):
        """Gets the progress_value of this Progress.  # noqa: E501


        :return: The progress_value of this Progress.  # noqa: E501
        :rtype: int
        """
        return self._progress_value

    @progress_value.setter
    def progress_value(self, progress_value):
        """Sets the progress_value of this Progress.


        :param progress_value: The progress_value of this Progress.  # noqa: E501
        :type: int
        """

        self._progress_value = progress_value

    @property
    def progress_maximum(self):
        """Gets the progress_maximum of this Progress.  # noqa: E501


        :return: The progress_maximum of this Progress.  # noqa: E501
        :rtype: int
        """
        return self._progress_maximum

    @progress_maximum.setter
    def progress_maximum(self, progress_maximum):
        """Sets the progress_maximum of this Progress.


        :param progress_maximum: The progress_maximum of this Progress.  # noqa: E501
        :type: int
        """

        self._progress_maximum = progress_maximum

    @property
    def progress_type(self):
        """Gets the progress_type of this Progress.  # noqa: E501

        value items out of max done, or show a progress bar  # noqa: E501

        :return: The progress_type of this Progress.  # noqa: E501
        :rtype: str
        """
        return self._progress_type

    @progress_type.setter
    def progress_type(self, progress_type):
        """Sets the progress_type of this Progress.

        value items out of max done, or show a progress bar  # noqa: E501

        :param progress_type: The progress_type of this Progress.  # noqa: E501
        :type: str
        """
        allowed_values = ["absolut", "bar"]  # noqa: E501
        if progress_type not in allowed_values:
            raise ValueError(
                "Invalid value for `progress_type` ({0}), must be one of {1}"  # noqa: E501
                .format(progress_type, allowed_values)
            )

        self._progress_type = progress_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Progress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Progress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
