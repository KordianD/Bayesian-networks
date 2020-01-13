    # partially copied from https://support.bayesfusion.com/docs/Wrappers/
import pysmile
import pysmile_license


def net_setup():
    net = pysmile.Network()
    net.read_file("mma.xdsl")
    return net


def get_posteriors(net, node_handle, posteriors_dict):
    node_id = net.get_node_id(node_handle)
    posteriors_dict[node_id] = {}

    if net.is_evidence(node_handle):
        print("Not implemented yet.")
    else:
        posteriors = net.get_node_value(node_handle)
        for i in range(0, len(posteriors)):
            posteriors_dict[node_id][net.get_outcome_id(node_handle, i)] = posteriors[i]


def get_all_posteriors(net):
    posteriors_dict = {}
    for handle in net.get_all_nodes():
        get_posteriors(net, handle, posteriors_dict)
    return posteriors_dict


def change_evidence_and_update(net, node_id, outcome_id):
    if outcome_id is not None:
        net.set_evidence(node_id, outcome_id)
    else:
        net.clear_evidence(node_id)
    net.update_beliefs()


def print_posteriors(net, node_handle):
    node_id = net.get_node_id(node_handle)
    if net.is_evidence(node_handle):
        print(node_id + " has evidence set (" +
              net.get_outcome_id(node_handle,
                                 net.get_evidence(node_handle)) + ")")
    else:
        posteriors = net.get_node_value(node_handle)
        for i in range(0, len(posteriors)):
            print("P(" + node_id + "=" +
                  net.get_outcome_id(node_handle, i) +
                  ")=" + str(posteriors[i]))


def print_all_posteriors(net):
    for handle in net.get_all_nodes():
        print_posteriors(net, handle)