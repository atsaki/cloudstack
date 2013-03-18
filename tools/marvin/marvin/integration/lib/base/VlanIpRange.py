# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from marvin.integration.lib.base import CloudStackEntity
from marvin.cloudstackAPI import createVlanIpRange
from marvin.cloudstackAPI import listVlanIpRanges
from marvin.cloudstackAPI import deleteVlanIpRange

class VlanIpRange(CloudStackEntity.CloudStackEntity):


    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


    @classmethod
    def create(cls, apiclient, VlanIpRangeFactory, **kwargs):
        cmd = createVlanIpRange.createVlanIpRangeCmd()
        [setattr(cmd, factoryKey, factoryValue) for factoryKey, factoryValue in VlanIpRangeFactory.__dict__.iteritems()]
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        vlaniprange = apiclient.createVlanIpRange(cmd)
        return VlanIpRange(vlaniprange.__dict__)


    @classmethod
    def list(self, apiclient, **kwargs):
        cmd = listVlanIpRanges.listVlanIpRangesCmd()
        [setattr(cmd, key, value) for key,value in kwargs.items]
        vlaniprange = apiclient.listVlanIpRanges(cmd)
        return map(lambda e: VlanIpRange(e.__dict__), vlaniprange)


    def delete(self, apiclient, id, **kwargs):
        cmd = deleteVlanIpRange.deleteVlanIpRangeCmd()
        cmd.id = id
        [setattr(cmd, key, value) for key,value in kwargs.items]
        vlaniprange = apiclient.deleteVlanIpRange(cmd)
