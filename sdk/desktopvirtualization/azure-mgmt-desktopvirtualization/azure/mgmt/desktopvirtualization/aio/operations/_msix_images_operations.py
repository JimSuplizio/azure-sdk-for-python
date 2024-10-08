# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._msix_images_operations import build_expand_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MsixImagesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.desktopvirtualization.aio.DesktopVirtualizationMgmtClient`'s
        :attr:`msix_images` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def expand(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_image_uri: _models.MSIXImageURI,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncIterable["_models.ExpandMsixImage"]:
        """Expands and Lists MSIX packages in an Image, given the Image Path.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_image_uri: Object containing URI to MSIX Image. Required.
        :type msix_image_uri: ~azure.mgmt.desktopvirtualization.models.MSIXImageURI
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either ExpandMsixImage or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.desktopvirtualization.models.ExpandMsixImage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def expand(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_image_uri: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncIterable["_models.ExpandMsixImage"]:
        """Expands and Lists MSIX packages in an Image, given the Image Path.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_image_uri: Object containing URI to MSIX Image. Required.
        :type msix_image_uri: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either ExpandMsixImage or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.desktopvirtualization.models.ExpandMsixImage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def expand(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_image_uri: Union[_models.MSIXImageURI, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterable["_models.ExpandMsixImage"]:
        """Expands and Lists MSIX packages in an Image, given the Image Path.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_image_uri: Object containing URI to MSIX Image. Is either a MSIXImageURI type or a
         IO[bytes] type. Required.
        :type msix_image_uri: ~azure.mgmt.desktopvirtualization.models.MSIXImageURI or IO[bytes]
        :return: An iterator like instance of either ExpandMsixImage or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.desktopvirtualization.models.ExpandMsixImage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ExpandMsixImageList] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(msix_image_uri, (IOBase, bytes)):
            _content = msix_image_uri
        else:
            _json = self._serialize.body(msix_image_uri, "MSIXImageURI")

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_expand_request(
                    resource_group_name=resource_group_name,
                    host_pool_name=host_pool_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    content_type=content_type,
                    json=_json,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ExpandMsixImageList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)
