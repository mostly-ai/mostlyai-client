# coding: utf-8

"""
    Public API of Mostly AI

    Public API of Mostly AI  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DeliveryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_delivery(self, **kwargs):  # noqa: E501
        """Creates a new delivery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_delivery(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryBody body:
        :param str synth_data_id: id of the synth data set
        :return: Delivery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_delivery_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_delivery_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_delivery_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a new delivery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_delivery_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryBody body:
        :param str synth_data_id: id of the synth data set
        :return: Delivery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'synth_data_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_delivery" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'synth_data_id' in params:
            query_params.append(('synth-data-id', params['synth_data_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delivery', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Delivery',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_deliveries(self, synth_data_id, **kwargs):  # noqa: E501
        """List deliveries of synth data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deliveries(synth_data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str synth_data_id: id of the synth data set (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_deliveries_with_http_info(synth_data_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_deliveries_with_http_info(synth_data_id, **kwargs)  # noqa: E501
            return data

    def get_deliveries_with_http_info(self, synth_data_id, **kwargs):  # noqa: E501
        """List deliveries of synth data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deliveries_with_http_info(synth_data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str synth_data_id: id of the synth data set (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['synth_data_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_deliveries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'synth_data_id' is set
        if ('synth_data_id' not in params or
                params['synth_data_id'] is None):
            raise ValueError("Missing the required parameter `synth_data_id` when calling `get_deliveries`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'synth_data_id' in params:
            query_params.append(('synth-data-id', params['synth_data_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delivery', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delivery_by_id(self, delivery_id, **kwargs):  # noqa: E501
        """Read a delivery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_by_id(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: Delivery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_delivery_by_id_with_http_info(delivery_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_delivery_by_id_with_http_info(delivery_id, **kwargs)  # noqa: E501
            return data

    def get_delivery_by_id_with_http_info(self, delivery_id, **kwargs):  # noqa: E501
        """Read a delivery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_by_id_with_http_info(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: Delivery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delivery_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_id' is set
        if ('delivery_id' not in params or
                params['delivery_id'] is None):
            raise ValueError("Missing the required parameter `delivery_id` when calling `get_delivery_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'delivery_id' in params:
            path_params['deliveryId'] = params['delivery_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delivery/{deliveryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Delivery',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delivery_progress(self, delivery_id, **kwargs):  # noqa: E501
        """Read the delivery progress.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_progress(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: JobProgress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_delivery_progress_with_http_info(delivery_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_delivery_progress_with_http_info(delivery_id, **kwargs)  # noqa: E501
            return data

    def get_delivery_progress_with_http_info(self, delivery_id, **kwargs):  # noqa: E501
        """Read the delivery progress.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_progress_with_http_info(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: JobProgress
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delivery_progress" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_id' is set
        if ('delivery_id' not in params or
                params['delivery_id'] is None):
            raise ValueError("Missing the required parameter `delivery_id` when calling `get_delivery_progress`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'delivery_id' in params:
            path_params['deliveryId'] = params['delivery_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delivery/{deliveryId}/deliver', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobProgress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_delivery(self, delivery_id, **kwargs):  # noqa: E501
        """Starts the delivery of the generator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_delivery(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_delivery_with_http_info(delivery_id, **kwargs)  # noqa: E501
        else:
            (data) = self.start_delivery_with_http_info(delivery_id, **kwargs)  # noqa: E501
            return data

    def start_delivery_with_http_info(self, delivery_id, **kwargs):  # noqa: E501
        """Starts the delivery of the generator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_delivery_with_http_info(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_delivery" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_id' is set
        if ('delivery_id' not in params or
                params['delivery_id'] is None):
            raise ValueError("Missing the required parameter `delivery_id` when calling `start_delivery`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'delivery_id' in params:
            path_params['deliveryId'] = params['delivery_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delivery/{deliveryId}/deliver', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stop_delivery(self, delivery_id, **kwargs):  # noqa: E501
        """Stops the delivery of the generator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_delivery(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stop_delivery_with_http_info(delivery_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stop_delivery_with_http_info(delivery_id, **kwargs)  # noqa: E501
            return data

    def stop_delivery_with_http_info(self, delivery_id, **kwargs):  # noqa: E501
        """Stops the delivery of the generator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_delivery_with_http_info(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_delivery" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_id' is set
        if ('delivery_id' not in params or
                params['delivery_id'] is None):
            raise ValueError("Missing the required parameter `delivery_id` when calling `stop_delivery`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'delivery_id' in params:
            path_params['deliveryId'] = params['delivery_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delivery/{deliveryId}/deliver', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_delivery(self, body, delivery_id, **kwargs):  # noqa: E501
        """Updates a delivery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_delivery(body, delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Delivery body: (required)
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: Delivery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_delivery_with_http_info(body, delivery_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_delivery_with_http_info(body, delivery_id, **kwargs)  # noqa: E501
            return data

    def update_delivery_with_http_info(self, body, delivery_id, **kwargs):  # noqa: E501
        """Updates a delivery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_delivery_with_http_info(body, delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Delivery body: (required)
        :param DeliveryId delivery_id: The unique identifier of the delivery (required)
        :return: Delivery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'delivery_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_delivery" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_delivery`")  # noqa: E501
        # verify the required parameter 'delivery_id' is set
        if ('delivery_id' not in params or
                params['delivery_id'] is None):
            raise ValueError("Missing the required parameter `delivery_id` when calling `update_delivery`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'delivery_id' in params:
            path_params['deliveryId'] = params['delivery_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delivery/{deliveryId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Delivery',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
