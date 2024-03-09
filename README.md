# matter-device

## 编译chip-tool
```
cd connectedhomeip
scripts/examples/gn_build_example.sh examples/chip-tool chipTool/
```
## 运行自动化测试
* 集成和认证测试 — Matter 文档 --- Integration and Certification Tests — Matter documentation (project-chip.github.io)
* 编译安装chip python库
    * connectedhomeip/docs/guides/python_chip_controller_building.md at master · project-chip/connectedhomeip (github.com)
    * connectedhomeip/docs/guides/matter-repl.md at master · project-chip/connectedhomeip (github.com)
    * scripts/build_python.sh -m platform -i separate
    * source separate/bin/activate
    * sudo  separate/bin/chip-repl 
* 运行自动测试
    * python框架
        * source separate/bin/activate
        * scripts/run_in_python_env.sh out/venv './scripts/tests/run_python_test.py --script src/python_testing/TC_RVCCLEANM_1_2.py --script-args "--storage-path admin_storage.json --commissioning-method on-network --discriminator 3840 --passcode 20202021 --PICS examples/rvc-app/rvc-common/pics/rvc-app-pics-values --endpoint=1"'
        * ./scripts/tests/run_python_test.py --script src/python_testing/TC_RVCCLEANM_1_2.py --script-args "--storage-path admin_storage.json --PICS examples/rvc-app/rvc-common/pics/rvc-app-pics-values --endpoint=1"
        * ./scripts/tests/run_python_test.py --app /home/xuesong/workdir/matter-device/rvc-app/out/chip-rvc-app --factoryreset --app-args "--KVS data/chip_kvs" --script src/python_testing/TC_RVCCLEANM_1_2.py --script-args "--storage-path admin_storage.json --commissioning-method on-network --discriminator 3840 --passcode 20202021 --PICS examples/rvc-app/rvc-common/pics/rvc-app-pics-values --endpoint=1"
    * yaml框架
        * 切root用户
        * source separate/bin/activate
        * 先使用chip-tool配网，./scripts/tests/yaml/chiptool.py tests Test_TC_OO_2_1 --server_path ./out/linux-x64-chip-tool/chip-tool -- nodeId 0x12344321
        * ./examples/rvc-app/run_all_yaml_tests.sh 0x12345678
