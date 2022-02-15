# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class EventRoutesOperations:
    """EventRoutesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.digitaltwins.core.models
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

    def list(
        self,
        event_routes_list_options: Optional["_models.EventRoutesListOptions"] = None,
        **kwargs
    ) -> AsyncIterable["_models.EventRouteCollection"]:
        """Retrieves all event routes.
        Status codes:


        * 200 OK.

        :param event_routes_list_options: Parameter group.
        :type event_routes_list_options: ~azure.digitaltwins.core.models.EventRoutesListOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either EventRouteCollection or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.digitaltwins.core.models.EventRouteCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EventRouteCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _traceparent = None
        _tracestate = None
        _max_items_per_page = None
        if event_routes_list_options is not None:
            _traceparent = event_routes_list_options.traceparent
            _tracestate = event_routes_list_options.tracestate
            _max_items_per_page = event_routes_list_options.max_items_per_page
        api_version = self._config.api_version
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            if _traceparent is not None:
                header_parameters['traceparent'] = self._serialize.header("traceparent", _traceparent, 'str')
            if _tracestate is not None:
                header_parameters['tracestate'] = self._serialize.header("tracestate", _tracestate, 'str')
            if _max_items_per_page is not None:
                header_parameters['max-items-per-page'] = self._serialize.header("max_items_per_page", _max_items_per_page, 'int')
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('EventRouteCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/eventroutes'}  # type: ignore

    async def get_by_id(
        self,
        id: str,
        event_routes_get_by_id_options: Optional["_models.EventRoutesGetByIdOptions"] = None,
        **kwargs
    ) -> "_models.DigitalTwinsEventRoute":
        """Retrieves an event route.
        Status codes:


        * 200 OK
        * 404 Not Found

          * EventRouteNotFound - The event route was not found.

        :param id: The id for an event route. The id is unique within event routes and case sensitive.
        :type id: str
        :param event_routes_get_by_id_options: Parameter group.
        :type event_routes_get_by_id_options: ~azure.digitaltwins.core.models.EventRoutesGetByIdOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DigitalTwinsEventRoute, or the result of cls(response)
        :rtype: ~azure.digitaltwins.core.models.DigitalTwinsEventRoute
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DigitalTwinsEventRoute"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _traceparent = None
        _tracestate = None
        if event_routes_get_by_id_options is not None:
            _traceparent = event_routes_get_by_id_options.traceparent
            _tracestate = event_routes_get_by_id_options.tracestate
        api_version = self._config.api_version
        accept = "application/json"

        # Construct URL
        url = self.get_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", _traceparent, 'str')
        if _tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", _tracestate, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DigitalTwinsEventRoute', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_by_id.metadata = {'url': '/eventroutes/{id}'}  # type: ignore

    async def add(
        self,
        id: str,
        event_route: Optional["_models.DigitalTwinsEventRoute"] = None,
        event_routes_add_options: Optional["_models.EventRoutesAddOptions"] = None,
        **kwargs
    ) -> None:
        """Adds or replaces an event route.
        Status codes:


        * 204 No Content
        * 400 Bad Request

          * EventRouteEndpointInvalid - The endpoint provided does not exist or is not active.
          * EventRouteFilterInvalid - The event route filter is invalid.
          * EventRouteIdInvalid - The event route id is invalid.
          * LimitExceeded - The maximum number of event routes allowed has been reached.

        :param id: The id for an event route. The id is unique within event routes and case sensitive.
        :type id: str
        :param event_route: The event route data.
        :type event_route: ~azure.digitaltwins.core.models.DigitalTwinsEventRoute
        :param event_routes_add_options: Parameter group.
        :type event_routes_add_options: ~azure.digitaltwins.core.models.EventRoutesAddOptions
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
        
        _traceparent = None
        _tracestate = None
        if event_routes_add_options is not None:
            _traceparent = event_routes_add_options.traceparent
            _tracestate = event_routes_add_options.tracestate
        api_version = self._config.api_version
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.add.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", _traceparent, 'str')
        if _tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", _tracestate, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if event_route is not None:
            body_content = self._serialize.body(event_route, 'DigitalTwinsEventRoute')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    add.metadata = {'url': '/eventroutes/{id}'}  # type: ignore

    async def delete(
        self,
        id: str,
        event_routes_delete_options: Optional["_models.EventRoutesDeleteOptions"] = None,
        **kwargs
    ) -> None:
        """Deletes an event route.
        Status codes:


        * 204 No Content
        * 404 Not Found

          * EventRouteNotFound - The event route was not found.

        :param id: The id for an event route. The id is unique within event routes and case sensitive.
        :type id: str
        :param event_routes_delete_options: Parameter group.
        :type event_routes_delete_options: ~azure.digitaltwins.core.models.EventRoutesDeleteOptions
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
        
        _traceparent = None
        _tracestate = None
        if event_routes_delete_options is not None:
            _traceparent = event_routes_delete_options.traceparent
            _tracestate = event_routes_delete_options.tracestate
        api_version = self._config.api_version
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", _traceparent, 'str')
        if _tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", _tracestate, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/eventroutes/{id}'}  # type: ignore
