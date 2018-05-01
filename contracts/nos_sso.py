from boa.builtins import concat
from boa.interop.Neo.Runtime import CheckWitness, GetTrigger, Log
from boa.interop.Neo.Storage import Delete, Get, GetContext, Put
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.System.ExecutionEngine import GetCallingScriptHash


def Main(operation, args):
    """Main definition of the nOS Single-Sign On dApp Smart Contract.

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return: bytearray: The result of the operation
    """
    Log("Done")
    return True
