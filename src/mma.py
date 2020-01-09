# partially copied from https://support.bayesfusion.com/docs/Wrappers/
import pysmile

# pysmile_license is your license key
import pysmile_license

def net_setup():
    net = pysmile.Network()
    net.read_file("mma.xdsl")

    # net.set_evidence("Forecast", "Moderate")
    # net.update_beliefs()
    # beliefs = net.get_node_value("Success")

    # for i in range(0, len(beliefs)):
    # print(net.get_outcome_id("Success", i) + "=" + str(beliefs[i]))

    print(net.get_first_node_id())
    print(net.get_all_node_ids())
 
net_setup()