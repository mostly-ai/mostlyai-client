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
from swagger_client.models.base_connector import BaseConnector  # noqa: F401,E501

class AzureStorageConnector(BaseConnector):
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
        'account_name': 'str',
        'account_key': 'str',
        'container': 'str'
    }
    if hasattr(BaseConnector, "swagger_types"):
        swagger_types.update(BaseConnector.swagger_types)

    attribute_map = {
        'account_name': 'accountName',
        'account_key': 'accountKey',
        'container': 'container'
    }
    if hasattr(BaseConnector, "attribute_map"):
        attribute_map.update(BaseConnector.attribute_map)

    def __init__(self, account_name=None, account_key=None, container=None, *args, **kwargs):  # noqa: E501
        """AzureStorageConnector - a model defined in Swagger"""  # noqa: E501
        self._account_name = None
        self._account_key = None
        self._container = None
        self.discriminator = None
        self.account_name = account_name
        self.account_key = account_key
        self.container = container
        BaseConnector.__init__(self, *args, **kwargs)

    @property
    def account_name(self):
        """Gets the account_name of this AzureStorageConnector.  # noqa: E501


        :return: The account_name of this AzureStorageConnector.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AzureStorageConnector.


        :param account_name: The account_name of this AzureStorageConnector.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_key(self):
        """Gets the account_key of this AzureStorageConnector.  # noqa: E501


        :return: The account_key of this AzureStorageConnector.  # noqa: E501
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """Sets the account_key of this AzureStorageConnector.


        :param account_key: The account_key of this AzureStorageConnector.  # noqa: E501
        :type: str
        """
        if account_key is None:
            raise ValueError("Invalid value for `account_key`, must not be `None`")  # noqa: E501

        self._account_key = account_key

    @property
    def container(self):
        """Gets the container of this AzureStorageConnector.  # noqa: E501


        :return: The container of this AzureStorageConnector.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this AzureStorageConnector.


        :param container: The container of this AzureStorageConnector.  # noqa: E501
        :type: str
        """
        if container is None:
            raise ValueError("Invalid value for `container`, must not be `None`")  # noqa: E501

        self._container = container

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
        if issubclass(AzureStorageConnector, dict):
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
        if not isinstance(other, AzureStorageConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
