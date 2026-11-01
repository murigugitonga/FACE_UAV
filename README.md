# FACE_UAV SIMULATION

> **Unclassified // Non-ITAR Dual-Use Emulation Framework**
> Benchmarking low-latency, multi-domain edge telemetry ingestion and resilient data fusion under degraded environments


This project is a high-performance software-defined defense research platform that models, processes and visualizes real-time asynchronous multi-frequency telemetry streams. Grounded in **Modular Open Systems Approach(MOSA)** and **Future Airbone Capability Environment(FACE)** defence architectural principles.
The core objective is to evaluate how distributed edge systems retain situational awareness and state alignment when subjected to electronic warfare (EW) disruption, co-ordinate drift, and network packet loss.

## Tech Stack
* **Core Engine (PCS):** C++17/20 `std::atomic`, CMake, Zero-Allocation Lock-Free Buffers.
* **Telemetry & EW Injector (PSSS):** Python 3.10+, PyZMQ, NumPy (Gaussian drift & EW fault emulation).
* **Command & Control Dashboard (HMI):** React 19, Typescript, TailwindCSS, HTML5 Canvas API.
* **Transport Services (TSS):** ZeroMQ, Google Flatbuffers (`flatc`).
* **Containerization & Deployment:** Docker (Multi-stage), Kubernetes (K8s manifests).

## MOSA & FACE Capability Mappinh

| FACE Architectural Segment | Project Module | Technical Function | 
| :--- | :--- | :--- |
| **Transport Services Segment (TSS)** | ZeroMQ + FlatBuffers | Low-overhead IPC bus & zero-copy binary layout contract |
| **Portable Component Segment (PCS)** | C++ Core Engine | Deterministic lock-free ingestion & out-of-order temporal fusion |
| **Platform-Specific Services Segment (PSSS)** | Python Service | High-rate multi-sensor emulation & programmatic EW fault injection |
| **Human-Machine Interface (HMI)** | React / Canvas UI | High-fidelity C2 tracking matrix & telemetry divergence rendering |
