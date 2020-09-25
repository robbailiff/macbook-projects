# -*- coding: utf-8 -*- #
# Copyright 2015 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Helper functions for DNS commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dns import util as api_util
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.command_lib.dns import flags


def ParseKey(algorithm, key_length, key_type, messages):
  """Generate a keyspec from the given (unparsed) command line arguments.

  Args:
    algorithm: (str) String mnemonic for the DNSSEC algorithm to be specified in
        the keyspec; must be a value from AlgorithmValueValuesEnum.
    key_length: (int) The key length value to include in the keyspec.
    key_type: (KeyTypeValueValuesEnum) Enum value for whether to create a
        keyspec for a KSK or a ZSK.
    messages: (module) Module (generally auto-generated by the API build rules)
        containing the API client's message classes.

  Returns:
    A messages.DnsKeySpec instance created from the given arguments.
  """

  key_spec = None

  if algorithm is not None or key_length is not None:
    spec_args = {}
    spec_args['keyType'] = key_type
    if algorithm is not None:
      spec_args['algorithm'] = messages.DnsKeySpec.AlgorithmValueValuesEnum(
          algorithm)
    if key_length is not None:
      spec_args['keyLength'] = key_length

    if spec_args:
      key_spec = messages.DnsKeySpec(**spec_args)

  return key_spec


def ParseDnssecConfigArgs(args, messages):
  """Parse all relevant command line arguments and generate a DNSSEC config.

  Args:
    args: (dict{str,(str|int)}) Dict of command line arguments; value type
        dependent on particular command line argument.
    messages: (module) Module (generally auto-generated by the API build rules)
        containing the API client's message classes.

  Returns:
    A messages.ManagedZoneDnsSecConfig instance populated from the given
    command line arguments.
  """

  dnssec_config = None
  key_specs = []

  ksk_key = ParseKey(
      args.ksk_algorithm,
      args.ksk_key_length,
      messages.DnsKeySpec.KeyTypeValueValuesEnum.keySigning,
      messages)
  if ksk_key is not None:
    key_specs.append(ksk_key)

  zsk_key = ParseKey(
      args.zsk_algorithm,
      args.zsk_key_length,
      messages.DnsKeySpec.KeyTypeValueValuesEnum.zoneSigning,
      messages)
  if zsk_key is not None:
    key_specs.append(zsk_key)

  dnssec_config_args = {}
  if key_specs:
    dnssec_config_args['defaultKeySpecs'] = key_specs
  if getattr(args, 'denial_of_existence', None) is not None:
    dnssec_config_args['nonExistence'] = (
        flags.GetDoeFlagMapper(messages).GetEnumForChoice(
            args.denial_of_existence))
  if args.dnssec_state is not None:
    dnssec_config_args['state'] = (
        flags.GetDnsSecStateFlagMapper(messages)
        .GetEnumForChoice(args.dnssec_state))

  if dnssec_config_args:
    dnssec_config = messages.ManagedZoneDnsSecConfig(**dnssec_config_args)

  return dnssec_config


def ParseManagedZoneForwardingConfig(server_list, messages):
  """Parses list of forwarding nameservers into ManagedZoneForwardingConfig.

  Args:
    server_list: (list) List of IP addreses to use as forwarding targets for
        the DNS Managed Zone.
    messages: (module) Module (generally auto-generated by the API build rules)
        containing the API client's message classes.

  Returns:
    A messages.ManagedZoneForwardingConfig instance populated from the given
    command line arguments.
  """

  if not server_list:
    return None

  if server_list == ['']:  # Handle explicit unset case for update
    return messages.ManagedZoneForwardingConfig(targetNameServers=[])

  target_servers = [
      messages.ManagedZoneForwardingConfigNameServerTarget(ipv4Address=name)
      for name in server_list
  ]

  return messages.ManagedZoneForwardingConfig(targetNameServers=target_servers)


def PolicyNetworkProcessor(parsed_value):
  """Build PolicyNetwork message from parsed_value."""
  # Parsed Value should be a list of compute.network resources
  m = GetMessages()
  if not parsed_value:
    return []

  return [
      m.PolicyNetwork(networkUrl=network_ref.SelfLink())
      for network_ref in parsed_value
  ]


def TargetNameServerType(value):
  """Build PolicyAlternativeNameServerConfigTargetNameServer msg from value."""
  m = GetMessages()
  return m.PolicyAlternativeNameServerConfigTargetNameServer(ipv4Address=value)


def ParseNetworks(value, project):
  """Build a list of PolicyNetworks from command line args."""
  if not value:
    return []
  registry = api_util.GetRegistry('v1beta2')
  networks = [
      registry.Parse(
          network_name,
          collection='compute.networks',
          params={'project': project}) for network_name in value
  ]
  return PolicyNetworkProcessor(networks)


def ParseAltNameServers(value):
  """Build a list of TargetNameServers from command line args."""
  if not value:
    return None
  m = GetMessages()
  name_servers = [TargetNameServerType(ipv4) for ipv4 in value]
  return m.PolicyAlternativeNameServerConfig(targetNameServers=name_servers)


def GetMessages():
  return apis.GetMessagesModule('dns', 'v1beta2')
