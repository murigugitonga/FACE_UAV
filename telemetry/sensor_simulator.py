# Telemetry & EW fault Injection Service (PSSS)

import time
import random
import zmq
import numpy as np

# import the auto-generated flatBuffers Python bindings
import generated.ResilientUAV.TSS.SensorType as SensorType
import generated.ResilientUAV.TSS.Vector3 as Vector3
import generated.ResilientUAV.TSS.IMUPayload as IMUPayload
import generated.ResilientUAV.TSS.GNSSPayload as GNSSPayload
import generated.ResilientUAV.TSS.VisualTrackPayload as VisualTrackPayload
import generated.ResilientUAV.TSS.TelemetryMessage as TelemetryMessage
import flatBuffers

def create_vector3(builder, x,y,z):
    """Helper function to pack the fixed-size Vector3 struct."""
    return Vector3.CreateVector3(builder, x, y,z)

def main():
     """Initialize ZeroMQ context and PUB socket (Brokerless TSS fabric)"""
     ctx = zmq.Context()
     socket = ctx.socket(zmq.PUB)

     # Bind to TCP socket (open to configuration via environment variables or k8s service meshes)
     bind_address = "tcp://*:5555"
     socket.bind(bind_address)
     print(f"[PSSS] Telemetry Service active. Broadcasting on {bind_address}...")

     message_id = 00
     entity_id = 0xAF01 # UAV Alpha-01 identifier

     #Baseline trajectory state (Simulating NRB co-ordinates origin as baseline)
     base_lat = 1.23367
     base_lon = 36.8219
     base_alt = 1500.0

     try:
        while True:
            start_tome = time.time()
            message_id  += 1
            timestamp_ms =  int(time.time() * 1000)

            # Initialize Flatbuffers builder (initial size 1024 bytes)
            builder = flatbuffers.Builder(1024)

            # Randomly interleave sensor types based on multi-frequency weighting
            # IMU @ 100Hz (frequent), Visual @ 30Hz, GNSS @5Hz (infrequent)
            choice = random.random()

            if choice < 0.65:
                
