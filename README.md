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

## MOSA & FACE Capability Mapping

| FACE Architectural Segment | Project Module | Technical Function | 
| :--- | :--- | :--- |
| **Transport Services Segment (TSS)** | ZeroMQ + FlatBuffers | Low-overhead IPC bus & zero-copy binary layout contract |
| **Portable Component Segment (PCS)** | C++ Core Engine | Deterministic lock-free ingestion & out-of-order temporal fusion |
| **Platform-Specific Services Segment (PSSS)** | Python Service | High-rate multi-sensor emulation & programmatic EW fault injection |
| **Human-Machine Interface (HMI)** | React / Canvas UI | High-fidelity C2 tracking matrix & telemetry divergence rendering |

## Deliverables & Progress Tracking

- [x] **Phase 0: Architecture & Environment Setup**
    - [x] Core stack definition & repo boilerplate setup
    - [x] Containerization framework setup.
    - [x] Github codespaces development container configuration.
    - [x] Baseline project README and system specification brief.
- [ ] **Phase 1: Binary Data Contract(TSS)**
    - [] Write unified `schema\telemetry.fbs` Flatbuffers schema.
    - [] Compile language bindings for C++, Python & Typescript.
- [ ] **Phase 2: Telemetry & EW Fault Tolerance**
    - [] Implement asynchronous multi-sensor generator (IMU @ 100Hz, GNSS @ 5Hz Visual Tracker @30Hz).
    - [] Implement Gaussian noise & EW transport disruption controller (ZeroMQ publisher).
- [ ] **Phase 3: High-Frequency Processing Engine (PCS)**
    - [] Implement  C++ single-producer single-consumer (SPSC) lock-free ring buffer.
    - [] Develop zero-copy ZMQ receiver thread.
    - [] Build temporal out-of-order alignment engine & state fusion processor.

- [ ] **Phase 4: Real-Time C2 Dashboard (HMI)**
    - [] Build lightweight ZMQ-to-websocket bridge.
    - [] Develop React 19 + Typescript real-time tactical canvas engine.
    - [] Implement Ground Truth vs. Estimated Edge Trail comparative UI Overlay.

- [ ] **Phase 5: Distributed System Verification**
    - [] Execute Docker-Compose & Kubernetes cluster deployment tests.
    - [] Benchmark fusion latency and memory footprint under severe simulated DDIL loss.

## Firing this up in Github Codespaces

```bash
 # Verify build toolchain
 g++ --version && flatc --version && cmake --version

 # Build C++ Core Engine (Post-Phase 1-3)
 mkdir -p core/build && cd core/build
 cmake .. && make -j&(nproc)

 # Launch Telemetry Generator
 python3 telemetry/sensor_simulator.py

 ```
 

