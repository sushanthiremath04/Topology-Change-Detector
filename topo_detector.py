from pox.core import core
import pox.openflow.discovery as discovery

log = core.getLogger()

# When switch connects
def _handle_ConnectionUp(event):
    log.info("Switch connected: %s", event.dpid)

# When switch disconnects
def _handle_ConnectionDown(event):
    log.info("Switch disconnected: %s", event.dpid)

# When link changes
def _handle_LinkEvent(event):
    link = event.link

    if event.added:
        log.info("Link added: %s <-> %s", link.dpid1, link.dpid2)
    else:
        log.info("Link removed: %s <-> %s", link.dpid1, link.dpid2)

def launch():
    log.info("Topology Change Detector Started")

    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("ConnectionDown", _handle_ConnectionDown)
    core.openflow_discovery.addListenerByName("LinkEvent", _handle_LinkEvent)
