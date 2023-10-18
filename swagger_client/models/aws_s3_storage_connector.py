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

class AwsS3StorageConnector(BaseConnector):
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
        'access_key': 'str',
        'secret_key': 'str',
        'region': 'str',
        'bucket': 'str'
    }
    if hasattr(BaseConnector, "swagger_types"):
        swagger_types.update(BaseConnector.swagger_types)

    attribute_map = {
        'access_key': 'accessKey',
        'secret_key': 'secretKey',
        'region': 'region',
        'bucket': 'bucket'
    }
    if hasattr(BaseConnector, "attribute_map"):
        attribute_map.update(BaseConnector.attribute_map)

    def __init__(self, access_key=None, secret_key=None, region=None, bucket=None, *args, **kwargs):  # noqa: E501
        """AwsS3StorageConnector - a model defined in Swagger"""  # noqa: E501
        self._access_key = None
        self._secret_key = None
        self._region = None
        self._bucket = None
        self.discriminator = None
        self.access_key = access_key
        self.secret_key = secret_key
        if region is not None:
            self.region = region
        self.bucket = bucket
        BaseConnector.__init__(self, *args, **kwargs)

    @property
    def access_key(self):
        """Gets the access_key of this AwsS3StorageConnector.  # noqa: E501


        :return: The access_key of this AwsS3StorageConnector.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AwsS3StorageConnector.


        :param access_key: The access_key of this AwsS3StorageConnector.  # noqa: E501
        :type: str
        """
        if access_key is None:
            raise ValueError("Invalid value for `access_key`, must not be `None`")  # noqa: E501

        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this AwsS3StorageConnector.  # noqa: E501


        :return: The secret_key of this AwsS3StorageConnector.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AwsS3StorageConnector.


        :param secret_key: The secret_key of this AwsS3StorageConnector.  # noqa: E501
        :type: str
        """
        if secret_key is None:
            raise ValueError("Invalid value for `secret_key`, must not be `None`")  # noqa: E501

        self._secret_key = secret_key

    @property
    def region(self):
        """Gets the region of this AwsS3StorageConnector.  # noqa: E501


        :return: The region of this AwsS3StorageConnector.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsS3StorageConnector.


        :param region: The region of this AwsS3StorageConnector.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def bucket(self):
        """Gets the bucket of this AwsS3StorageConnector.  # noqa: E501


        :return: The bucket of this AwsS3StorageConnector.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this AwsS3StorageConnector.


        :param bucket: The bucket of this AwsS3StorageConnector.  # noqa: E501
        :type: str
        """
        if bucket is None:
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

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
        if issubclass(AwsS3StorageConnector, dict):
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
        if not isinstance(other, AwsS3StorageConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
