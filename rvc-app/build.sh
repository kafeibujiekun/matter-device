#!/bin/bash

source ../connectedhomeip/scripts/activate.sh

gn gen --check \
    --fail-on-unused-args \
    --export-compile-commands \
    --root=$PWD/linux \
    "--args=is_debug=true chip_config_network_layer_ble=false chip_inet_config_enable_ipv4=false" \
    $PWD/out

ninja -C out
