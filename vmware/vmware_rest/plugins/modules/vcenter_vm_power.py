#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_vm_power
short_description: Operate a boot, hard shutdown, hard reset or hard suspend on a
  guest.
description: Ask the vCenter to boot, force shutdown or force reset a guest. If you
  want to do a soft shutdown or a soft reset, you can use M(vmware.vmware_rest.vmware_vm_guest_power)
  instead.
options:
  session_timeout:
    description:
    - 'Timeout settings for client session. '
    - 'The maximal number of seconds for the whole operation including connection
      establishment, request sending and response. '
    - The default value is 300s.
    type: float
    version_added: 2.1.0
  state:
    choices:
    - reset
    - start
    - stop
    - suspend
    description: []
    required: true
    type: str
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter password
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
  vm:
    description:
    - Virtual machine identifier. This parameter is mandatory.
    required: true
    type: str
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 0.1.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
seealso:
- description: Issues a request to the guest operating system asking it to perform
    a soft shutdown, standby (suspend) or soft reboot
  module: vmware.vmware_rest.vcenter_vm_guest_power
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Turn the power of the VM on
  vmware.vmware_rest.vcenter_vm_power:
    state: start
    vm: '{{ test_vm1_info.id }}'

- name: Collect the list of the existing VM
  vmware.vmware_rest.vcenter_vm_info:
  register: existing_vms
  until: existing_vms is not failed

- name: Turn off the VM
  vmware.vmware_rest.vcenter_vm_power:
    state: stop
    vm: '{{ item.vm }}'
  with_items: '{{ existing_vms.value }}'
  ignore_errors: yes

- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    name: test_vm1
    guest_OS: RHEL_7_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
    disks:
    - type: SATA
      backing:
        type: VMDK_FILE
        vmdk_file: '[local] test_vm1/{{ disk_name }}.vmdk'
    - type: SATA
      new_vmdk:
        name: second_disk
        capacity: 32000000000
    cdroms:
    - type: SATA
      sata:
        bus: 0
        unit: 2
    nics:
    - backing:
        type: STANDARD_PORTGROUP
        network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM\
          \ Network') }}"

  register: my_vm

- name: Turn on the power of the VM
  vmware.vmware_rest.vcenter_vm_power:
    state: start
    vm: '{{ my_vm.id }}'

- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    name: test_vm1
    guest_OS: RHEL_7_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
    disks:
    - type: SATA
      backing:
        type: VMDK_FILE
        vmdk_file: '[local] test_vm1/{{ disk_name }}.vmdk'
    - type: SATA
      new_vmdk:
        name: second_disk
        capacity: 32000000000
    nics:
    - backing:
        type: STANDARD_PORTGROUP
        network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM\
          \ Network') }}"

  register: my_vm
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Turn off the VM
msg:
  description: Turn off the VM
  returned: On success
  sample: All items completed
  type: str
results:
  description: Turn off the VM
  returned: On success
  sample:
  - _ansible_item_label:
      cpu_count: 1
      memory_size_MiB: 128
      name: vCLS-64491da9-1543-4a2f-9555-af08b9aac1f9
      power_state: POWERED_OFF
      vm: vm-1024
    _ansible_no_log: 0
    ansible_loop_var: item
    changed: 0
    failed: 0
    invocation:
      module_args:
        session_timeout: null
        state: stop
        vcenter_hostname: vcenter.test
        vcenter_password: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
        vcenter_rest_log_file: null
        vcenter_username: administrator@vsphere.local
        vcenter_validate_certs: 0
        vm: vm-1024
    item:
      cpu_count: 1
      memory_size_MiB: 128
      name: vCLS-64491da9-1543-4a2f-9555-af08b9aac1f9
      power_state: POWERED_OFF
      vm: vm-1024
    value:
      error_type: ALREADY_IN_DESIRED_STATE
      messages:
      - args: []
        default_message: Virtual machine is already powered off.
        id: com.vmware.api.vcenter.vm.power.already_powered_off
      - args: []
        default_message: The attempted operation cannot be performed in the current
          state (Powered off).
        id: vmsg.InvalidPowerState.summary
  - _ansible_item_label:
      cpu_count: 1
      memory_size_MiB: 1080
      name: test_vm1
      power_state: POWERED_ON
      vm: vm-1025
    _ansible_no_log: 0
    ansible_loop_var: item
    changed: 0
    failed: 0
    invocation:
      module_args:
        session_timeout: null
        state: stop
        vcenter_hostname: vcenter.test
        vcenter_password: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
        vcenter_rest_log_file: null
        vcenter_username: administrator@vsphere.local
        vcenter_validate_certs: 0
        vm: vm-1025
    item:
      cpu_count: 1
      memory_size_MiB: 1080
      name: test_vm1
      power_state: POWERED_ON
      vm: vm-1025
    value: {}
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "suspend": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "start": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "stop": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "reset": {"query": {}, "body": {}, "path": {"vm": "vm"}},
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["state"] = {
        "required": True,
        "type": "str",
        "choices": ["reset", "start", "stop", "suspend"],
    }
    argument_spec["vm"] = {"required": True, "type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/power").format(**params)


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _reset(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["reset"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["reset"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}/power?action=reset")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}/power?action=reset"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "reset")


async def _start(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["start"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["start"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}/power?action=start")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}/power?action=start"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "start")


async def _stop(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["stop"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["stop"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}/power?action=stop")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}/power?action=stop"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "stop")


async def _suspend(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["suspend"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["suspend"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}/power?action=suspend")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}/power?action=suspend"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "suspend")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
