from dbus_next.service import (ServiceInterface,
                               method, dbus_property, signal)

class MMModemCDMAInterface(ServiceInterface):

    def __init(self, mm_modem):
        super().__init__('org.freedesktop.ModemManager1.Modem.ModemCdma')
        self.mm_modem = mm_modem

    @method()
    async def Activate(self,):
        return 

    @method()
    async def ActivateManuel(self, properties: 'a{sv}') -> 'o':
        return
