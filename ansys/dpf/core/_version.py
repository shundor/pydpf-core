"""Version for ansys-dpf-core"""
# major, minor, patch
version_info = 0, 5, "dev2"
# Nice string for the version
__version__ = ".".join(map(str, version_info))
__ansys_version__ = "222"
min_server_version = "2.0"

server_to_ansys_grpc_dpf_version = {
    "1.0": "==0.2.2",
    "2.0": "==0.3.0",
    "3.0": ">=0.4.0",
    "4.0": ">=0.5.0",
}

server_to_ansys_version = {
    "1.0": "2021R1",
    "2.0": "2021R2",
    "3.0": "2022R1",
    "4.0": "2022R2",
}
