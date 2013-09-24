// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.
package com.cloud.hypervisor.vmware.mo;

import java.util.List;

import com.cloud.hypervisor.vmware.util.VmwareContext;

import com.vmware.vim25.ManagedObjectReference;
import com.vmware.vim25.mo.Network;

public class NetworkMO extends BaseMO {
    private Network network;
    
    public NetworkMO(VmwareContext context, ManagedObjectReference morCluster) {
        super(context, morCluster);
        network = new Network(context.getServerConnection(), morCluster);
    }

    public NetworkMO(VmwareContext context, String morType, String morValue) {
        super(context, morType, morValue);
        ManagedObjectReference networkMor = new ManagedObjectReference();
        networkMor.setType(morType);
        networkMor.setVal(morValue);
        network = new Network(context.getServerConnection(), networkMor);
    }

    public void destroyNetwork() throws Exception {
        network.destroyNetwork();
    }

    public List<ManagedObjectReference> getVMsOnNetwork() throws Exception {
        return (List<ManagedObjectReference>)_context.getVimClient().getDynamicProperty(_mor, "vm");
    }
}
