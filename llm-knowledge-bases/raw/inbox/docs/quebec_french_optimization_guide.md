## Optimizing Voice Agent for Quebec French

This guide outlines recommendations for optimizing the LiveKit voice agent for natural and accurate conversations in Quebec French, particularly when deployed on AWS using Docker.

**Core Goal:** Achieve low latency, high-quality voice, and precise understanding of Quebec French, including its unique pronunciations, vocabulary, and colloquialisms.

### I. Component-Specific Recommendations

**A. Speech-to-Text (STT)**

*   **Challenge:** Accurately transcribing Quebec French (`Français québécois`).
*   **Priority:** Use services explicitly offering `fr-CA` (French - Canada) locale/language codes.
*   **Top Contenders & Actions:**
    1.  **Google Cloud Speech-to-Text (`fr-CA`):**
        *   Strong general language support, `fr-CA` specific models.
        *   Utilize `phone_call` model optimization if applicable.
        *   Explore model adaptation/custom vocabulary.
        *   **Action:** Primary candidate for testing.
    2.  **Deepgram (`fr-CA`):**
        *   Known for speed and real-time capabilities (e.g., Nova-2 model).
        *   **Action:** Strong secondary candidate for testing.
    3.  **AWS Transcribe (`fr-CA`):**
        *   Native AWS service, good for integration.
        *   **Action:** Test, especially if tight AWS integration is key.
    4.  **Microsoft Azure Speech Services (`fr-CA`):**
        *   Robust STT capabilities.
        *   **Action:** Evaluate as another alternative.
*   **Key:** Extensively test with diverse Quebec French audio samples.

**B. Text-to-Speech (TTS)**

*   **Challenge:** Generating a voice that sounds authentically Quebecois.
*   **Priority:** Listen to voice samples extensively.
*   **Top Contenders & Actions:**
    1.  **ElevenLabs:**
        *   Highly natural and emotive voices; multilingual models.
        *   Potential for voice cloning or finding/fine-tuning a Quebecois-like voice.
        *   **Action:** Top candidate if budget allows for premium quality and customization.
    2.  **Google Cloud Text-to-Speech (`fr-CA` WaveNet voices):**
        *   Very natural voices, specific `fr-CA` options.
        *   **Action:** Excellent, often more cost-effective, high-quality option.
    3.  **Microsoft Azure Speech Services (`fr-CA` neural voices):**
        *   Natural neural voices available.
        *   **Action:** Evaluate for authentic Quebecois sound.
    4.  **AWS Polly (`fr-CA` neural voices, e.g., "Chantal"):**
        *   Native AWS service.
        *   **Action:** Convenient, but compare naturalness against top-tier competitors.

**C. Voice Activity Detection (VAD)**

*   **Current Implementation:** `silero.VAD.load()`
*   **Recommendation:**
    *   **Stick with Silero VAD.** It's efficient, lightweight, and language-agnostic at its core.
    *   **Action:** Fine-tune its parameters (`min_speech_duration`, `min_silence_duration`, `activation_threshold`) based on testing with Quebec French speech patterns and rhythms.

**D. Turn Detection**

*   **Challenge:** Handling natural conversational flow specific to Quebec French.
*   **Top Recommendation:**
    1.  **LiveKit Turn Detector Plugin (`MultilingualModel`):**
        *   Adds contextual awareness (analyzes transcribed text) to VAD.
        *   Supports "French," which should cover many Quebecois linguistic cues when paired with a good `fr-CA` STT.
        *   **Action:** Implement this in conjunction with Silero VAD and your chosen `fr-CA` STT.
            ```python
            # Example AgentSession setup
            from livekit.plugins.turn_detector.multilingual import MultilingualModel
            from livekit.plugins import silero, your_chosen_stt # e.g., google_speech

            session = AgentSession(
                stt=your_chosen_stt.STT(language="fr-CA", ...), # Critical: STT must be fr-CA
                llm=llm,
                tts=tts,
                vad=silero.VAD.load(),
                turn_detection=MultilingualModel(),
                # ... other params
            )
            ```
        *   Ensure STT accurately reports/is set to `fr-CA` for the turn detector to function optimally.
*   **Alternative (Simpler but Less Sophisticated):**
    *   **VAD-Only with Tuned Endpointing:** If the `MultilingualModel` is not feasible, set `turn_detection="vad"` in `AgentSession` and meticulously tune `min_endpointing_delay` and `max_endpointing_delay` (if applicable without the turn detector). This will require extensive trial and error.

### II. Hardware & AWS Deployment (Dockerized)

*   **Container Orchestration:**
    *   **Recommendation:** Start with **Amazon ECS with Fargate** for simplicity and serverless management.
    *   **Alternative:** If more control or cost optimization at high scale is needed, consider **Amazon ECS with EC2 Instances.**
    *   **EKS:** Only if existing Kubernetes expertise/infrastructure justifies the overhead.
*   **Instance Types (for ECS with EC2 or EKS):**
    *   **CPU-Optimized:** Prioritize (e.g., AWS `c5.large`, `c6i.large`) as STT/TTS/Turn Detection are CPU-bound.
    *   **Memory:** Start with 4GB-8GB RAM per instance and monitor.
    *   **Network:** Ensure good network performance.
*   **Scaling:** Configure auto-scaling based on CPU utilization or active calls.
*   **Logging & Monitoring:** Utilize Amazon CloudWatch.

### III. Workflow Summary & Testing Strategy

1.  **Selection:** Choose STT (`fr-CA`), TTS (`fr-CA`), VAD (Silero), and Turn Detection (LiveKit `MultilingualModel`).
2.  **AWS Setup:** Deploy via Docker to ECS (Fargate recommended to start).
3.  **Rigorous Iterative Testing:**
    *   Engage native Quebec French speakers for testing.
    *   Cover diverse scenarios (short/long utterances, interruptions, noise).
    *   Collect detailed feedback on:
        *   Transcription accuracy (especially Quebecois nuances).
        *   TTS voice naturalness, accent, and intonation.
        *   Turn-taking smoothness (interruptions, delays).
        *   Overall conversation quality.
    *   Leverage Langfuse (or similar tools) to track metrics (latency, accuracy) for each component (STT, TTS, VAD event timing, turn detection effectiveness).

This iterative process of selection, deployment, testing, and fine-tuning is key to achieving a high-quality Quebec French voice agent. 