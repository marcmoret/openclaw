# Clean Session Architecture Guide

## Overview

This document provides a comprehensive guide to the clean session architecture for the LiveKit voice agent system. The architecture uses a **Modular Component + Builder Pattern** with focused, single-responsibility components.

## Architecture Principles

### **Single Responsibility**
Each component handles ONE clear purpose:
- **Participant** → Phone numbers and connection handling
- **Data** → Dynamic data fetching and configuration processing
- **Audio** → Audio components and room options setup
- **Agents** → Agent creation and selection logic
- **Lifecycle** → Event handling, cleanup, and resource management
- **Observability** → Session monitoring, Langfuse tracking, and metrics collection

### **Separation of Concerns**
- Builder orchestrates components without business logic
- Components are isolated and testable independently
- Configuration is layered and predictable

### **Fluent Interface**
- Method chaining for readable configuration
- Preset methods for common use cases
- Type-safe configuration options

## Architecture Structure

```
src/session/
├── __init__.py                # Public interface exports (SessionBuilder, SessionResult)
├── components/                # Focused components
│   ├── participant.py        # Participant initialization & phone numbers
│   ├── data.py              # Dynamic data fetching & configuration
│   ├── audio.py             # Audio components & room options
│   ├── agents.py            # Agent creation & management
│   ├── lifecycle.py         # Event handling & cleanup
│   └── observability.py     # Session monitoring & Langfuse tracking
├── builder.py               # Main session builder with fluent API
└── config.py                # Session result model
```

## Component Details

### **ParticipantManager** (`components/participant.py`)
**Responsibility**: Handle participant connection and phone number extraction

```python
class ParticipantManager:
    def __init__(self, ctx: JobContext)
    async def initialize(self) -> None
    def get_phone_numbers(self) -> Tuple[str, Optional[str]]
```

**What it handles:**
- Wait for participant connection
- Extract caller phone number (SIP vs non-SIP)
- Extract inbound phone number from trunk
- Use configuration constants for defaults

### **DataManager** (`components/data.py`)
**Responsibility**: Fetch and manage dynamic data and configuration

```python
class DataManager:
    def __init__(self, session_id: str)
    async def initialize(self, caller_phone: str, inbound_phone: Optional[str]) -> None
    def is_data_fetched(self) -> bool
    def get_language_config(self) -> Dict[str, Any]
    def get_clinic_config(self) -> Dict[str, Any]
    def get_dynamic_data(self) -> Optional[DynamicData]
```

**What it handles:**
- Fetch dynamic data from AI service
- Extract language from dynamic data (single source of truth)
- Process clinic configuration based on language
- Handle configuration processing for agents

### **AudioManager** (`components/audio.py`)
**Responsibility**: Create audio components and room options

```python
class AudioManager:
    def __init__(self)
    def create_background_player(self, ambient_volume: float = 0.5, thinking_volume: float = 0.2) -> BackgroundAudioPlayer
    def create_room_options(self, job_context: JobContext, language_config: Dict, noise_cancellation_type: str = "bvc_telephony") -> tuple[RoomInputOptions, RoomOutputOptions]
    def get_background_player(self) -> Optional[BackgroundAudioPlayer]
    def get_room_options(self) -> tuple[Optional[RoomInputOptions], Optional[RoomOutputOptions]]
```

**What it handles:**
- Create background audio player with configurable ambient and thinking volumes
- Setup room input/output options with noise cancellation
- Handle different noise cancellation types (NC, BVC, BVC_Telephony)
- Store and provide access to created audio components

### **AgentsManager** (`components/agents.py`)
**Responsibility**: Create and configure agents

```python
class AgentsManager:
    def __init__(self)
    def create_agents(self, call_context: CallContext, language_config: Dict, ctx: JobContext) -> Dict[AgentName, Callable[[], BaseAgent]]
    def determine_first_agent(self, is_dynamic_data_fetched: bool, language_config: Dict, userdata: UserData) -> Agent
    def get_agents(self) -> Dict[AgentName, Callable[[], BaseAgent]]
    def get_first_agent(self) -> Optional[Agent]
```

**What it handles:**
- Process agent configurations from language config using `resolve_agent_config`
- Create lazy-loaded agent factories using `create_call_agents`
- Determine which agent runs first based on data fetch status and config
- Handle different agent types (standard, OmniMed, technical issue)
- Store agents in UserData for access by other components

### **LifecycleManager** (`components/lifecycle.py`)
**Responsibility**: Handle session lifecycle and events

```python
class LifecycleManager:
    def __init__(self, ctx: JobContext, session_id: str, started_at: datetime)
    def setup_turn_tracking(self, agent_session: AgentSession, language_config: Dict) -> None
    def setup_event_handlers(self, agent_session: AgentSession) -> None
```

**What it handles:**
- Setup turn tracking and silence detection
- Handle participant disconnection events
- Setup shutdown callbacks and cleanup
- Manage egress recording lifecycle

### **SessionObserver** (`components/observability.py`)
**Responsibility**: Handle session observability and metrics tracking

```python
class SessionObserver:
    def __init__(self, session_id: str, job_ctx: JobContext, session: AgentSession)
    def track_custom_event(self, name: str, input_data: Optional[Dict] = None,
                          output_data: Optional[Dict] = None, metadata: Optional[Dict] = None) -> None
    def add_session_metadata(self, metadata: Dict[str, Any]) -> None
```

**What it handles:**
- Initialize Langfuse tracing and observability
- Track session metadata (environment, language, participants, phone numbers)
- Monitor LLM, TTS, STT, VAD, and EOU metrics automatically
- Handle agent state changes and conversation events
- Provide custom event tracking capability
- Integrate with LiveKit metrics collection system
- Support custom observability events for external tracking

## Configuration System

### **Layered Configuration**
The system uses a layered configuration approach:

1. **Global Defaults** → `src/configs/config.py` - System-wide defaults
2. **Presets** → `src/utils/session_loader.py` - "default", "french", "openai_realtime"
3. **Dynamic Config** → language_config from dynamic data - Per-clinic/language settings
4. **Runtime Overrides** → SessionBuilder fluent interface - Method chaining customization

### **SessionResult Model**
```python
@dataclass
class SessionResult:
    agent_session: AgentSession[UserData]      # Main session with userdata
    first_agent: Agent                          # Agent to start with
    room_input_options: RoomInputOptions        # Audio input configuration
    room_output_options: RoomOutputOptions      # Audio output configuration
    background_audio_player: BackgroundAudioPlayer  # Ambient/thinking sounds
    lifecycle_manager: LifecycleManager         # Event handling and cleanup
    session_observer: SessionObserver           # Observability and metrics tracking
```

## SessionBuilder Interface

### **Main Builder Class**
```python
class SessionBuilder:
    def __init__(self, ctx: JobContext, session_id: str, started_at: datetime)

    # Configuration methods (fluent interface)
    def with_preset(self, preset_name: str) -> 'SessionBuilder'
    def with_audio_settings(self, ambient_volume: float = 0.5,
                          thinking_volume: float = 0.2,
                          noise_cancellation: str = "bvc_telephony") -> 'SessionBuilder'

    # Preset factory methods
    @classmethod
    def create_default(cls, ctx, session_id, started_at) -> 'SessionBuilder'

    @classmethod
    def create_french(cls, ctx, session_id, started_at) -> 'SessionBuilder'

    # Main build method
    async def build(self) -> SessionResult
```

### **Build Process Flow**
1. **Initialize participant** → Get participant and phone numbers
2. **Fetch dynamic data** → Get clinic configuration and settings
3. **Create agent session** → UserData, LiveKit session with LLM/STT/TTS
4. **Setup audio** → Background player and room options
5. **Create agents** → All available agents for the session
6. **Setup lifecycle** → Turn tracking, event handlers and cleanup
7. **Initialize observability** → SessionObserver for Langfuse tracking and metrics
8. **Return result** → Complete session components

## Usage Patterns

### **Primary Usage (Recommended)**
```python
from src.session import SessionBuilder

# Create session with default configuration
result = await SessionBuilder.create_default(ctx, session_id, started_at).build()

# Extract components
agent_session = result.agent_session
first_agent = result.first_agent
room_input_options = result.room_input_options
room_output_options = result.room_output_options
background_audio_player = result.background_audio_player
lifecycle_manager = result.lifecycle_manager
session_observer = result.session_observer

# Optional: Add custom observability events
if session_observer:
    session_observer.track_custom_event("session_started", {"custom_data": "value"})
```

### **Advanced Usage (Custom Configuration)**
```python
# French with custom audio settings
result = await (SessionBuilder.create_french(ctx, session_id, started_at)
    .with_audio_settings(ambient_volume=0.3, thinking_volume=0.1)
    .build())

# Full customization
result = await (SessionBuilder(ctx, session_id, started_at)
    .with_preset("french")
    .with_audio_settings(noise_cancellation="nc")
    .build())
```

### **Migration from Legacy Interface**
```python
# Legacy interface (still available)
from src.utils.session_utils import setup_session_components_and_handlers

components = await setup_session_components_and_handlers(ctx, session_id, started_at)
(agent_session, first_agent, room_input, room_output, bg_audio, turn_tracker) = components

# Modern SessionBuilder (recommended)
from src.session import SessionBuilder
result = await SessionBuilder.create_default(ctx, session_id, started_at).build()
```

## Integration Points

### **Main Entry Point**
The session builder integrates with `main.py` entry point:
```python
from src.session import SessionBuilder

# Create session using the clean architecture
result = await SessionBuilder.create_default(ctx, session_id, started_at).build()
```

### **Key Dependencies**
- **`src/models/context.py`** - UserData and CallContext models
- **`src/utils/session_loader.py`** - Dynamic service loading and presets
- **`src/agents/__init__.py`** - Agent factory and creation system
- **`src/services/ai_service.py`** - Dynamic data and configuration fetching
- **`src/configs/config.py`** - Global configuration defaults

## Development Guidelines

### **✅ Do This**
- Use `SessionBuilder.create_default()` for standard English sessions
- Use `SessionBuilder.create_french()` for French sessions
- Use fluent interface for custom configuration
- Handle the complete `SessionResult` tuple properly
- Add new configuration via the layered system

### **❌ Avoid This**
- Don't bypass the builder - always use SessionBuilder
- Don't modify components directly - use the fluent interface
- Don't create new SessionConfig classes - extend the existing layers
- Don't forget to handle lifecycle management properly

## Testing Strategy

- **Unit Tests**: Each component can be tested independently with mocked dependencies
- **Integration Tests**: End-to-end session creation and component interaction
- **Mock Strategy**: Mock JobContext, AI service, and external dependencies
- **Component Isolation**: Test component logic without builder complexity

## Error Handling

- **Component Level**: Each component handles its own errors gracefully
- **Builder Level**: Aggregates and reports configuration issues
- **Fallback Strategy**: Technical issue agent on critical failures
- **Validation**: Assertions ensure all required components are created

## Logging

- **Session Context**: All logs include session_id for tracing
- **Component Prefixes**: Clear log prefixes for debugging specific components
- **Error Tracking**: Full stack traces with context information
