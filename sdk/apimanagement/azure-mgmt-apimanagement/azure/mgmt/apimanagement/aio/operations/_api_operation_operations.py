# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._api_operation_operations import build_create_or_update_request, build_delete_request, build_get_entity_tag_request, build_get_request, build_list_by_api_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ApiOperationOperations:
    """ApiOperationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~api_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_api(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        tags: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.OperationCollection"]:
        """Lists a collection of the operations for the specified API.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :type api_id: str
        :param filter: |     Field     |     Usage     |     Supported operators     |     Supported
         functions     |</br>|-------------|-------------|-------------|-------------|</br>| name |
         filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |</br>|
         displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith
         |</br>| method | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith
         |</br>| description | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith,
         endswith |</br>| urlTemplate | filter | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |</br>.
        :type filter: str
        :param top: Number of records to return.
        :type top: int
        :param skip: Number of records to skip.
        :type skip: int
        :param tags: Include tags in the response.
        :type tags: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either OperationCollection or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~api_management_client.models.OperationCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OperationCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_api_request(
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    api_id=api_id,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    skip=skip,
                    tags=tags,
                    template_url=self.list_by_api.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_api_request(
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    api_id=api_id,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    skip=skip,
                    tags=tags,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("OperationCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_api.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations'}  # type: ignore

    @distributed_trace_async
    async def get_entity_tag(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        **kwargs: Any
    ) -> bool:
        """Gets the entity state (Etag) version of the API operation specified by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_entity_tag_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            template_url=self.get_entity_tag.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))


        if cls:
            return cls(pipeline_response, None, response_headers)
        return 200 <= response.status_code <= 299

    get_entity_tag.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        **kwargs: Any
    ) -> "_models.OperationContract":
        """Gets the details of the API Operation specified by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OperationContract, or the result of cls(response)
        :rtype: ~api_management_client.models.OperationContract
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OperationContract"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))

        deserialized = self._deserialize('OperationContract', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}'}  # type: ignore


    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        parameters: "_models.OperationContract",
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.OperationContract":
        """Creates a new operation in the API or updates an existing one.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance.
        :type operation_id: str
        :param parameters: Create parameters.
        :type parameters: ~api_management_client.models.OperationContract
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OperationContract, or the result of cls(response)
        :rtype: ~api_management_client.models.OperationContract
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OperationContract"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'OperationContract')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
            
            deserialized = self._deserialize('OperationContract', pipeline_response)

        if response.status_code == 201:
            response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
            
            deserialized = self._deserialize('OperationContract', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        if_match: str,
        parameters: "_models.OperationUpdateContract",
        **kwargs: Any
    ) -> "_models.OperationContract":
        """Updates the details of the operation in the API specified by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance.
        :type operation_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update.
        :type if_match: str
        :param parameters: API Operation Update parameters.
        :type parameters: ~api_management_client.models.OperationUpdateContract
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OperationContract, or the result of cls(response)
        :rtype: ~api_management_client.models.OperationContract
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OperationContract"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'OperationUpdateContract')

        request = build_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            if_match=if_match,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))

        deserialized = self._deserialize('OperationContract', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        if_match: str,
        **kwargs: Any
    ) -> None:
        """Deletes the specified operation in the API.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance.
        :type operation_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}'}  # type: ignore

