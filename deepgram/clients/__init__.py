# Copyright 2023-2024 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

# common
from .common import (
    TextSource,
    BufferSource,
    StreamSource,
    FileSource,
    UrlSource,
    Sentiment,
)
from .listen import (
    OpenResponse,
    MetadataResponse,
    CloseResponse,
    UnhandledResponse,
    ErrorResponse,
)

from .listen_router import Listen
from .read_router import Read
from .speak_router import Speak

# listen
from .listen import LiveTranscriptionEvents

## backward compat
from .prerecorded import (
    PreRecordedClient,
    AsyncPreRecordedClient,
)
from .live import (
    LiveClient,
    AsyncLiveClient,
)

# rest
## input
from .listen import (
    PrerecordedOptions,
    PreRecordedStreamSource,
    # UrlSource,
    # FileSource,
    PrerecordedSource,
)

## output
from .listen import (
    AsyncPrerecordedResponse,
    PrerecordedResponse,
    SyncPrerecordedResponse,
)


# websocket
## input
from .listen import (
    LiveOptions,
)

## output
from .listen import (
    # OpenResponse,
    LiveResultResponse,
    # MetadataResponse,
    SpeechStartedResponse,
    UtteranceEndResponse,
    # CloseResponse,
    # ErrorResponse,
    # UnhandledResponse,
)

## clients
from .listen import (
    ListenWebSocketClient,
    AsyncListenWebSocketClient,
)


# read
from .analyze import ReadClient, AsyncReadClient
from .analyze import AnalyzeClient, AsyncAnalyzeClient
from .analyze import AnalyzeOptions
from .analyze import (
    AnalyzeStreamSource,
    AnalyzeSource,
)
from .analyze import (
    AsyncAnalyzeResponse,
    AnalyzeResponse,
    SyncAnalyzeResponse,
)

# speak
## common
from .speak import (
    SpeakOptions,
    # FileSource,
    SpeakWebSocketSource,
    SpeakSource,
)

from .speak import SpeakWebSocketEvents

## speak REST
from .speak import (
    SpeakClient,  # backward compat
    SpeakRESTClient,
    AsyncSpeakRESTClient,
)

from .speak import (
    SpeakResponse,  # backward compat
    SpeakRESTResponse,
)

## speak WebSocket
from .speak import (
    SpeakWebSocketClient,
    AsyncSpeakWebSocketClient,
)
from .speak import (
    SpeakWebSocketResponse,
    # OpenResponse,
    # MetadataResponse,
    FlushedResponse,
    # CloseResponse,
    # UnhandledResponse,
    WarningResponse,
    # ErrorResponse,
)

# manage
from .manage import ManageClient, AsyncManageClient
from .manage import (
    ProjectOptions,
    KeyOptions,
    ScopeOptions,
    InviteOptions,
    UsageRequestOptions,
    UsageSummaryOptions,
    UsageFieldsOptions,
)
from .manage import (
    Message,
    Project,
    ProjectsResponse,
    MembersResponse,
    Key,
    KeyResponse,
    KeysResponse,
    ScopesResponse,
    InvitesResponse,
    UsageRequest,
    UsageRequestsResponse,
    UsageSummaryResponse,
    UsageFieldsResponse,
    Balance,
    BalancesResponse,
)

# selfhosted
from .selfhosted import (
    OnPremClient,
    AsyncOnPremClient,
    SelfHostedClient,
    AsyncSelfHostedClient,
)
