#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, Union, List, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = "Generic stream"

    @property
    def stream_id(self) -> None:
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id: str) -> None:
        self._stream_id: str = stream_id

    @property
    def stream_type(self) -> str:
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type: str) -> None:
        self._stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered_data = self.filter_data(data_batch)
        total_val_count, total_tmp, avg_tmp, n = 0, 0, 0, 0
        for data in filtered_data:
            type, value = data.split(":", 1)
            match type:
                case "temp":
                    total_tmp += float(value)
                    total_val_count += 1
                    n += 1
                case "pressure":
                    n += 1
                case "humidity":
                    n += 1
        if total_val_count:
            avg_tmp = total_tmp / total_val_count
        return f"{n} readings processed, avg. temp: {avg_tmp}°C"

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data = []
        if not criteria:
            criteria = ["temp", "pressure", "humidity"]
        for data in data_batch:
            try:
                type, value = data.split(":", 1)
                if type not in criteria:
                    raise ValueError
                float(value)
                filtered_data.append(data)
            except (ValueError, TypeError):
                continue
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"name": "Sensor Stream",
                "stream_id": self.stream_id,
                "stream_type": "Environmental Data",
                "data_type": "Sensor data"}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered_data = self.filter_data(data_batch)
        net_flow, n = 0, 0
        for data in filtered_data:
            action, value = data.split(":", 1)
            match action:
                case "buy":
                    net_flow += int(value)
                    n += 1
                case "sell":
                    net_flow -= int(value)
                    n += 1
        return (f"{n} operations, " + "net flow {0:+} units".format(net_flow))

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data = []
        if not criteria:
            criteria = ["buy", "sell"]
        for data in data_batch:
            try:
                type, value = data.split(":", 1)
                if type not in criteria:
                    raise ValueError
                int(value)
                filtered_data.append(data)
            except (ValueError, TypeError):
                continue
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"name": "Transaction Stream",
                "stream_id": self.stream_id,
                "stream_type": "Financial Data",
                "data_type": "Transaction data"}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered_data = self.filter_data(data_batch)
        err_count, n = 0, 0
        for data in filtered_data:
            match data:
                case "error":
                    err_count += 1
                    n += 1
                case "login":
                    n += 1
                case "logout":
                    n += 1
        return (f"{n} events, {err_count} error"
                f"{'' if err_count < 2 else 's'} detected")

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data = []
        if not criteria:
            criteria = ["error", "login", "logout"]
        for data in data_batch:
            try:
                if data not in criteria:
                    raise ValueError
                filtered_data.append(data)
            except (ValueError, TypeError):
                continue
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"name": "Event Stream",
                "stream_id": self.stream_id,
                "stream_type": "System Events",
                "data_type": "Event data"}


class StreamProcessor:
    @staticmethod
    def process_stream_batch(streams: List[DataStream],
                             data: List[Any]) -> None:
        try:
            for s in streams:
                result = s.process_batch(data)
                print(f"- {s.get_stats().get('data_type')}: {result}")
        except Exception as e:
            print(f"Error processing stream "
                  f"{s.get_stats().get('stream_id')}: {e}")

    def filter_stream_batch(streams: List[DataStream],
                            data_batch: List[Any]) -> None:
        print("Stream filtering active: High-priority data only")
        crit_alerts, large_trans = 0, 0
        for s in streams:
            data = s.filter_data(data_batch)
            if s.get_stats().get("name") == "Event Stream":
                for d in data:
                    if d == "error":
                        crit_alerts += 1
            if s.get_stats().get("name") == "Transaction Stream":
                for d in data:
                    if int(d.split(":")[1]) > 150:
                        large_trans += 1
        return (f"{crit_alerts} critical sensor alerts, "
                f"{large_trans} large transaction"
                f"{'' if large_trans < 2 else 's'}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensors = [SensorStream("SENSOR_001"),
               TransactionStream("TRANS_001"),
               EventStream("EVENT_001")]
    data_batches = [["temp:22.5", "humidity:65", "pressure:1013", "temp:23.5"],
                    ["buy:100", "sell:150", "buy:75"],
                    ["login", "error", "logout"]]

    for sensor, data in zip(sensors, data_batches):
        print(f"Initializing {sensor.get_stats().get('name')}")
        print(f"Stream ID: {sensor.get_stats().get('stream_id')}, "
              f"Type: {sensor.get_stats().get('stream_type')}")
        print(f"Processing sensor batch: [{', '.join(data)}]")
        print(f"Sensor analysis: {sensor.process_batch(data)}")
        print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed streams types through unified interface...\n")

    streams = [SensorStream("SENSOR_002"),
               TransactionStream("TRANS_002"),
               EventStream("EVENT_002")]
    data = ["temp:23.5", "logout", "error", "sell:200",
            "buy:100", "login", "temp:24.5", "error",
            "buy:50", "humidity:70"]

    print("Batch 1 results:")
    StreamProcessor.process_stream_batch(streams, data)
    print()

    print(f"Filtered results: "
          f"{StreamProcessor.filter_stream_batch(streams, data)}")

    print("\nAll streams processed successfully. Nexus throughput optimal")
